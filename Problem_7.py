def reverse(x):
    sum = 0
    tmp = x
    if(x < 0):
        x = -x
    while(x > 0):
        sum = sum * 10 + x % 10
        x = int(x / 10)
    if(tmp < 0):
        sum = -sum
    if sum > 2 ** 31 - 1 or sum < -(2 ** 31):
        return 0
    else: return sum

if __name__ == "__main__":
    x = input()
    print(reverse(int(x)))