"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
# When score is smaller than 0 or greater than 100 it prompts you an error
if score < 0 or score > 100:
    print("Invalid score")
else:
    # When score is 90 or greater it will print "Excellent"
    if score >= 90:
        print("Excellent")
    # When score is 50 or greater it will print "Pass"
    elif score >= 50:
        print("Pass")
    # When score is lesser than 50 it will print "bad"
    elif score < 50:
        print("Bad")
