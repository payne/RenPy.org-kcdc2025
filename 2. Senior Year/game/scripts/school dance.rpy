# Senior Year - school dance.rpy
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

# This is an example of a “dating simulator” game, a very popular genre
# in visual novels. This uses a minimal amount of Python code for managing
# game state, which in this game is made up of three variables for keeping
# track of the player's relationship points with each character.
#
# This script is for the third phase of the game, which shows the story’s
# resolution, based on the player’s choices in phases one and two.


# Phase 3:
# The school dance, a week later
# ------------------------------

label week_later:
    play music "music/funkorama.mp3"

    scene dance
    with fade
    
    narrator "A week has passed, and it’s time for the school’s “Welcome Back” dance..."
    
    # Which ending?
    # -------------

    if alex_points >= 3:
        jump alex_ending
    elif sam_points >= 3:
        jump sam_ending
    elif jordan_points >= 3:
        jump jordan_ending
    else:
        jump friend_ending


# The “Alex” ending
# -----------------

label alex_ending:
    show alex at center
    
    alex "Hey, [player_name]! Want to dance?"
    
    mc "I’d love to, Alex."
    
    narrator "You and Alex spend the evening talking about art, dreams, and the future."
    narrator "A beautiful friendship has blossomed, with potential for something more."
    
    show alex dokidoki at center

    alex "Thank you for appreciating my art... and me."
    
    mc "Thank you for sharing your passion with me."
    
    narrator "Sometimes the best relationships start with shared understanding and mutual respect."
    
    jump credits


# The “Sam” ending
# ----------------

label sam_ending:
    show sam
    
    sam "This dance is nice, but want to step outside and talk under the stars?"
    
    mc "That sounds perfect, Sam."

    scene school night with fade
    show sam at center

    narrator "You and Sam step outside, away from the noise of the dance."
    narrator "You spend hours discussing everything from philosophy to your hopes for the future."
    narrator "Intellectual compatibility has grown into something deeper."
    
    mc "I love how we can talk about anything together."
    
    show sam blushing at center

    sam  "Great minds think alike, but great hearts understand each other."
    
    narrator "A connection built on respect and shared values is a strong foundation."
    
    jump credits


# The “Jordan” ending
# -------------------

label jordan_ending:
    show jordan
    
    jordan "I wrote a song inspired by our conversations. Want to hear it?"
    
    mc "I’d be honored, Jordan."

    scene classroom night
    show jordan at center

    narrator """Jordan leads you out of the gym and into a nearby classroom. In the quiet
    of the empty room, he plays a heartfelt song just for you."""

    show jordan sparkling at center
    
    jordan "This song is about finding someone who truly listens."
    
    mc "And it’s about finding someone worth listening to."
    
    narrator "Harmony in music, harmony in life."
    
    jump credits


# The “Friend” ending
# (a.k.a. the “Friending”)
# ------------------------

label friend_ending:
    narrator "You've made several good friends at your new school."
    narrator "Sometimes the best approach is to take things slow and let relationships develop naturally."
    narrator "High school is just the beginning of your story."
    
    mc "I’m grateful for all the new friendships I’ve made."
    
    narrator "The future is full of possibilities."
    
    jump credits

# Credits
label credits:
    scene black
    with fade
    
    centered "{size=+10}Thank you for playing!{/size}"
    centered "This simple dating simulator demonstrates:"
    centered "✅ Character development through dialogue"
    centered "✅ Choice-based branching storylines" 
    centered "✅ Point systems for relationship tracking"
    centered "✅ Multiple endings based on player decisions"
    centered """{size=-5}{b}Remember:{/b} Real relationships are built on mutual respect, 
        communication, and genuine care for each other.{/size}"""

    return