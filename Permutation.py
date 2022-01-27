import copy
import os
os.system("cls")

def permutation_recursive(nums, path):
    if len(nums) == 0:
        return [path]
    output = []

    for i in range(len(nums)):
        copy_path = copy.deepcopy(path)
        copy_path.append(nums[i])
        permutations = permutation_recursive(nums[:i] + nums[i + 1:], copy_path)
        output += permutations
    return output

def permute(nums):
    return permutation_recursive(nums, [])

if __name__=="__main__":
    list = []
    size = int(input("Enter List Size:\t"))
    print("")
    for i in range(size):
        num = int(input(f"Enter {i+1} Number:\t\t"))
        list.append(num)
    print("")
    print(f"Toal Permutation of {list} is:")
    print("\t", permute(list))



