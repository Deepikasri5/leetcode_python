def two_sum(nums,target):
    #one-pass hash table
    dic={}
    for i, num in enumerate(nums):
        diff = target-num
        if diff in dic:
            return dic[diff], i
        dic[num]=i
    return []
    

def main():
    nums=[2,7,9,15]
    target = 9
    result = two_sum(nums,target)
    print("indices", result)

main()

# TC - O(N)
# SC - O(N)

