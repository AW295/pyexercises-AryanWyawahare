"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer to whether they want to continue.
# 2. Process: Ask up to five times; ignore capitalization and surrounding spaces.
# 3. Out: A message for each answer and a summary.
# 4. Stop on "no" or after five attempts. The summary contains attempts and the
#    reason the loop stopped.


# Your code below
attempts = 0
stop_reason = "maximum attempts reached"

while attempts < 5:
    attempts += 1
    print(f"Attempt number: {attempts}")
    answer = input("Do you want to continue? (yes/no): ").strip().lower()

    if answer == "yes":
        print("You chose to continue.")
    elif answer == "no":
        print("You chose to stop.")
        stop_reason = "the user answered no"
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print(f"Summary: {attempts} attempt(s); stopped because {stop_reason}.")