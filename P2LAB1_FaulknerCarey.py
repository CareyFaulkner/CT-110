# Carey Faulkner
# 08 MAR 2025
# Circle Calculations
# Calculating the diameter, circumference, and area of a circle

radius = float(input("What's the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")