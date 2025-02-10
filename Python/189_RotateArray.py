def main():
    print("starting program")
    try:
        nums: list[int] = [1,2,3,4,5,6,7]
        rotate(self=__name__, nums=nums, k=3)
        print(f"Test Case 1 Result: {nums}")

        nums: list[int] = [-1,-100,3,99]
        rotate(self=__name__, nums=nums, k=2)
        print(f"Test Case 2 Result: {nums}")

        # nums: list[int] = [-1,-100,3,99]
        # rotate(self=__name__, nums=nums, k=2)
        # print(f"Test Case 3 Result: {nums}")
    except Exception as e:
        print(f"Error occurred: {e}")

def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums.pop())




if __name__ == "__main__":
    main()