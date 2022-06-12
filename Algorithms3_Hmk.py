import math
print('*************************Welcome to Below The Arithmetical Mean*********************')

List1 = [1, 3, 5, 6, 4, 10, 2, 3]
List2 = []
List3 = [198, 3, 4, 9, 10, 9, 2]
List4 = []


def below_mean(the_list):
    list2 = []
    e_sum = 0
    float(e_sum)

    for i in the_list:
        x = float(i)
        e_sum = e_sum + x

    div = len(the_list)
    avg = e_sum / div
    print('The mean is: ', avg)
    for j in the_list:
        if j < avg:
            list2.append(j)
    return list2


l: list = below_mean(List1)
print('The updated list: ', l)
print('************************************************************************************************')
print('**************************************Welcome to Two Lowest Elements****************************')

x = min(List3)
List3.remove(x)

for i in List3:
    if i >= x:
        List4.append(i)
y = min(List4)
print('The two lowest values are: ', x, 'and', y)
print('\n')
print('**********************************************************************************************')




