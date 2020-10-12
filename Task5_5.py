nums= [1,2,3,65,35,45,77,44,44,56,11,22,33,44,55,22,55,14,65]

max(nums)


for even, element in enumerate(nums):
      if element % 2 == 0:
          nums[even] = 77


print(nums)
