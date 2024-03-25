import copy


class Rover:
    def __init__(self, locations):
        self.locations = locations


def check_int(i):
    if i.isdigit():
        number = int(i)
        return number
    else:
        print("Invalid input given. Please enter a valid number.")
        return 0


def check_format(s):
    try:
        b = [int(x) for x in s.split()]
    except ValueError:
        print("Error : Please enter valid integers.")
        b = [0]
    if len(b) != 2:
        print("Please enter only 2 valid coordinates in the format, 'x y'")
        return None, False
    else:
        return b, True


def decode_instructions(I, initial_pos, instructions, plateau_size):
    border = True
    loc = []
    y = copy.deepcopy(initial_pos)
    y = tuple(y)
    loc.append(y)
    for s in instructions:
        if s == "N":
            initial_pos[1] = initial_pos[1]+1
            if initial_pos[1] > plateau_size[1]:
                border = False
                break
            x = copy.deepcopy(initial_pos)
            x = tuple(x)
            loc.append(x)
            continue
        elif s == "S":
            initial_pos[1] = initial_pos[1]-1
            if initial_pos[1] < 0:
                border = False
                break
            x = copy.deepcopy(initial_pos)
            x = tuple(x)
            loc.append(x)
            continue
        elif s == "E":
            initial_pos[0] = initial_pos[0]+1
            if initial_pos[0] > plateau_size[0]:
                border = False
                break
            x = copy.deepcopy(initial_pos)
            x = tuple(x)
            loc.append(x)
            continue
        else:
            initial_pos[0] = initial_pos[0]-1
            if initial_pos[0] < 0:
                border = False
                break
            x = copy.deepcopy(initial_pos)
            x = tuple(x)
            loc.append(x)
    return loc, border


if __name__ == "__main__":

    I = {
        'N': [1, 1],
        'S': [1, -1],
        'W': [0, 1],
        'E': [0, -1]
    }

    j = False
    plateau_size = []
    while (j == False):
        s = input(
            "\nPlease enter the size of the plateau in the format, 'x y'. \n\n")
        plateau_size, k = check_format(s)
        if k == False:
            continue
        if (plateau_size[0] > 0 and plateau_size[1] > 0):
            j = True
        else:
            print("Please enter positive coordinates for plateau size")
    print("Plateau size is set to", plateau_size)

    m = False
    while (m == False):
        s2 = input(
            "\nPlease enter the number of rovers you would like to put on the plateau. \n\n")
        i2 = check_int(s2)
        if (i2 > 0):
            m = True
        print("Number of rovers is ", i2)

    Rovers = []
    for x in range(0, i2):
        rover_pos = []
        x = False
        while (x == False):
            s = input(
                "\nPlease enter the initial coordinates of the rover in the format, 'x y'. \n\n")
            rover_pos, k = check_format(s)
            if k == False:
                continue
            if (rover_pos[0] <= plateau_size[0] and rover_pos[0] >= 0 and rover_pos[1] <= plateau_size[1] and rover_pos[1] >= 0):
                x = True
            else:
                print(
                    "Error: Please enter initial coordinates within the bounds of the plateau size.")
                x = False

        print("Rover initial coordinates is set to ", rover_pos)

        z = False
        while (z == False):
            t = copy.deepcopy(rover_pos)
            temp = True
            rover_instructions = input(
                "\nPlease enter the instructions for the rover route. \n\n")
            for i in rover_instructions:
                if i not in I:
                    print("Please enter a string with only N S E W without spaces.")
                    temp = False
                    break
            if temp == False:
                continue
            location, border = decode_instructions(
                I, t, rover_instructions, plateau_size)
            if border == False:
                print(
                    "Instructions moved rover out of plateau region, please re-enter instructions")
                continue
            if temp == True and border == True:
                z = True

        print("Rover was successfully loaded with instructions: ", rover_instructions)

        location = dict.fromkeys(location)
        r = Rover(location)
        Rovers.append(r)

    # for r in Rovers:
    #   print(r.locations)

    col = plateau_size[0]+1
    row = plateau_size[1]+1
    plateau = [[0] * (col) for i in range(row)]
    for r in Rovers:
        for key in r.locations:
            plateau[key[0]][key[1]] = plateau[key[0]][key[1]]+1
    answers = []
    for i in range(row):
        for j in range(col):
            if plateau[i][j] > 1:
                answers.append((i, j))

    for index, item in enumerate(answers):
        print("\nIntersection point", index+1, ":", item[0], item[1])
