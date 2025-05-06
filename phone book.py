c=0
def add(d):
     global c
     name=input("enter name:")
     if name not in d:
            no=input("enter number:")
            if len(no)!=10:
                print("invalid number")
            else:
                d[name]=no
                c+=1
                print("contact added ")
     else:
            print("name alredy in contact")
def delete(d):
    global c
    if c==0:
              print("phone book is empty")
    else:
                name=input("enter name:")
                if name not in d:
                    print(f"{name} not present in phone book")
                else : 
                     d.pop(name)
                     c-=1
                     print("contact deleted ")
def show(d):
    global c
    if c==0:
              print("phone book is empty")
    else:
              t=1
              sort=dict(sorted(d.items()))
              for x,y in sort.items():
                  print(f"{t}.{x}:{y}")
                  t+=1
print("\t\tWELCOME TO OUR PHONE BOOK")
print("our menu\n1.add number\n2.delete number\n3.show all number\n4.exit")
d={}
while True:
    ch=int(input("enter your choice:"))
    if ch==1:
        add(d)
    elif ch==2:
        delete(d)
    elif ch==3:
        show(d)
    elif ch==4:
          print("thank you")
          break
    else:
        print("wrong choice")
                  
              
        
            
        
