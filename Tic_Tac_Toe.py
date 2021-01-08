# a list for  xo table
xo_list = ['', '', '', '', '', '', '', '', '']


def check_winner(mylist, profile):
    mybool = False

    if (mylist[0] == profile) and (mylist[1] == profile) and (mylist[2] == profile):
        mybool = True
    elif (mylist[0] == profile) and (mylist[3] == profile) and (mylist[6] == profile):
        mybool = True
    elif (mylist[0] == profile) and (mylist[4] == profile) and (mylist[8] == profile):
        mybool = True
    elif (mylist[3] == profile) and (mylist[4] == profile) and (mylist[5] == profile):
        mybool = True
    elif (mylist[6] == profile) and (mylist[7] == profile) and (mylist[8] == profile):
        mybool = True
    elif (mylist[6] == profile) and (mylist[4] == profile) and (mylist[2] == profile):
        mybool = True
    elif (mylist[7] == profile) and (mylist[4] == profile) and (mylist[1] == profile):
        mybool = True
    elif (mylist[8] == profile) and (mylist[5] == profile) and (mylist[2] == profile):
        mybool = True
    else:
        mybool = False
    return mybool


# a function that displays the xo position depending on the given list
def display(a):
    dash = "    |"
    line = "---------------------------"
    print(a[6]+dash+a[7]+dash+a[8]+"    ")
    print(line)
    print(a[3]+dash+a[4]+dash+a[5]+"    ")
    print(line)
    print(a[0]+dash+a[1]+dash+a[2]+"    ")
    print(line)


def get_point(n):
    return n-1


player_1 = input("Pick X or O to start the play: ")
if player_1.lower() == 'x':
    player_1_profile = 'X'
    player_2_profile = 'O'
elif player_1.lower() == 'o':
    player_1_profile = 'O'
    player_2_profile = 'X'
while True:

    display(xo_list)
    player_1_input = int(input("Player 1: "))
    xo_list[get_point(player_1_input)] = player_1_profile
    display(xo_list)

    # Check if player 1 won
    if check_winner(xo_list, player_1_profile) == True:
        print("Player 1 WON!!! Congratulation!!!")
        break

    player_2_input = int(input("Player 2: "))
    xo_list[get_point(player_2_input)] = player_2_profile

    if check_winner(xo_list, player_2_profile) == True:
        print("Player 2 WON!!! Congratulation!!!")
        break
