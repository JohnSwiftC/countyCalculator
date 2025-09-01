print("Hello, welcome to the world of the joker! Today youll have to solve two riddles")
riddles = ["What's bought by the yard and worn by the foot?", "What has hands, but can't clap?"]
answers = ["carpet", "clock"]

for i in range(0, len(riddles)):
    print(riddles[i])
    answer = input("What is the answer? ")
    if answer == answers[i]:
        print("Correct!")
    else:
        print("False!")
    




print("Hello, my name is Joe and I need your help! I cant seem to count all my apples, will you help me?")
questions = ["My backpack has 31 apples, and i have 5 in my hand", "Ohh no I just dropped 12 in the dirt, how mnay do I have now?"]
answers = [36, 24]

for i in range(0, len(questions)):
    print(questions[i])
    answer = input("How many apples do I have?")
    if int(answer) == answers[i]: 
        print("That sounds right!")
    else:
        print("I dont think thats right!")