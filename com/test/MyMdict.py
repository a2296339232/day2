if __name__ == '__main__':
    num=int(input("请输入你想输入键值对的个数"))
    mdict=dict()

    for i in range(num):
        keys=input("请输入键")
        val=input("请输入值")
        mdict[keys]=val

    print(mdict)
    keys=mdict.keys()
    print(mdict.values())
    itemss= mdict.items()
    for i in keys :
        print(i)