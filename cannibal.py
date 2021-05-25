import requests
def api():
 while True:
  try:
   api_address = "http://api.openweathermap.org/data/2.5/weather?q="
   city=input("Enter City: ")


   url = api_address+city+"&appid=09fe6247b87b124499dc7fc3f49b5ae1"

   json_data=requests.get(url).json()


   print("STATUS      : ", json_data['weather'][0]['main'])
   print("DESCRIPTION : ",json_data['weather'][0]['description'])
   print("TEMPERATURE : ", json_data['main']['temp']-273.15 )
   break
  except:
    print("Enter valid input")


class boat:
    def __init__(self):
        self.x="_"
        self.y="_"
        self.s="R"

b= boat()

class game:
    def __init__(self):
        self.mr=self.cr=3
        self.ml=self.cl=0

g= game()

def disp():
    k1=k2=0
    for i in range(2):
        print()
    for i in range(1,g.ml+1):
        print("M",end="")
        k1+=1
    if k1<3:
        for i in range(1,4-k1):
            print(" ",end="")
    print(" ",end="")
    for j in range(1,g.cl+1):
        print("C",end="")

        k2+=1
    if k2<3:
        for i in range(1,4-k2):
            print(" ",end="")


    #printing river boat
    if b.s=='L':
        print("\\_",b.x,"_",b.y,"_/",end="")
        print("_ _ _ _ _ _ _ _",end="")
    elif b.s=="R":
        print("_ _ _ _ _ _ _ _",end="")
        print("\\_",b.x,"_",b.y,"_/",end="")
    k1=k2=0


    #printing right side
    for i in range(1,g.mr+1):
        print("M",end="")
        k1+=1
    if k1<3:
        for i in range(1,4-k1):
            print(" ",end="")
    print(" ",end="")
    for j in range(1,g.cr+1):
        print("C",end="")
        k2+=1
    if k2<3:
        for i in range(1,4-k2):
            print(" ",end="")
    print(" ",end="")
    print("\n\n")

def func():
    api()
    disp()

    while g.ml<3 and g.cr<4 and g.mr<4 and g.cl<4:
        print("\nEnter C(cannibals), M(missionaries and N(No person) on boat:\n")
        print("Enter 1st person")
        b.x=input()
        if  b.x==27:
            exit()
        #  else:
        #print(b.x,"\n")
        b.x=b.x.upper()
        while b.x!='C' and b.x!='M'and b.x!='N':
            print("")
            print("WRONG!! ENTER INPUT AGAIN:")
            b.x=input()
            if b.x==27:
                exit()
            else:
                print(b.x)
            b.x=b.x.upper()
            if b.x=="M" or b.x=="C" and b.x=="N":
                break
        print("Enter 2nd person")
        b.y=input()
        if b.y==27:
            exit()
        #  else:
        #  print(b.y)
        b.y=b.y.upper()
        while b.y!="C"and b.y!="M"and b.y!="N":
            print()
            print("WRONG ! ENTER INPUT AGAIN  ")
            b.y=input()
            if b.y==27:
                exit()
            else:
                print(b.y)
            b.y=b.y.upper()
            if b.y=="M" or b.y=="C"or b.y=="N":
                break
        disp()
        if b.s=="R":
            b.s="L"
            if b.x=="M":
                g.mr-=1
                g.ml+=1
            elif b.x=="C":
                g.cr-=1
                g.cl+=1
            elif b.y=="N":
                pass

            if b.y=="M":
                g.mr-=1
                g.ml+=1
            elif b.y=="C":
                g.cr-=1
                g.cl+=1
            elif b.y=="N":
                pass
        elif b.s=="L":
            b.s="R"
            if b.x=="M":
                g.mr+=1
                g.ml-=1
            elif b.x=="C":
                g.cr+=1
                g.cl-=1
            elif b.x=="N":
                pass
            if b.y=="M":
                g.mr+=1
                g.ml-=1
            elif b.y=="C":
                g.cr+=1
                g.cl-=1
            elif b.y=="N":
                pass
        print("\n\nAfter boat moving")
        b.x="_"
        b.y="_"
        disp()
        if g.ml>0:
            if g.cl>g.ml:
                lose()
                exit()
        if g.mr>0:
            if g.cr>g.mr:
                lose()
                exit()
        if g.mr>3 or g.cr>3 or g.ml>3 or g.cl>3:
            print("WRONG INPUT! loSE thE GAME")
            exit()
        if g.ml==3:
            print("")
            win()
            exit()

def win():
    print("\n\nYOU WON")
def lose():
    print("\n\nYOU LOSE")

func()
