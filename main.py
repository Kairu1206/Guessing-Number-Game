import random
nums = []

def clear():
  print('\033[H\033[J', end='')

def playagain():
  print("Another game?")
  while True:
    answer = input("Enter here: ")
    if answer.lower().strip() == "yes":
      nums.clear()
      clear()
      game()
    elif answer.lower().strip() == "no":
      print("Thank you for playing our game!")
      print("See you soon!")
      break
    else:
      print("Invalid input!")
      continue

def randomNum(x, y):
  for i in range(y-x):  
    rannum = random.randint(x, y)
    nums.append(rannum)
  return nums

def calculatesum():
  sumNum = 0
  for num in nums: 
    sumNum += num
  return abs(sumNum)

def checkanswer(sumofnumber):
  numofguess = 3
  while numofguess:
    print("What is the sum of all the number?")
    guess = int(input("Answer: "))
    print()
    if guess == sumofnumber:
      print("Congratulation!")
      print()
      playagain()
      break
    elif guess < sumofnumber:
      print("Too low!")
      print()
      numofguess -= 1
      continue
    elif guess > sumofnumber:
      print("Too high!")
      print()
      numofguess -= 1
      continue  
  if numofguess == 0:
    print("The answer is " + str(sumofnumber))
    playagain()

def game():
  firstnum = int(input("First number: "))
  lastnum = int(input("Last number: "))
  clear()
  randomNum(firstnum, lastnum)
  print()
  print("Your list of random numbers is: " + str(nums))
  checkanswer(calculatesum())

game()

