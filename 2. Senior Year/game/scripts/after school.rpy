# Senior Year - after school.rpy
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

# This is an example of a “dating simulator” game, a very popular genre
# in visual novels. This uses a minimal amount of Python code for managing
# game state, which in this game is made up of three variables for keeping
# track of the player's relationship points with each character.
#
# This script is for the second phase of the game, where the player has a
# follow-up encounter with the character they chose to talk to in phase one.


# Phase 2:
# After school
# ------------

label after_school:
    play music "music/new friendly.mp3"

    scene hallway
    with fade
    
    narrator "Eventually, 3:00 p.m. rolls around."
    narrator "It’s always a little awkward on the first day at a new school, but you survived it!"
    
    mc "Classes have ended. I should now figure out what to do next."


    # The choice:
    # Meet up with the boy, or explore the school?
    # --------------------------------------------

    menu:
        "Visit Alex in the art studio." if alex_points > 0:
            jump meet_with_alex
        
        "Find Sam in the debate room." if sam_points > 0:
            jump meet_with_sam

        "Meet Jordan in the music room." if jordan_points > 0:
            jump meet_with_jordan
                
        "Explore the school on your own.":
            jump explore_school
    

# Meet with Alex in the art room
# ------------------------------

label meet_with_alex:
    scene art room with fade
    show alex
    
    alex "You actually came! I’m so excited to show you what I’ve been working on."

    narrator """Alex shows you around the art studio, and also shows you his latest projects.
    You can see the passion in his eyes as he talks about his work."""
    
    mc "Your art is amazing, Alex. You have such a unique style."
    
    alex "Thank you! Art has always been my way of understanding the world."
    

    # The choice:
    # Show interest in Alex's art or not?
    # -----------------------------------

    menu:
        "I’d love to learn more about your artistic process.":
            $ alex_points += 1
            $ display_heart_score("alex")
            alex "Really? I could teach you some basic techniques!"
            mc "That would be wonderful!"

        "Cool.":
            alex "Yeah."
    
    jump week_later


# Meet with Sam at the practice debate
# ------------------------------------

label meet_with_sam:
    scene debate room
    show sam
    
    sam "[player_name]! I’m glad you came to watch our practice debate!"

    narrator """You watch as Sam and the team passionately discuss the afternoon’s designated topic.
    You’re impressed by how articulate and knowledgeable Sam is."""

    mc """You presented your arguments so clearly and thoughtfully, even though you were arguing
    for a resolution you didn’t believe in."""

    sam "Thanks! I try to understand all sides."
    

    # The choice:
    # Show interest in Sam's debate skills or not?
    # --------------------------------------------
    
    menu:
        "I admire your willingness to see different perspectives.":
            $ sam_points += 1
            $ display_heart_score("sam")
            sam "Understanding different perspectives makes us better people."
            mc "I completely agree."

        "Dope.":
            sam "Thanks."
    
    jump week_later


# Meet with Jordan in the music room
# ----------------------------------

label meet_with_jordan:
    scene music room
    show jordan
    
    jordan "I’m glad you came! Welcome to the music room."

    narrator """Jordan starts by strumming a few chords on the guitar, and you can feel 
    the passion in his music. He plays an original song, and you’re captivated by its melodies."""

    jordan "Thanks for listening. Not many people appreciate original music."
    
    mc "I liked it, Jordan. You have real talent."
    
    jordan "Music... it helps me express emotions I can't put into words."
    

    # The choice:
    # Show interest in Jordan's music or not?
    # ---------------------------------------

    menu:
        "Your music made me feel something special.":
            $ jordan_points += 1
            $ display_heart_score("jordan")
            jordan "That’s the nicest thing anyone’s said about my songs!"
            mc "I mean it sincerely."

        "Rad.":
            jordan "..."
    
    jump week_later


# Explore the school instead
# --------------------------

label explore_school:
    scene school
    
    narrator "You spent the rest of the afternoon exploring and getting to know the school better."
    narrator "Sometimes it’s good to take things slow and see what develops naturally."
    
    jump week_later