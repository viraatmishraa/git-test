def duplicheck():
    n=input("enter the size of array: ")
    if not n:
        print("size is not given \n go again \n")
        duplicheck()

    try: 
        n=int(n)
    except Exception as e:
        print(e)
        print("go again\n")
        duplicheck()

    if n <= 0:
        print("empty array \n go again\n")   
        duplicheck()
    arr=[]
    set1={}
    for i in range (0,n):
        inp=input(f"enter the element {i+1}: ")
        arr.append(inp)
    set1=set(arr)
    array=list(set1)
    print(f"new array={array}")

duplicheck()