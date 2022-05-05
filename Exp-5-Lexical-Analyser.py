non_tokens = ['//', '#']
operators = ['{', '}','(',')',',','>',"=",";"]
keywords = ['int','if','else', 'return']
white_spaces = [' ', '\n','\t']

res = []

def add_token(t):
    t = t.strip()
    if len(t) == 0:
        return

    temp = {'lexeme' : t}

    if t in operators:
        temp['token'] = 'operator'
    elif t in keywords:
        temp['token'] = 'keyword'
    else:
        temp['token'] = 'identifier'

    res.append(temp)



def main():
    with open('sample_cpp_code.txt') as f:
        code = f.read()
        
        lines = code.split('\n')
        for line in lines:
            if len(line) == 0:
                continue
            
            temp = ""
            for ch in line:
                if temp in non_tokens:
                    break

                if ch in operators:
                    add_token(temp)
                    add_token(ch)
                    temp = ""
                    continue
                
                if ch in white_spaces and len(temp) != 0:
                    add_token(temp)
                    temp = ""
                elif ch not in white_spaces:
                    temp += ch

    print('-'*10 + "Lexical Analysis" + '-'*10 + '\n')
    for r in res:
        print(r['lexeme'], "\t- ", r['token'])


if __name__ == '__main__':
    main()