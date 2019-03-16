if __name__ == '__main__':
    lis=list()
    print(lis)
    #appen 追加
    lis.append("a")
    lis.append("b")
    print(lis)
    #insert 向索引目标添加
    #lis.insert(4, "ccc") 索引下标可以超过当前数组限界，超出限界默认至最后添加
    lis.insert(2,1)
    print(lis)

    print(type(lis))
    liss=[1,2,3]
    print(liss)
    #默认删除后面的元素
    print(lis)
    print(type(lis.pop()))
    # del list[]删除对应索引对应的索引元素
    del lis[0]
    print(lis)

    #lis.remove("值") 对应值删除列表内元素

    #del lis删除的是整个对象 打印报错
