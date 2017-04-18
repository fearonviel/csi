#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("dna.txt", "r") as data:
    dna_sequence = data.read()

eva = {
    "Gender": "TGAAGGACCTTC",
    "Race": "AAAACCTCA",
    "Hair color": "TTAGCTATCGC",
    "Eye color": "TTGTGGTGGC",
    "Face shape": "AGGCCTCA",
}

miha = {
    "Gender": "TGCAGGAACTTC",
    "Race": "AAAACCTCA",
    "Hair color": "GCCAGTGCCG",
    "Eye color": "GGGAGGTGGC",
    "Face shape": "GCCACGG",
}

matej = {
    "Gender": "TGCAGGAACTTC",
    "Race": "AAAACCTCA",
    "Hair color": "CCAGCAATCGC",
    "Eye color": "AAGTAGTGAC",
    "Face shape": "AGGCCTCA",
}

larisa = {
    "Gender": "TGAAGGACCTTC",
    "Race": "AAAACCTCA",
    "Hair color": "GCCAGTGCCG",
    "Eye color": "AAGTAGTGAC",
    "Face shape": "AGGCCTCA",
}


def find_suspect(suspect):
    if all((suspect[x]) in dna_sequence for x in suspect):
        return True

if find_suspect(larisa) is True:
    print("Larisa is the culprit!")
elif find_suspect(matej) is True:
    print("Matej is the culprit!")
elif find_suspect(miha) is True:
    print("Miha is the culprit!")
elif find_suspect(eva) is True:
    print("Eva is the culprit!")



