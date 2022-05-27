def sum_list_1(my_list) -> int:
    """* Создать список, состоящий из кубов нечётных чисел от 1 до 1000"""

    for i in range(1, 1001):
        if i % 2 != 0:
            cube = i ** 3
            my_list.append(cube)

    return my_list


def sum_list_2(my_list) -> int:
    """Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7"""

    division_list = []
    for i in my_list:
        temp = i
        amount = 0
        while temp != 0:
            amount += temp % 10
            temp //= 10
        if amount % 7 == 0:
            division_list.append(i)

    return division_list

def sum_list_17(my_list) -> int:
    """К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
  этого списка, сумма цифр которых делится нацело на 7"""

    i = 0
    for element in my_list:
        my_list[i] += 17
        i += 1

    return my_list

if __name__ == '__main__':
    my_list = []
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)
    result_3 = sum_list_17(my_list)
    print(result_3)
    result_4 = sum_list_2(my_list)
    print(result_4)