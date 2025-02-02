def main():
    print("starting program")

    nums: list[int] = [1,1,2] # Input array
    expectedNums: list[int]  = [1,2] # The expected answer with correct length.

    k: int = removeDuplicates(self=__name__, nums=nums); # Calls your implementation
    print (f"output: {nums}")
    print (f"k: {k}")

    assert k == len(expectedNums)

    for i in range(len(expectedNums)):
        assert nums[i] == expectedNums[i]


def removeDuplicates(self, nums: list[int]) -> int:
    """
    Identifies duplicates in an array of numbers and removes them
    """
    occurred: list[int] = []
    index: int = 0
    for i in range(len(nums)):
        if (not(nums[i] in occurred)):
            occurred.append(nums[i])
            nums[index] = nums[i]
            index+=1

    return index







if __name__ == "__main__":
    main()