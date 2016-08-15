

def moveZero(arr):
    pos = 0
    i = 0
    while i<len(arr):
        if arr[i] != 0:
            arr[pos] = arr[i]
	    pos += 1
        i += 1
    i = pos
    while i < len(arr):
        arr[i] = 0
        i += 1
    return arr 

if __name__ == "__main__":
    arr = [1,3,0,8,1,2,0,4,0,7]
    print (moveZero(arr))
     
