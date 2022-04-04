def func_allowlist():
    with open('Lists/RAW/allowlist.txt', 'r') as f:
        allowlist = f.read().splitlines()

    adguardallow = open('Lists/AdGuard/allowlist.txt', 'w')
    allowlines = ["!\n","! Title: WcktKlwn's Allow Overrides\n","! Description: URL's that need to be set to allow for websites to work\n","! Homepage: https://github.com/wcktklwn/Webfilter\n","\n"]
    for allow in allowlist:
        allowlines.append("@@||%s^\n" % (allow))

    adguardallow.writelines(allowlines)
    adguardallow.close()


func_allowlist()