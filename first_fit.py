# process=input("Enter the process list:").split()
# request=input("Enter the memory requests:").split()
def first_fit(request,block_size):
    process=['p1','p2','p3','p4','p5','p6']
    x=lambda x: int(x)
    request=list(map(x,request))
    # block_size=input("Enter the memory block size:").split()
    block_size=list(map(x,block_size))
    alloc={}
    for i in request:
        flag=0
        ind=request.index(i)
        for j in block_size:
            if j-i>=0 and j not in alloc.values():
                flag=1
                alloc[process[ind]]=j
                break
        if flag==0:
            alloc[process[ind]]=0
    print("The Allocations are:")
    print(alloc)
    return alloc
