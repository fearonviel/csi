#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("dna.txt", "r") as data:
    dna_sequence = data.read()

suspect_criteria = {
    "Black hair": "CCAGCAATCGC",
    "Brown hair": "GCCAGTGCCG",
    "Blonde hair": "TTAGCTATCGC",

    "Square face": "GCCACGG",
    "Round face": "ACCACAA",
    "Oval face": "AGGCCTCA",

    "Blue eyes": "TTGTGGTGGC",
    "Green eyes": "GGGAGGTGGC",
    "Brown eyes": "AAGTAGTGAC",

    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC",

    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG",
}

print("Culprit's characteristics:")
for x in suspect_criteria:
    if suspect_criteria[x] in dna_sequence:
        print x

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
    for x in suspect:
        if (suspect[x]) in dna_sequence:
            print(x +": Match!")
        else:
            print(x + ": Not a match!")

print("------------------")
print("Comparing suspects:")
print
print("Larisa:")
find_suspect(larisa)
print
print("Matej:")
find_suspect(matej)
print
print("Miha:")
find_suspect(miha)
print
print("Eva:")
find_suspect(eva)

