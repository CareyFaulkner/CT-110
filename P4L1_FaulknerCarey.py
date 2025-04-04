# Carey Faulkner
# 03 APR 2025
# Turtle Shapes with Loops: Square and Triangle

import turtle

t = turtle.Turtle()

# Draw a square using for loop
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a triangle using while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.right(120)
    sides += 1

turtle.done()