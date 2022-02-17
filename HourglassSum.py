def hourglassSum(arr):
    
    arr2 = []
    
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            
            mid = arr[i+1][j+1]
            
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            arr2.append((top+mid+bottom))
             
            
    return max(arr2)
