# activity 1
# no= int(input("Enter a number:"))
# original=no
# reverseno=0
# while no !=0:
#     digit=no%10
#     reverseno=reverseno*10+digit
#     no//=10

# if original==reverseno:
#     print("It is a pallindrom number")
# else:
#      print("It is not pallindrom number")
# number=183
# number//=10
# print(number)
# activity 2
n1= int(input("Enter a number:"))
n2= int(input("Enter a number:"))
while n2:
    n3=n2
    n2=n1%n2
    n1=n3
print(n1)