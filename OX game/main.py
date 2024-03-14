positions:list[int] = list(number for number in range(1, 10))

MODE_HUMAN_VS_HUMAN = '1'
MODE_HUMAN_VS_AI = '2'

def show_bord() -> None:
	for row in range(3):
		print(f'{positions[row*3]}\t{positions[row * 3 + 1]}\t{positions[row * 3 + 2]}\t')


def game_logic(user_choice:int, user_char:str):
	if 9 < user_choice < 1 or positions[user_choice-1] in ('X', '0'):
		return False
	
	positions[user_choice-1] = user_char
	return True


def check_win(positions:list):
	win = False
	win_cells:tuple[tuple] = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),	
		(0, 3, 6), (1, 4, 7), (2, 5, 8), 
		(0, 4, 8), (2, 4, 6) 				
	)

	for item in win_cells:
		if (positions[item[0]] == positions[item[1]] and positions[item[0]] == positions[item[2]]):
			win = positions[item[0]]
			
	return win

def computer_step(human:str, ai:str):
	available_steps:list[int] = [item-1 for item in positions if type(item) == int]
	best_steps:tuple[int] = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	
	for char in (ai, human):
		for pos in available_steps:
			board_ai:list = positions[:]
			board_ai[pos] = char
			if (check_win(board_ai) != False):
				return pos
			
	for pos in best_steps:
		if pos in available_steps:
			return pos

	return False

def next_player(current_player):
	if current_player == "X":
		return "O"
	return "X"

def start_game(mode) -> None:
	current_player:str = "X"
	ai_player:str = "O"
	game_counter:int = 1
	show_bord()	

	while (game_counter < 9) and (not check_win(positions)):
		print('-' * 30)
		

		user_choice:int = int(input(f"{current_player}, you're turn. Choose a cell:\t"))

		if(game_logic(user_char=current_player, user_choice=user_choice)):		
			print('-' * 30)
			
			current_player = next_player(current_player)

			game_counter += 1

			if mode == MODE_HUMAN_VS_AI:
				if type(computer_step("X", "O")) == int:				
					positions[computer_step("X", "O")] = ai_player
					current_player = next_player(current_player)
					game_counter += 1
			
			show_bord()
			
		else:
			print("Mistake! Try again")

		if game_counter == 10:
			print("Draw. Friendship won.")
			break

	if check_win(positions):
		print(f'{check_win(positions)} won')

print("Добро пожаловать в Крестики-нолики!")

mode = 0
while mode not in (MODE_HUMAN_VS_HUMAN, MODE_HUMAN_VS_AI):
	print("Режимы игры:\n1 - человек vs человек\n2 - человек vs робот")
	mode = input("Выберите режим:\n")

start_game(mode)