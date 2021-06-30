# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

total_heights = 0
for height in student_heights:
    total_heights += height
print(f"Total Heights is: {total_heights}")

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(f"Total Students is: {num_of_students}")

average_height = round(total_heights / num_of_students)
print(f"Average Height is: {average_height}")

# total_heights = sum(student_heights)
# num_of_students = len(student_heights)
# average_height = round(total_heights / student_heights)
# print(average_height)
# 156 178 165 171 187 168
