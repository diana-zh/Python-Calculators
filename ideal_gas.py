# Diana Zhang, Nov 2020
# Program does ideal gas calculations using equation PV = nRT

print("Select operation.")
print("1. Calculate P in Ideal Gas")
print("2. Calculate V in Ideal Gas")
print("3. Calculate n in Ideal Gas")
print("4. Calculate T in Ideal Gas\n")

while True:
    # User input
    choice = input("Enter choice (1/2/3/4): ")

    # Check if user's choice is 1 of 4 options
    if choice in ('1', '2', '3', '4'):
        R = 8.31415
        K = 273.15 # Celsius to Kelvin conversion factor

        if choice == '1':
            V = float(input("\nEnter volume in L: "))
            T = float(input("Enter temperature in C: "))
            n = float(input("Enter mols: "))

            print("\nThe pressure is", ((n * R * (T + K))/V), "kPa\n")

        elif choice == '2':
            P = float(input("\nEnter pressure in kPa: "))
            T = float(input("Enter temperature in C: "))
            n = float(input("Enter mols: "))

            print("The volume is", (n * R * (T + K))/P, "L\n")

        elif choice == '3':

            P = float(input("\nEnter pressure in kPa: "))
            V = float(input("Enter volume in L: "))
            T = float(input("Enter temperature in C: "))

            print("The number of mols is", ((P * V)/(R * (T + K))), "mol\n")

        elif choice == '4':

            P = float(input("Enter pressure in kPa: "))
            V = float(input("Enter volume in L: "))
            n = float(input("Enter mols: "))            

            temp = (P * V) / (R * n)

            print ("\nThe temperature is", temp, "K")
            print ("The temperature is", (temp - K), "C\n") # Conversion to Celsius

            break
    else:
        print("Invalid Input")