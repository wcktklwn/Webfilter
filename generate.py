allowlist = open("Lists/RAW/allowlist.txt", 'r')

for allow in allowlist.readlines():
    print("@@||%s^" % (allow))