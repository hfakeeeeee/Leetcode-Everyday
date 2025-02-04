def plusOne(digits):
    result = []
    num = 0
    expo = len(digits) - 1
    for i in digits:
        num += i * pow(10, expo)
        expo -= 1
    num += 1
    while(num != 0):
        result.insert(0, num % 10)
        num = num // 10
    return result

if __name__ == "__main__":
    digits = [1, 2, 2]
    print(plusOne(digits))