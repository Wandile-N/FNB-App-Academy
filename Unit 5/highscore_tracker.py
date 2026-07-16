while True:
    score = input("Enter the game score: ")
    try:
        if int(score) >= 100 :
            print("Wow! That's new high score")
            old_score = int(score)
        elif int(score) >= 100 and old_score != -1:
            print("Wow! Good score, keep playing!")
        else:
            print("Good try, keep playing!")
        
    except ValueError:
        if str(score).strip().lower() == "stop":
            print("Game session ended!")
            break
        else:
            print("Enter score please!")