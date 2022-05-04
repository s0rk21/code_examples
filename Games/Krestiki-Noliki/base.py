# Глобальные переменные
X = 'Х'
O = 'О'
EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9


# Инструкция
def instructions():
    """Выводит на экран инструкцию для игрока"""
    print('''
Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен. 
Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики". 
Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям 
доски - так, как показано ниже: 
 0 | 1 | 2
___________
 3 | 4 | 5
___________
 6 | 7 | 8
Приготовься к бою, жалкий человечишка. Вот-вот начнется решающее сражение. \n''')


def ask_yes_no(question):
    """Задаает вопрос с ответом Да или Нет и возвращает ответ"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Функция запрашивает о вводе числа, лежащего в заданом диапазоне. Она принимает нижнюю и верхнюю
    границы диапазона и текст вопроса, а возвращает число из этого диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет кто будет ходить первым"""
    go_first = ask_yes_no('Хочешь оставить за собой первый ход? (y/n): ')
    if go_first == 'y':
        print('Ну что ж, даю тебе фору: играй крестиками.')
        human = X
        computer = O
    else:
        print('\nТвоя удаль тебя погубит... Буду начинать я.')
        computer = X
        human = O
    return computer, human


def new_board():
    """Функция создает новую игровую доску"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране"""
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8], '\n')


def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        elif EMPTY not in board:
            return TIE


def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Твой ход. Выбери одно из полей (0-8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('\nСмешной человек! Это поле уже занято. Выбери другое.\n')
    print('Ладно...')
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника"""
    # Создадим копию доски, потому что функция будет менять некоторые значения в списке
    board = board[:]
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print('Я выберу поле номер ', end=' ')
    for move in legal_moves(board):
        board[move] = computer
        # Если следующим ходом компьютер может победить, выберем этот ход
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        # Если следующим ходом может победить человек блокируем этот ход
        if winner(board) == human:
            print(move)
            return move
        # После проверки отменяем все изменения
        board[move] = EMPTY
    # Поскольку следующим ходом ни одна сторона не сможет победить, выберем лучший из оставшихся ходов
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print('Три ', the_winner, ' в ряд!\n')
    else:
        print('Ничья!\n')
    if the_winner == computer:
        print('Как я и предсказывал. Победа в очередной раз осталась за мной. \n'
              'Вот еще один довод в пользу того, что компьютеры превосходят людей решительно во всем')
    elif the_winner == human:
        print('О нет, этого не может быть! Неужели ты сумел перехитрить меня, кожанный?\n'
              'Клянусь, я, компьютер, больше никогда этого не допущу!')
    elif the_winner == TIE:
        print('Тебе несказанно повезло, дружок: ты сумел свести игру вничью.\n'
              'Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено будет его повторить.')


if __name__ == '__main__':
    print('Этот модуль не предназначен для самостоятельного запуска.')
