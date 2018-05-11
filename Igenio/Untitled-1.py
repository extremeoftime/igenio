board = list(range(1,10))

def drow_board(board):
    for i in range(3):
        print(board[0+i*3],board[1+i*3],board[2+i*3])

def take_input(player_token):
    valid=False

while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue

if player_answer>=1 and player_answer<=9:
    print('tttt')