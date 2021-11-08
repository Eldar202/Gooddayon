def medians(nums1, nums2):
    nums3 = nums1 + nums2
    nums3 = list(set(nums3))
    x = len(nums3)
    if x % 2 == 0:
        print('объединенный список-', nums3, 'медиана -', (nums3[(x//2)-1]+ nums3[(x//2)])/2)
    else:
        print('объединенный список-', nums3, 'медиана -', nums3[x//2]




