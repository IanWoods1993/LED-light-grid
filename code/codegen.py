for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open ("../letters/" + str(char) + ".txt", 'r') as inFile, open("../display/" + str(char) + ".py", 'w') as outFile:
        outFile.write("@staticmethod\n")
        outFile.write("def " + char + "(strip, pos):\n")
        lineNum = 0
        for line in inFile.readlines():
            for pos in range(0, len(line)):
                if (line[pos] == "X"):
                    outFile.write("  strip.setPixelColor(64 * pos + " + str(lineNum * 8 + pos) + ", Color(0, 0, 255))\n")
            lineNum += 1

        outFile.write("  strip.show()\n")
