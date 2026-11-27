# a = 10
# b = 5

# print(a + b)
# print(a - b)
# print(a / b)
# print(a // b)
# print(a * b)
# print(a ** b)
# print(a % b)
# print(a == b)



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# for num in (num1, num2):

#     if num <= 1:
#         print(num, "is Not Prime")

#     else:
#         count = 0

#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count = count + 1

#         if count == 2:
#             print(num, "is Prime")
#         else:
#             print(num, "is Not Prime")


# day = int(input("enter the day in number/n"))
# match day:
#     case 1:
#         print("its monday")
#     case 2:
#         print("its tuesday")
#     case 3:
#         print("its wendsday")
#     case 4:
#         print("its tursday")
#     case 5:
#         print("its friday")
#     case 6:
#         print("its saturday")
#     case 7:
#         print("its sunday")            

# day = int(input("enter the value\n"))
# match day:
#     case 1:
#         print("its monday")
#     case 2:
#         print("its tuesday")















# day = int(input("enter the day"))
# match day:
#     case range (1,6):
#         print("its weekday")
#     case  6 | 7:
#         print("its weekend")

# day = int(input("enter the name\n"))
# match day:
#     case range (1, 6):
#         print("weekday")
#     case 6 | 7:
#         print("weekend")    







# # day = int(input("enter day number 1-7: "))

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("its working day")
#     case 6 | 7:
#         print("its weekend")


# day = int(input("enter the number\n"))
# month = int(input("3nter the number\n"))

# match day:
#     case 1 | 2 | 3 | 4 | 5 if month != 12:
#         print("its workind day")

#     case 6 | 7 if month == 12:
#         print("its weekend")



# day = int(input("enter thr number\n"))
# match day:
#    case 1:
#     print("its monday")
#    case 5:
#     print("its tuesady")




# day = int(input("enter the number\n"))
# match day:
#     case range(1,6):
#         print("its weekday"),
#     case 6 | 7:
#         print("its weekend")


# day = int(input("enter the number\n"))
# month = int(input("enter the number\n"))
# match day:
#     case 1 | 2 | 3 | 4 | 5 if month != 12:
#         print("its weekday")
#     case 6 | 7 if month == 12:
#        print("its weekend")    

# age = 26
# salary = 50000
# match age:
#     case (age) if age <= 26 and salary > 50000:
#         print ("elibigible")

#     case _:
#         print("not elibible")



# num = int(input("enter the number\n"))

# match num:
#     case x if x > 0 and x % 2 == 0:
#         print("its even number")


#     case x if x > 0 and x % 2 != 0:
#         print("its odd number")
        
#     case x if x < 0:
#         print("its nagtive number")

#     case _:
#       print("its invalit number")  


# 20 * 1 = 12
# num = 20
# i = num + 1
# output = num + i

# num = int(input("enter the number/n"))
# match num:
#     case x if x > 0 and x % 2 == 0:
#         print("n")
#     case x if x > 0 and x % 2 != 0:
#        print("odd")    
















# num = int(input("enter the number\n"))
# match num:
#     case x if x > 0 and x % 2 == 0:
#         print("its even number")
#     case x if x > 0 and x % 2 != 0:
#         print("its odd number")
#     case x if x < 0:
#         print("nagative number")
#     case _:
#         print("invalid number")


# num = 12
# i = num * 1
# output = num * i


# for i in range (1,11):
#     output = num * i
#     print(f"{num} * {i} = {output}")


# num = 15
# i = num * 1
# output= num * i

# for i in range (1,11):
#     output = num * i
#     print(f"{num} * {i} = {output}")

# state = [ 'KA', 'KL', 'AP','TS']

# for i in state:
#     print(f"current value of state{state}")


# for i in state:
#     print(f"current state{state}")



# for i in "India":
#     print(i.upper())


# 12 * 1

# num = 12
# i = num * 1
# ouput = num * i

# for i in range(1,11):
#     ouput = num * i
#     print(f"{num} * {i} = {ouput}")


    # num = 12
# i = num * 1
# output = num * i


# for i in range (1,11):
#     output = num * i
#     print(f"{num} * {i} = {output}")



# list_of_list = [20, 13, 24, 36, 17, 13, 90]

# for i in list_of_list:
#     if i >= 18:
#       print(i)

# day = int(input("enter the number/n"))
# match day:
#     case x if x > 0 and x % 2 == 0:
#         print("even")
#     case x if x >  0 and x % 2 != 0:
#         print("odd")
#     case x if x < 0:
#         print("nagetive")
#     case _:
#         print("invalid")       


# list_of_list = [20, 13, 24, 36, 17, 13, 90]

# for i in list_of_list:
#     if i >= 18:
#         print(i)

# list_of_list = [20, 13, 24, 36, 17, 13, 90]

# adult = []
# children = []

# for i in list_of_list:
#     if i >= 18:
#         adult.append(i)
#     else:
#         children.append(i)

# print(f"adult ={adult}")
# print(f"childre ={children}")


# list_of_list = [20, 13, 24, 36, 17, 13, 90]


# adult = []
# children = []

# for i in list_of_list:
#     if i >= 18:
#         adult.append(i)
#     else:
#         children.append(i)

# print(f"adult = {adult}")
# print(f"children ={children}")


# for i in range(10):
#     print(i)
#     if i == 5:
#       break
    
#     print(f"value= {i}")


# for i in range(10):
#     print("*" * i)

# for i in range (5, 0,-1):
#     print("*" * i)

# for i in range(10):
#     print("*" * i)

# for i in range(10,0,-1):
#     print("*" * i)


# name = "Kiran"
# reverse = ""
# i = len(name) - 1  # i = 4

# while i >= 0:
#     reverse = reverse + name[i]
#     i = i - 1

# print(reverse)


# for i in range (1, 10):

#     continue
#     print(f"value of num")




# for i in range (10):
#     print(i)

#     if i == 5:
#     #   continue
#         break

#     print(f"the value of i id ={i}")
#     print("execution completed")
 

# for i in range (10):
#     print(i)
#     print(f"the value of i id ={i}")
#     continue

# set1 = {10, 20, 30, 40, 50}
# for i in set1:
#     print(i)


# dresses = { "id": 1,
#         "title": "Floral Summer Dress",
#         "price": 1499,
#         "description": "Lightweight floral dress suitable for summer.",
#         "category": "Women's Dress",
#         "image": "floral_dress.jpg",
#         "rating": {
#             "rate": 4.5,
#             "count": 120}
# }

# print(dresses.keys())
# print(dresses.values())
# print(dresses.items())

dresses = [
    {
        "id": 1,
        "title": "Floral Summer Dress",
        "price": 1499,
        "description": "Lightweight floral dress suitable for summer.",
        "category": "Women's Dress",
        "image": "floral_dress.jpg",
        "rating": {
            "rate": 4.5,
            "count": 120
        }
    },
    {
        "id": 2,
        "title": "Black Party Gown",
        "price": 2999,
        "description": "Elegant black gown for parties and events.",
        "category": "Women's Gown",
        "image": "black_gown.jpg",
        "rating": {
            "rate": 4.8,
            "count": 95
        }
    },
    {
        "id": 3,
        "title": "Blue Denim Dress",
        "price": 1999,
        "description": "Comfortable denim dress for casual wear.",
        "category": "Casual Dress",
        "image": "denim_dress.jpg",
        "rating": {
            "rate": 4.3,
            "count": 150
        }
    },
    {
        "id": 4,
        "title": "Red Maxi Dress",
        "price": 2499,
        "description": "Stylish red maxi dress with soft fabric.",
        "category": "Maxi Dress",
        "image": "red_maxi.jpg",
        "rating": {
            "rate": 4.6,
            "count": 85
        }
    },
    {
        "id": 5,
        "title": "Green Cotton Kurti",
        "price": 999,
        "description": "Simple and comfortable cotton kurti.",
        "category": "Kurti",
        "image": "green_kurti.jpg",
        "rating": {
            "rate": 4.2,
            "count": 200
        }
    }
]

# for el in dresses:
#     print(el)
# print(el)

# for el in dresses:
#     print(el.get('price'))

# for el in dresses:
#     print(el.get('title'))


# sum = 0

# for el in dresses:
#     print(f"{el.get('title')}   \t  {el.get('price')}")
#     print("_" * 20)
#     sum += el.get("price")


# print(f" {"total"} \t\t\t   {sum}")



# state = ['KA','KL','AP','TS']

# state.reverse()

# for i in state:
    # print(state)

# for state in state:
#     print(state)

# for i in enumerate(state):
#     print(i)



# for i, state in enumerate(state):
#     print(f"value of the index {i} is {state}")


# num = [2, 4, 6, 8]
# square = []
# for i in num:
#      square.append(i*i)
#      print(square)
     


# num = [2, 4, 6, 8]
# square = []
# for i in num:
#      square.append(i*i)
# print(square)  



# state = ['KA','KL','AP','TS']

# # output = [i.lower() for i in state]
# # print(output)




# state = ['KA', 'kl', 'ap', 'tS']

# upper = []

# for i in state: 
#     upper.append(i.upper())

# print(upper)




# state = ['KA', 'KL','AP','TS']

# upper = []

# for i  in state:
#     upper.append(i.upper())

# print(upper)


# name = "lishmitha"
# lower = []
# for i in name:
#     lower.append(i.upper())
# print(lower)


# name = "lishmitha"
# lower = ""
# for i in name:
#     lower = lower + i.upper()
# print(lower)


# num = [2, 3, 4, 5, 6]

# added = num.copy()

# added.append(7)

# print(added)

# num = [2, 3, 4, 5, 6]
# new_number = [7, 8, 9, 10, 11]

# for i in num:
#     # new_number.append(0)
#     num.pop()
#     # print(new_number)
# #     print(num)


# fac = 2
# for i in range(5,0,-1):
#     fac *= i
# print(fac)


# str1 ="india"

# rev = ""
# for i in str1:
#     rev = i + rev
# print(rev)

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1


# counter = 1
# while counter <= 3:
#     password = input ("enter into a password \n")
#     if password == "12345":
#       print("correct password")
#       counter = 4
#     else:
#        print("error, retry the password")
#        counter += 1
    

# counter = 5
# while counter <= 3:
#     password = input ("enter into a password \n")
#     if password == "12345":
#       print("correct password")
#       counter = 4
#     else:
#        print("error, retry the password")
#        counter += 1


# num = [2, 4, 6, 8]
# while num:
#     print(num.pop())
#     print(num)

# counter = 0
# while True:
#     print("Good moring")
#     counter += 1
#     if counter == 3:
#         break

# # 
# a = 5
# while a <= 10:
#     print(a)
#     a = a + 1


# a = 10
# while a <= 5:
#     print(a)
#     a = a + 1    

# a = 5
# while a >= 1:
#     print(a)
#     a = a - 1


# num = [1, 2, 3, 4, 5]
# square = []
# for i in num:
#     square.append(i ** 2)
# print(square)


# num = [1, 2, 3, 4, 5, 6, 7, 8]
# even = []
# for i in num:
#     if i % 2 == 0:
#         even.append(i)
    
# print(even)

# num = [1, 2, 3, 4, 5, 6, 7, 8]

# odd = []
# for i in num:
#     if i % 2 != 0:
#         odd.append(i)
# print(odd)




# for num in range(1, 10):
#     print(num)

# languages = ["python", "java","sql"]
# for i in languages:
#     print(i)

# num = [1, 2, 3, 4, 5, 6]
# square = []
# for i in num:
#     square.append(i ** 2)
# print(square)    

# num = [ 2, 4, 6, 8]
# evaluate = []
# for i in num:
#     evaluate.append(i * 2)
# print(evaluate)    

# num = [1, 2, 3, 4, 5, 6]
# even = []
# for i in num:
#     if i % 2 == 0:
#         even.append(i)
# print(even)    

# num = [1, 2, 3, 4, 5, 6]

# odd = []
# for i in num:
#     if i % 2 != 0:
#         odd.append(i)
# print(odd)      


# words = ["cat", "elphant","dog","tigar", "ant"]
# greater = []
# for i in words:
#     if len(i)>3:
#         greater.append(i)
# print(greater)    


# words = ["cat", "elphant","dog","tigar", "ant"]
# greater = []
# for i in words:
#     if len(i)>3:
#         greater.append(i)
# print(greater)    

# num= [-5, 10, -2, 15]
# positive = []
# for i in num:
#     if i>0:
#         positive.append(i)
# print(positive)  


# num= [-5, 10, -2, 15]
# negative = []
# for i in num:
#     if i <0:
#         negative.append(i)
# print(negative)     


# numbers = [1, 2, 3, 4, 5, 6]


# for i in numbers:
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")
    

# numbers = [1, 2, 3, 4, 5, 6]

# lable = []

# for i in numbers:
#     if i % 2 == 0:
#         lable.append("even")
#     else:
#         lable.append("odd")

# print(lable)

# numbers = [1, 2, 3, 4, 5, 6]

# lable = []
# for i in numbers:
#     if i % 2 == 0:
#         lable.append("even")
#     else:
#         lable.append("odd")
        
# print(lable)


# numbers = [10, -5, 20, -3, 0]
# result = []
# for i in numbers:
#     if i < 0:
#         result.append(0)
#     else:
#         result.append(1)
# print(result)     

# numbers = [10, -5, 20, -3, 0]
# result = []
# for i in numbers:
#     if i <0:
#         result.append(1000000)
#     else:
#         result.append(1)
#     print(result)

# numbers = int(input("Enter the number: "))

# numbers = range(1, 31)

# result = []

# for i in numbers:
#     if i % 2 == 0 and i % 5 != 0:
#         print("number is divisible")
#     else:
#         print("number is not divisible")


# data = int(input(f"enter the number"))

# if data % 2 == 0 and data % 5 !=0:
#     print("number is devisible")
# else:
#     print("number is not devisible")

# num = range(1, 50)
# result = []
# for i in num:
#     if i >10 and i <= 30:
#         result.append(i)
# print(result)     


# pair = []

# for x in [1, 2, 3]:
#     for y in [10,20]:
#         pair.append((x,y))
          
# print(pair)

# pair = []

# for x in [1, 2, 3]:
#    for y in [10, 20]:
#      pair.append((x,y))
# print(pair)


# count = 1
# while count <= 5:
#     print(count)
#     count = count + 1


# count = 1
# while count <= 10:
#     if count == 5:
#         break

#     print(count)
#     count = count + 1




# count = 10

# while count<= 15:
#     if count == 5:
#         print(count)
#         break
#     print(count)
#     count = count + 1

# count = 5
# while count <= 2:
#     if count ==1:
#         print(count)
#         break
#     print(count)
#     count= count + 1


# number =int(input(f"enter the number: "))
# while number <=0:
#     print("number invalied")
#     number= int(input(f"enter the number: "))
#     print("number is valie")

# for row in range (5):
#     for coloumn in range (5):
#         print("*",end=" ")

#     print()


for row in range (1, 6):
    for column in range(row):
        print(row,end=" ")
    print()

# for row in range (6,0,-1):
#     for column in range(row):
#         print("*", end=" ")
#     print()  


