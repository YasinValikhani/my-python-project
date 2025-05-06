# shoping_list = ['apple', 'orange', 'kiwi', 'bennana', 'coffe']

# for i in range(len(shoping_list)):

#     print(shoping_list[i])


# numbers = [3,5,6,7,8,9,11]
# a = 20

# results = []  
# for number in numbers:
#     result = (number + a)

# print(result)

# num_list = [3, 7, 2, 9, 5]
# constant = 10
# for num in num_list:
#     result = num + constant
#     print(result)

# numbers = []
# for i in range(5):
#     number = int(input("please enter a number: "))
#     numbers.append(number)
# print(f"list if numbers: ",numbers)
  

# order = str(input("please enter a order(Insert/Pop/Remove/Count): "))
# if order == "insert":
#     amount = int(input("please enter a amount: "))
#     index =  int(input("please enter a index: "))
#     numbers.insert(index, amount)
# elif order == "pop":
#     index =  int(input("please enter a index: "))
#     numbers.pop(index)
# elif order == "remove" :
#     value = int(input("Enter the value to remove: "))
#     numbers.remove(value)
# elif order == "count":
#     value = int(input("Enter the value to count: "))
#     count = numbers.count(value)
#     print(f"The value {value} appears {count} times in the list.")
# else :
#     print("invalied order")        
# print(f"updated list: ",numbers)
x = int(input("Enter the number of list elements : "))
list = [int(input("Enter element : ")) for i in range(x)]
print(f"original list: ",list)
sorted_list = sorted(list, key=lambda x:(-(x % 10), x))
print(f"sorted list: ",sorted_list)








