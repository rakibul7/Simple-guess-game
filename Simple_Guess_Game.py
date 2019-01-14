import random

#GET GUESS
def get_gess():
    return list(input("What is your GUESS ?"))



#GENERATES COMPUTER CODE 123

def generates_code():
    digits=[str(num) for num in range(10) ]
# here we will shuffle the digits
    random.shuffle
# here we will grub the first three digits
    return digits[:4]



#GENERATES CLUES

def generate_clues(code,user_guess):
    if user_guess == code:
        return " CODE CRACKED"

    clues=[]


    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append["match"]
        elif num in code:
            clues.append("close")

    if clues == [] :
        return ["nope"]
    else:
        return clues



#RUN GAME LOGIC
print("""###################
Welcome Code breaker
###################""")

secret_code = generates_code()

clue_report=[]

while clue_report !="CODE CRACKED":
    guess = get_gess()
    clue_report = generate_clues(guess,secret_code)
    for clue in clue_report:
        print(clue)