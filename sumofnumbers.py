def show_sequence(n):
    #a=sum(range(n+1))
    num=1
    sum=0
    b=0
    if n == 0:
        return (str(n) + '=0')
    else:
        if n < 0:
            return (str(n) + '<0')
        else:
            while num <= n:
                sum +=num
                b = (str(b) + '+' + str(num))
                num += 1
            c= (b + ' ' + '=' + ' ' + str(sum))
            return c;
