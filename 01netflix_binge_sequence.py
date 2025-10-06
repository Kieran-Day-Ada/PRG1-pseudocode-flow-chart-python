print("=== Netflix Binge Calculator ===")
    
# Input
series_name = input("Enter the series name: ")
episodes_per_season = int(input("Enter episodes per season: "))
number_of_seasons = int(input("Enter number of seasons: "))
episode_length_minutes = int(input("Enter episode length in minutes: "))
episodes_per_day = int(input("Number of episodes to watch per day: "))

# Calculations
total_episodes = episodes_per_season * number_of_seasons
total_minutes = total_episodes * episode_length_minutes
total_hours = total_minutes / 60
total_days = (total_episodes / episodes_per_day) * (total_hours / 24)

"""
Prediction on running program 1 with the following inputs:
Series: "Stranger Things"
Episodes per season: 8
Seasons: 4
Episode length: 50 minutes

Prediction:
- Inputs saved into the corresponding variables
- total_episodes calculated as 8 * 4 = 32
- total_minutes calculated as 32 * 50 = 1600
- total_hours calculated as 1600 / 60 = 26.666 etc.
- total_days calculated as 1.111 etc.

Outputs:
"To binge-watch Stranger Things you need:
26.7 hours
That's 1.1 full days of your life!"


How does the program calculate total hours?
- Input num eps per season
- Input num seasons
- Input episode duration (minutes)
- Multiply all three together, divide by 60 for minutes -> hours.

What happens if you enter 0 seasons?
- It will return a duration of 0

"""

# Output
print(f"\nTo binge-watch {series_name} you need:")
print(f"{total_hours:.1f} hours")
print(f"That's {total_days:.1f} full days of your life!")

if total_days > 7:
    print("You are unable to watch this series in a single week. :(")