import random 

def breaking(n):
    return [int(i) for i in str(n)]
        
def checking(n):
    m = breaking(n)
    if len(m) == len(set(m)):
        return True
    else:
        return False

def generator():
    while True:
        n = random.randint(1000,9999)
        if checking(n):
            return n

def counter(n,p):
    result = [0,0]
    a = breaking(n)
    b = breaking(p)
    for i,j in zip(a,b):
        if j in a:
            if j == i:
                result[0] += 1
            else:
                result[1] += 1
    return result

n = generator()
k = int(input("How many attempts will the game last? Enter number: "))

while k > 0:
    p = int(input("Your number is: "))
      
    if not checking(p):
        print("ERROR! Number has repeated digits. Try to guess again.")
        continue
    if p < 1000:
        print("ERROR! Number has less than 4 digits. Try to guess again")
        continue
    if p > 9999:
        print("ERROR! Number has more than 4 digits. Try to guess again")
        continue 
    result = counter(n,p)
    print(f"{result[0]} bulls and {result[1]} cows")
    k -=1
      
    if result[0] == 4:
        print("You win!")
        break
else:
    print(f"You lose :(\n Hidden number was {n}")