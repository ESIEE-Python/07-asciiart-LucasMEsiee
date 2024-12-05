""""
Exercice ASCIIART
"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(5000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
      passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    result = []
    i = 1
    last_element = s[0]
    for index,elt in  enumerate(s[1:]):
        if elt == last_element:
            i = i+1
        else:
            result.append((last_element,i))
            i = 1
        if index == len(s) - 2:
            result.append((elt,i))
        last_element = elt
    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
      passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    result = []
    # cas de base
    def recursif(s,index,last_element,i,result):
        if index == len(s):
            result.append((last_element,i))
            return result
    # recherche nombre de caractères identiques au premier
        if s[index] == last_element:
            return recursif( s, index + 1, last_element, i + 1, result)
    # appel récursif
        result.append((last_element,i))
        return recursif(s,index + 1,s[index],1,result)

    if not s:
        return[]
    return recursif(s,1,s[0],1,result)
#### Fonction principale
def main():
    """
    Fonction main pour tester les fonctions secondaires
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
if __name__ == "__main__":
    main()
