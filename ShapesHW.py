# Size of the staircases
size = 8
for line in range (size):
    print()
    # Prints the first staircase
    for number in range (line+1):
        print('*', end = '')
    # Prints the spaces in between staircase 1 and 2
    for space in range (size-line-1):
        print(' ', end = '')
    # Prints the second staircase
    for number in range (size-line):
        print('*', end ='')
    # Prints the spaces inbetween staircase 2 and 3
    for space in range (line):
        print(' ', end = ' ')
    # Prints the third staircase
    for number in range (size-line):
        print('*', end ='')
    # Prints the spaces inbetween staircase 3 and 4
    for space in range (size-line-1):
        print (' ',end = '')
    # Prints the last staircase
    for number in range (line+1):
        print('*', end = '')
