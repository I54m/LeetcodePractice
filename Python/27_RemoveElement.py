def main():
    print("starting program")
    nums: list[int] = [3,2,2,3] # Input array
    val: int = 3 # Value to remove
    expectedNums: list[int]  = [2,2] # The expected answer with correct length.
                                # It is sorted with no values equaling val.

    k: int = removeElement(self=__name__, nums=nums, val=val); # Calls your implementation
    print (f"output: {nums}")
    print (f"k: {k}")


    assert k == len(expectedNums)
    # nums.sort; # Sort the first k elements of nums
    for i in range(len(expectedNums)):
        assert nums[i] == expectedNums[i]


def removeElement(self, nums: list[int], val: int) -> int:
    index: int = 0
    for i in range(len(nums)):
        if (nums[i] !=val):
            nums[index] = nums[i]
            index+=1
    return index





if __name__ == "__main__":
    main()