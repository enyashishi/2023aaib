# 因為是淘汰賽，n對的話，只要比n-1場，就淘汰其他隊，就得冠軍了
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1 