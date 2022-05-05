class Grammer:

    def __init__(self, s):
        #reading the grammer string :
        self.prods = {}
        self.terminals = set()
        self.non_terminals = set()
        for line in s.split('\n'):
            if len(line) > 0:
                lhs = line[0]
                self.non_terminals.add(lhs)
                self.prods[lhs] = []

                rhs = line[3:]

                for word in rhs.split('|'):
                    for ch in word:
                        if ch.isupper():
                            self.non_terminals.add(ch)
                        else:
                            self.terminals.add(ch)
        
                    self.prods[lhs].append(word)
        
        print("Grammer object created")
        print("\t-> Non Terminals : ", self.non_terminals)
        print("\t-> Terminals : ",self.terminals)
        print("\t-> Production Rules : ")
        for ch in self.prods:
            print("\t\t",ch, " : ", self.prods[ch])


    
    def first(self, ch):
        ans = set()

        if ch in self.non_terminals:
            alternatives = self.prods[ch]

            for alt in alternatives:
                ans.update(self.first(alt[0]))
            
            return ans

        elif ch in self.terminals:
            return {ch}

        elif ch=='' or ch=='@':
            return {'@'}
    
    def follow(self, ch):
        ans = set()

        if ch == "S":
            ans.add("$")

        for lhs,rhs in self.prods.items():

            for alternative in rhs:
                #print("checking alt : ", alternative)
                if ch not in alternative:
                    continue
                
                #print(ch," found in alt")
                loc = alternative.index(ch)

                if loc+1 == len(alternative):
                    ans.update(self.follow(lhs))
                else:
                    right_ch = alternative[loc+1]
                    #print("right ch : ", right_ch)

                    if right_ch in self.terminals:
                        ans.add(right_ch)
                    elif right_ch in self.non_terminals:
                        ans.update(self.first(right_ch))

        return ans
                

                
                
                    


example_string1 = '''
S->ABC|ghi|jkl
A->a|b|c
B->b
C->d
'''

example_string2 = '''
S->ACD

C->a|b
'''

def main():

    g1 = Grammer(example_string1)
    print('\n')

    print("\nFirst of each non-terminal :")
    for ch in g1.non_terminals:
        print(f"first({ch}) : ", g1.first(ch))

    print("\nFirst of each terminal :")
    for ch in g1.terminals:
        print(f"first({ch}) : ", g1.first(ch))
    print('\n\n')

    g2 = Grammer(example_string2)
    print('\n')

    ch = "S"
    print(f"follow({ch}) : ", g2.follow(ch))

    ch = "A"
    print(f"follow({ch}) : ", g2.follow(ch))

    ch = "D"
    print(f"follow({ch}) : ", g2.follow(ch))


if __name__ == '__main__':
    main()