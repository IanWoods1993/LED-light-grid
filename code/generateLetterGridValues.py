def main():
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open("../letters/" + str(char) + ".txt", 'r') as inFile, open("display/letterGridValues/" + str(char) + ".py",
                                                                           'w') as outFile:
            outFile.write("def " + char + "(strip, pos):\n")
            outFile.write("  arr = []\n")
            lineNum = 0
            positionInStrip = 0
            for line in inFile.readlines():
                line = line.rstrip('\n')
                # reverse the string if it's an odd number
                if lineNum % 2 == 1:
                    line = line[::-1]

                for positionInLine in range(0, len(line)):
                    if line[positionInLine] == "X":
                        writeLine(line, lineNum, positionInLine, positionInStrip, outFile)
                        positionInStrip += 1
                        
                lineNum += 1

            outFile.write("  return arr\n")


def writeLine(line, lineNum, positionInLine, positionInStrip, outFile):
        outFile.write("  arr.append(64 * pos + " + str(lineNum * 8 + positionInLine) + ")\n")


main()
