print("        ________   ________    _________  ____________;_")
print("       - ______ \ - ______ \ / _____   //.  .  ._______/")
print("      / /     / // /     / //_/     / // ___   /")
print("     / /     / // /     / /       .-'//_/|_/,-'")
print("    / /     / // /     / /     .-'.-'")
print("   / /     / // /     / /     / /")
print("  / /     / // /     / /     / /")
print(" / /_____/ // /_____/ /     / /")
print(" \________- \________-     /_/")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
x = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n')
if x == "left":
    y = input(
        'You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
    )
    if y == "wait":
        z = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n"
        )
        z = z.lower()
        if z == "red":
            print("Burned by a fire.\nGame Over.")
        elif z == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif z == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by a trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
