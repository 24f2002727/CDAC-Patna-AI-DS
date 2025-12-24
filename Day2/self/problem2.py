"""
For a given list of elements check if the list is pallindrome or not
"""
def problem2(lst):
    if lst=="":
        return True
    
    # for element in lst:
    #     str_elem=str(element)
    #     if element!=str_elem[::-1]:
    #         return False
    # return True
    return(lst==lst[::-1])

list1=["Ram","Shyam"]
list2=["heh","ihi","RAma"]
list3=["@#$#@",1221,""," ","RAMA"]
list4=["hi",1221,"hi"]
print(problem2(list1))
print(problem2(list2))
print(problem2(list3))
print(problem2(list4))

    