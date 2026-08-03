#!/usr/bin/env python3
"""Finite, source-formula VIG toy; not an LVLM/benchmark execution."""
import csv, hashlib, json, math, random
from pathlib import Path
OUT=Path('outputs/claim1_vig_definition_toy')
def nll(ps): return [-math.log(p) for p in ps]
def run():
    # Predicted probabilities for the observed answer tokens.  Fixed synthetic
    # conditions: matching image improves grounded tokens, conflict worsens them,
    # while weakly visual tokens stay nearly unchanged.
    rows=[('matching-grounded',[.20,.30,.25],[.70,.75,.65]),
          ('partial-grounded',[.20,.30,.25],[.42,.46,.40]),
          ('conflicting-grounded',[.70,.75,.65],[.20,.30,.25]),
          ('weak-visual',[.62,.58,.60],[.61,.59,.60])]
    out=[]
    for name,txt,img in rows:
        diffs=[a-b for a,b in zip(nll(txt),nll(img))]
        # log(PPL_text/PPL_image) equals mean token CE difference.
        vig=sum(diffs)/len(diffs)
        out.append({'condition':name,'token_loss_differences':diffs,'vig':vig,
                    'ppl_text':math.exp(sum(nll(txt))/len(txt)),
                    'ppl_image':math.exp(sum(nll(img))/len(img))})
    return out
if __name__=='__main__':
 OUT.mkdir(parents=True,exist_ok=True); rows=run()
 config={'seed':20260803,'metric':'VIG=log(PPL(A|Q)/PPL(A|Q,I))=mean_t(CE_text-CE_image)','scope':'synthetic fixed probability toy; no VLM, image, or benchmark'}
 (OUT/'config.json').write_text(json.dumps(config,indent=2)+'\n')
 (OUT/'raw_probabilities.json').write_text(json.dumps(rows,indent=2)+'\n')
 with (OUT/'results.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['condition','vig','ppl_text','ppl_image'],extrasaction='ignore'); w.writeheader(); w.writerows(rows)
 summary={'verdict':'toy','scope':config['scope'],'results':rows,'controls':'matching/partial/conflicting image conditioning plus weak-visual near-zero control','conclusion':'Formula behavior only; neither Table 1 nor LVLM grounding is verified or falsified.'}
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 with (OUT/'SHA256SUMS').open('w') as f:
  for p in ['config.json','raw_probabilities.json','results.csv','summary.json']:
   f.write(hashlib.sha256((OUT/p).read_bytes()).hexdigest()+'  '+p+'\n')
