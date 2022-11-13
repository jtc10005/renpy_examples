# screen choice(items):

#     window:
#         style "menu_window"

#         vbox:
#             style "menu"

#             for i in items:

#                 if i.action:

#                     button:
#                         action i.action
#                         style "menu_choice_button"

#                         text i.caption style "menu_choice"

#                 else:
#                     text i.caption style "menu_caption"