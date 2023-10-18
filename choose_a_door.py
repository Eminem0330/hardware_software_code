def choose_a_door():
    prize = 4
    msg = "Choose the correct door 1,2,3"

    print("Do you want to win a prize?")
    # print statement tells the computer to print out what is in the paranethasis
    door = int(input(msg))

    while door < 1 or door > 3:
    #while statements mean that
        print("Invalid door")
        door = int(input(msg))
    if door == 1:
        prize = 2+9 // 10 * 100
    elif door == 2:
        prize += 6
    elif door == 3:
        for i in range(door):
            prize += 1
    print("You won " + str(prize) + " tickets!")
def main():
    choose_a_door()
if __name__ = "__main__"
    main()

print("dheldojs fhsj")
