# numbers = list(range(1,101))
# Unique_number = list(set(numbers))

# print(Unique_number)

# print(------------------------)

# my_set = {1, 2, 3, 4, 5}
# print(my_set)

# print(------------------------)

# my_set = {'World'}
# my_set.add('hello')

# print(my_set)

# print(------------------------)


# my_set = set(range(1,6))
# my_set.remove(3)

# print(my_set)


# print(------------------------)

# number0= {1, 2, 3, 4, 5, 8, 10}
# number1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

# number = (number0-number1).union(number1-number0)
# print(number)

# print(------------------------)

# participants = set()

# quastion = input('do you want to enter the name of participants?(yes/no): ')
# if quastion == 'yes':
#     for i in range(4):
#         name = input('pleas enter participants name: ')
#         participants.add(name)


#     removed_name = 'Eve'
#     if removed_name in participants:
#             participants.discard(removed_name)
#             print('removed participants:',removed_name)    
#     else:
#             print('participants name NOT in the list.')     
# else: 
#     print('ok')    


# print('Remaining names:',participants)

# participants = set()

# question = input('do you want to enter the name of participants? (yes/no): ')
# if question.lower() == 'yes':
#     for i in range(4):
#         name = input('please enter participant\'s name: ')
#         participants.add(name)

#     removed_name = 'Eve'
#     if removed_name in participants:
#         participants.discard(removed_name)
#         print('removed participant:', removed_name)    
#     else:
#         print(removed_name, 'NOT in the list.')    
#     print('Remaining names:', participants)    
# else: 
#     print('ok')    

# print('Remaining names:',participants)

my_list = set()

for i in range(8):
    number = int(input("pleas enter a number: "))
    my_list.add(number)

print(list(my_list))

