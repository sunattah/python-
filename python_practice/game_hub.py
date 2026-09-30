input_list = ["Minecraft", "Roblox", "Minecraft", "FIFA", "Roblox", "Fortnite"]
convert = set(input_list)
print(convert)
clean_libery = list(convert)
print(clean_libery)

available_games = "Witcher 3", "Cyberpunk", "GTA V"
user_game = input("enter your game: ")
if user_game not in available_games:
    print("Invalid movie")
else:
    print("correct option the film you are looking for it here")