print("welcome to python quiz!!")
playing=input("do you like to play??-- ")
if playing.lower()!="yes":
    quit()
print("okay lets play!!")
score=0
#1 
answer=input("who developed python? --")
if answer.lower()=="guido van rossum":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#2
answer=input("which is the correct extension of python? --")
if answer.lower()==".py":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#3
answer=input("what is the other name of child class in python inheritance? --")
if answer.lower()=="derived class":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#4
answer=input("what is lambda function? --")
if answer.lower()=="anonymous function":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#5
answer=input("the variable listed inside the parenthese in the function definition --")
if answer.lower()=="parameter":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#6
answer=input("what is function? --")
if answer.lower()=="block of code":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#7
answer=input("the function which we users can create to help them to perform certain tasks? --")
if answer.lower()=="UDFs":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#8
answer=input("what is nested loop? --")
if answer.lower()=="loop inside loop":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#9
answer=input("decision making in a programming language is automated using----------? --")
if answer.lower()=="conditional statements":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
#10
answer=input("the order in which computer executes statement in a script? --")
if answer.lower()=="control flow":
    print("correct!!")
    score=score+1
else:
    print("incorrect answer")
print("you got"+str(score)+" question correct!!")
print("you have got :"+str((score/10)*100)+"%")
