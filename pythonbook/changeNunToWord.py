knownnum={
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9: 'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',



}
def changemethod():
    input=raw_input("plz enter a number\n")
    list1= list(input)
    result=""


    if len(list1)==1:
        result=knownnum[int(list1[0])]
        # print result
    elif len(list1)==2 :
        if list1[0]=='1':
            result=knownnum[int(input)]
            # print result
        else:
            result=knownnum[(int(list1[0])*10)]+"_"+knownnum[int(list1[1])]
            # print result

    elif len(list1)==3:
        if int(input)%100==0:

            result=knownnum[int(input)/100]+"_hundred"
            # print result
        else:
            if list1[1]=='1':
                # print list1
                result=knownnum[int(list1[0])]+"_hundred and "+knownnum[int(list1[1]+list1[2])]
                # print result
            else:
                result=knownnum[int(list1[0])]+"_hundred and "+knownnum[int(list1[1])*10]+"_"+knownnum[int(list1[2])]
                # print result
    print result


    # if inputNumber>=0 and inputNumber<=20:
    #     result=knownnum[inputNumber]
    #     print result
    #
    # elif inputNumber>20 and inputNumber<100:
    #     list1=str(input)
    #     number1=(int(list1[0]))*10
    #     number2=int(list1[1])
    #     result=knownnum[number1]+"_"+knownnum[number2]
    #     print result
    #
    # elif inputNumber>=100 and inputNumber<=1000:
    #     list1=str(input)
    #
    #     result=knownnum[int(list1[0])]+"_hundred and "+knownnum[(int(list1[1])*10)]+"_"+knownnum[int(list1[2])]
    #     print result





if __name__=="__main__":
    changemethod()


