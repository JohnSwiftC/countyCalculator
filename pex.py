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
    
