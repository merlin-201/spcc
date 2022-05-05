import re

# ----------------------------- input source code ---------------------------- #
source_code = '''
MACRO
INCR &ARG1,&ARG2,&ARG3
ADD AREG,&ARG1
ADD AREG,&ARG2
ADD AREG,&ARG3
MEND
START
INCR A,B,C
INCR DATA1,DATA2,DATA3
A DC 2
B DC 2
C DS 2
DATA1 DC 3
DATA2 DS 2
DATA3 DC 4
END
'''

# ------------------------------ Data Structures ----------------------------- #

MDT = {
    'card' : []
}

MNT = {
    'macro_name' : [],
    'mdt_index' : []
}

ALA = {
    'argument' : []
}

MDTC = 1
MNTC = 1

# ------------------------------ helper function ----------------------------- #

def print_tables():
    print('\n' + '='*10 + ' MDT ' + '='*10)
    print('\nindex\t\tcard\n'+'-'*18)
    for i in range(len(MDT['card'])):
        print(i+1,"\t\t\t",MDT['card'][i])
    
    print('\n'+'='*10 + ' MNT ' + '='*10)
    print('\nindex\t\tmacro_name\t\tmdt_index\n'+'-'*33)
    for i in range(len(MNT['macro_name'])):
        print(i+1,"\t\t\t",MNT['macro_name'][i],"\t\t",MNT['mdt_index'][i])

    print('\n'+'='*10 + ' ALA ' + '='*10)
    print('\nindex\t\targument\n'+'-'*18)
    for i in range(len(ALA['argument'])):
        print(i+1,"\t\t\t",ALA['argument'][i])


def read_macro_name_line(macro_name_line):
    global MDTC
    global MNTC

    macro_name = macro_name_line.split()[0]
    arguments = macro_name_line.split()[1].split(',')

    MDT['card'].append(macro_name_line)

    MNT['macro_name'].append(macro_name)
    MNT['mdt_index'].append(MDTC)

    #preparing argument list array
    for arg in arguments:
        ALA['argument'].append(arg)
    
    MDTC += 1
    MNTC += 1
    return

def replace_dummy_arguments_with_ALA_pos_indicators(line):
    args = [ term for term in re.split('\s|,', line) if '&' == term[0]]
    for arg in args:
        pos_indicator = "#" + str( ALA['argument'].index(arg) + 1 )
        line = line.replace(arg, pos_indicator)

    return line

def replace_pos_indicators_with_arguments(line):
    pos_indicators = [ term for term in re.split('\s|,', line) if '#' == term[0]]
    for p in pos_indicators:
        arg = ALA['argument'][ int(p[1:]) - 1 ]
        line = line.replace(p, arg)

    return line

# ---------------------------------- Pass 1 ---------------------------------- #

def pass1(source):
    intermediate_code = []

    i = 0
    while source[i] != "END":
        if source[i] == "MACRO":
            i += 1
            read_macro_name_line(source[i])
            i += 1
            while source[i] != "MEND":
                line = source[i]
                line = replace_dummy_arguments_with_ALA_pos_indicators(line)

                MDT['card'].append(line)
                i += 1
            MDT['card'].append("MEND")
        else:
            intermediate_code.append(source[i])
        
        i += 1

    #print results of pass 1 :
    print('*'*20 + " PASS 1 " + '*'*20)
    print_tables()
    print('\nIntermediate Code : ')
    for line in intermediate_code:
        print(line)
    
    return intermediate_code

# ---------------------------------- Pass 2 ---------------------------------- #

def pass2(intermediate_code):
    expanded_code = []
    for line in intermediate_code:
        if line.split()[0] in MNT['macro_name']:
            #expanding the macro call
            macro_name = line.split()[0]
            arguments = line.split()[1].split(',')

            # initialise MDTP
            MDTP = int( MNT['mdt_index'][ MNT['macro_name'].index(macro_name) ] ) -1 

            #overwrite the ALA
            for i,arg in enumerate(arguments):
                ALA['argument'][i] = arg
            MDTP += 1

            while MDT['card'][MDTP] != "MEND":
                line = MDT['card'][MDTP]
                line = replace_pos_indicators_with_arguments(line)
                expanded_code.append(line)

                MDTP += 1

        else:
            expanded_code.append(line)
    
    #print results of pass  :
    print('\n' + '*'*20 + " PASS 2 " + '*'*20)
    print('\n' + '-'*7 + 'Expanded Code : ' + '-'*7)
    for line in expanded_code:
        print(line)


# ------------------------------- main function ------------------------------ #
def main():
    source = source_code.split('\n')[1:-1]
    
    intermediate_code = pass1(source)
    expanded_code = pass2(intermediate_code)

if __name__ == '__main__':
    main()