def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        main_index = j
        for i in range(j+1,n):
            if alist[main_index] > alist[i]:
        #两种都能得出正确结果，但是还不确定是否满足这个选择算法
        #         alist[main_index],alist[i] = alist[i],alist[main_index]
        # alist[j] = alist[main_index]
                main_index = i
        alist[j],alist[main_index] = alist[main_index],alist[j]


if __name__ == "__main__":
    li = [54, 23, 56, 67, 27, 86, 24]
    select_sort(li)
    print(li)
