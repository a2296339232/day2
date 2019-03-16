if __name__ == '__main__':
    mdict=dict()
    keys=["a","b","c","d"]
    values=["啊","波","次","得"]
    for i in keys:
        mdict[i]=values[keys.index(i)]
    print(mdict)

    json={"id":1,type:{"name":"贝奥兰迪","age":18}}
    #字典内字典对象 通过类似二维数组下标的访问方式，依旧是键的值去访问属性
    print(json[type]["name"])
    json["names"]="比利海灵顿"
    print(json)
    del json["names"]
    print(json)

    print(str(json))

    mdict[("kazuya")]="木吉鬼步"
    print(mdict)

    for k,y in mdict.items():
        print("键对应：",k,"\t","值对应",y)

    mdict = {"木吉":"kazuya","比利海灵顿":"森之之妖精","理查德米罗斯":"香蕉君"}
    i=1
    json={k:v for k,v in mdict.items()}
    print(mdict)
    print(json)
    #深拷贝    传值
    mdict=json.copy()
    mdict["van"]="暗黑佟大为"
    print(mdict)
    print(json)
    #浅拷贝传地址
    json=mdict
    json["啊？"]="给给给党"
    print(json)
    print(mdict)