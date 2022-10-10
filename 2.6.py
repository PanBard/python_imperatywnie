a = True
b = True

lewa_str_rown = not (a and b)
prawa_str_rown = (not a) or (not b)

if lewa_str_rown == prawa_str_rown:
    print("Pierwsze praow de Morgana jest ok")

else:
    print("Nigdy to nie bedzie wyswieltone")