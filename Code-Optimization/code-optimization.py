# Algebraic

def asm(code):
  code1=[]
  for i in code:
    if "+0" in i:
      i=i.replace("+0","")
    if "*1" in i:
      i=i.replace("*1","")
    code1.append(i)
  for i in code1:
    i=i.split("=")
    if(i[0]==i[1]):
      continue
    print(i[0]+"="+i[1])
n=int(input("Enter number:"))
code=[]
for _ in range(n):
  s=input("Enter line:")
  code.append(s)
asm(code)

# Dead Code

def dc(code):
  tod=[]
  for i in code:
    print(i)
  print("-"*15)
  for i in code:
    #tod=[]
    if "if" in i:
      j=code.index(i)
      i1=i.split(" ")
      i1[1]=i1[1][1:len(i[1])-2]
      c=i1[1].split("==")
      d=code[j-1].split("=")
      if(c[1]!=d[1]):
        tod.append(code[j])
        #code.remove(code[j])
        j=j+1
        while(code[j][0]==" "):
          tod.append(code[j])
          j=j+1
          if(j==len(code)):
            break
  print("Optimized code after dead code elimination:")
  for a in code:
    if "return" in a:
      break
    if a in tod:
      continue
    print(a)
n=int(input("Enter no of lines:"))
code=[]
for _ in range(n):
  s=input("Enter line:")
  code.append(s)
dc(code)