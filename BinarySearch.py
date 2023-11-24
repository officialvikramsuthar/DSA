

arr = [10, 40, 60, 99, 104]


def binarySearch(arr, el):
    length = len(arr)
    start = 0
    middle = int(length/2)
    end = length
    found = -1

    while(end > start):
        if(arr[middle] == el):
            found = middle
            break
            
        elif(arr[middle] < el):
            start = middle

        else:
            end=middle

        middle = int((start + end)/2)
    
    return found