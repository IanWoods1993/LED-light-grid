def main():
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open("letters/" + str(char) + ".txt", 'r') as inFile, open("better-letters/" + str(char) + ".txt",
                                                                        'w') as outFile:
            for line in inFile.readlines():
                line = line.rstrip()
                while len(line) < 8:
                    line = line + " "
                outFile.write(line + "\n")


main()
