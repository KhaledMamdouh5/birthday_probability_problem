n=input("Enter the number of people in the room: ")

def at_least_two_in_the_room(n):
    if n < 2:
        print('Room has less than 2 people')
        return 0
    elif n == 2:
        return 1/365
    else:
        s = 1/365
        for i in range (1,n-1):
            s = s + 1/(365-i)
        previous = at_least_two_in_the_room(n-1)
        return previous+(1-previous)*s
    
P = at_least_two_in_the_room(int(n))*100
print ("The probability that at least 2 out of " + n +" share the same birthday is " + str(P) + "%")