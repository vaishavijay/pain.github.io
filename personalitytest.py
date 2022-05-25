import sys


def display(personality_type):
    print(f"Your personality type is -> {personality_type}")


def run():
    questions: list = [
        """
Question 1:
a.You enjoy being in groups
b.You enjoy one-on-one interactions
""",
        """
Question 2:
a.You are more outgoing and think out loud
b.You are more reserved and think to yourself
""",
        """
Question 3:
a.You seek many tasks, public activities, interaction with others
b.You seek private, solitary activities with quiet to concentrate
""",
        """
Question 4:
a.You are more communicative and prefer express yourself
b.You are prefer keep to yourself
""",
        """
Question 5:
a.You are more active and like to initiate things
b.You are more reflective and like deliberate things
""",
        """
Question 6:
a.You interpret things literally
b.You look for meaning and possibilities outside of the box
""",
        """
Question 7:
a.You are more practical, realistic, and experiential 
b.You are more imaginative, innovative, and theoretical
""",
        """
Question 8:
a.You like things more standard, usual, and conventional
b.You like things more different, novel, and unique
""",
        """
Question 9:
a.You focus on here-and-now
b.You look to the future, global perspective, and focus on the “big picture”
""",
        """
Question 10:
a.You prefer facts, things, and “what is” 
b.You prefer ideas, dreams, “what could be,” and the philosophical
""",
        """
Question 11:
a.You are more logical, thinking, and questioning 
b.You are more empathetic, feeling, and accommodating
""",
        """
Question 12:
a.You are candid, straight forward, and frank 
b.You tactful, kind, and encouraging
""",
        """
Question 13:
a.You are more firm, tend to criticize, and tend to hold the line 
b.You are more gentle, tend to appreciate, and conciliated
""",
        """
Question 14:
a.You are more tough-minded and just 
b.You are more tender-hearted and merciful
""",
        """
Question 15:
a.You are matter of fact and issue-oriented 
b.You are sensitive, people-oriented, and compassionate
""",
        """
Question 16:
a.You are organized
b.You are flexible
""",
        """
Question 17:
a.You like to plan and be scheduled
b.You don't like to plan and prefer being spontaneous
""",
        """
Question 18:
a.You like a structured lifestyle
b.You like an easygoing lifestyle
""",
        """
Question 19:
a.You prefer to plan ahead 
b.You prefer to go with the flow
""",
        """
Question 20:
a.You prefer to be controlled and governed
b.You prefer to be freedom
"""
    ]

    count_of_a: int = 0
    count_of_b: int = 0
    personality_dichotomy: str = ''
    count = 0

    for question in questions:
        answer = ''
        while not (answer == 'A' or answer == 'B'):
            count_of_a = 0
            count_of_b = 0
            try:
                answer = input(question).upper()
                if not (answer == 'A' or answer == 'B'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a = count_of_a + 1
                if answer == 'B':
                    count_of_b = count_of_b + 1
                count = count + 1

        if count == 5:
            if count_of_a > count_of_b:
                personality_dichotomy = personality_dichotomy + 'E '
            else:
                personality_dichotomy = personality_dichotomy + 'I '
        else:
            if count == 10:
                if count_of_a > count_of_b:
                    personality_dichotomy = personality_dichotomy + 'S '
                else:
                    personality_dichotomy = personality_dichotomy + 'N '
            else:
                if count == 15:
                    if count_of_a > count_of_b:
                        personality_dichotomy = personality_dichotomy + 'T '
                    else:
                        personality_dichotomy = personality_dichotomy + 'F '
                else:
                    if count == 20:
                        if count_of_a > count_of_b:
                            personality_dichotomy = personality_dichotomy + 'J '
                        else:
                            personality_dichotomy = personality_dichotomy + 'P '

    display(personality_dichotomy)


def exit_application():
    print("Exiting application...")
    sys.exit(0)


def main():
    user_input = input("""
    Welcome to the Meyers Briggs Personality Test
    Press 1  to take test
    Press 2 to exit application -> """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": run,
            "2": exit_application
        }
        return switcher.get(user_input)()


if __name__ == "__main__":
    main()
