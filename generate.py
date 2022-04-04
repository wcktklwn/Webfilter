with open('Lists/RAW/allowlist.txt', 'r') as f:
    allowlist = f.read().splitlines() 

adguardallow = open('Lists/AdGuard/allowlist.txt', 'w')
allowlines = []

for allow in allowlist:
    allowlines.append("@@||%s^" % (allow))
    print(allowlines)