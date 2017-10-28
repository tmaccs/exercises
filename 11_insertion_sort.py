def insertion_sort(alist):
    # #插入排序
    # #自己的方法
    # n = len(alist)
    # for j in range(1,n):
    #     unlistnum = alist[j]
    #     for i in range(j):
    #         if alist[i] > unlistnum:
    #             alist[i],alist[j] = alist[j],alist[i]

    #教程中的方法
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1,n):
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i >0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break







if __name__ == "__main__":
    li = [54, 23, 27, 67, 54, 86, 24]
    insertion_sort(li)
    print(li)