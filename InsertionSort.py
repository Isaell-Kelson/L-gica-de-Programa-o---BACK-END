def exercicio(array):
    
    for step in range(1, len(array)):
        key = array[step]
        a = step - 1

        while a >= 0 and key < array[a]:
            array[a + 1] = array[a]
            a = a - 1

        array[a + 1] = key


data = [1, 9, 7, 13, 11, 21, 5, 17, 3, 15, 19, 23, 31, 29, 33, 41, 39, 35, 47, 43, 53, 49, 59, 57, 51, 63, 71, 87, 73, 65,]
exercicio(data)
print('Ordem crescente')
print(data)