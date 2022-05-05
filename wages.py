def wages(w,h):
    import random
    
    h=random.randrange(35) + 35
    print("Number of hours: ",h)
    if h>60:
        t1=h-60
        wage=10*40 + 10*20*1.5 + 10*t1*2
    elif (h>40) and h<=60:
        t1 = h-40
        wage = 10*40 + 10*1.5*t1
    elif h<=40:
        wage=print("The salary cannot be generated \a")
    return wage
print("Total wage: ",wages(10,37))
