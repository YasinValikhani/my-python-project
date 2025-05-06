
# import random
# Random_Wather = random.choice(['rainy', 'sunny', 'cloudy', 'snowy'])
# print (Random_Wather)
# if Random_Wather == ('rainy' and 'snowy') :
#     print("sit the fo%kdown at home.")
# else :
#     print("you can go out!")

# n1 = int(input())
# n2 = int(input())
# if n1 > n2:
#     print(n1)
# else :
#     print(n2)

# user_age = int(input("inter your age: "))
# if user_age < int(18) :
#     print("you must waiting to growup!")
# else :
#     print("wellcome :)")


# n1 = int(input("inter first number: "))
# n2 = int(input("inter second number: "))
# n3 = int(input("inter third number: "))


# if n1 > n2 and n1 > n3:
#       print(n1)
# elif n2 > n1 and n2 > n3: 
#      print(n2)   
# elif n3 > n1 and n3 > n2:     
#      print(n3)
# else :
#        print("all entered number are egual")    
    

# number = int(input("please inter a number: "))
# if int(number)%2 == 0:
#     print("even")
# else :
#     print("odd")


 
# name = input("Enter your name: ")  
# role = input("Enter your role: ")  

# valid_roles = ["User", "Manager", "System Manager", "Management"]  
 
# if name == "Manager" or name == "System Manager":  
#     print("You have access to system settings.")  
# elif role not in valid_roles:  
#     print("The entered role is not valid.")  
# elif name == "User" and role == "Management":  
#     print("You have access to the management section.")  
# else:  
#     print("You only have normal user access.")


# print("Wellcome to the BiliShop")

# purchase_amount = int(input("pleas enter your purchase amount: "))

# if purchase_amount <= 500:
#     discount = (purchase_amount*5)//100
# elif  500 <= purchase_amount <= 1000:
#     discount = (purchase_amount*10)//100
# else:  
#     discount = (purchase_amount*20)//100

# amount_payable = (purchase_amount) - (discount)  
# print("The purchase amount:",purchase_amount)          
# print(discount,"$","discount applied." )
# print("The payment amount is",amount_payable,"$.")


from Calculator import Add,Multiply

num1 = int(input('pleass enter a number: '))
num2 = 9
sum = Add(num1,num2)
multiply = Multiply(num1,num2)

print(sum,multiply)
