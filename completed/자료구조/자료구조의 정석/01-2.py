#가장 큰 두 수의 차

def maxTwoDiff(nums):
    nums.sort()
    j = len(nums)-1
    return nums[j]-nums[0]

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()

#더 효율적인 답

def maxTwoDiff(nums):
    return max(nums)-min(nums)

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
