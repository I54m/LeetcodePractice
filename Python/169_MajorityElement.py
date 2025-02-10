def main():
    print("starting program")
    try:
        nums: list[int] = [3,2,3]
        output = majorityElement(self=__name__, nums=nums)
        print(f"Test Case 1 Result: {output}")

        nums: list[int] = [6,5,5]
        output = majorityElement(self=__name__, nums=nums)
        print(f"Test Case 2 Result: {output}")

    except Exception as e:
        print(f"Error occurred: {e}")

def majorityElement(self, nums: list[int]) -> int:
    nums.sort()
    mean = int(len(nums)/2)
    return nums[mean]






if __name__ == "__main__":
    main()