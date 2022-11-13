screen button():
    hbox:
        textbutton "Start" action Confirm("You sure?", name, restart_game)

label name:
    python:
        povname = renpy.input("What is your new name going to be??", length=32)
        povname = povname.strip()


    pov "Your name is [povname]!"
    
    # $ yes_no_question = "Is this Correct?"
    # $ yes_action = chapter_1
    # $ no_action = name
    # call yes_no pass(msg = "{color=#f00}Is this Correct?")
    menu:
        "Is this Correct?"

        "Yes":
            $ renpy.retain_after_load()
            jump chapter_1

        "No":
            jump name