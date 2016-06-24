year=int(raw_input("plz enter year\n"))
month=int(raw_input("plz enter month\n"))
day=int(raw_input("plz enter day\n"))
result=0
plusday=0
for i in range (1,month):
    if i in [1,3,5,7,8,10,12]:
        date=31
    elif i==2:
        date=28
    elif i in[4,6,9,11]:
        date=30

    plusday=plusday+date



if (year%4==0 or (year/400==0 and year%100!=0)) and month>2  :
    result=day+plusday+1
    print result
else:
    result=day+plusday
    print result

