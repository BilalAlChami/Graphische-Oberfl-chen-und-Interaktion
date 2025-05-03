# Testen mit 45 u. 30
a = int(input("Eingabe von a: "))
b = int(input("Eingabe von b: "))
print ("ggT("+str(a)+","+str(b)+") = ", end = '')
while a != b:
    if a < b :
        b = b - a
    else:
        a = a - b
print (a)
