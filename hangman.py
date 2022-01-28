import random as rand
import turtle as trl
import time as time

#List of words and identifying letters
words = ["Horse", "Zebra", "Phone", "Mouse", "Water", "Cream","Trash","Stair"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#defining turtle
draw = trl.Turtle()
draw.penup()

#define which word is chosed
chosen = rand.choice(words)
#chosen = "Shell"


wrongLet = []


#main cycle
def startCycle():
  ans1 = "  _  "
  ans2 = "  _  "
  ans3 = "  _  "
  ans4 = "  _  "
  ans5 = "  _  "
  check = 1
  drawCheck = 0
  while check == 1:
    check = 0
    print("")
    print(ans1 + ans2 + ans3 + ans4 + ans5)
    if (let1 == ans1 and let2 == ans2 and let3 == ans3 and let4 == ans4 and let5 == ans5):
      print("Great Job! The word was " + chosen)
      break
    else:
      print("What letter would you like to guess?")
      askLet = input("Letters already chosen: " + str(wrongLet) + "\n")
      #checkIflet = any(askLet in "H" for askLet in letters)
      if (askLet == let1):
        ans1 = askLet
        wrongLet.append(askLet)
        check = 1
      elif (askLet == let2):
        ans2 = askLet
        wrongLet.append(askLet)
        check = 1
      elif (askLet == let3):
        ans3 = askLet
        wrongLet.append(askLet)
        check = 1
      elif (askLet == let4):
        ans4 = askLet
        wrongLet.append(askLet)
        check = 1
      elif (askLet == let5):
        ans5 = askLet
        wrongLet.append(askLet)
        check = 1
      #If already chosen a letter NOT WORKING
      elif (askLet == wrongLet):
        print("already chosen")
        check = 1
      #If not a CAPS letterNOT WORKING
      elif ():
       print("Not a character, enter a letter in CAPS")
       check = 1
      else:
        wrongLet.append(askLet)
        drawCheck += 1
        if (drawCheck == 1):
          draw.goto(-50, -25)
          draw.pendown()
          draw.forward(100)
          check = 1
        elif (drawCheck ==2):
          draw.backward(50)
          draw.left(90)
          draw.forward(250)
          check = 1
        elif (drawCheck ==3):
          draw.left(90)
          draw.forward(60)
          draw.left(90)
          draw.forward(30)
          check = 1
        elif (drawCheck ==4):
          draw.penup()
          draw.goto(-80, 175)
          draw.pendown()
          draw.circle(20)
          check = 1
        elif (drawCheck ==5):
          draw.penup()
          draw.left(90)
          draw.forward(20)
          draw.right(90)
          draw.forward(20)
          draw.pendown()
          draw.forward(70)
          check = 1
        elif (drawCheck ==6):
          draw.right(30)
          draw.forward(30)
          draw.backward(30)
          check = 1
        elif (drawCheck ==7):
          draw.left(60)
          draw.forward(30)
          draw.backward(30)
          draw.right(30)
          check = 1
        elif (drawCheck ==8):
          draw.backward(45)
          draw.right(90)
          draw.forward(30)
          draw.backward(30)
          check = 1
        elif (drawCheck ==9):
          draw.left(180)
          draw.forward(30)
          draw.backward(30)
          check = 1
        elif (drawCheck ==10):
          draw.penup()
          draw.right(90)
          draw.backward(45)
          draw.right(90)
          draw.forward(10)
          draw.pendown()
          draw.circle(1)
          draw.penup()
          draw.backward(20)
          draw.pendown()
          draw.circle(1)
          draw.penup()
          draw.forward(15)
          draw.left(90)
          draw.forward(10)
          draw.left(90)
          draw.pendown()
          draw.forward(25)
          print("You Lose! Try Again!")
          time.sleep(5)
          break
  if check == 1:
    wn = trl.Screen()
    wn.mainloop()
    

#writing each variable to each letter
if (chosen == "Horse"):
  let1 = "H"
  let2 = "O"
  let3 = "R"
  let4 = "S"
  let5 = "E"
  startCycle()
elif (chosen == "Zebra"):
  let1 = "Z"
  let2 = "E"
  let3 = "B"
  let4 = "R"
  let5 = "A"
  startCycle()
elif (chosen == "Phone"):
  let1 = "P"
  let2 = "H"
  let3 = "O"
  let4 = "N"
  let5 = "E"
  startCycle()
elif (chosen == "Mouse"):
  let1 = "M"
  let2 = "O"
  let3 = "U"
  let4 = "S"
  let5 = "E"
  startCycle()
elif (chosen == "Water"):
  let1 = "W"
  let2 = "A"
  let3 = "T"
  let4 = "E"
  let5 = "R"
  startCycle()
elif (chosen == "Shell"):
  let1 = "S"
  let2 = "H"
  let3 = "E"
  let4 = "L"
  let5 = "L"
  startCycle()
elif (chosen == "Cream"):
  let1 = "C"
  let2 = "R"
  let3 = "E"
  let4 = "A"
  let5 = "M"
elif (chosen == "Trash"):
  let1 = "T"
  let2 = "R"
  let3 = "A"
  let4 = "S"
  let5 = "H"
elif (chosen == "Stair"):
  let1 = "S"
  let2 = "T"
  let3 = "A"
  let4 = "I"
  let5 = "R"







