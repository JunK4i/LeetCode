class Solution:
    import heapq
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # #does not make use of sorted array
        # size = m+n
        # for i in range(m, size):
        #     nums1[i] = nums2[i-m]
        # heapq.heapify(nums1)
        # # Uses O(n*log(m+n))
        # new = heapq.nsmallest(size, nums1)
        # for i in range(len(new)):
        #     nums1[i] = new[i]
        
        # Three pointers, 2 pointing at the end of each list and one at the new latest location on array
        i,j,k = m-1, n-1, m+n-1
       
        # Compare biggest elements and put at end of nums1

        #continue until j expended
        while j>=0: 
            #if i not expended and i bigger than j 
            print(f"i{nums1[i]},j{nums2[j]},k{nums1[k]}")
            print(nums1)
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            #i expended (add nums2 into nums1) or j bigger than i
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
            


        


        