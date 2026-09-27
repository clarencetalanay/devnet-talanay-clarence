"""
Module 2 — Lesson 4: Functions
Student: Clarence Nathan Lee D. Talanay
Date: 9/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[Instead of rewriting the same block of code over and over again, you write it once inside a 
function, give it a name, and "call" it whenever you need it. You can even pass ingredients 
(parameters) into it, and it will cook up and give back a final result (return value).]


============================================
KEY VOCABULARY
============================================
- function: a reusable block of code that performs a specific task
- parameter: a variable listed inside the function's parentheses that accepts incoming data
- argument: the actual data you pass into the function when you call it
- return value: the final result that a function sends back out when it finishes running


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

item_price = 100.0
discount = 20
final_cost = calculate_discount(item_price, discount)

print(f"Original Price: ${item_price}")
print(f"Price after {discount}% discount: ${final_cost}")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[Forgetting to use the 'return' keyword inside a function, which causes the 
function to output 'None' when you try to save or print its result.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Like a math formula on a calculator or a custom button on a video game controller 
that triggers a specific combo move every time you press it.]
"""