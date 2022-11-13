label intro:    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene personal_room_night

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen

    # These display lines of dialogue.
    e "Its a new world..."

    e "You've a new life..."

    menu: 
        "You were called Max.  Do you want to keep using this name?"

        "Yes":
            $ povname = "Max"
            $ renpy.retain_after_load()
            jump chapter_1

        "No":
            jump name

    return
