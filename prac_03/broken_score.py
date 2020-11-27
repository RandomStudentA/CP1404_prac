import random
def main():
    score = random.randrange(-100, 100)
    print(score_status(score))


def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        # When score is 90 or greater it will print "Excellent"
        if score >= 90:
            return "Excellent"
        # When score is 50 or greater it will print "Pass"
        elif score >= 50:
            return "Pass"
        # When score is lesser than 50 it will print "bad"
        elif score < 50:
            return "Bad"


main()
