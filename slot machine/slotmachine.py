
import random 

symbols = ['🍒', '🍇', '🍉', '7️⃣']

def play():
    result = random.choices(symbols, k=3)
    print("|".join(result))
    if result.count('7️⃣') == 3:
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

while True:
    play()
    # Ask if the player wants to play again
    play_again = input("Do you want to play again 😁? (Y/N): ").strip().upper()
    if play_again != 'Y':
        print("Goodbye! 👋")
        break