# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# converting weight to an integer and height to floating point and use the equation
bmi = (float(weight) / (float(height) ** 2))

# convert bmi to an integer and print the result
bmi_as_int = int(bmi)

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or 
# bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
