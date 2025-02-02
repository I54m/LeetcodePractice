def main():
    print("starting program")
    try:
        nums: list[int] = [1,2,3,0,0,0]
        merge(self=__name__, nums1=nums, m=3, nums2=[2,5,6], n=3)
        print(f"Test Case 1 Result: {nums}")

        nums: list[int] = [1]
        merge(self=__name__, nums1=nums, m=1, nums2=[], n=0)
        print(f"Test Case 2 Result: {nums}")

        nums: list[int] = [0]
        merge(self=__name__, nums1=nums, m=0, nums2=[1], n=1)
        print(f"Test Case 3 Result: {nums}")
    except Exception as e:
        print(f"Error occurred: {e}")


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    j: int = m
    for i in range(n):
        nums1[j] = nums2[i]
        j+=1
    list.sort(nums1)





if __name__ == "__main__":
    main()