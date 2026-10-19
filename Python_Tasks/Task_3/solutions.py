def frequency_of_word(sentence):
    count = {}
    words = sentence.lower().split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
# sentence = "python is easy and python is powerful"
# print(frequency_of_word(sentence))
def frequency_of_char(word):
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
# word = "banana"
# print(frequency_of_char(word))
def single_char(word):
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in word:
        if count[char]==1:
            return char
    return None
# word = "swiss"
# print(single_char(word))
def isAnagram(s1,s2):
    return frequency_of_char(s1) == frequency_of_char(s2)
# s1 = "save"                  
# s2 = "vase"
# print(isAnagram(s1,s2))
def first_repeating_char(word):
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
            if count[char]>1:
                return char
        else:
            count[char] = 1
# word = "programming"
# print(first_repeating_char(word))           #5
def zeroes_at_end(l):
    result = []
    zero_count = 0
    for i in l :
        if i==0:
            zero_count += 1
        else:
            result.append(i)
    result.extend([0]*zero_count)
    return result
# l = [0, 3, 0, 1, 2, 0, 4]
# print(zeroes_at_end(l))
def second_highest_distinct(l):
    unique = []
    if len(unique) < 2:
        return None
    return unique[1]
# nums = [10, 20, 40, 30, 40, 20]
# print(second_highest_distinct(nums))
def remove_dup(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result
# nums = [4, 2, 4, 5, 2, 7, 5]
# print(remove_dup(nums))
def missing_num(nums,N):
    for i in range(1,N+1):
        if i not in nums:
            return i
# nums = [1, 2, 4, 5, 6]
# N = 6
# print(missing_num(nums,N))
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return nums[i],nums[j]
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums,target))                 #10
def near_zero(nums):
    min_num = max(nums)
    for num in nums:
        if num>0 and num<min_num:
            min_num = num
    return min_num
# nums = [-8, -3, 2, 5, -2]
# print (near_zero(nums))
def common(list1,list2):
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return common
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# print(common(list1,list2))
def rotate_right(nums,k):
    n=len(nums)
    k=k%n
    def reverse(start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start,end=start+1,end-1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    return nums
# nums = [1, 2, 3, 4, 5]
# k = 2
# print(rotate_right(nums,k))
def max_sum(nums):
    max_sum = nums[0]+nums[1]
    for i in range(len(nums)-1):
        if nums[i]+nums[i+1]>max_sum:
            max_sum = nums[i]+nums[i+1]
    return max_sum
# nums = [4, 7, 2, 9, 5]
# print(max_sum(nums))
def pairs(nums,target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                pair=sorted([nums[i],nums[j]])
                if pair not in pairs:
                    pairs.append(pair)
    return sorted(pairs)
# nums = [2, 4, 3, 5, 7, 8, 1]
# target = 9
# print(pairs(nums,target))
