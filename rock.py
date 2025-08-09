import random
import time

choices = ['R', 'P', 'S']

# ASCII Art
R = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
P = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
S = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = {'R': R, 'P': P, 'S': S}

def game1(player, computer, scores, streak):
    if player == computer:
        print("Draw")
        streak["human"] = 0  # reset streak
    elif (player == "R" and computer == "S") or \
         (player == "P" and computer == "R") or \
         (player == "S" and computer == "P"):
        print("Human Scored!")
        scores["human"] += 1
        streak["human"] += 1
    elif (computer == "R" and player == "S") or \
         (computer == "P" and player == "R") or \
         (computer == "S" and player == "P"):
        print("Computer Scored!")
        scores["computer"] += 1
        streak["human"] = 0  # reset streak
    else:
        print("Error!")

scores = {"human": 0, "computer": 0}
streak = {"human": 0}

while True:
    player_choice = input("Enter Option (R, P, S): ").upper()
    computer_choice = random.choice(choices)

    print(f"\nYou chose:\n{art[player_choice]}")
    time.sleep(0.5)
    print(f"Computer chose:\n{art[computer_choice]}")
    time.sleep(0.5)

    game1(player_choice, computer_choice, scores, streak)

    # Show current scoreboard
    print(f"Score → You: {scores['human']} | Computer: {scores['computer']}")
    if streak["human"] >= 3:
        print(f"🔥 Win Streak: {streak['human']}!")
    if scores["human"] == 5:
        print("🏆 You are a Champion!")
    if scores["human"] == 10:
        print("👑 Unstoppable!")

    ex = input("\nWant to Play More (Y/N)? ").upper()
    if ex == "N":
        print("\nFinal Scores:")
        print("Human Score:", scores["human"])
        print("Computer Score:", scores["computer"])
        break
