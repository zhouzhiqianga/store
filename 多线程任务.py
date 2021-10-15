from threading import Thread
import time
hamburger=0

class cook(Thread):
    name = ""
    count=0
    def run(self) -> None:
        global hamburger
        while True:
            if hamburger < 500 :
                self.count=self.count+1
                hamburger += 1
                print(self.name,"已经做好了1个")

                if hamburger == 500:
                    time.sleep(0.1)
                    # print("汉堡篮子已满！请等待三秒...")
                else:
                    continue
            else:
                print(self.name,"做了",self.count,"个")
                break


class customer(Thread):
    name = ""
    money = 500
    def run(self) -> None:
        global hamburger
        while True:
            if self.money >0 :
                self.money -=1
                hamburger  -= 1
                print(self.name,"吃了个汉堡")
                if hamburger <= 0:
                    time.sleep(3)
                else:
                    continue
            else:
                print("钱用完了")
                break



p1=cook()
p1.name="1"
p2=cook()
p2.name="2"
p3=cook()
p3.name="3"

a1=customer()
a1.name="1号"
a2=customer()
a2.name="2号"
a3=customer()
a3.name="3号"
a4=customer()
a4.name="4号"
a5=customer()
a5.name="5号"
a6=customer()
a6.name="6号"

p1.start()
p2.start()
p3.start()

a1.start()
a2.start()
a3.start()
a4.start()
a5.start()
a6.start()




















































