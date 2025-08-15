# Simple Dating Simulator Tutorial
# A basic Ren'Py dating sim example suitable for tutorials

# Define characters
define narrator = Character(None)
define mc = Character("[playername]", color="#4a90e2")
define alex = Character("Alex", color="#e74c3c")
define sam = Character("Sam", color="#2ecc71")
define jordan = Character("Jordan", color="#9b59b6")



# Start of the game
label start:
    # Define variables
    $ playername = "Player"
    $ alex_points = 0
    $ sam_points = 0
    $ jordan_points = 0

    # Get player name
    $ playername = renpy.input("What's your name?", length=20)
    $ playername = playername.strip()
    
    if playername == "":
        $ playername = "Player"
    
    # Introduction
    scene hallway
    with fade
    
    narrator "Welcome to Riverside High School, where your senior year is about to get interesting!"
    
    mc "Hi, I'm [playername]. Just transferred here and trying to make new friends."
    
    narrator "You notice three interesting people you could potentially get to know better..."
    
    # Introduce characters
    show alex at left
    alex "Hey there! I'm Alex. I love art and spending time in the school's art studio."
    
    show sam at center
    sam "Hi! I'm Sam, captain of the debate team. Always up for a good intellectual discussion!"
    
    show jordan at right
    jordan "Jordan here. I'm into music and usually hang out in the music room during lunch."
    
    narrator "Who would you like to get to know first?"
    
    menu:
        "Talk to {b}Alex{/b}, the artist.":
            jump introduce_alex
        "Talk to {b}Sam{/b}, the debate team captain.":
            jump introduce_sam
        "Talk to {b}Jordan{/b}, the musician.":
            jump introduce_jordan

# Alex Route - Scene 1
label introduce_alex:
    scene classroom
    show alex
    
    $ alex_points += 1
    
    mc "I'd love to see some of your artwork, Alex."
    
    alex "Really? That's so sweet! Most people think art is just a hobby."
    
    mc "Art is important! It expresses things words sometimes can't."
    
    alex "Wow, you really get it! Want to come to the art studio after school?"
    
    menu:
        "I'd love to see your art studio!":
            $ alex_points += 1
            alex "Awesome! Meet me there at 3 PM!"
            jump after_school
        "Maybe another time?":
            alex "Oh, okay. No pressure! See you around."
            jump after_school

# Sam Route - Scene 1
label introduce_sam:
    scene classroom
    show sam
    
    $ sam_points += 1
    
    mc "I heard you're on the debate team. That sounds really cool!"
    
    sam "It is! We discuss everything from environmental policy to social issues."
    
    mc "I love hearing different perspectives on important topics."
    
    sam "Perfect! We're having a practice debate tomorrow. Want to come watch?"
    
    menu:
        "That sounds fascinating!":
            $ sam_points += 1
            sam "Great! It's in room 204 after school."
            jump after_school
        "I'm not sure if that's my thing...":
            sam "No worries! Everyone has different interests."
            jump after_school

# Jordan Route - Scene 1
label introduce_jordan:
    scene classroom
    show jordan
    
    $ jordan_points += 1
    
    mc "Music is such a universal language, isn't it?"
    
    jordan "Exactly! I've been working on some original compositions."
    
    mc "That's incredible! What kind of music do you write?"
    
    jordan "Mostly indie folk with some electronic elements. Want to hear one of my numbers sometime?"
    
    menu:
        "I'd love to hear your music!":
            $ jordan_points += 1
            jordan "Cool! Meet me in the music room after classes."
            jump after_school
        "Music isn't really my thing...":
            jordan "That's okay, not everyone connects with music the same way."
            jump after_school

# Day 2 - Choose your focus
label after_school:
    scene hallway
    with fade
    
    narrator "Eventually, 3:00 p.m. rolls around."
    narrator "It’s always a little awkward on the first day at a new school, but you survived it!"
    
    mc "Classes have ended. I should now figure out what to do next."
    
    if alex_points > 0:
        menu:
            "Visit Alex in the art studio":
                jump meet_with_alex
            "Explore the school on your own":
                jump explore_school
    elif sam_points > 0:
        menu:
            "Find Sam in the debate room":
                jump meet_with_sam
            "Explore the school on your own":
                jump explore_school
    elif jordan_points > 0:
        menu:
            "Meet Jordan in the music room":
                jump meet_with_jordan
            "Explore the school on your own":
                jump explore_school
    else:
        jump explore_school

# Alex Route - Scene 2
label meet_with_alex:
    scene art room
    show alex
    
    alex "You actually came! I'm so excited to show you what I've been working on."
    
    mc "Your art is amazing, Alex. You have such a unique style."
    
    alex "Thank you! Art has always been my way of understanding the world."
    
    menu:
        "I'd love to learn more about your artistic process":
            $ alex_points += 1
            alex "Really? I could teach you some basic techniques!"
            mc "That would be wonderful!"
        "Cool.":
            alex "Thanks."
    
    jump week_later

# Sam Route - Scene 2
label meet_with_sam:
    scene debate room
    show sam
    
    sam "I'm glad you came to watch our practice debate!"
    
    mc "You presented your arguments so clearly and thoughtfully."
    
    sam "Thanks! I believe in the power of respectful dialogue."
    
    menu:
        "I admire how you listen to opposing viewpoints":
            $ sam_points += 1
            sam "Understanding different perspectives makes us all stronger!"
            mc "I completely agree."
        "Dope.":
            sam "Thanks."
    
    jump week_later

# Jordan Route - Scene 2
label meet_with_jordan:
    scene music room
    show jordan
    
    jordan "Thanks for listening to my song. Not many people appreciate original music."
    
    mc "It was beautiful, Jordan. You have real talent."
    
    jordan "Music helps me express emotions I can't put into words."
    
    menu:
        "Your music made me feel something special":
            $ jordan_points += 1
            jordan "That's the best compliment you could give me!"
            mc "I mean it sincerely."
        "Rad.":
            jordan "Thanks."
    
    jump week_later

# Neutral route
label explore_school:
    scene school
    
    narrator "You spent the day exploring and getting to know the school better."
    narrator "Sometimes it's good to take things slow and see what develops naturally."
    
    jump week_later

# A week later - Ending based on choices
label week_later:
    scene dance
    with fade
    
    narrator "A week has passed, and it's time for the school's casual spring dance..."
    
    if alex_points >= 3:
        jump alex_ending
    elif sam_points >= 3:
        jump sam_ending
    elif jordan_points >= 3:
        jump jordan_ending
    else:
        jump friend_ending

# Alex Ending
label alex_ending:
    show alex
    
    alex "Hey [playername]! Want to dance?"
    
    mc "I'd love to, Alex."
    
    narrator "You and Alex spend the evening talking about art, dreams, and the future."
    narrator "A beautiful friendship has blossomed, with potential for something more."
    
    alex "Thank you for appreciating my art... and me."
    
    mc "Thank you for sharing your passion with me."
    
    narrator "Sometimes the best relationships start with shared understanding and mutual respect."
    
    jump credits

# Sam Ending
label sam_ending:
    show sam
    
    sam "This dance is nice, but want to step outside and talk under the stars?"
    
    mc "That sounds perfect, Sam."

    scene school night
    show sam at center

    narrator "You and Sam step outside."
    narrator "You spend hours discussing everything from philosophy to your hopes for the future."
    narrator "Intellectual compatibility has grown into something deeper."
    
    sam "I love how we can talk about anything together."
    
    mc "Great minds think alike, but great hearts understand each other."
    
    narrator "A connection built on respect and shared values is a strong foundation."
    
    jump credits

# Jordan Ending
label jordan_ending:
    show jordan
    
    jordan "I wrote a song inspired by our conversations. Want to hear it?"
    
    mc "I'd be honored, Jordan."
    
    narrator "Jordan plays a gentle melody that captures the growing connection between you."
    narrator "Music really is a universal language of the heart."
    
    jordan "This song is about finding someone who truly listens."
    
    mc "And it's about finding someone worth listening to."
    
    narrator "Harmony in music, harmony in life."
    
    jump credits

# Friend Ending
label friend_ending:
    narrator "You've made several good friends at your new school."
    narrator "Sometimes the best approach is to take things slow and let relationships develop naturally."
    narrator "High school is just the beginning of your story."
    
    mc "I'm grateful for all the new friendships I've made."
    
    narrator "The future is full of possibilities."
    
    jump credits

# Credits
label credits:
    scene black
    with fade
    
    centered "{size=+10}Thank You for Playing!{/size}"
    centered "This simple dating simulator demonstrates:"
    centered "✅ Character development through dialogue"
    centered "✅ Choice-based branching storylines" 
    centered "✅ Point systems for relationship tracking"
    centered "✅ Multiple endings based on player decisions"
    centered "Perfect foundation for learning Ren'Py basics!"
    centered "{size=-5}Remember: Real relationships are built on mutual respect,communication, and genuine care for each other.{/size}"
    
    return