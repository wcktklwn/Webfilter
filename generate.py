def func_allowlist():
    with open('Lists/RAW/allowlist.txt', 'r') as f:
        allowlist = f.read().splitlines()
    adguardallow = open('Lists/AdGuard/allowlist.txt', 'w')
    allowlines = ["!\n","! Title: WcktKlwn's Allow Overrides\n","! Description: URL's that need to be set to allow for websites to work\n","! Homepage: https://github.com/wcktklwn/Webfilter\n","\n"]
    for allow in allowlist:
        allowlines.append("@@||%s^\n" % (allow))
    adguardallow.writelines(allowlines)
    adguardallow.close()

def func_blocklist():
    with open('Lists/RAW/blocklist.txt', 'r') as f:
        blocklist = f.read().splitlines()
    adguardblock = open('Lists/AdGuard/blocklist.txt', 'w')
    blocklines = ["!\n","! Title: WcktKlwn's block Overrides\n","! Description: URL's that need to be set to block for websites to work\n","! Homepage: https://github.com/wcktklwn/Webfilter\n","\n"]
    for block in blocklist:
        blocklines.append("@@||%s^\n" % (block))
    adguardblock.writelines(blocklines)
    adguardblock.close()

def func_personallist():
    with open('Lists/RAW/personallist.txt', 'r') as f:
        personallist = f.read().splitlines()
    adguardpersonal = open('Lists/AdGuard/personallist.txt', 'w')
    personallines = ["!\n","! Title: WcktKlwn's personal Overrides\n","! Description: URL's that need to be set to personal for websites to work\n","! Homepage: https://github.com/wcktklwn/Webfilter\n","\n"]
    for personal in personallist:
        personallines.append("||%s^\n" % (personal))
    adguardpersonal.writelines(personallines)
    adguardpersonal.close()

func_allowlist()
func_blocklist()
func_personallist()
