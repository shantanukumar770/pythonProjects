import random
def chkGuess(g, n):
    if g == n:
        pass
    elif g in range(n - 2, n + 3):
        print("\nYou are about to guess . . .")
    elif g in range(n - 5, n + 6):
        print("\nYou are too close . . .")
    elif g in range(n - 10, n + 11):
        print("\nYou are enough close . . .")
    else:
        print("\nYou are far away . . .")

list = []
for i in range(100):
    i = i + 1
    list.append(i)
turn = 15
guess = 0
num = random.choice(list)
print(f"\n\nI've a number in my mind between 1 to 100\nCan you guess it\nYou have {turn} tries")

#print(f"\nNumber is:\t{num}")
# input a number
while True:
  try:
    guess = int(input("\nYour Guess:\t"))
    while turn > 0:
        if guess == num:
            print(f"\n\n!  !  !    B I N G O    !  !  !\nYou guessed it in {16-turn} tries")
            break
        elif guess != num:
            chkGuess(guess, num)
            turn = turn - 1
            if turn == 0:
                print(f"\nNo More Tries Left\nNumber is:\t{num}")
                break
            else:
                print(f"\nTry Again ! ! !\n{turn} more tries left")
                guess = int(input("\nYour Guess:\t"))
    break
  except ValueError:
      print("\nPlease input integer only...")
      continue
input("\n\n\nPress Enter Key For Exit")