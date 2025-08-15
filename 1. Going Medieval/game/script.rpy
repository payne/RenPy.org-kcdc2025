# Going Medieval - script.rpy
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

# This is a simple Ren'Py game that demonstrates how you can build
# a “Choose Your Own Adventure”-style game with Ren'Py using only the
# Ren'Py scripting language, *without* any Python code.
#
# If you’re new to programming or just want to concentrate on the story,
# graphics, and sound of a visual novel, this is a good place to start.
#
# For simplicity’s sake, there’s only one choice in the game, and it
# leads to one of two endings, depending on whether you choose the phone
# (the wrong choice) or the peppercorns (the right choice).


# Starting point:
# Museum and time machine
# -----------------------

label start:

    scene bg museum_outside
    play music "happy alley.mp3"

    "It was a lovely spring day, and you were visiting the local science museum."

    "Little did you know that this visit would change your life forever."

    scene bg museum_fire
    play music "volatile reaction.mp3" fadeout 1.0

    "About a half hour into your museum visit, there's a sudden {b}explosion{/b}!"

    "The blast blocks your path to the exit, so you have no choice but to find another way out."

    "You find a door marked “Authorized Personnel Only” and slip inside."

    scene bg time_machine

    "You find yourself in a room filled with strange equipment, and a scientist working at a console."

    show scientist at right

    "Scientist" "Thank goodness you're here! I was testing my new time machine by opening a portal when the explosion occurred."

    "Scientist" "I assure you, the two events are coincidental and unrelated. Well, I’m pretty sure, anyway."

    "Scientist" "There’s no time left! The only escape is through the time machine! Quick, follow me!"

    hide scientist with dissolve

    "The scientist jumps into the time machine and disappears in a flash of light."

    "The fire is spreading, and you have no choice but to follow the scientist through the time machine."

    "There’s just enough time to grab one thing before you go."

    show phone at truecenter

    "You see a phone on a table beside the time machine. It could come in handy."

    hide phone
    show peppercorns at truecenter

    "Beside the table is a twenty-pound bucket of peppercorns. You have no idea why they’re here, but they might be useful."

    hide peppercorns


# The choice
# Phone or peppercorns?
# ---------------------

    menu:
        "Which item do you take?"

        "Take the phone":
            jump took_phone_route

        "Take the bucket of peppercorns":
            jump took_peppercorns_route


# The player chose the phone
# (Bad ending)
# --------------------------

label took_phone_route:
    show bg time_warp with fade
    play music "time warp.mp3" fadein 0.5 fadeout 1.5

    "You grab your phone and step through the portal."

    scene bg english_village with fade
    play music "curb your enthusiasm.mp3" fadeout 1.0

    "You arrive in a small village in England in the year 1180, and you discover that the phone’s battery was completely drained."

    show merchant at center

    "Merchant (in Middle English)" "I ne may nout understanden þine hæþene deoren stefnes, and þæt smothe blæce stan þe þu hældest, þeah hit fayr beo, is unnytt."

    "You discover that the English they spoke in the 12th century sounds {i}nothing at all{/i} like 21st century English."

    "In Gen Z terms, you’re “giving village idiot vibes.”"

    scene bg poor_ending
    with fade

    "The locals take pity on you, and give you menial tasks, for which they pay you a loaf of bread a week. As a special treat, they give you a turnip on St. Swithin’s Day."

    "You die of malnutrition and dysentery a few months later."

    "{b}The end.{/b}"

    return


# The player chose the peppercorns
# (Good ending)
# --------------------------------

label took_peppercorns_route:
    show bg time_warp with fade
    play music "time warp.mp3" fadein 0.5 fadeout 1.5

    "You grab the bucket of peppercorns and step through the portal."

    scene bg english_village with fade
    play music "crunk knight.mp3" fadeout 1.0

    "You arrive in a small village in England in the year 1180, and are careful to show the locals only a handful of your peppercorns."

    show merchant at center

    "Merchant (in Middle English)" "Hafestu piporcornes? We clepið þæt “blæc golde!” Wilcume, freond!"

    "While the English they speak sounds {i}nothing at all{/i} like 21st century English, they’re willing to teach you because you have what they like to call “black gold.”"

    "You learn (or perhaps you {i}knew{/i}) that peppercorns are a valuable commodity in the medieval period, and you can trade them for goods and services."

    scene bg rich_ending
    with fade

    "You learn that 20 pounds of peppercorns is more than enough to make you a feudal lord, with a manorial estate and serfs to work the land."

    "You’re now an incredibly wealthy merchant in the spice trade, living the 12th century equivalent of the high life."

    "(Medieval toilets are terrible, though, so you have {i}that{/i} to look forward to.)"

    "{b}The end.{/b}"