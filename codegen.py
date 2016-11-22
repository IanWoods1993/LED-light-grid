with open ("A.txt", 'r') as f:
    lineNum = 0
    for line in f.readlines():
        for pos in range(0, len(line)):
            if (line[pos] == "X"):
                print("strip.setPixelColor(" + str(lineNum * 8 + pos) + ", Color(0, 0, 255)")
        lineNum += 1

print("strip.show()")
