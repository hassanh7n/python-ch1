# a = ["hello"]
# b = ["world"]
# c = a + b
# print(c)

# d = ("hi", 0, 2, 0.5, True)
# print(a)

# e = [ 0, 3, 5, 0.5, False, "hello!"]
# print(e[0])

# e.append("world")
# print(e)


# f = {"name" : "hassan" , "age" : "21"}
# print(f["name"])



# L = [9, 7, 5, -3, 0, -6]
# N = -3
# J = 5.5

# for i in range(len(L)):
#     # print(L[i], i)
#     if N == L[i]:
#         print("Founded index :", i + 1, L[i])
#         L[i] = J
#         break
#     else:
#         print("Not found")
# print(L)
# for i in range(len(L)):
#     min_index = i
#     for j in range(i + 1, len(L)):
#         if L[j] < L[min_index]:
#             L[j], L[min_index] = L[min_index], L[j]
#             print(L)
# z = input("Enter a number")
# print(z)


# def userData():
#     d = {}
#     while True:
#         studentId = input("Enter student Id")
#         studentMarks = input("Enter student marks")
#         d.pop(studentId, studentMarks)
#         wannaContinue = input("Do you want to continue? (yes/no)")
#         if studentId in d:
#             print("Student id already existed")
#         else:
#             d[studentId] = studentMarks.split(".")
#         if wannaContinue.lower() == "no":
#             return d
        
# studentData = userData()
# print(studentData)
# d = {'7': ['21, 29'], '11': [' 11 07 25']}

# def getAvgMarks(d):
#     avgMarks = {}
#     for student_id in d:
#         marks_list = []
#         # Parse each mark string
#         for mark_str in d[student_id]:
#             # Handle both comma and space separated numbers
#             numbers = [num.strip() for num in mark_str.replace(',', ' ').split()]
#             marks_list.extend([int(num) for num in numbers if num])
        
#         # Calculate average if marks exist
#         if marks_list:
#             avgMarks[student_id] = sum(marks_list) / len(marks_list)
    
#     return avgMarks

# # Calculate averages
# avgMarks = getAvgMarks(d)

# # Print results with formatted output
# for student_id in avgMarks:
#     print(f"Student ID: {student_id} - Average marks: {avgMarks[student_id]:.2f}")
    

# def even_or_number():
#     n = int(input("Enetr a number"))
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")  
# even_or_number()


# L = [9, 7, 5, -3, 0, -6]


# for i in range(len(L)):
#     min_index = i
#     for numbers in range(i + 1, (len(L))):
#         if L[numbers] < L[min_index]:
#             L[numbers], L[min_index] = L[min_index], L[numbers]
#             print(L)


# def calculator(a, b, operator):
#     result = 0
#     if operator == "+":
#         result = a + b
#     elif operator == "-":
#         result = a - b
#     elif operator == "*":
#         result = a * b
#     elif operator == "/":
#         result = a / b
#     return result

# hi = calculator(2, 3, "/")
# print(hi)



def count_vowel(text):
    vowels = 0;
    for i in text:
        # print(i)
        if i == "o" or i == "a" or i == "e" or i == "i" or i == "u":
            vowels += 1
    return vowels


print(count_vowel("hello"))