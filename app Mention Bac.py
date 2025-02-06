noteBac = float(input("Quelle est ta moyenne ? "))

if noteBac > 20 or noteBac < 0:
    print("La note doit être comprise entre 0 et 20.")
else:
    if noteBac >= 18:
        print("Félicitations Du Jury!")
    elif noteBac >= 16:
        print("Très Bien")
    elif noteBac >= 14:
        print("Bien")
    elif noteBac >= 12:
        print("Assez Bien")
    elif noteBac >= 10:
        print("Tout juste la moyenne")
    else:
        print("Désolé, tu n'as pas ton bac.")