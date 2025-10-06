print("=== Spotify Playlist Mood Detector ===")
    
# Input
playlist_name = input("Enter your playlist name: ")
playlist_size = int(input("How many songs in your playlist? "))

# Initialise counters
happy_songs = 0
sad_songs = 0
energetic_songs = 0
chill_songs = 0
romantic_songs = 0

# Iteration through playlist
for i in range(playlist_size):
    print(f"\nSong {i+1}:")
    song_mood = input("Enter mood (happy/sad/energetic/chill): ").lower()
    
    if song_mood == "happy":
        happy_songs += 1
    elif song_mood == "sad":
        sad_songs += 1
    elif song_mood == "energetic":
        energetic_songs += 1
    elif song_mood == "chill":
        chill_songs += 1
    else:
        romantic_songs += 1

def most_common_mood():
    mood_totals = [happy_songs, sad_songs, energetic_songs, chill_songs, romantic_songs]
    mood_types = ["happy", "sad", "energetic", "chill", "romantic"]

    largest = 0
    index = 0 # Counter variable used to set what type of mood was seen as the largest.
    most_common = ""
    for mood_count in mood_totals: # Check each mood_total one by one.
        if mood_count > largest: # Is the current mood total being looked at the biggest we've seen yet?
            largest = mood_count # If so, update the largest variable to the largest value we just saw.
            most_common = str(mood_types[index]) # Since we found a new largest value, update what mood type this was seen in.
        index += 1

    return most_common # Return the type of mood that was the most common.


# Calculate totals and percentages
total_songs = happy_songs + sad_songs + energetic_songs + chill_songs

"""
Prediction on running program 3 with the following inputs:
- Playlist: "My Vibes"
- Songs: 5
- Moods: happy, sad, energetic, happy, chill

Prediction:
- Inputs saved into the corresponding variables
- Eventually happy_songs = 2, sad_songs = 1, energetic_songs = 1, chill_songs = 1

Outputs:
"Your playlist 'My Vibes' analysis:
2 happy songs (40%)
1 sad songs (20%)
1 energetic songs (20%)
1 chill songs (20%)
Overall mood: Upbeat! :)

How does the counter system work?
- Checks against a user input and increments a specific counter based on the value.

What determines the "Overall mood"?
- The amount of happy songs relative to the amount of sad songs.

"""

# Output results
print(f"\nYour playlist '{playlist_name}' analysis:")
print(f"{happy_songs} happy songs ({(happy_songs/total_songs)*100:.1f}%)")
print(f"{sad_songs} sad songs ({(sad_songs/total_songs)*100:.1f}%)")
print(f"{energetic_songs} energetic songs ({(energetic_songs/total_songs)*100:.1f}%)")
print(f"{chill_songs} chill songs ({(chill_songs/total_songs)*100:.1f}%)")
print(f"{romantic_songs} romantic songs ({(romantic_songs/total_songs)*100:.1f}%)")
print(f"Most common mood in your playlist: {most_common_mood()}")

if happy_songs > sad_songs:
    print("Overall mood: Upbeat! 😊")
else:
    print("Overall mood: Contemplative 🤔")