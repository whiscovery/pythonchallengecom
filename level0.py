original = ""
original += "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr "
original += "amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr "
original += "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

after = ""

for c in original:
    if ord(c) > 122 or ord(c) < 97:
        c = c
    elif ord(c) > 120 and ord(c) < 123:
        c = chr(ord(c) - 24)
    else:
        c = chr(ord(c) + 2)
    after += c

print(after)
