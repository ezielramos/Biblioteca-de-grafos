class DSU:

    def __init__(self, n:int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]

    def set_of(self, x:int)->int:
        if x == self.parent[x]:
            return x        
        self.parent[x] = self.set_of(self.parent[x])
        return self.parent[x]

    def merge(self, x:int, y:int) -> bool:
        s1, s2 = self.set_of(x), self.set_of(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
                self.rank[s2] += self.rank[s1]
            else:
                self.parent[s2] = s1
                self.rank[s1] += self.rank[s2]
        return s1 != s2