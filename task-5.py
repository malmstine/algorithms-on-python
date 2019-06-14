# Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв

let_1 = input("Введите первую букву: ")
let_2 = input("Введите вторую букву: ")

c_let_start = ord('a') - 1
c_let_1 = ord(let_1)
c_let_2 = ord(let_2)

pos_let_1 = c_let_1 - c_let_start
pos_let_2 = c_let_2 - c_let_start
spacing = abs(c_let_2 - c_let_1)

print(f'Позиция 1 буквы {pos_let_1}\n'
      f'Позиция второй буквы {pos_let_2}\n'
      f'Расстояние между ними {spacing}')