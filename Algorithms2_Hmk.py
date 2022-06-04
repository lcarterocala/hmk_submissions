import math

print('\n')
print('*******************************Welcome to String Splitter****************************')
yourString = input('Please type your string; then press ENTER: ')
numString = len(yourString)
stringList1 = []
stringList2 = []

if numString % 2 == 0:
    evenString = numString // 2
    e_splitPoint = evenString
    stringList1 = yourString[:e_splitPoint]
    stringList2 = yourString[e_splitPoint:]
    print(stringList2 + stringList1)
else:
    oddString = numString // 2
    o_splitPoint = math.ceil(oddString)
    stringList1 = yourString[:o_splitPoint]
    stringList2 = yourString[o_splitPoint:]
    print(stringList2 + stringList1)
print('*************************************************************************************')
print('****************************************Welcome to Unique String finder**************')
uniqueString = input('Please type your string; then press ENTER: ')
setString = set()
listString = []

for itm in uniqueString:
    listString.append(itm)
    setString.add(itm)

if len(setString) == len(listString):
    print('TRUE, characters are unique!')
else:
    print('FALSE, characters are not unique.')

print('**************************************************************************************')
# print("Using the split() method")
# a = "Hello, World!"
# print(b.split("n"))
# print("\n")


# print("Creative Assignment")
# print("Puting the split string into a new list[] using a for loop")
# newlist = []
# txt = a.split(",")
# for x in txt:
#    newlist.append(x)
# print(newlist)
# print("\n")