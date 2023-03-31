W = float(input("가로: "))
D = float(input("세로: "))
H = float(input("높이: "))

V = W * D * H

if (V < 0):
    print("Error has occurred. Close the program.")

elif (V > 120):
    print("It's too heavy.")

else:
    print("total lenght: %f" %V)

    print("Do you want to calculate the bill? Enter Y/N")
    answer = str(input())

    if (answer == "N"):
        print ("Exit the program.")

    else:
        if (V <= 80):
            print("5$")

        elif (80 < V <= 100):
            print("8$")

        elif (100 < V <= 120):
            print("10$")



