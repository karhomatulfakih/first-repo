#Game tic tac toe
import random
#Tampilan game menyala
    #o	Value board – Format 2D
board = [[1,2,3],
         [4,"X",6],
         [7,8,9]]
    #o	Bentuk fisik board
def board_pyshical_form(board):
    print("+-------+-------+-------+")
    for r in range(3):
        print("|       |       |       |")
        print(f"|   {board[r][0]}   |   {board[r][1]}   |   {board[r][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    #o	Tentukan mana lokasi yang kosong, yang bisa dipilih oleh user
def free_value(board):
    free = []
    for row in board:
        for cell in row:
            if cell != "O" and cell != "X":
                free.append(cell)
    return free

#User melangkah
def user_move(board):
    while True:
    #o	Butuh input – input harus valid 1-9
        try:
            move = int(input("Please enter your move:"))
            if move < 1 or move > 9:
                print("input must be between 1-9")
                continue
        except:
            print("Input invalid, please enter valid number!")
            continue
    #o	Kemudian input yang 1-9 itu dikonversikan ke 2D karena valuenya berformat 2D
        row = (move-1) // 3
        col = (move-1) % 3
    #o	Cek apakah pilihan user benar ? misal tidak memilih lagi yang sudah bertanda ‘X’ atau ‘O’
        if board[row][col] == "X" or board[row][col] == "O":
            print("The position already occupied, choose another number!")
            continue
    #o	Kalau sudah memilih berarti value angka itu berubah jadi ‘O’
        board[row][col] = "O"
        break
#Komputer melangkah
def robot_move(board):
    #o	Komputer memilih angka random dari value yang tersisa, yang tidak ‘X’ atau ‘O’
    free = free_value(board)
    move = random.choice(free)
    #o	Pilihan ini diterjemahkan ke 2D
    row = (move-1) // 3
    col = (move-1) % 3
    #o	Kalau sudah memilih berarti value yang dipilih dirubah jadi ‘X’
    board[row][col] = "X"
#Cek apa sudah ada yang menang
def victory_condition(board, sign): 
    #o	Cek apa 3 baris ada yang valuenya sama ? ‘X’ atau ‘O’
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == sign:
            return True
    #o	Cek apa 3 kolom ada yang valuenya sama ? ‘X’ atau ‘O’
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True
    #o	Cek 2 diagonal ada yang valuenya sama ? ‘X’ atau ‘O’
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        return True
#Jika tidak ada ruang lagi berarti permainan imbang
def draw_condition(board):
    #o	Jika lokasi kosong yang bisa dipilih habis berarti game imbang
    free = free_value(board)
    return len(free) == 0
    

#Mekanisme Game
while True:
    board_pyshical_form(board)
    free_value(board)
    user_move(board)
    if victory_condition(board, "O"):
        print("You won!")
        break
    if victory_condition(board, "X"):
        print("Robot won! Accept robot supremacy")
        break
    if draw_condition(board):
        print("It's a Tie, We reign together!")
        break
    robot_move(board)
    if victory_condition(board, "O"):
        print("You won!")
        break
    if victory_condition(board, "X"):
        print("Robot won! Accept robot supremacy")
        break
    if draw_condition(board):
        print("It's a Tie, We reign together!")
        break
    