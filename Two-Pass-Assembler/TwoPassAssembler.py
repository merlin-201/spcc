# Two Pass Assembler Program

# --------------------------------------------------------------------------------------
#               M O T   T A B L E   A N D   R E G I S T E R    T A B L E
# ---------------------------------------------------------------------------------------

# Machine Object Table
motTable = {
    "STOP": "['IS', 00]",
    "ADD": "['IS', 01]",
    "SUB": "['IS', 02]",
    "MULTI": "['IS', 03]",
    "MOVER": "['IS', 04]",
    "MOVEM": "['IS', 05]",
    "COMB": "['IS', 06]",
    "BC": "['IS', 07]",
    "DIV": "['IS', 08]",
    "READ": "['IS', 09]",
    "PRINT": "['IS', 10]",
    "START": "['AD', 01]",
    "END": "['AD', 02]",
    "ORIGIN": "['AD', 03]",
    "EQU": "['AD', 04]",
    "LTORG": "['AD', 05]",
    "DS": "['DL', 01]",
    "DS": "['DL', 02]"
}

# Registers Table
registers = {
    "AREG": "['RG', 01]",
    "BREG": "['RG', 02]",
    "CREG": "['RG', 03]",
    "DREG": "['RG', 04]",
}

# --------------------------------------------------------------------------------------
#               P A S S - 1     O F     2 - P A S S     A S S E M B L E R
# ---------------------------------------------------------------------------------------

# Pass-1 of 2-Pass Assembler
def passOne(instructions):

    intermediateCode = []
    symbolTable = dict()
    literalTable = dict()
    literalCount, locationCounter = 0, 200

    for instruction in instructions:

        lineCode = []

        for word in instruction:
            
            # Case-1: If the keyword is LTORG -> Literal Tables will start filling
            if word == 'LTORG':
                base = locationCounter
                for key, value in literalTable.items():
                    literalTable[key] = base
                    base = base + 1

            # Case-2: If the keyword is a constant
            if word.isnumeric():
                lineCode.append(['C', int(word)])
            
            # Case-3: If the keyword is a Literal
            elif word[0] == '=':
                if word not in literalTable:
                    literalTable[word[2:3]] = literalCount
                    lineCode.append(['L', literalCount])
                    literalCount = literalCount + 1
                else:
                    lineCode.append(['S', literalTable[word]])
            
            # Case-4: If the keyword is an assembly instruction present in MOT table or the keyword is a register
            elif word in motTable or word in registers:
                for key, value in motTable.items():
                    temp = []
                    if key == word:
                        temp.append(motTable[key][2:4])
                        temp.append(motTable[key][7:9])
                        lineCode.append(temp)
                for key, value in registers.items():
                    temp = []
                    if key == word:
                        temp.append(registers[key][2:4])
                        temp.append(registers[key][7:9])
                        lineCode.append(temp)
            
            # Case-5: Since, check for LTORG, constant, literal, as well as valid assembly is done, the keyword left would definitely be a symbol
            else:
                if word not in symbolTable:
                    symbolTable[word] = locationCounter
                    lineCode.append(['S', locationCounter])
                else:
                    lineCode.append(['S', symbolTable[word]])

        # Updating the location counter
        locationCounter = locationCounter + 1
        intermediateCode.append(lineCode)

    # Pass-1 returns Intermediate Code and equivalent Data structures output
    return [symbolTable, literalTable, intermediateCode]

# --------------------------------------------------------------------------------------
#               P A S S - 2     O F     2 - P A S S     A S S E M B L E R
# ---------------------------------------------------------------------------------------

# Pass-2 of 2-Pass Assembler
def passTwo(passOneOutput):
    symbolTable, literalTable, interCode = passOneOutput[0], passOneOutput[1], passOneOutput[2]

    machineCode = []
    for instruction in passOneOutput[2]:
        temp = []
        for word in instruction:
            if(word[0] == "AD" or word[0] == "C"):  continue
            index = int(word[1])
            if(word[0] == 'L'):
                literals = list(literalTable.values())
                temp.append(literals[index])
            else:
                temp.append(int(word[1]))
        machineCode.append(temp)

    return machineCode

# --------------------------------------------------------------------------------------
#                               D R I V E R     C O D E
# ---------------------------------------------------------------------------------------

# Driver Code
def main():
    
    # File Handling
    file = open("Code.txt", "r")
    print("\nThe Assembly Language Code served as Input to Pass-1 Assembler is as follows:")
    print("-----------------------------------------------------------------------------\n")

    # Parsing the assembly code
    instructions = []
    for line in file:
        instruction = line.rstrip().split(" ")
        instructions.append(instruction)

    for instruction in instructions:
        print(" ".join(instruction))

    # Call to Pass-1 of Two Pass Assembler
    passOneOuptut = passOne(instructions)

    print("\nThe Intermediary Code and Status of Data Structures after Pass-1 are as follows:") 
    print("-------------------------------------------------------------------------------\n")

    print("-> Symbol Table: ")
    print("-----------------")   
    print(passOneOuptut[0])
    print("\n")

    print("-> Literal Table: ")
    print("------------------")   
    print(passOneOuptut[1])
    print("\n")

    print("-> Intermediary Code: ")
    print("---------------------\n")
    i = 1
    for instruction in passOneOuptut[2]:
        print("Line " + str(i) + " Machine Code -> ", instruction)
        i = i + 1
    
    print("\n-> The Final Machine Code after Pass-2 are as follows:") 
    print("---------------------------------------------------\n")

    # Call to Pass-2 of Two Pass Assembler
    passTwoOutput = passTwo(passOneOuptut)
    i = 1
    for instruction in passTwoOutput:
        print("Line " + str(i) + " Machine Code -> ", instruction)
        i = i + 1

    print("\n")

# Call to the Main Function
main()