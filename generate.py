allowlist = open("Lists/RAW/allowlist.txt", 'r')
print(allowlist.readlines())

for allow in allowlist.readlines():
    print("@@||%s^" % (allow))