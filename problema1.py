
ap = float(input("Ingrese el alto panel: "))
anp = float(input("Ingrese el ancho panel: "))

ac = float(input("Alto techo: "))
anc = float(input("Ancho techo: "))

def calculate_panels(ap, anp, ac, anc):
    p1 = (ac // ap) * (anc // anp)
    p2 = (ac // anp) * (anc // ap)
    return int(max(p1, p2))

total = calculate_panels(ap, anp, ac, anc)

print("Paneles totales :", total)
