"""
For the given dictionary print only keys and value(other than where value is dictionary),
the dictionary can be nested dictionary.If dictionary encounter print it's key value pair.
"""
def dct_print(dct):
    for key,value in dct.items():
        if type(value)!=dict:
            print(key," ",value)
        else:
            dct_print(value)

# def problem3(dct):
#     for key,value in dct.items():
#         if type(value)!=dict:
#             print(key," ",value)
#         else:
#             problem3(value)
    
dict1={"name":"shivam","age":20,"address":{"vill":"gokhula","p.o.+p.s":{"p.o.":"sikandra","p.s.":"sikandra"},"district":"jamui"},"location":{"state":"Bihar","country":"India"}}
dct_print(dict1)
# print(type(dict1))