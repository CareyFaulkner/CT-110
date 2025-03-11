# Carey Faulkner
# 08 MAR 2025
# P2LAB2
# Calculates the number of gallons needed to drive a vehicle based on MPG.

# Create a dictionary with car models and their corresponding MPG values
dict_keys = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = dict_keys.keys()

print("dict_keys:")
for key in keys:
    print(key)

vehicle = input("Enter the vehicle to see it's mpg: ")

if vehicle in dict_keys:
    mpg = dict_keys[vehicle]
    print(f"The {vehicle} gets: {mpg} mpg")

    miles = float(input(f"How many miles will you drive the {vehicle}: "))

    gallons_needed = miles / mpg

    print(f"{gallons_needed:.2f} gallons are needed to drive the {vehicle} {miles} miles")
