country_population = {"iowa": 3929271, "new_york": 14382379}
total = country_population["iowa"] + country_population["new_york"]

while 1==1:
    answer = input("How many people are there in total?")
    if total == int(answer):
        print("Good job")   
        print("You're a math super star")
        break
    else:
        print("Bad job")



