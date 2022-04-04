with open('Lists/RAW/allowlist.txt') as f:
    allow = f.read().splitlines() 


for allow in allowlist.readlines():
    print("@@||%s^" % (allow))