# Trivia Game
# A Ren'Py demo game by Joey deVilla
# written for Kansas City Developer Conference 2025
# and presented on August 15, 2025
# =================================================

# Constants
# ---------
define QUESTION_TIME_LIMIT = 7    # Seconds to answer each question
define QUESTIONS_PER_GAME = 3    # Max questions per round (caps to what's available)

# Sound effects
# -------------
define BEEP_SFX = "sfx/beep.mp3"
define BUZZ_SFX = "sfx/buzz.mp3"
define CORRECT_SFX = "sfx/correct.mp3"
define INCORRECT_SFX = "sfx/incorrect.mp3"


init python:
    import json, random

    # Create a dedicated sound channel for all sound effects 
    # (using the "Sound" mixer)
    renpy.music.register_channel(
        "trivia_sfx",
        mixer="sfx",
        loop=False,
        stop_on_mute=True,
        tight=True
    )


    class TriviaPack(object):
        def __init__(self, questions, defaults):
            self.questions = questions
            self.defaults = defaults or {}

        @staticmethod
        def load(path="questions.json"):
            # Load JSON from /game folder
            data = json.loads(renpy.file(path).read().decode("utf-8"))
            questions = data.get("questions", [])
            defaults = data.get("defaults", {})
            return TriviaPack(questions, defaults)


    def prepare_question(raw_q):
        import renpy # for renpy.log if needed
        import random

        # Base fields
        question_text = raw_q.get("question", "Missing question text.")
        question_image = raw_q.get("image")
        corr = raw_q.get("correct_answer") or {}
        inc_list = raw_q.get("incorrect_answers") or []

        corr_text = corr.get("text", "Correct answer (missing)")
        corr_comment = corr.get("comment", None)

        answers = [{
            "text": corr_text,
            "correct": True,
            "comment": corr_comment
        }]

        # Add incorrect answers (skip items without text)
        for ia in inc_list:
            t = (ia or {}).get("text")
            if not t:
                continue
            answers.append({
                "text": t,
                "correct": False,
                "comment": (ia or {}).get("comment", None)
            })

        # Minimal safety: ensure at least 2 choices so UI doesn't look broken.
        if len(answers) < 2:
            renpy.log("Trivia warning: Less than 2 answers for a question; adding a placeholder.")
            answers.append({
                "text": "N/A",
                "correct": False,
                "comment": None
            })

        random.shuffle(answers)

        return {
            "question": question_text,
            "image": question_image,
            "answers": answers,
        }


label start:
    $ pack = TriviaPack.load("questions.json")
    $ questions_raw = pack.questions
    $ available = len(questions_raw)

    if available == 0:
        "No questions found in questions.json. Add some and try again."
        return

    # Determine how many to play this round
    $ requested = QUESTIONS_PER_GAME if QUESTIONS_PER_GAME and QUESTIONS_PER_GAME > 0 else available
    $ total = requested if requested <= available else available

    if available < requested:
        "Heads up: The pack has only [available] questions, but [requested] were requested. We'll use [available]."

    # Build a shuffled subset of exactly `total` questions
    $ order = list(range(available))
    $ random.shuffle(order)
    $ order = order[:total]

    $ score = 0
    $ idx = 0

    while idx < total:
        $ q_raw = questions_raw[order[idx]]
        $ q = prepare_question(q_raw)

        # Show timed question
        call screen trivia_question_screen(q, idx+1, total, QUESTION_TIME_LIMIT)
        $ chosen = _return

        if chosen == "timeout":
            $ is_correct = False
            $ renpy.sound.play(BUZZ_SFX, channel="trivia_sfx")
            call screen trivia_feedback_screen(is_correct, "Time’s Up!")
        else:
            $ chosen_ans = q["answers"][chosen]
            $ is_correct = chosen_ans["correct"]
            $ comment = chosen_ans.get("comment")

            if is_correct:
                $ score += 1
                $ renpy.sound.play(CORRECT_SFX, channel="trivia_sfx")
            else:
                $ renpy.sound.play(INCORRECT_SFX, channel="trivia_sfx")

            call screen trivia_feedback_screen(is_correct, comment_text=comment)

        $ idx += 1


    # Show the results
    call screen trivia_results_screen(score, total)
    if _return == "again":
        jump start
    return