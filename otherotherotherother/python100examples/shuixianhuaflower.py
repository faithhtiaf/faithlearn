for i in range(100,1000):
    a=i/100
    j=i/10%10
    k=i%10
    if a**3+j**3+k**3==i:
        print i


