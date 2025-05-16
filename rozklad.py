def rozklad(n):
    i = 2
    while i <= int(n**0.5) and n > 1:
        if n % i ==0:
            print(i ,end="*")
            n = n // i
        else:
            i+=1
    print(i)


rozklad(44100)