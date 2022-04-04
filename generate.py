with open('Lists/RAW/allowlist.txt') as f:
    allowlist = f.read().splitlines() 


for allow in allowlist():
    print("@@||%s^" % (allow))