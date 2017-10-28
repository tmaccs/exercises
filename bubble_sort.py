def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count +=1
        if count == 0:
            return 

if __name__ == "__main__":
    li = [54,23,56,67,27,86,24]
    bubble_sort(li)
    print(li)