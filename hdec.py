print(r"""HH\   HH\       HHHHHHH\  HHHHHH\ HH\   HH\  HHHHHH\  HHHHHHH\ HH\     HH\ 
HH |  HH |      HH  __HH\ \_HH  _|HHH\  HH |HH  __HH\ HH  __HH\\HH\   HH  |
HH |  HH |      HH |  HH |  HH |  HHHH\ HH |HH /  HH |HH |  HH |\HH\ HH  / 
HHHHHHHH |      HHHHHHH\ |  HH |  HH HH\HH |HHHHHHHH |HHHHHHH  | \HHHH  /  
HH  __HH |      HH  __HH\   HH |  HH \HHHH |HH  __HH |HH  __HH<   \HH  /   
HH |  HH |      HH |  HH |  HH |  HH |\HHH |HH |  HH |HH |  HH |   HH |    
HH |  HH |      HHHHHHH  |HHHHHH\ HH | \HH |HH |  HH |HH |  HH |   HH |    
\__|  \__|      \_______/ \______|\__|  \__|\__|  \__|\__|  \__|   \__|

✦ Decoder
""")

while True:
    out = ""
    hbin = input("> ")
    hlist = hbin.split(" ")
    for i in hlist:
        char = ""
        for j in i:
            if j == "h":
                char += "0"
            elif j == "H":
                char += "1"
        try:
            out += chr(eval("0b" + char))
        except:
            continue
    print(out)