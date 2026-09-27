"""
Module 2 — Lesson 1: Variables & Data Types
Student: [Clarence Nathan Lee D. Talanay]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[A variable is a label for box. You write a label on the outside(the variable name)
and put something valuable inside it (the data/value). A data type is simply the category of 
stuff you put inside that box. For example, if you put a text inside the box, it's a text box(string), 
if you drop in a whole number, it's a number box(integer), and if you put a light switch 
inside that can only be ON or OFF, that's a true/false box(boolean).]


============================================
KEY VOCABULARY
============================================
- variable: name for a container
- data type: format of data
- int: short for integer, contains whole numbers
- float: contains any number with decimal point
- string: contains texts enclosed in single or double quotes
- boolean: A data type with only two possible values, true or false
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

character_name = "Tarnished" # string
current_level = 67 # int
rune_points = 4850.5 # float
is_quest_active = True # boolean

print(f"Character: {character_name}")
print(f"Level: {current_level} (Runes: {rune_points})")
print(f"Active Quest Status: {is_quest_active}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[Trying to add text and numbers together directly, which causes a 
crash because Python doesn't automatically combine them.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Like filling out a form or Excel cells where each box expects a specific type of data.]
"""
