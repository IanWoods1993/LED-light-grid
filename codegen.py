for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open (str(char) + ".txt", 'r') as inFile, open(str(char) + ".py", 'w') as outFile:
        outFile.write("def " + char + "():\n")
        lineNum = 0
        for line in inFile.readlines():
            for pos in range(0, len(line)):
                if (line[pos] == "X"):
                    outFile.write("  strip.setPixelColor(" + str(lineNum * 8 + pos) + ", Color(0, 0, 255))\n")
            lineNum += 1

        outFile.write("  strip.show()\n")
