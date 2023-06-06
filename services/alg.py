import numpy as np

class Alg:
    def __init__(self, num, graph):
        self.num = num
        self.graph = graph

        self.matches = np.full(num, -1)
        self.used = np.full(num, False)

    def do_kuhn(self):
        for vert in range(self.num):
            for i in range(len(self.used)):
                self.used[i] = False

            self.__dfs(vert)
        
        return self.matches

    def __dfs(self, vert):
        if self.used[vert]:
            return False
        self.used[vert] = True

        for i in range(len(self.graph[vert])):
            to = self.graph[vert][i]
            if self.matches[to] == -1 or self.__dfs(self.matches[to]):
                self.matches[to] = vert
                return True
        
        return False
    
    def to_string(self):
        answer = ""

        for i in range(len(self.matches)):
            if self.matches[i] != -1:
                answer += f"{self.matches[i] + 1} {i + 1}\n"

        return answer