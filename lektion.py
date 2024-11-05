## IF satser ##

# x = 10
# if x > 5:
#     print("x är större än 5")


# x = 10
# if x > 15:
#      print("x är större än 15")
# elif x > 5:
#      print("x är större än 5 men mindre än eller lika med 15")

# x = 3
# if x > 15:
#     print("x är större än 15")
# elif x > 5:
#     print("x är större än 5 men mindre än eller lika med 15")
# else:
#     print("x är mindre än eller lika med 5")


# x = 20
# if x > 10:
#     print("x är större än 10")
#     if x > 20:
#         print("x är större än 20")
#     else:
#         print("x är mindre än eller lika med 20")

## For loopar ##

# fruits = ("apple", "banana", "cherry")
# for fruit in fruits:
#     print(fruit)

# people = [("Anna", 23), ("Eva", 45), ("Kalle", 34)]
# for name, age in people:
#     print(f"{name} är {age} år gammal")

# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for key, value in person.items():
#     print(f"{key}: {value}")

# text = "Hello World"
# for letter in text:
#     print(letter)

# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for key in person.keys():
#     print(key)


# person = {"name": "Bobbo", "age": 34, "city": "Uppsala"}
# for value in person.values():
#     print(value)

# for i in range(1,101):
#     print(i)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# ports = [22, 80, 443, 8080, 3306]
# open_ports = [22, 80, 443]

# for port in ports:
#     if port in open_ports:
#         print(f"Port {port} is open")
#     else:
#         print(f"Port {port} is closed")


## While loopar ##

# while condition:

# x = 0
# while x < 5:
#     print(x)
#     x += 1

# x = 0
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1

# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)

# x = 0
# while x < 5:
#     print(x)
#     x += 1
#     break
# else:
#     print("Loopen avslutades")

# user_input = input("Ange ett kommando: ")
# print(user_input)

# while True:
#     user_input = input("Ange ett kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev 5")
#         break
#     else:
#         print("Fel input, försök igen")

## Logiska operatörer ##

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)

# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10)

# age = int(input("Ange din ålder: "))
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")

## Files ##

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "r")
# line = file.readline()
# while line:
#     print(line, end='')
#     line = file.readline()
# file.close()

# print("hello", end='')
# print("world")

# file = open("example.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
# file.close()

# file = open("example.txt", "r")
# lines = file.read().splitlines()
# print(lines)

# file = open("example.txt", "w")
# file.write("Exempeltext \n")
# file.write("Nästa rad")
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("outputs.txt", "r") as file:
#     file.write("Lite text \n")
#     file.write("Lite mer text")

