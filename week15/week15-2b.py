class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s) # 長度
        zero = 0 # 等一下也要
        one = 0 # 想找出全部的1
        for i in range(N):
            if s[i]=='1': one += 1
# 現在就知道總共有幾個 one
#print('一開始的時候，都在右邊，統計結果','zero',zero,'one',one)
        ans = 0
        for i in range(N-1): # 要逐格去修正
            if s[i]=='0': # 吐出'0'給左邊
                zero += 1
            if s[i]=='1':
                one -= 1
 # print('中間過程中,','zero',zero,'one',one)
            ans = max(ans, zero + one)
        return ans