# UI styling
# ----------
init 1:
    style answer_button is button
    style answer_button_text is button_text

    style answer_button:
        xfill True
        xpadding 28
        ypadding 18

    style answer_button_text:
        size 42
        text_align 0.5   # center the text within its area
        xalign 0.5       # center the text displayable within the button
        bold True


# === Visual effects ===

# Red screen flash synced to the 3-2-1 beep
transform quick_flash:
    alpha 0.80
    linear 0.22 alpha 0.0

# Pulse for the countdown text (brief scale-up, then fade the overlay copy)
transform countdown_pulse:
    alpha 1.0
    zoom 1.0
    easein 0.10 zoom 1.12
    easeout 0.15 zoom 1.0 alpha 0.0

# --- Screens ---

screen trivia_question_screen(q, q_num, total, limit):
    tag trivia
    default time_left = int(limit)
    default last_beeped = None
    default flash_on = False    # toggled on 3/2/1 to drive red flash + text pulse

    # Question background
    if q["image"]:
        add q["image"]

    # Top panel: question number + text
    frame:
        xalign 0.5
        yalign 0.08
        xmaximum 0.9
        background Frame("#0000", 0, 0)
        has vbox
        spacing 10
        text ("Question {}/{}".format(q_num, total)) size 26
        text q["question"] size 60 bold True
        

    # Right-top: countdown display (with layered pulse on beep)
    frame:
        xalign 0.95
        yalign 0.08
        background Frame("#0008", 10, 10)
        padding (10, 6)
        fixed:
            # Base, steady countdown text (auto-updates as time_left changes)
            text "Time: [time_left]s" size 28
            # Overlay pulsing duplicate when flash_on is active
            if flash_on:
                text "Time: [time_left]s" size 28 at countdown_pulse

    # Center panel: choices (moved to middle and larger)
    frame:
        xalign 0.5
        yalign 0.55          # a hair below center to avoid overlapping the question text
        xmaximum 0.8
        has vbox
        spacing 16

        for i, ans in enumerate(q["answers"]):
            textbutton ans["text"] style "answer_button" action Return(i)

    # Countdown mechanics:
    # 1) Decrement once per second (never below 0)
    timer 1.0 action SetScreenVariable("time_left", max(0, time_left - 1)) repeat True

    # 2) After decrement, if time_left is 3/2/1 and not yet beeped for that value, play beep + trigger flash
    timer 1.01 repeat True action If(
        (time_left in (3, 2, 1)) and (last_beeped != time_left),
        [
            Function(renpy.sound.play, BEEP_SFX, channel="trivia_sfx"),
            SetScreenVariable("last_beeped", time_left),
            SetScreenVariable("flash_on", True)
        ],
        None
    )

    # 3) Red flash overlay (fades out quickly)
    if flash_on:
        add Solid("#f00") at quick_flash
        # Turn off the flag once the flash/pulse has played
        timer 0.25 action SetScreenVariable("flash_on", False)

    # 4) When we hit 0, immediately return a special sentinel value
    if time_left <= 0:
        timer 0.01 action Return("timeout")

# Unified feedback screen used for correct, incorrect, and time's up
screen trivia_feedback_screen(is_correct=None, label_text=None, comment_text=None):
    tag trivia

    # Decide the headline
    $ msg = label_text
    if msg is None:
        if is_correct is True:
            $ msg = "Correct!"
        elif is_correct is False:
            $ msg = "Incorrect!"
        else:
            $ msg = "Time’s Up!"

    # Center overlay with headline + optional comment
    frame:
        xalign 0.5
        yalign 0.40
        background Frame("#0008", 14, 14)
        padding (24, 18)
        has vbox
        spacing 10

        text msg size 58
        if comment_text:
            text comment_text size 30

    # Bottom prompt to continue (no auto-advance)
    frame:
        xalign 0.5
        yalign 0.95
        background Frame("#0008", 10, 10)
        padding (10, 6)
        text "Tap / click / press a key to continue" size 24

    key "K_SPACE" action Return(True)
    key "K_RETURN" action Return(True)
    key "K_KP_ENTER" action Return(True)
    key "mouseup_1" action Return(True)

screen trivia_results_screen(score, total):
    tag trivia
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        has vbox
        spacing 16

        text "Quiz Complete!" size 48
        text "Score: {}/{}".format(score, total) size 36
        textbutton "Play Again" action Return("again")
        textbutton "Quit" action Return("quit")