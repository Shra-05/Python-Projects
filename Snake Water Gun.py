import random
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def check(comp, user):
    if comp == user:
        return 0
    elif comp == 0 and user == 1:
        return -1
    elif comp == 1 and user == 2:
        return -1
    elif comp == 2 and user == 0:
        return -1
    else:
        return 1


while True:
    comp = random.randint(0,2)
    user = int(input("Enter:- 0 for Snake, 1 for water, 2 for Gun\n"))
    com = f'I Choose {comp}'
    print(com)
    speaker.Speak(com)


    if user <= 2:
        score = check (comp,user)
        if score == 0:
            Tie = "Oh!! Tie"
            print(Tie)
            speaker.Speak(Tie)
        elif score == 1:
            win = "Yep!! You Won"
            print(win)
            speaker.Speak(win)
        else:
            lose = "Oh!! You Lose"
            print(lose)
            speaker.Speak(lose)
    else:
        invalid = 'Invalid Input, Enter again number between 0 and 2'
        print(invalid)
        speaker.Speak(invalid)