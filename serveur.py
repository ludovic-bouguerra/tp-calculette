
def add(val1, val2):
    """Ajoute deux valeurs entre elles

    @type val1: int | float
    @param val1: Valeur 1

    @type val2: int | float
    @param val2: Valeur 2

    @rtype: int | float
    @return: Retourne la somme des deux valeurs
    """
    return val1 + val2


def sub(val1, val2):
    """Soustraction valeurs entre elles

    @type val1: int | float
    @param val1: Valeur 1

    @type val2: int | float
    @param val2: Valeur 2

    @rtype: int | float
    @return: Retourne la soustraction des deux valeurs
    """
    return val1 - val2

def mul(val1, val2):
    """Multiplication valeurs entre elles

    @type val1: int | float
    @param val1: Valeur 1

    @type val2: int | float
    @param val2: Valeur 2

    @rtype: int | float
    @return: Retourne la multiplication des deux valeurs
    """
    return val1 * val2


def div(val1, val2):
    """Division valeurs entre elles

    @type val1: int | float
    @param val1: Valeur 1

    @type val2: int | float
    @param val2: Valeur 2 si 0 retourne None

    @rtype: int | float
    @return: Retourne la division des deux valeurs sauf si val 2 VAUT 0
    """
    if (val2 == 0):
        return None
    else:
        return val1 / val2

