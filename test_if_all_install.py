from easygui import *
import sys

# A nice welcome message
ret_val = msgbox("Hello, World!")
if ret_val is None: # User closed msgbox
    sys.exit(0)

msg = "What is your favorite flavor?\nOr Press <cancel> to exit."
title = "Ice Cream Survey"
choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    msgbox("You chose: {}".format(choice), "Survey Result")