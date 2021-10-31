x = input('Введите последовательность чисел через пробел: ')
nums = x.split()
nums = [int(item) for item in nums]
def ind_missing_nums(nums):
    n = max(nums)
    nums1 = list(range(1,n+1))
    m=[]
    for i in nums1:
        if i not in nums:
            m.append(i)
    print("Недостающие элементы списка:", m)
ind_missing_nums(nums)







