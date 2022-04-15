from graphs.digraph import DiGraph

class DFS:
     def __init__(self, g: DiGraph, s):
         self.marked = [False for _ in range(g.V)]
         self.top_labels = [i for i in range(g.V)]
         self.g = g
         self.dfs(g, s)
         self.n = g.V + 1

     def dfs(self, g, u):
         self.marked[u] = True
         for e in g.get_outboundedges(u):
             v = e.get_tail()
             if not self.marked[v]:
                 self.dfs(g, v)
         self.top_labels[u] = self.n
         self.n = self.n - 1        

if __name__ == '__main__':
  

    g = DiGraph.fromstdin()
    print(g)         