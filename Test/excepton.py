# try:
#     num1 = int(input('first number: '))
#     num2 = int(input('second number: '))

#     print(num1 / num2)

# except ZeroDivisionError:
#     print('the second number canot be zero')

# try:
#     with open('data.txt', 'r') as file:
#         content = [int(line.strip()) for line in file]
#         print('list of number:',content)
# except ValueError:
#     print('pleas enter a INT value!!')      

# while True:
#     try:
#         num1 = int(input('first number: '))
#         num2 = int(input('second number: '))
#         num3 = int(input('third number: '))

#         print('average of numbers:',(num1 + num2 + num3)/3) 

#     except ValueError:
#             print('pleas enter a INT value!!')         


# try: 
#     with open('data.txt', 'r') as file:
#         student = {}
#         for line in file:
#             parts = line.strip().split()
#             if len(parts) == 2 and parts[1].isdigit():
#                 student[parts[0]] = int(parts[1])
#             else:
#                 raise ValueError(f"Invalid format in line: {line.strip()}")
   
#         print('students dictionary:', student)
# except FileNotFoundError:
#     print("Error: The file 'data.txt' does not exist.")
# except ValueError as e:
#     print("Error:", e) 


