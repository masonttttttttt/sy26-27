for i in range(1, 14):
    for j in range(1, 26):
        if i == 1 or i == 13 or j == 1 or j == 25:
            print ("*",end = "")
        else:
            print (" ",end = "")
    print()