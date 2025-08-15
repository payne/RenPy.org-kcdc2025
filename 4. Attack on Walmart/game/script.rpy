# Attack on Walmart - script.rpy
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

init python:
  # Utility functions
  # =================

  # This function displays quantities of an item 
  # using the correct singular or plural form
  # (e.g. "5 cans" or "1 point")
  def display_quantity(amount, item_name):
    if amount != 1:
      noun = f"{item_name}s"
    else:
      noun = item_name
    return f"{amount} {noun}"
    

# RPG combat stats screen
# =======================
screen simple_stats_screen:
  frame:
    xalign 0.01 yalign 0.05
    xminimum 220 xmaximum 220
    vbox:
      text "Florida Man" size 22 xalign 0.5
      null height 5
      hbox:
        bar:
          xmaximum 130
          value florida_man_health
          range FLORIDA_MAN_MAX_HEALTH
          left_gutter 0
          right_gutter 0
          thumb None
          thumb_shadow None

        null width 5

        text "[florida_man_health] / [FLORIDA_MAN_MAX_HEALTH]" size 16
        
  frame:
    xalign 0.99 yalign 0.05
    xminimum 220 xmaximum 220
    vbox:
      text "Hellcow" size 22 xalign 0.5
      null height 5
      hbox:
        bar:
          xmaximum 130
          value hellcow_health
          range HELLCOW_MAX_HEALTH
          left_gutter 0
          right_gutter 0
          thumb None
          thumb_shadow None

        null width 5

        text "[hellcow_health] / [HELLCOW_MAX_HEALTH]" size 16


label start:
  # Initialization
  # ==============

  # The characters
  define fm = Character('Florida Man', color="#CD0000")
  define hc = Character('Hellcow', color="#B5B5B5")

  # Initial state constants
  $ HELLCOW_MAX_HEALTH = 15
  $ FLORIDA_MAN_MAX_HEALTH = 15
  $ INITIAL_WHITE_CLAW_SUPPLY = 2
  
  # Initialize game state
  $ hellcow_health = HELLCOW_MAX_HEALTH
  $ florida_man_health = FLORIDA_MAN_MAX_HEALTH
  $ white_claw_supply = INITIAL_WHITE_CLAW_SUPPLY


  # Intro cutscene
  # --------------
  scene hell with fade
  show hellcow
  hc "The time is nigh for my takeover of Florida!"
  hc "My powers at at their peak, and no one can stop me!"

  scene walmart-parking-lot with pixellate
  show florida-man-float
  fm "Not so fast, Carl’s Junior! You gotta git through me first!"
  fm "I got lotsa cans of White Claw and whoop-ass!"
  
  scene hell
  show hellcow
  hc "..."


# The game
# ========

play music "music/lets_fighting_love.mp3"

scene walmart-parking-lot with fade
show screen simple_stats_screen
show florida-man at left
show hellcow at right

# The game loop
# -------------
# The "body" of the game, which executes until one of the characters’
# hit points drops to 0 or less.
while True:

  # Florida Man’s turn
  # ------------------
  menu:
    "Attack Hellcow with your shopping cart":
      "You get into position to make your attack."

      # Florida Man has a 66% chance of hitting Hellcow.
      $ florida_man_connected = renpy.random.randint(1, 3) < 3

      if florida_man_connected:
        # If Florida Man hits Hellcow, he does 1 - 4 points of damage.
        $ florida_man_damage = renpy.random.randint(1, 4)
        $ hellcow_health -= florida_man_damage
        play audio "music/hadouken.mp3"
        "You batter Hellcow with your trusty shopping cart, dealing [display_quantity(florida_man_damage, 'point')] of damage."

        if hellcow_health > 0:
          fm "WORLD STAR! WORLD STAR! WORLD STAR!"
        else:
          "With that last blow, Hellcow is down for the count!"
          jump florida_man_victory

      else:
        "Swing and a miss! Hellcow dodges your attack."

    
    "Drink a White Claw (You have [display_quantity(white_claw_supply, 'can')])" if white_claw_supply > 0:
      $ health_restored = renpy.random.randint(1, 5)
      $ florida_man_health = min(florida_man_health + health_restored, FLORIDA_MAN_MAX_HEALTH)
      $ white_claw_supply -= 1
      play audio "music/aint-no-laws.mp3"
      fm "“Ain’t no laws when you’re drinkin’ Claws!!!”"
      "The nearly taste-free beverage restores [display_quantity(health_restored, 'point')] of health."


  # Hellcow’s turn
  # --------------
  "Hellcow attacks!"

  # Hellcow has a 50% chance of hitting Florida Man.
  $ hellcow_connected = renpy.random.randint(1, 2) == 1

  if hellcow_connected:
    # If Hellcow hits Florida Man, she does 1 - 8 points of damage
    $ hellcow_damage = renpy.random.randint(1, 8)
    $ florida_man_health -= hellcow_damage

    play audio "music/moo.mp3"
    hc "Moooo!"
    "Hellcow strikes you with superbovine strength, delivering [display_quantity(hellcow_damage, 'point')] of damage."

    if florida_man_health > 0:
      fm "Take THAT, Florida Man!"
    else:
      "The last thing you see before you expire is a hoof in your face."
      jump hellcow_victory

  else:
    "AWWWW YISSS! You deftly dodge Hellcow’s hoof, which would’ve really hurt, had it connected."


# Endings
# =======

# The bad ending
# --------------
# If Hellcow wins, play this scene.

label hellcow_victory:

  play music "music/imperial-march.mp3"
  scene hell-on-earth
  hide screen simple_stats_screen
  show hellcow at right

  hc "Another dead hooo-man! HAHAHAHA!!!"
  hc "And I shall bring my Satanic realm to this plane!"
  "And so Hellcow turned Florida into a hellscape. To nobody’s surprise, I-4 looks exactly the same."
  
  jump end


# The good ending
# ---------------
# If Florida Man wins, play this scene.

label florida_man_victory:

  play music "music/we-are-the-champions.mp3"
  scene burgers
  hide screen simple_stats_screen
  show florida-man-float at left

  fm "I love the smell of cow in the evening."
  fm "It smells like...VICTORY!"
  fm "Tastes like it, too."

  jump end

label end:
  "The end."