

print('************************Welcome to Algorithms***********************')

My_number = input('Please type your number, then press ENTER: ')
print('Your Number is: %s. ' % My_number)

# Convert the user's string input into an integer
My_Num = int(My_number)

FinSum = 0
tempNum = []
# Numbers are put into a list tempNum
while My_Num > 0:
    tempNum.append(My_Num)
    My_Num = My_Num - 1

# Add all the numbers in the list
for i in tempNum:
    FinSum = FinSum + i
print(FinSum)
print('***********************************************************************')
print('\n')
print('******************************Welcome to Max Number Finder********************')

Num1 = input('Please type your 1st number, then press ENTER: ')
Num2 = input('Please type your 2nd number, then press ENTER: ')
Num3 = input('Please type your 3rd number, then press ENTER: ')


Num1 = int(Num1)
Num2 = int(Num2)
Num3 = int(Num3)
tempBig = 0


if Num1 > Num2:
    tempBig = Num1
elif Num2 > Num1:
    tempBig = Num2


if tempBig > Num3:
    print('The Largest Number is ', tempBig)
else:
    print('The Largest number is ', Num3)

print('***********************************************************************')
print('\n')

print('******************************Welcome to Even & Odd Number Counter********************')
E_O_Num = input('Please type number for analysis, then press ENTER: ')
# E_O_Num = int(E_O_Num)

evenCounter = 0
oddCounter = 0

digits = []
for i in range(len(E_O_Num)):
    digits.append(int(E_O_Num[i]))
    # digits[i] = int(E_O_Num[i])
print(digits)

for i in range(len(digits)):
    if digits[i] % 2 == 0:
        evenCounter = evenCounter + 1
    else:
        oddCounter = oddCounter + 1

print('Your number contains the following amount of even digits: ', evenCounter)
print('Your number contains the following amount of odd digits: ', oddCounter)



