def max1(a,b):# функция посика максимального из 2х чисел
    if a>b:
        return a
    return b


def merge_sort(nums): # функция упорядовачиня списка
    if len(nums) > 1:
        mid = len (nums) //2
        left = nums [:mid]
        right = nums [mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len (left) and j <len(right):
            if left[i] < right [j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1