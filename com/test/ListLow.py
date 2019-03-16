if __name__ == '__main__':
    mlist=[1,'AAA','The Word','给不给党',12.6,True]
    unlist=[str(i) for i in mlist]
    for i in unlist:
        unlist[unlist.index(i)]=i.upper()
    print(unlist)

    mlist = [1, 'AAA', 'The Word', '给不给党', 12.6, True]
    for i in mlist:
        if isinstance(i,str):
           mlist[mlist.index(i)]= i.lower()
    print(mlist)