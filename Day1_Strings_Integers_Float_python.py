# Print Welcome message
print("Hello User!!!!")

#Strings
Var = "Sowjanya"
print(Var)

Var1 = 1
print(Var1)

Var2 = 0.5
print(Var2)

Var3 = 'Monkey\'s' #If we want to add single quote inside the variable and need to add Babie's then we should add Babies\'s then python understood s where Single qute ends
print(Var3)

Var4 = "Monkey's" #Diff between Double quote and single quote
print(Var4)

Var5 = """ADAS Systems Engineer with 8+ years of experience, now transitioning into AI/ML Engineering.
Following a focused 60-day plan to build skills in Python, Deep Learning, Computer Vision and Automotive AI.
Goal: Land an AI/ML Systems Engineer role in Chennai's automotive industry by mid-2026."""
print(Var5)

#How many CHaraccters in my Varaible
Var6 = "Sowjanya"
print(len(Var6))

#To access individual characted in Var6 we need to use Square Bracket
print(Var6[0])
print(Var6[1])
print(Var6[2])
print(Var6[3])
print(Var6[4])
print(Var6[5])
print(Var6[6])
print(Var6[7])

print(Var6[len(Var6)-1]) #to access the last charcter in variable need to use length of the variable -1

#Range of characters
print(Var6[0:6])
print(Var6[:6])

print(Var6[6:])

print(Var6.lower()) # To print all charcters in Lowercase

print(Var6.upper()) # To print all charcters in Uppercase

print(Var6.count('Sowjanya')) # to count the number of characters in a string

print(Var6.count('a')) #to count a singgle character in an argument 

print(Var6.find('Sowjanya'))  #To find the index where character can be found so it retuen the first index number

print(Var6.find("Automotive")) #To find unknown word it return negative number because it doesn't exist

Var7 = Var6.replace('Sowjanya', "Automative")
print(Var7)
print(Var6)

Greeting = "Hello"
name = "Sowjanya"

Name = Greeting + ', ' + name + ' '+"Welcome!!" #Too lengthy
print(Name)

Name = "{}, {} Welcome!!" . format(Greeting, name) #placeorders
print(Name)

Name = f"{Greeting}, {name} Welcome!!" . format(Greeting, name) #fstring
print(Name)

Name = f"{Greeting}, {name.upper()} Welcome!!" . format(Greeting, name) #fstring with Uppercase
print(Name)

Name = f"{Greeting}, {name.lower()} Welcome!!" . format(Greeting, name) #fstring with Lowercase
print(Name)

print(help(dir))
print(help(str.lower))

#Integers and float
num = 3
print(type(num)) #Type of varibale it shows

num1 = 3.46
print(type(num1)) #Type of varibale it shows

#"""Arthematic Operators
# Add        - 3 + 2 
# Sub        - 3 - 2
# Mul        - 3 * 2
# Div        - 3 / 2
# Floor Div  - 3 // 2
# Exponent   - 3 ** 2
# Modulus    - 3 % 2 """

print(3**2) 
print(3//2) 
print(3 % 2) #output is remainder

print(3 + (2 * 4))
print((3 + 2) * 4)

num = 1
num = num + 1
print(num)

num1 = 1
num1 += 1
print(num1)

#absolute value
print(abs(-4))
print(round(3.75))
print(round(3.75,1))

#"""Comparisions
# Equal            - 3 == 2 
# Not Equal        - 3 != 2
# Greater          - 3 > 2
# Lessthan         - 3 < 2
# Greater or equal - 3 >= 2
# Less or Equal   - 3 <= 2"""

num3 = 4
num4 = 5
print(num3 == num4)
print(num3 != num4)
print(num3 > num4)
print(num3 < num4)
print(num3 >= num4)
print(num3 <= num4)

num_1 = '1000'
num_2 = '2000'
print(num_1 + num_2)

num_1 = int("1000")
num_2 = int("2000")
print(num_1 + num_2)