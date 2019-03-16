import  random
if __name__ == '__main__':
    rimu=["比利海灵顿","木吉kazuya","范达克霍姆","贝奥兰迪"]
    list=sorted(rimu,reverse=True)
    print(list)
    print(rimu)

    rimu=[1,16,32,2,66,88]
    random.shuffle(rimu)
    print(rimu)

    print(sorted(rimu))
    rimu.sort()

    rimu.reverse()
    print(rimu)