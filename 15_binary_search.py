def binary_search(alist,item):
    # 二分查找
    n = len(alist)
    # 递归到n>0
    if n > 0:
        # //是取整除
        mid_num = n//2
        if alist[mid_num] == item:
           return True
        elif alist[mid_num] > item:
            # 这样切片的时候不会取到mid_
            return binary_search(alist[:mid_num],item)
        elif alist[mid_num] < item:
            return binary_search(alist[mid_num+1:],item)
    return False

if __name__ == "__main__":
    alist=[23,34,54,76,84,95,235]
    item=11
    print(binary_search(alist,item))