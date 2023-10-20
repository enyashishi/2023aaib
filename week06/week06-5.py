class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
         d = {}
         for c in s:
             if c in d:
                 d[c] = d[c] + 1
             else:
                 d[c] = 1
         #print(d) #可以印看看<字母出現在次數統計結果

         for c in t:
             if c not in d: #沒出現過
                 return c #找到多出來的字母
             if d[c] == 0: #字母用光了
                return c #找到多出來的字母
             else:
                d[c] = d[c] - 1   

         return ""