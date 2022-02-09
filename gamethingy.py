import os, random
os.system('cls')


Afruits=["banana","apples","strawberries","blueberries","oranges" ]
for elem in Afruits:
    print(f"the furit is {elem}")

for i in range(len(Afruits)-1):
    print(i, end=" ")
    print("The fruit is ", Afruits[i] )

indexFruit=random.randint()
word=Afruits[indexFruit]
print(word)
word=random.choice(Afruits)
print(word)
check=True
while check:
    try:
        letter = input("enter a letter")
        if letter.isalpha
        
    except ValueError:
        print("only a letter please")