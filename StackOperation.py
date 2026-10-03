MAX = 5
STACK = []

def push():
    if len(STACK)==MAX:
        print("Stack Overflow!! Stack is Full ")
    else:
        item=int(input("Enter element to push : "))
        STACK.append(item)
        print(item ,"inserted into the stack.")

def pop():
    if len(STACK)==0:
        print("Stack is Empty!!!")
    else:
        item = STACK.pop()
        print(item,"Deleted from the stack.")

def peek():
    if len(STACK)==0:
        print("stack is empty")
    else:
        print("Top element is ", STACK[-1])

def display():
    if len(STACK)==0:
        print("stack is empty!!")
    else:
        print("stack elements are:")
        for i in range(len(STACK)-1,-1,-1):
            print(STACK[i])

def is_empty():
    if len(STACK)==0:
        print("Stack is empty")
    else:
        print("Stack is not Empty")

def is_full():
    if len(STACK)==MAX:
        print("Stack isfull")
    else:
        print('Stack is not full')
        print("Available Space : ",MAX -len(stack))

while(True):
    print("\n====================STACK MENU====================")
    print("\n1.push\n2.pop\n3.peek\n4.display\n5.isempty\n6.isfull\n7.exit")
    choice = int(input("Enter the Choice :"))

    if choice ==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        is_empty()
    elif choice==6:
        is_full()
    elif choice==7:
        print("program Terminated!!!")
        break
    else:
        print("Invalid Input!! Please try again")