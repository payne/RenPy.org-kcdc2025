# Senior Year - initial meeting.rpy
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

# This is an example of a “dating simulator” game, a very popular genre
# in visual novels. This uses a minimal amount of Python code for managing
# game state, which in this game is made up of three variables for keeping
# track of the player's relationship points with each character.
#
# This script is for the first phase of the game, where the player meets
# three pretty, pretty boys: Alex, Sam, and Jordan.


# Characters
# ----------

define narrator = Character(None)
define mc = Character("[player_name]", color="#4a90e2")

define alex = Character("Alex", image="alex", color="#e74c3c")
image alex dokidoki = "images/characters/alex dokidoki.png"
image side alex = "images/characters/side alex.png"

define jordan = Character("Jordan", image="jordan", color="#9b59b6")
image jordan sparkling = "images/characters/jordan sparkling.png"
image side jordan = "images/characters/side jordan.png"

define sam = Character("Sam", image="sam", color="#2ecc71")
image sam blushing = "images/characters/sam blushing.png"
image side sam = "images/characters/side sam.png"


# Game state
# ----------

default player_name = "Player"
default alex_points = 0
default sam_points = 0
default jordan_points = 0


# Utility functions
# -----------------

init python:
    def point_or_points(points):
        return "point" if points == 1 else "points"

    def display_heart_score(name):
        renpy.play("sound/add points.mp3", channel="sound")

        if name == "alex":
            renpy.say(narrator, f"You have [alex_points] 💖 {point_or_points(alex_points)} with Alex.")
        elif name == "sam":
            renpy.say(narrator, f"You have [sam_points] 💖 {point_or_points(sam_points)} with Sam.")
        elif name == "jordan":
            renpy.say(narrator, f"You have [jordan_points] 💖 {point_or_points(jordan_points)} with Jordan.")


# Starting point:
# High school hallway / meet the pretty, pretty boys
# --------------------------------------------------

label start:
    play music "music/aerosol of my love.mp3"

    # Get player name
    $ player_name = renpy.input("What’s your name?", length=20)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Player"
    

    # Phase 1: The hallway
    # --------------------
    scene hallway
    with fade
    
    narrator "Welcome to Kansas City Central High School, where your senior year is about to get interesting!"

    mc "Hi, I’m [player_name]. I just transferred here, and I’m trying to make new friends."

    narrator "You notice three interesting people you could potentially get to know better..."
    
    # Introduce the pretty, pretty boys
    show alex at left
    alex "Greetings and salutations! I’m Alex. I love art and spending time in the school’s art studio."
    
    show sam at center
    sam "Hi! I’m Sam, captain of the debate team. Always up for a good intellectual discussion!"
    
    show jordan at right
    jordan "Jordan here. I’m into music and usually hang out in the music room between classes."
    
    narrator "Who would you like to get to know first?"
    

    # The choice
    # Alex, Sam, or Jordan?
    # ---------------------

    menu:
        "Talk to {b}Alex{/b}, the artist.":
            jump introduce_alex
        "Talk to {b}Sam{/b}, the debate team captain.":
            jump introduce_sam
        "Talk to {b}Jordan{/b}, the musician.":
            jump introduce_jordan


# Get to know Alex
# ----------------

label introduce_alex:
    scene classroom
    show alex
    
    $ alex_points += 1
    $ display_heart_score("alex")
    
    mc "So... you love art?"
    
    alex """Art is important! It allows people to express themselves in unique ways. 
    Most people think art is just a hobby."""

    mc "What inspires your work?"

    alex "Come to the art studio after school, and I’ll show you."
    

    # The choice:
    # Meet Alex after school?
    # -----------------------

    menu:
        "I’d love to!":
            $ alex_points += 1
            $ display_heart_score("alex")
            alex "Awesome! Meet me there at 3 p.m."
            jump after_school

        "Maybe another time?":
            alex "Oh, okay. No pressure! But if you change your mind, you know where to find me."
            jump after_school


# Get to know Sam
# ----------------

label introduce_sam:
    scene classroom
    show sam
    
    $ sam_points += 1
    $ display_heart_score("sam")

    mc "Debate team, huh? That sounds interesting."
    
    sam "It is! We discuss everything, from environmental policy to social issues."

    mc "Have you ever had to argue for something you didn't believe in?"

    sam """Actually, I’ll be doing that in this afternoon’s practice debate after classes.
    You should come watch! It’s a great way to see how we think on our feet."""
    

    # The choice:
    # Meet Sam after school?
    # ----------------------

    menu:
        "You know what? I think I will!":
            $ sam_points += 1
            $ display_heart_score("sam")
            sam "Great! Room 204, 3 p.m. See you there!"
            jump after_school

        "I’m not sure if that’s my thing...":
            sam "No worries! The invite stands."
            jump after_school


# Get to know Jordan
# ------------------

label introduce_jordan:
    scene classroom
    show jordan
    
    $ jordan_points += 1
    $ display_heart_score("jordan")
    
    mc "Music, huh? What do you play?"

    jordan "Mostly guitar, with some keyboard. I’ve been working on some original compositions."

    mc "What kind of music do you write?"
    
    jordan "Mostly indie folk with some electronic elements. Want to hear one of my numbers sometime?"


    # The choice:
    # Meet Jordan after school?
    # -------------------------

    menu:
        "I’d love to!":
            $ jordan_points += 1
            $ display_heart_score("jordan")
            jordan "Cool! Meet me in the music room after classes."
            jump after_school

        "Maybe — I’ve got to see how my schedule looks.":
            jordan """That’s okay, I get how busy the first day of school can be.
            But if you can make some time, I’ll be in the music room after school."""
            jump after_school
