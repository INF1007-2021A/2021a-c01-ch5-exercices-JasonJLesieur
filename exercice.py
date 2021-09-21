#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = number * -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list[" "]
    for pre in prefixes:
        nom = prefixes + suffixe
        list.append(nom)
    return [""]


def prime_integer_summation() -> int:
    list = [1, 2, 3]
    somme = 0
    nombre = 0
    diviseur = range(2, int(math.sqrt(nombre)))


    while len(list) < 100:
        is_prime = true



    else: return somme




def factorial(number: int) -> int:
    return math.factorial(number)


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
