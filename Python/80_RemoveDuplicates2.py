def main():
    print("starting program")

    nums: list[int] = [1,1,1,2,2,3] # Input array
    expectedNums: list[int]  = [1,1,2,2,3] # The expected answer with correct length.

    k: int = removeDuplicates(self=__name__, nums=nums); # Calls your implementation
    print (f"output: {nums}")
    print (f"k: {k}")

    assert k == len(expectedNums)

    for i in range(len(expectedNums)):
        assert nums[i] == expectedNums[i]


def removeDuplicates(self, nums: list[int]) -> int:
    count: int = 0
    index: int = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            count = 0
            nums[index] = nums[i]
            index+=1
        else:
            count+=1
            if count <=1:
                nums[index] = nums[i]
                index+=1
    return index


        # count = 0
        # current = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         count = 0
        #         nums[current] = nums[i]
        #         current += 1
        #     else:
        #         count += 1
        #         if count <= 1:
        #             nums[current] = nums[i]
        #             current += 1
        # return current


    # index: int = 0
    # for i in range(1, len(nums)):
    #     if (nums.count(nums[i]) <= 2):
    #         if (nums.count(nums[i]) == 1):
    #             print(f"setting index: {index} to {nums[i]}")
    #             nums[index] = nums[i]
    #             index+=1
    #         else:
    #             print(f"setting index: {index} to {nums[i]}")
    #             print(f"setting index: {index+1} to {nums[i]}")
    #             nums[index] = nums[i]
    #             nums[index+1] = nums[i]
    #             index+=2
            

    #     # if ((i+1 == len(nums)) or index+2 >= len(nums)):
    #     #     if ((nums[i] != nums[i-1])):
    #     #         nums[index] = nums[i]
    #     #         print(f"setting index: {index} to {nums[i]}")
    #     #         index+=1
    #     #     else:
    #     #         continue
    #     # elif (not ((nums[i] != nums[index-1]) and (nums[i] != nums[index+1]))): # Number does NOT occur more than twice
    #     #     # if (nums[index+1] != nums[i]):
    #     #         nums[index] = nums[i]
    #     #         # nums[index+1] = nums[i]
    #     #         print(f"setting index: {index} to {nums[i]}")
    #     #         index+=1

    # return index







if __name__ == "__main__":
    main()