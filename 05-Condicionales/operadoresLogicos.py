# Operadores Logicos
"""
 and -> Y
 or -> O
 ! -> negacion
 not -> no
"""

edad_minima = 18
edad_maxima = 65
edad_oficial = 18

# AND
if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

# OR
pais = "Argentina"
if pais == "Argentina" or pais == "España" or pais == "Colombia":
    print(f"{pais} es de habla hispana")
else:
    print(f"{pais} no es de habla hispana")

# NOT -> si no es ...
pais = "España"
if not (pais == "Argentina" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es de habla hispana")
else:
    print(f"{pais} SI es de habla hispana")

# !=
pais = "USA"
if pais != "Argentina" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es de habla hispana")
else:
    print(f"{pais} SI es de habla hispana")
