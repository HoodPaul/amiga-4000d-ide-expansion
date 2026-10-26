#!/usr/bin/env python3
"""Audit saved CAD, pin maps, documentation and submitted manufacturing data."""
import argparse,json,math,re
from collections import defaultdict
from pathlib import Path
from design_data import ROOT,BOARD,read,child,entries,reference,point,pads,fingerprints,schematic_map,sha256

def audit(netlist=None):
    board=read(BOARD)
    baseline=json.loads((ROOT/'verification/design-baseline.json').read_text())
    assert fingerprints(board)==baseline['electrical_fingerprints'],'Electrical geometry differs from revision 0.1 baseline'
    expected={k:sorted(v) for k,v in json.loads((ROOT/'verification/connection_map.json').read_text()).items()}
    actual=defaultdict(list);ps=pads(board)
    for p in ps:actual[p['net']].append(p['ref']+'.'+p['pin'])
    assert {k:sorted(v) for k,v in actual.items()}==expected,'PCB pin map mismatch'
    assert len(ps)==192 and len(expected)==56
    selected=Path(netlist) if netlist else ROOT/'verification/schematic.net'
    assert schematic_map(selected)==expected,'Schematic netlist mismatch'
    bypin={(p['ref'],p['pin']):p['pos'] for p in ps}
    centres={}
    for ref in ['J1','J2','J3','J4','J5']:
        a,b,c=[bypin[(ref,n)] for n in ['1','2','3']]
        assert b[1]>a[1] and c[0]<a[0],ref+' pin orientation'
        assert abs(math.dist(a,b)-2.54)<1e-6 and abs(math.dist(a,c)-2.54)<1e-6
        p=[q['pos'] for q in ps if q['ref']==ref]
        centres[ref]=[sum(q[i] for q in p)/len(p) for i in [0,1]]
    assert abs(centres['J1'][0]-centres['J4'][0])<1e-6
    assert abs(centres['J1'][1]-centres['J4'][1]-9.144)<1e-6
    silk=[]
    for t in entries(board,'gr_text'):
        if str(child(t,'layer')[1]) not in ['F.SilkS','B.SilkS']:continue
        font=child(child(t,'effects'),'font')
        assert min(float(x) for x in child(font,'size')[1:])>=1.0,'Printed text below 1 mm'
        assert float(child(font,'thickness')[1])>=.15-1e-9,'Text stroke below 0.15 mm'
        silk.append(str(t[1]))
    for name in ['Amiga 4000D IDE Expansion','IDE B / Secondary','IDE A / Primary','Floppy','REV 0.1']:
        assert name in silk,name+' label missing'
    for f in entries(board,'footprint'):
        ref=reference(f)
        if ref not in ['J2','J3','J5']:continue
        px,py=bypin[(ref,'1')];arrows=[];top=False
        for line in entries(f,'fp_line'):
            if str(child(line,'layer')[1])!='F.SilkS':continue
            a,c=point(f,child(line,'start')),point(f,child(line,'end'))
            assert float(child(child(line,'stroke'),'width')[1])>=.15-1e-9
            if all(abs(q[0]-px)<.61 and py-2.70<q[1]<py-2.18 for q in [a,c]):arrows.append(line)
            if abs(a[1]-51.9)<1e-6 and abs(c[1]-51.9)<1e-6 and abs(a[0]-c[0])>50:top=True
        assert len(arrows)==3,ref+' concealed pin-1 triangle'
        if ref=='J3':assert top,'J3 upper horizontal outline missing'
    ordered=json.loads((ROOT/'verification/ordered-revision.json').read_text())
    for relative,expected_hash in ordered['manufacturing_sha256'].items():
        assert sha256(ROOT/relative)==expected_hash,'Submitted manufacturing file changed: '+relative
    for relative,expected_hash in ordered['cad_sha256'].items():
        assert sha256(ROOT/relative)==expected_hash,'Ordered PCB/local footprint changed: '+relative
    checked_links=0
    for md in ROOT.rglob('*.md'):
        if '.git' in md.parts or 'build' in md.parts:continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',md.read_text()):
            if re.match(r'^[a-z]+:|^#',target):continue
            target=target.split('#')[0]
            assert (md.parent/target).exists(),str(md.relative_to(ROOT))+': broken link '+target
            checked_links+=1
    return {'status':'PASS','pads':len(ps),'nets':len(expected),'vias':len(entries(board,'via')),
      'electrical_fingerprints':'unchanged','submitted_manufacturing_files':'unchanged',
      'recorded_cad_files':'unchanged','printed_text_min_height_mm':1.0,
      'documentation_links_checked':checked_links,'schematic_netlist':str(selected.relative_to(ROOT)) if selected.is_relative_to(ROOT) else str(selected),
      'fresh_netlist_supplied':bool(netlist),'native_drc_run_by_this_audit':False,'hardware_tested':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--netlist',help='Fresh KiCad s-expression netlist for schematic parity')
    args=parser.parse_args()
    print(json.dumps(audit(args.netlist),indent=2))
