# Mutable oder immutable ?

def vergleich(a,aText,b,bText):
    if a is b:
        str = aText," und ",bText,"sind gleich und voneinander abhängig"
    else:
        str = aText," und ",bText,"sind nicht gleich und voneinander unabhängig"
    return str

# Foile 42
x = 1
y = x
print ("x: ",x," y: ",y)
# Die Wertänderung von y hat keinen Einfluss auf x
y = 2
print ("x: ",x," y: ",y)
print(vergleich(x,"x",y,"y"))


# L I S T E N, Folie 43
# Es werden keine Zahlen gespeichert, sondern Listen
l1 = [1, 3, 4]

# Beide Listen verweisen auf dieselbe Liste
l2 = l1
print("L1: ",l1," L2: ",l2)

# l1[2] wird geändert, aber die Änderung scheint auch für l2 zu gelten
l1[2] = 5
print("L1: ",l1," L2: ",l2)
print(vergleich(l1,"L1",l2,"L2"))

# T U P E L, Folie 44: immutable
# Packing a tuple
t1 = ("Apfel", "Orange", "Kiwi")
t2 = t1
print("T1: ",t1," T2: ",t2)
# t2[1] = "Melone" führt zum Fehler, weil
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
t2 = ("zyx", 42, False, 3.14, True)
print("T1: ",t1," T2: ",t2)

# Unpacking a tuple
(rot, orange, gruen) = t1
print(rot)
print(orange)
print(gruen)

# Loop über t1
for x in t1:
  print(x)

# Konvertiere eine Tupel in eine Liste und ändere es:
l3 = list(t1)
l3[1] = "Melone"
t1 = tuple(l3)
print(t1)

# S E T S
s1 = {"UNIX", "Linux", "Windows"}
print(s1)
# Dupplikate werden entfernt
s2 = {"UNIX", "Linux", "Linux", "LINUX", "Windows"}
print(s2)

# 1 = wahr, 0 = falsch
s1 = {"UNIX", "Linux", "Windows", True, 1, 2, False, 0}
# int(1) bringt nichts:
s1 = {"UNIX", "Linux", "Windows", True, 1, 2, False, 0}
# str(1) zeigt 1 auch an
s1 = {"UNIX", "Linux", "Windows", True, str(1), 2, False, 0}
print(s1)
print(len(s1))

# Achtung bei der Verwendung des Set-Konstruktors: ()
s3 = set(("MySQL", "MariaDB", "SQL Server")) 
print(s3)
print("MySQL" in s3)
s3.add("Oracle")
print(s3)
s4 = {"Informix", "DB2"}
s3.update(s4)
print(s3)
s3.remove("DB2")
print(s3)

# D I C T I O N A R I E S
# Dictionaries are changeable
d1 = {
  "brand": "Samsung",
  "model": "S23 Ultra",
  "year": 2023
}
print(d1)
print(d1["model"])
d1["model"] = "Fold 5"
print(d1["model"])
print(d1)









