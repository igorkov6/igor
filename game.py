# game.py
# =========================================
#               Игорь Ковалев igorkov6@gmail.com
# SkillFactory: FPW-2.0
# Модуль:       B5
#               B5.6 Итоговое практическое задание
# project:      игра крестики - нолики
# interpreter:  Python 3.8
# ide:          PyCharm 2021.3.2
# release:      v1.01 26.03.2022
#               v1.02 01.04.2022
#               v1.05 03.04.2022
#     игрок играет с компьютером
#     игровая стратегия не реализована -
#       компьютер выполняет случайный ход
#     после каждой игры право первого
#       хода переходит сопернику
#     размер игрового поля задается произвольно
# =========================================

import random

# =========================================
# константы
# =========================================

# размер игрового поля
# минимальное значение - 2
GAME_FIELD_SIZE = 3

# игровой символ
GAME_SYMBOL = ('0', 'X')

# =========================================
# глобальные переменные
# использование глобальных переменных
# оправдано наглядностью кода
# =========================================

# игровое поле
# YX  0    1    2
# 0 ['0', '0', '0']
# 1 ['0', '0', '0']
# 2 ['0', '0', '0']
game_field = list()

# признак первого хода
# False - первый ход игрока
# True - первый ход компьютера
game_first_move = False


# =========================================
# вспомогательные функции
# =========================================


# печать игрового поля
def game_field_separ_print():
    print('   +', end='')
    for i in range(GAME_FIELD_SIZE):
        print('-----+', end='')
    print()


def game_field_print():
    # верхняя строка легенды
    print(' ', end='')
    for i in range(GAME_FIELD_SIZE):
        print('    ', i, end='')
    print()
    # разделитель
    game_field_separ_print()
    # строки поля
    row = 0
    for line in game_field:
        print(row, end='')
        for col in line:
            print('  | ', col, end='')
        print('  |')
        row += 1
        # разделитель
        game_field_separ_print()


# ход компьютера
def game_comp_move():
    while True:
        
        # определить случайные координаты
        x, y = random.randint(0, GAME_FIELD_SIZE - 1), random.randint(0, GAME_FIELD_SIZE - 1)
        
        # если ячейка свободна - занять
        if game_field[y][x] == ' ':
            game_field[y][x] = GAME_SYMBOL[game_first_move]
            break


# ход игрока
def game_gamer_move():
    while True:
        
        # получить координаты ячейки
        n = input('Ваш ход (YX): ')
        
        # контроль ошибок ввода
        # детализация ошибок опущена
        # ради компактности и наглядности кода
        if len(n) == 2 and n.isdigit():
            y, x = int(n[0]), int(n[1])
            if y < GAME_FIELD_SIZE and x < GAME_FIELD_SIZE:
                
                # если ячейка свободна - занять
                if game_field[y][x] == ' ':
                    game_field[y][x] = GAME_SYMBOL[not game_first_move]
                    break
        
        print('\nОшибка!\nПовторите ввод.\n')


# контроль игровой ситуации
# образ игровой ситуации:
# --строки---   --столбцы--   диагонали
#  0   1   2     3   4   5     6   7
# 000 000 000   000 000 000   000 000
def game_is_over():
    # образ игровой ситуации
    game_image = ['' for i in range(GAME_FIELD_SIZE * 2 + 2)]
    
    # получить образы игровой ситуации
    for i in range(GAME_FIELD_SIZE):
        game_image[i] = ''.join(game_field[i])  # образы строк
        game_image[GAME_FIELD_SIZE * 2] += game_image[i][i]  # диагональ 00-11-22
        game_image[GAME_FIELD_SIZE + i] = ''.join(f[GAME_FIELD_SIZE - 1 - i] for f in game_field)  # образы столбцов
        game_image[GAME_FIELD_SIZE * 2 + 1] += game_image[GAME_FIELD_SIZE + i][i]  # диагональ 20-11-02
    
    # контроль выигрыша компьютера
    if GAME_SYMBOL[game_first_move] * GAME_FIELD_SIZE in game_image:
        print('\nЯ выиграл!\n')
        return True
    
    # контроль выигрыша игрока
    if GAME_SYMBOL[not game_first_move] * GAME_FIELD_SIZE in game_image:
        print('\nВы выиграли!\n')
        return True
    
    # контроль ничьей - нет свободных полей
    if ' ' not in (game_field[y][x] for y in range(GAME_FIELD_SIZE) for x in range(GAME_FIELD_SIZE)):
        print('\nНичья!\n')
        return True
    
    # игра продолжается
    return False


# =========================================
# главный цикл
# =========================================

random.seed()
while True:
    
    # запрос новой игры
    if input('\nНачать новую игру? (n - нет): ').lower() == 'n':
        print('\nBye!')
        break
    
    # инициализация нового игрового поля
    game_field = [[' ' for x in range(GAME_FIELD_SIZE)] for y in range(GAME_FIELD_SIZE)]
    
    # переход первого хода
    game_first_move = not game_first_move
    print('\nМои - ', GAME_SYMBOL[game_first_move], ', ваши - ', GAME_SYMBOL[not game_first_move])
    
    # определить первый ход компьютера
    is_comp_move_enabled = game_first_move
    
    # цикл игры
    while True:
        
        # ход компьютера
        # выполнить, если первый ход компьютера
        if is_comp_move_enabled:
            game_comp_move()
            if game_is_over():
                break
            print('\nМой ход:')
        is_comp_move_enabled = True
        
        # печать игрового поля
        game_field_print()
        
        # ход игрока
        game_gamer_move()
        if game_is_over():
            break
    
    # печать финального поля
    game_field_print()

# =========================================