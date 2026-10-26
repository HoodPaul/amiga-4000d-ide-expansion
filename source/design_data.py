"""Shared readers for the saved KiCad revision 0.1 data."""
from pathlib import Path
import hashlib,json,math
import sexpdata as sx

ROOT=Path(__file__).resolve().parents[1]
BOARD=ROOT/'Amiga4000_IDE_Expansion.kicad_pcb'

def child(node,key):
    return next((x for x in node if isinstance(x,list) and x and str(x[0])==key),None)

def entries(node,key):
    return [x for x in node if isinstance(x,list) and x and str(x[0])==key]

def read(path):
    with Path(path).open() as f:return sx.load(f)

def sha256(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def digest(value):
    return hashlib.sha256(json.dumps(value,default=str,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def reference(fp):
    for q in entries(fp,'fp_text'):
        if str(q[1])=='reference':return str(q[2])
    for q in entries(fp,'property'):
        if str(q[1])=='Reference':return str(q[2])
    raise ValueError('Footprint has no reference')

def point(fp,local):
    at=child(fp,'at');angle=math.radians(float(at[3]) if len(at)>3 else 0)
    x,y=float(local[1]),float(local[2])
    return [float(at[1])+x*math.cos(angle)+y*math.sin(angle),float(at[2])-x*math.sin(angle)+y*math.cos(angle)]

def pads(board):
    result=[]
    for f in entries(board,'footprint'):
        ref=reference(f)
        for q in entries(f,'pad'):
            net=child(q,'net')
            result.append({'ref':ref,'pin':str(q[1]),'net':str(net[2]),'pos':point(f,child(q,'at'))})
    return result

def fingerprints(board):
    fps=[]
    for f in entries(board,'footprint'):
        if not entries(f,'pad'):continue
        fps.append([reference(f),child(f,'at'),child(f,'layer'),entries(f,'pad')])
    return {
      'nets':digest(entries(board,'net')),
      'pads_and_component_placement':digest(fps),
      'tracks_and_vias':digest(entries(board,'segment')+entries(board,'via')),
      'zones_and_filled_copper':digest(entries(board,'zone')),
      'outline':digest([q for q in board if isinstance(q,list) and q and str(q[0]).startswith('gr_') and child(q,'layer') and str(child(q,'layer')[1])=='Edge.Cuts']),
      'layers':digest(child(board,'layers'))}

def schematic_map(path):
    tree=read(path);result={}
    for n in child(tree,'nets')[1:]:
        result[str(child(n,'name')[1]).lstrip('/')]=sorted(str(child(q,'ref')[1])+'.'+str(child(q,'pin')[1]) for q in entries(n,'node'))
    return result
