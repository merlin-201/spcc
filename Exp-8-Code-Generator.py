def cg(code):
    c = code[0]
    d = {}
    c1 = c.split("=")
    op = {
        "+" : "ADD",
        "-" : "SUB"
    }

    j=1
    f=""

    for i in c1[1]:
        if i in op.keys():
            f=i
            continue

        print("MOV" + " " + "R" + str(j) + "," + i)
        j = j+1
    
    print( op[f] + " " + "R1" + "," + "R2")

    d[ c1[0] ] = "R1"

    for w in code[1:]:
        ch = 0
        r = []
        r = w.split("=")

        if len( r[1] ) == 1:
            print("MOV" + " " + r[0] + "," + d[r[1]])
        else:
            for t in r[1]:
                if t in op.keys() :
                    f = t
                    continue

                if t in d.keys() :
                    ch = 1
                    if r[1].index(t) == 0 :
                        ind = 2
                    else:
                        ind = 1
                    print("MOV" + " " + " " + " R2" + "," + r[1][ind] )
                    m = d[t]
                
            if ch==0 :
                print("MOV" + " " + " " + "R1" + "," + r[1][0] )
                print("MOV" + " " + " " + "R2" + "," + r[1][2] )
                m = "R1"
                
            print( op[f] + " " + m + "," + "R2" )
        
        d[r[0]] = "R1"

def main():
    code = [
        "A=B+C",
        "B=A-D",
        "C=B+C",
        "D=B"
    ]
    print("Generated Code : \n")
    cg(code)

if __name__ == "__main__":
    main()