def myfunc():
    n = int(input("Введите количество дел: "))
    list1 = []

    for i in range(n):
        a = input("Введите дело: ")
        list1.append(a)

    with open("mydz.txt", "w") as file:
        for i in range(0, n, 2):
            file.write(list1[i] + " ")

    print("Список дел записан")


