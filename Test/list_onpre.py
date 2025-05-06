# odd_number = [number for number in range(1,10,2)]
# print(odd_number[::-1])


# append_odd_numbers = sum(number for number in range(1,10,2) if number % 2 != 0)
# print(append_odd_numbers)



odd_numbers = []
even_numbers = []
jam = 0
ram = 0
for i in range(5):
    num = int(input(f"enter a number:" ))
    if num % 2 != 0:
         odd_numbers.append(num)
         jam += 1

    else:
         even_numbers.append(num)
         ram += 1

print(f"list of even number: ",even_numbers)
print(f"list of odd number: ",odd_numbers)
print (f"the number of even number: ",ram)
print (f"the number of odd number: ",jam)



# even_numbers = 0
# odd_numbers = 0
# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# for number in numbers:
#      if number % 2 == 0:
#           even_numbers += 1 
#      else:
#           odd_numbers += 1 
# print(f"list:",numbers)
# print(f"number of even number: ",even_numbers)
# print(f"number of odd number: ",odd_numbers)


# numbers = [number for number in range (1,100)]
# print(f"original list: ",numbers)
# print()
# for num in numbers:
#     if num %2 == 0:
#      numbers.remove(num)

# print(f"odd number list: ",numbers)  

# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# Odd number list: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
