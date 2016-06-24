a=raw_input("plz enter a string \n")
letters=0
countspace=0
countnumber=0
countothers=0
lm=0
for c in a:
    if c.isalpha():
        letters+=1
    if c.isdigit():
        countnumber+=1
    if c.isalnum():
        lm+=1
    if c.isspace():
        countspace+=1

    else:
        countothers+=1

print  letters,countothers,countnumber,countothers,lm
print c.capitalize()
print c.center(3)
