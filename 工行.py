#友情提示：若要完整执行本系统，需要用户手动创建新用户信息；每次重新执行都需要重新添加新用户信息。
import random
import DBUtils
from DBUtils import update,query
print("===============================================")
print("|------------中国工商银行账户管理系统-------------|")
print("|------------------1、开户---------------------|")
print("|------------------2、存钱---------------------|")
print("|------------------3、取钱---------------------|")
print("|------------------4、转账---------------------|")
print("|------------------5、查询---------------------|")
print("|------------------6、退出---------------------|")
print("===============================================")
bank_name="地球国际总部银行"#全局变量
bank={}
#{'Frank': {'password': '123456', 'country': '中国', 'province': '沙河', 'street': '老牛湾', 'door': '0001', 'account': 60547549, 'bank_name': '汉科软地球中国区老牛湾分行', 'money': 0}}
#                 元素1   ，元素 2 ，元素3
def bank_useradd(username,password,country,province,street,door,account):
    if  len(bank) >100:
        return 3
    if username in bank:
        return 2
    bank[username]={

        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "account":account,
        "bank_name":bank_name,
        "money":100000000
    }
    return 1
#1、添加用户
def useradd():
    username=input("请输入您的用户名")
    password=input("请输入您的密码")#print(bank[username]["password"])
    print("下面请您输入你的地址")
    country=input("\t\t请输入你所在的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入你的街道")
    door=input("\t\t请输入您的门牌号")
    money = input('\t\t请输入您的金额')
    account=random.randint(10000000,99999999)
    #             元素1    元素2    元素3
    # while 1:#判断随机数生成的账号是否重复,循环到不重复为止
    #     if account in bank:
    #         account=random.randint(10000000,99999999)
    #     else:
    #         break
    # status=bank_useradd(username,password,country,province,street,door,account)
    sql = 'insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)'
    params = [username,account,password,country,province,street,door,money,"汉科软地球中国区老牛湾分行"]
    update(sql,params)
    # if status ==3 :
    #     print("用户已满")
    # elif status== 2:
    #     print("用户库已存在")
    # elif status == 1:
    #     print("恭喜你成功开户，以下是您的信息")
    #     info = '''
    #                 ------------个人信息------------
    #                 用户名:%s
    #                 账号：%s
    #                 密码：*****
    #                 国籍：%s
    #                 省份：%s
    #                 街道：%s
    #                 门牌号：%s
    #                 余额：%s￥
    #                 开户行名称：%s
    #             '''
    #     # 每个元素都可传入%
    #     print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


#2、存钱
def savemoney():
    username=input("请输入您的用户名")
    password=input('请输入您的密码')
    sql2 = "select * from users where username=%s "
    params2 = [username]
    a=query(sql2,params2)
    print(a)



    if username==a[0]["username"]:
        num = input("请输入您的存款金额:")
        num = int(num)
        if num < 0:
            num = 0
        # bank[accountnumber]["money"] = bank[accountnumber]["money"] + num
        sql1 = "update  users set money=money+%s where username=%s and password=%s"
        params1 = [num,username,password]
        update(sql1,params1)

    #     print("恭喜您存款成功，以下是您的信息")
    #     info = '''
    #     ------------个人信息------------
    #                 用户名：%s
    #                 账号:%s
    #                 存款金额：%s￥
    #                 开户行名称：%s
    #     '''
    #     print(info % (accountnumber,bank[accountnumber]["account"],bank[accountnumber]["money"],bank_name,))
    # else:
    #     return False
#3、取钱
def Withdrawmoney():
    accountnumber=input("请输入您的用户名")
    password=input("请输入您的密码")
    sql3 = "select * from users where username=%s "
    params3 = [accountnumber]
    a = query(sql3, params3)
    print(a)
    # if accountnumber in bank:
    #     if password in bank[accountnumber]["password"]:
    if accountnumber == a[0]["username"]:
        if password == a[0]["password"]:
           takemoney = input("请输入您的取款金额")
           takemoney = int(takemoney)
           if takemoney < 0:
                takemoney = 0
           if takemoney <= a[0]["money"]:
                # bank[accountnumber]["money"] = bank[accountnumber]["money"] - takemoney
                sql1 = "update  users set money=money-%s where username=%s and password=%s"
                params1 = [takemoney, accountnumber, password,]
                update(sql1, params1)

                # info = '''
                #                    ------------个人信息------------
                #     用户名:%s
                #     密码：%s
                #     余额：%s￥
                #     取款金额：%s￥
                #     银行名称：%s
                #           '''
                # print(info % (accountnumber,bank[accountnumber]["account"],bank[accountnumber]["money"],takemoney,bank_name))
                # return 0
           else:
               print("您的余额不足！")
               return 3
        else:
            print("您的密码输入错误！")
            return 2
    else:
        print("您的账户不存在")
        return 1
#4、转账
def Transferaccount():
    accountnumber = input("请输入您的用户名")
    password=input("请输入您转出账号的密码")
    sql5 = "select * from users where username=%s and password=%s"
    params5 = [accountnumber,password]
    a = query(sql5, params5)
    print(a)
    if accountnumber==a[0]["username"]:
        if password==a[0]["password"]:
            Turninaccount = input("请输入您的转入用户名")
            sql8 = "select * from users where username=%s "
            params8 = [Turninaccount]
            b = query(sql8, params8)
            print(b)
            if Turninaccount==b[0]["username"]:
                Turnoutmoney = input("请输入您转账金额")
                Turnoutmoney = int(Turnoutmoney)
                if Turnoutmoney < 0:
                    Turnoutmoney = 0
                if Turnoutmoney <= a[0]["money"]:
                    print("是否转账？")
                    a = input("请输入是或否")
                    if a == "是" :
                        # bank[Turninaccount]["money"] = bank[Turninaccount]["money"]+Turnoutmoney
                        # bank[accountnumber]["money"] = bank[accountnumber]["money"]-Turnoutmoney
                        print("恭喜您转账成功！")
                        sql9 = "update  users set money=money-%s where username=%s and password=%s"
                        params9 = [Turnoutmoney, accountnumber, password]
                        update(sql9, params9)
                        sql10 = "update  users set money=money+%s where username=%s"
                        params10 = [Turnoutmoney, Turninaccount]
                        update(sql10, params10)

        #                 info = '''
        # ------------个人信息------------
        #             用户名：%s
        #             转出账号:%s
        #             转入账号:%s
        #             转出账号密码：%s
        #             转账金额：%s￥
        #             余额：%s￥
        #             开户行名称:%s
        # '''
        #                 if a == "否":
        #                   print("将不会进行转账")
        #                 print(info % (accountnumber,bank[accountnumber]["account"],bank[Turninaccount]["account"],Turninaccount,Turnoutmoney,bank[accountnumber]["money"],bank_name))
                        return 0
                    else:
                        print("取消转账")
                else:
                    print("您的余额不足！")
                    return 3
            else:
                print("您的收款账户？")
                return 1
        else:
            print("密码错误")
            return 2
    else:
        print("用户名错误")
        return 1
#5、查询
def makeenquiries():
    accountnumber = input("请输入您的用户名")
    password=input("请输入您的密码")
    sql7 = "select * from users where username=%s and password=%s"
    params7 = [accountnumber,password]
    a = query(sql7, params7)
    print(a)
    if accountnumber==a[0]["username"]:

        if password==a[0]["password"]:
             print("恭喜您查询成功，以下是您的信息")
             info = '''
        ------------个人信息------------
                    用户名：%s
                    当前账号:%s
                    密码:%s
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s￥
                    当前账户的开户行：%s 
        '''
             print(info % (a[0]["username"],a[0]["account"],a[0]["password"],a[0]["country"],a[0]["provine"],a[0]["street"],a[0]["door"],a[0]["money"],a[0]["bankname"]))
        else:
            print("密码错误！")
    else:
        print("用户名错误！")

while True:
    begin = input("请选择业务")
    if begin == "1":
        useradd()
        # print(bank)
    elif begin == "2":
        savemoney()
        # print(bank)
    elif begin == "3":
        Withdrawmoney()
        # print(bank)
    elif begin == "4":
        Transferaccount()
        # print(bank)
    elif begin == "5":
        makeenquiries()
        # print(bank)
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break