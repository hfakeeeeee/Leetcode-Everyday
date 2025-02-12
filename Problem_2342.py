from collections import defaultdict

def maximumSum(self, nums):
    def get_digit_sum(num): 
        sum = 0 
        while num > 0:
            sum+= num%10
            num = num//10
        return sum


    ans = -1 
    sums = defaultdict(int)
    for num in nums:
        dig_sum = get_digit_sum(num)
        
        if dig_sum in sums: 
            if sums[dig_sum]+num > ans: 
                ans = sums[dig_sum]+num
            if sums[dig_sum]<num: 
                sums[dig_sum]=num
        else: 
            sums[dig_sum] = num

    return ans