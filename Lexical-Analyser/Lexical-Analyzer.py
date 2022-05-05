# Lexical Analyzer Program

nonTokens = ['#include<stdio.h>', '//', '/*', ' ', '\n', '\b', '\t', '']
operators = ['+', '-', '*', '/', '<', '>', '>=', '<=', '==', '!=', '(', ')', '[', ']', '{', '}', '<<', '>>']
separators = [',', ';']
keywords = ['int', 'main()', 'if', 'return', 'while', 'for', 'cout', 'cin', 'endl', 'using', 'namespace', 'std']
constant = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# --------------------------------------------------------------------------------------
#                           L E X I C A L   A N A L Y Z E R
# ---------------------------------------------------------------------------------------

def LexicalAnalyzer(instructions):

    LexicalAnalysis = dict()
    for line in instructions:

        if(len(line) == 0): continue
        
        for ch in line:
            if ch in nonTokens:
                LexicalAnalysis[ch] = 'Non-Token'
            elif ch in operators:
                LexicalAnalysis[ch] = 'Operator'
            elif ch in separators:
                LexicalAnalysis[ch] = 'Separator'
            elif ch in keywords:
                LexicalAnalysis[ch] = 'Keyword'
            elif ch in constant:
                LexicalAnalysis[ch] = 'Constant'
            else:
                LexicalAnalysis[ch] = 'Identifier'
    
    print("\n-> Lexical Analysis Output: ")
    print("-----------------------------")

    print("\n\tLexeme   \t  Token")
    print("----------------------------------")
    for key, value in LexicalAnalysis.items():
        if(key == '#include<stdio.h>'): print(key + "\t" + value)
        elif(key == 'namespace'):   print(key + "\t\t" + value)
        else:   print(key + "\t\t\t" + value)
    print("\n")

# --------------------------------------------------------------------------------------
#                               D R I V E R     C O D E
# ---------------------------------------------------------------------------------------

# Driver Code
def main():
    
    # File Handling
    file = open("Code.txt", "r")
    print("\nThe CPP Program served as an Input to Lexical Analyzer is as follows:")
    print("-----------------------------------------------------------------------------\n")

    # Parsing the assembly code
    instructions = []
    for line in file:
        instruction = line.rstrip().split(" ")
        instructions.append(instruction)

    for instruction in instructions:
        print(" ".join(instruction))

    LexicalAnalyzer(instructions)

# Call to the Main function
main()