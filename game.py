import random
import pandas as pd
import sys,time


while True:
    print("——圣杯战争——")
    print("规则：Saber克制Lancer；Acher克制Saber；Lancer克制Acher；Rider克制Caster；Caster克制Assassin；Assassin克制Rider；其他无克制")
    print("[职介序号:1.Saber 2.Acher 3.Lancer 4.Rider 5.Caster 6.Assassin 7.Berserker]")
    aStr = input("请开始召唤英灵,输入序号：")
    macStr = random.randint(1,7)

    
#英灵座
    Saber = random.choice(["阿蒂拉", "罗摩","亚瑟王","兰陵王"])
    Acher = random.choice(["拿破仑", "伊修塔尔", "吉尔伽美什","阿塔兰忒"])
    Lancer = random.choice(["斯卡哈","李书文","恩奇都"])
    Rider = random.choice(["伊斯坎达尔", "奥兹曼迪亚斯", "魁札尔·科亚特尔","欧罗巴"])
    Caster = random.choice(["美狄亚", "梅林", "玄奘三蔵"])
    Assassin = random.choice(["酒吞童子", "山之翁", "赛米拉米斯"])
    Berserker = random.choice(["源赖光", "项羽", "赫拉克勒斯"])

     #转换
    dic = {}
    dic[1] = Saber
    dic[2] = Acher
    dic[3] = Lancer
    dic[4] = Rider
    dic[5] = Caster
    dic[6] = Assassin
    dic[7] = Berserker


    
    #如果输入的是数字，并且在1234567中
    if aStr.isdigit() and (int(aStr) in [1,2,3,4,5,6,7]): #用户的
        a = int(aStr)
        am = dic[a]
    

    if macStr in [1,2,3,4,5,6,7]:  #远坂凛的
        mac = int(macStr)
        macdd = dic[mac]
        
        
    dk = [Saber,Acher,Lancer,Rider,Caster,Assassin,Berserker]


    print("你召唤了：", am)

    # 远坂凛随机选择出拳
    #mac = random.choice(dk)

    print("远坂凛召唤了：",macdd)
    if am in dk:
        if (a == 7 and mac !=7) or (a !=7 and mac == 7):
            for i in range(100):
                    str = '激斗中'
                    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))   
                    sys.stdout.flush()
                    time.sleep(0.001)
            print("\n互相克制，两败俱伤")
            print("圣杯战争结束，下一次圣杯战争需要等6年")
            time.sleep(6)
            wish = input("你想再来一次么？y(Y) or n(N)")
            if wish == 'y' or wish == 'Y':
                continue
            if wish == 'n' or wish == 'N':
                break
        elif (a == 1 and mac ==3 or 
              a == 2 and mac ==1 or 
              a == 3 and mac ==2 or
              a == 4 and mac == 5 or
              a == 5 and mac == 6 or
              a == 6 and mac == 4):
            for i in range(100):
                    str = '激斗中'
                    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
                    sys.stdout.flush()
                    time.sleep(0.1)
            print("\n恭喜，你获得了圣杯！")
            print("圣杯战争结束，下一次圣杯战争需要等6年")
            time.sleep(6)
            wish = input("你想再来一次么？y(Y) or n(N)")
            if wish == 'y' or wish == 'Y':
                continue
            if wish == 'n' or wish == 'N':
                break
        elif (a == 3 and mac ==1 or 
              a == 1 and mac ==2 or 
              a == 2 and mac ==3 or
              a == 5 and mac == 4 or
              a == 6 and mac == 5 or
              a == 4 and mac == 6):
            for i in range(100):
                    str = '激斗中'
                    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
                    sys.stdout.flush()
                    time.sleep(0.1)
            print("\n很遗憾，你输了,无法获得圣杯！")
            print("圣杯战争结束，下一次圣杯战争需要等6年")
            time.sleep(6)
            wish = input("你想再来一次么？y(Y) or n(N)")
            if wish == 'y' or wish == 'Y':
                continue
            if wish == 'n' or wish == 'N':
                break
        elif(am == macdd):
            print("圣杯受到了污染，召唤出错，圣杯战争终止！")
            print("圣杯战争结束，下一次圣杯战争需要等6年")
            time.sleep(6)
            wish = input("你想再来一次么？y(Y) or n(N)")
            if wish == 'y' or wish == 'Y':
                continue
            if wish == 'n' or wish == 'N':
                break
        else:
            print("激斗中",end = "")
            for i in range(100):
                    str = '激斗中'
                    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
                    sys.stdout.flush()
                    time.sleep(0.2)
                    cl.sendMessage(to,"\n没有职介克制，难说！")
                    cl.sendMessage(to,"\n圣杯战争结束，下一次圣杯战争需要等6年")
            time.sleep(6)
            wish = input("你想再来一次么？y(Y) or n(N)")
            if wish == 'y' or wish == 'Y':
                continue
            if wish == 'n' or wish == 'N':
                break
    else:
        print("输入错误")
        break
else:
    print("Game Over")