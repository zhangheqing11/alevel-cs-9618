#!/usr/bin/env python3
"""Re-render the exact original-page inventory recorded by the human T38 audit."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from check_handbook import ROOT,SOURCES


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('/tmp/T38-source-review'))
    parser.add_argument('--evidence',action='store_true',help='extract six official evidence.doc files with macOS textutil')
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    import pymupdf
    coverage=json.loads(Path(__file__).with_name('T38-coverage.json').read_text())
    pages={(p['row'].split(':')[0],p['kind'],p['page']) for p in coverage['representative_rendered_pages']}
    pages.update(tuple(p) for p in coverage['supplemental_pages'])
    for name in coverage['practice_reviewed_pages']:
        match=re.fullmatch(r'(9618_[sw]\d{2}_4[123])_(qp|ms)_(\d+)\.png',name)
        pages.add((match[1],match[2],int(match[3])))
    for paper,kind,page in sorted(pages):
        filename=re.sub(r'_(4[123])$','_'+kind+r'_\1.pdf',paper)
        stem=f'{paper}_{kind}_{page}'
        with pymupdf.open(SOURCES/'pastpapers'/filename) as doc:
            doc[page-1].get_pixmap(matrix=pymupdf.Matrix(1.7,1.7)).save(args.out/(stem+'.png'))
            (args.out/(stem+'.txt')).write_text(doc[page-1].get_text(sort=True))
    if args.evidence:
        manifest={p['paper']:p for p in json.loads((ROOT/'pipeline/extract/source_files_p4.json').read_text())}
        for ex in coverage['practice']:
            paper=ex['exercise'].rsplit('_q',1)[0];record=manifest[paper]
            relative=next(f['path'] for f in record['files'] if Path(f['path']).name=='evidence.doc')
            out=subprocess.run(['textutil','-convert','txt','-stdout',str(SOURCES/'pastpapers'/record['sf']/relative)],
                capture_output=True,text=True,check=True).stdout
            (args.out/(ex['exercise']+'-evidence.txt')).write_text(out)
    print(f'Rendered {len(pages)} unique QP/MS pages to {args.out}; this does not assert human review.')


if __name__=='__main__':main()
