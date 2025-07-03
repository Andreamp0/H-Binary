print(r"""HH\   HH\       HHHHHHH\  HHHHHH\ HH\   HH\  HHHHHH\  HHHHHHH\ HH\     HH\ 
HH |  HH |      HH  __HH\ \_HH  _|HHH\  HH |HH  __HH\ HH  __HH\\HH\   HH  |
HH |  HH |      HH |  HH |  HH |  HHHH\ HH |HH /  HH |HH |  HH |\HH\ HH  / 
HHHHHHHH |      HHHHHHH\ |  HH |  HH HH\HH |HHHHHHHH |HHHHHHH  | \HHHH  /  
HH  __HH |      HH  __HH\   HH |  HH \HHHH |HH  __HH |HH  __HH<   \HH  /   
HH |  HH |      HH |  HH |  HH |  HH |\HHH |HH |  HH |HH |  HH |   HH |    
HH |  HH |      HHHHHHH  |HHHHHH\ HH | \HH |HH |  HH |HH |  HH |   HH |    
\__|  \__|      \_______/ \______|\__|  \__|\__|  \__|\__|  \__|   \__|

✦ Encoder
""")

while True:
    out = ""
    text = input("> ")
    raw = [str(bin(ord(i))) for i in text]
    for i in raw:
        for j in i:
            if j == "0":
                out += "h"
            elif j == "1":
                out += "H"
        out += " "
    print(out)