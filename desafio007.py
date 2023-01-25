def juntando_listas(nums1, nums2):
    nums1 = nums1 + nums2
    nums1.sort()

    return nums1

def main():
    nums1 = [2, 5, 7, 10]
    nums2 = [1, 11, 6, 8]
    m = len(nums1)
    n = len(nums2)
    nums1 = juntando_listas(nums1, nums2)
    print(nums1)
    print(m, n, len(nums1))

if __name__ == '__main__':
    main()