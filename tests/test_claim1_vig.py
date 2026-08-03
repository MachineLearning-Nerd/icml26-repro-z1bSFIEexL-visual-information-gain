import sys; sys.path.insert(0,'src')
from claim1_vig_definition_toy import run
r={x['condition']:x for x in run()}
assert r['matching-grounded']['vig']>r['partial-grounded']['vig']>0
assert r['conflicting-grounded']['vig']<0
assert abs(r['weak-visual']['vig'])<.02
for x in r.values(): assert abs(x['vig']-sum(x['token_loss_differences'])/3)<1e-12
