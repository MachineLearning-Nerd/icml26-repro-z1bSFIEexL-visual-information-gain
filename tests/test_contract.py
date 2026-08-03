import json
p=json.load(open('contract/live_claims.json'))
assert p['orid']=='z1bSFIEexL'
assert len(p['claims'])==6
