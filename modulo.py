def modulo(nombre, diviseur):
    if not isinstance(nombre, int) or not isinstance(diviseur, int):
        raise TypeError("Les deux arguments doivent être des entiers.")
    if diviseur == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")

    return nombre % diviseur
