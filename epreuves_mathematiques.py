def factorielle(n):
    """
    Retourne la factorielle de n de manière récursive
    """
    return 1 if n == 0 else n * factorielle(n - 1)
