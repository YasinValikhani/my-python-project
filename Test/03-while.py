# count = 2
# print(2)
# while count <= 100:
#      if count % 2 != 0:
#       print(count)     
#      count += 1
# print("bye")        

# for i in range(2, 11, 2):  
#     print(i)  
# num1, num2 = 2, 3
# while num1 <= 100:
#     print(num1)
#     num1, num2 = num2, num1 + num2


# count = 2  
# while count <= 100:   
#     is_count = True  
#     n = 2  
#     while n <= count // 2:  
#         if count % n == 0:  
#             is_count = False   
#             break 
#         n += 1  
#     if is_count: 
#         print(count)  
#     count += 1  


# total_sum = 0  

# for number in range(2, 101):  
#     is_number = True 
#     for i in range(2, int(number**0.5) + 1):  
#         if number % i == 0:  
#             is_number = False 
#             break  
            
#     if is_number:  
#         total_sum += number   
# print(total_sum)



# F_n = []
# num1, num2 = 0, 1
# for i in range(0,20):
#     if num1 > 20:
#          break
#     F_n.append(num1)
#     num1, num2 = num2, num1 + num2
#     print(F_n)
 
# def is_prime(n):
#     """بررسی می‌کند که آیا عدد ورودی اول است یا خیر"""
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # آزمایش تابع با چند عدد مختلف
# print(is_prime(17))  # باید True برگرداند
# print(is_prime(18))  # باید False برگرداند
# print(is_prime(19))  # باید True برگرداند
# print(is_prime(20))  # باید False برگرداند
# print(is_prime(23))  # باید True برگرداند


# def reverse_string(x):
#    return x[::-1]

# user_input = input("Enter a word: ")
# reversed_string = reverse_string(user_input)
# print("Reversed string:",reversed_string)    

# count = 0
# def increase_count():
#     for i in range(10):
#         global count
#         count += 1 

# increase_count()
# print(count)        
# ----------------------------

# total = 0 
# print("total value:",total)
# def tatal_value():
#     global total
#     for i in range(10):
#         total += 10

# tatal_value()
# print("total after first function call:",total)
# tatal_value()
# print("Total after second function call:",total)

