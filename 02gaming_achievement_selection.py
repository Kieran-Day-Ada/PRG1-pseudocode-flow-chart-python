print("=== Gaming Achievement Checker ===")
    
# Input
player_score, time_played_hours, enemies_defeated = -1, -1, -1


def non_zero_input(input_prompt):
    while True:
        user_input = input(input_prompt)

        try:
            value = int(user_input)
            if value >= 0:
                return value
            else:
                print("This number cannot be negative. Please try again.")
        except ValueError:
            print("You must input a number. Please try again.")


    
player_score = non_zero_input("Enter your player score: ")
time_played_hours = non_zero_input("Enter hours played: ")
enemies_defeated = non_zero_input("Enter number of enemies defeated: ")


# Selection logic
if player_score >= 15000 and time_played_hours >= 100:
    achievement = "Legend"
elif player_score >= 10000 and time_played_hours >= 50:
    achievement = "Master Player"
elif enemies_defeated >= 1000:
    achievement = "Combat Expert"
elif time_played_hours >= 20:
    achievement = "Dedicated Gamer"
elif player_score >= 5000:
    achievement = "Rising Star"
else:
    achievement = "Newcomer"

"""
Prediction on running program 2 with the following inputs:
Score: 12000
Hours played: 60
Enemies defeated: 800

Prediction:
- Inputs saved into the corresponding variables
- First if statement evals to true so achievement = "Master Player"

Outputs:
"Congratulations! You've earned: Master Player
You've unlocked the secret bonus level!"

Which condition is checked first in the if-elif chain?
- The first one that would assign master player if true.

What achievement would you get with score=6000, hours=15, enemies=500?
- Rising Star

"""

# Output
print(f"\nCongratulations! You've earned: {achievement}")

if achievement == "Master Player":
    print("You've unlocked the secret bonus level!")