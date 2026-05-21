import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 75)
    # Fetch the hiscore 
    with open("Day10/practice/hiscore.txt", "r") as f:
        hiscore= f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}, The higest score is: {hiscore}")
    if(score > hiscore):
        print("Congratulations! You achieved a new high score!")
        # write this hiscore to the file
        with open("Day10/practice/hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print("Game Over! Better luck next time.")

    return score

game()