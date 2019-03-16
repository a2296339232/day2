if __name__ == '__main__':

    for i in range(0,110):

        if(i%10==9  and i!=0):
            print(str(i).ljust(5))
        else:
            print(str(i).ljust(5), end="")

