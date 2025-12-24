"""
WAP to get sequence of lines from user(break if user enter nothing). Then print the same lines but all lines must be in small case.
"""
def  problem1():
    lines:list[str]=[]
        
    while(True):
        line=input()
        if line:
            lines.append(line)
        else:
            break
        # modified_line=[word.lower() for word in line if word!=""]
        # lines=""
        # for word in modified_line:
            # lines+=word
        # print(lines)
        # breaking=input("Enter anything for taking more lines else type nothing")
        # if breaking=="":
        #     break
    # return 0
    for line in lines:
        print(line.lower())
problem1()
