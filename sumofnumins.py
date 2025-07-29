#sum of all numbers in string
s='1sdefdc34rdff54'
total=0
num=""
for char in s:
    if char.isdigit():
        num+=char
    else:
        if num!="":
            total+=int(num)
            num=""
if num!="":
    total+=int(num)
print(total)