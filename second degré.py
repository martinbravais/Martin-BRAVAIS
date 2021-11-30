from math import sqrt
 


def fonction_secnd():
    a = float(input ("choisir a "))
    b = float(input ("choisir b "))
    c = float(input ("choisir c "))
    delta = b*b - (4*a*c)
    if delta < 0:
        print("le delta est négatif, il n'y a donc pas de solutions")
    elif delta > 0:
        x =(-b - sqrt(delta))/2*a
        y = (-b + sqrt(delta))/2*a
        return str(x)and str(y)
    elif delta == 0:
        f = (-b)/2*a
        return str(f)
    

fonction_secnd ()
