def binarySearch(l, target, low=None , high = None):
    if low is None:
        low =0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1
    mid = (low + high) // 2

    if l[mid] == target:
        return mid
    elif target < l[mid]:
        return binarySearch(l, target, low, mid-1)
    else:
        return binarySearch(l, target, mid+1, high)
    
if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    sorted_list = sorted(l)
    target = 10
    print(binarySearch(sorted_list, target))