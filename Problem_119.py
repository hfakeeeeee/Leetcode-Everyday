def getRow(rowIndex):
    if(rowIndex == 0): return [1]
    temp = []
    while(len(temp) <= rowIndex):
        subarray = []
        k = len(temp)
        j = 0
        subarray.append(1)
        while(k > 1):
            subarray.append(temp[j] + temp[j + 1])
            k -= 1
            j += 1
        subarray.append(1)
        temp[:] = subarray
    return temp
        
if __name__ == "__main__":
    numrows = input()
    print(getRow(int(numrows)))