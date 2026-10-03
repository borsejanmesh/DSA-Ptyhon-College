queue = []

def addcall():
    callid = input(print("Enter Your Customer ID"))
    calltime = input(print("Enter Your Call time Duration"))

    callrecord = (callid, calltime)

    queue.append(callrecord)
    print("Call Added Successfully")


    while True:

        print("1. Add call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Check Queue is Empty")
        print("5. Exit")

        choice = input("Enter your Choice")

        if choice == "1":
            addcall()
        else:
            print("Please Enter Valid Choice")

def answercall():
    if len(queue) == 0:
        print("No Calls On Waiting")

        return
callid, calltime = queue.pop(0) 
print("Call Answered Successfully")
