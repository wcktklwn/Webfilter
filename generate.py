allowlist = open("allowlist.txt", 'r')

for allow in allowlist.readlines():
    print(allow)