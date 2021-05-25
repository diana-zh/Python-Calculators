# Diana Zhang, Nov 2020
# This program calculates which molecule (out of 2) is the limiting reagent.

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

mol1 = float(input('\nEnter mol of first molecule: '))
coef1 = float(input('Enter coefficient of first molecule: '))
mol2 = float(input('Enter mol of second molecule: '))
coef2 = float(input('Enter coefficient of second molecule: '))

complete2 = multiply(mol1, divide(coef2, coef1))
complete1 = multiply(mol2, divide(coef1, coef2))

if complete2 > mol2: # Checking mol ratios of two reactants
    print('\nMolecule 2 is the limiting reagent\n')
elif complete2 == complete1:
    print('\nThere is no limiting reagent. The molecules are in stoichiometric proportion with each other.\n')
else:
    print('\nMolecule 1 is the limiting reagent\n')
