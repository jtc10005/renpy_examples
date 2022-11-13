screen mansion_entry:
    imagemap:
        ground "/Castle/main_image.jpg"
    imagebutton:   
        idle "map-icon_sized.png"
        hover "map-icon_sized.png"
        focus_mask True
        xpos 0 ypos 0
        action Jump("mansion_map") 

screen mansion_map: #Preparing the imagemap
    modal True
    imagemap:
        ground "/Castle/castle_floor1_plan.jpg"
        # hover "planets-hover.png"
        textbutton "Close Map":
                    pos (1700, 5)
                    action Jump("close_map")
        textbutton "Pool [pool_count]":
                    pos (960, 300)
                    action Jump("pool")          
        textbutton "Courtyard":
                    pos (900, 500)
                    action Jump("courtyard")
        textbutton "Study":
                    pos (650, 500)
                    action Jump("study")
        textbutton "Pantry":
                    pos (1250, 500)
                    action Jump("pantry")                                    
        # hotspot (62, 399, 90, 91) focus_mask True clicked Jump("mercury")
        # hotspot (227, 302, 141, 137) focus_mask True clicked Jump("venus")
        # hotspot (405, 218, 164, 118) focus_mask True clicked Jump("earth")
        # hotspot (591, 78, 123, 111) focus_mask True clicked Jump("mars")

define pool_count = 0
        # The game starts here.
# label start:
#     "This is an imagemap tutorial."
#     call screen mansion_entry

label mansion_map:
    call screen mansion_map #Displaying the imagemap

label pool:
    "It is the pool."
    $ pool_count = pool_count + 1
    if pool_count < 2:
        jump mansion_map
    else:
        "you have been to the pool [pool_count] times"
        jump mansion_map

label courtyard:
    "It is the courtyard."
    jump mansion_map

label study:
    "It is the study."
    jump mansion_map
    
label pantry:
    "It is the pantry."
    jump mansion_map

label close_map:
    call screen mansion_entry