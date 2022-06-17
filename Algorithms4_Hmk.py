counter = 0
numbers = [7, 3, 5, 6, 4, 10, 3, 2]
print('*******************************************Welcome to Even First**************************************************')
print('Given: ', numbers)
print('\n')
for j in range(len(numbers)):
    int(numbers[j])

for i in range(len(numbers)):
    if (numbers[counter] % 2) != 0:
        numbers.append(numbers[counter])
        numbers.remove(numbers[counter])
    counter = counter + 1
print('Final Output: ', numbers)

print('*******************************************Welcome to increment a Number**********************************************')
yourArray = []
n = int(input('Enter the number of elements desired, in your array; then press ENTER: '))
print('Enter your numbers. Press enter after each number.')
for i in range(0, n):
    num = int(input())
    yourArray.append(num)


def update_array(array):
        for x in range(len(array)):
            array[x] = array[x] + 1

        for i in range(len(array)):
            if array[0] == 2:
                array[0] = array[0] - 1
            if array[i] > 9:
                array[i] = array[i] * 0
        print(array)


update_array(yourArray)



