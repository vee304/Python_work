
def subseq(ind, dis, arr):
    n = len(arr)

    if ind >= n:
        print(dis)
        return
    
    i = ind
    dis.append(arr[i])
    subseq(ind+1, dis, arr)

    dis.remove(arr[i])
    subseq(ind+1, dis, arr)


arr = [3,1,2]
dis = []
subseq(0, dis, arr)