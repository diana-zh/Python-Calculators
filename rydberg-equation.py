# Diana Zhang, Nov 2020

# Program calculates wavenumber and wavelength using Rydberg's equation, given initial and final energy levels

error = '\nInvalid energy level. Please type a positive integer!\n'

while True:
    try:
        num1 = float(input('Enter initial n number: '))
        num2 = float(input('Enter final n number: '))
        break
    except ValueError: # Check non-numerical input
        print(error)

if num1 <= 0: # Check negative or 0
    print(error)

elif num2 <= 0: # Check negative or 0
    print(error)

elif (num1).is_integer() and (num2).is_integer(): # Calculation performed if both numbers are integers
 
    wavenumber = (-109677.58341)*((1 / ((num1) ** 2)) - (1 / (num2) ** 2))
    wavelength = 1 / wavenumber # Wavelength is reciprocal of wavenumber

    print('\nThe wavenumber is', wavenumber,'cm-1')
    print('The wavelength is',(wavelength),'cm')
    print('The wavelength is',((1e7) * wavelength), 'nm\n') # Conversion of cm to nm

    if num1 > num2: # Checks emission or absorption
        print('Light is being emitted.\n')
    else:
        print('Light is being absorbed.\n')
else: # Takes care of floats
    print(error)
