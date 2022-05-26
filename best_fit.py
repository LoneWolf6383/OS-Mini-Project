from copy import deepcopy
# process=input("Enter the process list:").split()
# request=input("Enter the memory requests:").split()
def best_fit(request,block_size):
    x=lambda x: int(x)
    process=['p1','p2','p3','p4','p5','p6']
    request=list(map(x,request))
    # block_size=input("Enter the memory block size:").split()
    block_size=list(map(x,block_size))
    mem_diff=[]
    for i in request:
        l=[]
        for j in block_size:
            l.append(j-i)
        mem_diff.append(l)
    alloc={}
    for i in range(len(mem_diff)):
        flag=0
        list1=deepcopy(mem_diff[i])
        list1.sort()
        for j in range(len(list1)):
            ind=mem_diff[i].index(list1[j])
            if mem_diff[i][ind]>=0 and block_size[ind] not in alloc.values():
                alloc[process[i]]=block_size[ind]
                flag=1
                break
        if flag==0:
            alloc[process[i]]=0
    print("The Allocations are:")
    print(alloc)
    return alloc
