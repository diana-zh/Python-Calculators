# Diana Zhang, Nov 2020
# This calculator allows the user to input an initial number of chromosomes & chromatids and calculate how many remain after cell division.


initial = int(input('\nEnter initial number of chromosomes in your organism: ')) # Gets initial number from user
double_initial = initial * 2
half_initial = initial // 2

print('\nMitosis') # Prints chromosome & chromatid numbers after mitosis
print('Start with:', initial, 'chromosomes &', double_initial, 'chromatids')
print('End of Mitosis (2 cells): ', initial, 'chromosomes &', initial, 'chromatids\n')

print('Meiosis I') # Prints chromosome & chromatid numbers after meiosis I
print('Start with:', initial, 'chromosomes &', double_initial, 'chromatids')
print('End of Meiosis I (2 cells): ', half_initial, 'chromosomes &', initial, 'chromatids\n')

print('Meiosis II') # Prints chromosome & chromatid numbers after meiosis II
print('Start with:', half_initial, 'chromosomes &', initial, 'chromatids')
print('End of Meiosis II (4 cells): ', initial, 'chromosomes &', initial, 'chromatids\n')
