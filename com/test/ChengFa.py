if __name__ == '__main__':
    num=range(1,10)
    for i in num:
        for j in range(1,i+1):
            print(i,"*",j,"=",i*j,"\t",end="")
        print()

    for i in num:
        for j in range(1,i+1):
            mm=str(i*j).ljust(3)
            print(i,"*",j,"=",mm,end="",sep=" ")
        print()


    numm=str(1 * 10).ljust(1)
    print(numm,1)
    print(1, 1)
