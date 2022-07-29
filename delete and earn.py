#TC: O(n)
#SC: O(n)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums)+1)
        for i in nums:
            freq[i] = freq[i]+i
        
        dp = [0] * len(freq)
        dp[0] = freq[0]
        dp[1] = freq[1]
        for i in range(2,len(dp)):
            dp[i] = max(freq[i]+dp[i-2],dp[i-1])
        return dp[-1]
        