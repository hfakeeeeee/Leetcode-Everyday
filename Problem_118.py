def generate(numRows):
    result = []
    temp = []
    if numRows == 0: return 0
    for i in range(1, numRows + 1):
        subarray = []
        if(i == 1): 
            subarray.append(1)
            temp[:] = subarray
            result.append(subarray)
            continue
        k = len(temp)
        j = 0
        subarray.append(1)
        while(k > 1):
            subarray.append(temp[j] + temp[j + 1])
            k -= 1
            j += 1
        subarray.append(1)
        temp[:] = subarray
        result.append(subarray)
    return result
        

if __name__ == "__main__":
    numrows = input()
    print(generate(int(numrows)))