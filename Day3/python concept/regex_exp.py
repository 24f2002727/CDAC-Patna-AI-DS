import re

pattern = re.compile('([a-zA-Z]+)@([\d]+)')

s:str = "Prabhakar@123456@"

m = pattern.match(s) # This will return substring that will match in a given string
print(m)

# This will return None if string is not fully matched
# Hence this can be used to validate data
print(pattern.fullmatch(s)) 

print(m.group(1))
