def main():
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open ("../letters/" + str(char) + ".txt", 'r') as inFile, open("../display-letters/" + str(char) + ".py", 'w') as outFile:
            outFile.write("@staticmethod\n")
            outFile.write("def " + char + "(strip, pos):\n")
            lineNum = 0
            for line in inFile.readlines():
    	        if (lineNum % 2 == 1):
    	            for pos in range(len(line), 0):
                        writeLine(line, lineNum, pos, outFile)
                else: 
    	            for pos in range(0, len(line)):
		        writeLine(line, lineNum, pos, outFile)
            
	        lineNum += 1
            
	    outFile.write("  strip.show()\n")

def writeLine(line, lineNum, positionInLine, outFile):
    if (line[positionInLine] == "X"):
        outFile.write("  strip.setPixelColor(64 * pos + " + str(lineNum * 8 + positionInLine) + ", Color(0, 0, 255))\n")

main()
