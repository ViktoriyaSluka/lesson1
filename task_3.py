def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    quantity_of_percent = int(input("Введите число от 1 до 100: "))
    special_quantity = (11, 12, 13, 14)
    end_of_percent = quantity_of_percent % 10
    if quantity_of_percent in special_quantity:
        print(quantity_of_percent, "процентов")
    elif end_of_percent in (2, 3, 4):
        print(quantity_of_percent, "процента")
    elif end_of_percent == 1:
        print(quantity_of_percent, "процент")
    else:
        print(quantity_of_percent, "процентов")
    return number

if __name__ == '__main__':
    for n in range(1, 101):
        print(transform_string(n))