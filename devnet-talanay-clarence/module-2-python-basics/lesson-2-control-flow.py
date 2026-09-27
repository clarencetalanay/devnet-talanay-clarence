"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Clarence Nathan Lee D. Talanay]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[When decididing whether to bring an umbrella if it's raining, or wear a jacket if it's cold, 
an if / elif / else statement lets your program check a situation and choose a specific 
path of action based on whether something is true or false.]


============================================
KEY VOCABULARY
============================================
- condition: a rule or question that evaluates to true or false
- if / elif / else: decisions used to check conditions
- comparison operator: symbols used to compare values(>, <, ==)
- boolean expression: code that results in either true or false
(add more as needed)

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

age = 16

if age < 5:
    print("Ticket is free!")
elif age < 18:
    print("Child ticket price: $8")
else:
    print("Adult ticket price: $12")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[Using a single equals sign (=) instead of a double equals sign (==)
when checking if two values are equal, which causes a syntax error.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Like a vending machine checking if you inserted enough money before 
deciding whether to dispense your food or ask for more money.]
"""
