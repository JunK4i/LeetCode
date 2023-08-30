class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 
        dup_count = 1
        for i in range(1, len(nums)):
            print(f"{nums},{k},{i},{dup_count}")
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1 
                dup_count = 1
            elif dup_count < 2:
                nums[k] = nums[i]
                k += 1 
                dup_count += 1
        return k
        #k pointer tracks where i should overwrite (1 ahead of the "accepted" array)
        #initialise with count=1 and k at index 1 (0 is already accounted for)
        #iterate through 1->n-1
        #if the nums[i] is not the same as the number before it (end of duplicates)
        #overwrite k element with i element. Reset duplicate counter to 1
        #if the dup_count is less than 2, increase k (allow for max 2 dups), increase count
        #if the dup_count is more than 2 and still not end of duplicates, continue to next element, but keep k pointed at the last location  
