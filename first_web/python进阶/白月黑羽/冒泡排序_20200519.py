arr = [23,41,25,54,19,14]

def dubblesoft(arr):
    length =len(arr)
    for j in range(length-1,0,-1):

        for i in range(0,length-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

    print(arr)

dubblesoft(arr)