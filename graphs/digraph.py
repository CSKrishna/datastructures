import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.bag import Bag

class Edge:
    def __init__(self, tuple) -> None:
        self.tuple = tuple
        
    def get_head(self):
        return self.tuple[0]

    def get_tail(self):
        return self.tuple[1]

    def __str__(self):
        return str(self.get_tail())
class DiGraph:

    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices must be non-negative")
        self.V = V
        self.out_adj = {} #set of list of outbound  edges from a vertex
        self.in_adj = {} # set of list of inbound edges to a vertex

        for v in range(V):
            self.out_adj[v] = Bag()
            self.in_adj[v] = Bag()

        self.E = 0

    def add(self, E):
        u = E.get_head()   
        v = E.get_tail()
        self.out_adj[u].add(E)
        self.in_adj[v].add(E)
    
    @classmethod
    def fromstdin(cls):
        V = int(sys.stdin.readline())
        digraph = cls(V)

        E = int(sys.stdin.readline())
        if E < 0:
            raise ValueError("Number of vertices must be non-negative")  
        digraph.E = E

        for _ in range(E):
            u, v = sys.stdin.readline().split()
            u = int(u)
            v = int(v)
            e = Edge((u, v))
            digraph.add(e)
           

        return digraph

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.out_adj[v])) for v in range(self.V))    
        return s

if __name__ == '__main__':
  


    g = DiGraph.fromstdin()
    #e = Edge((3,4))
  
    #print(str(e))
    #print (e)
    print(g)