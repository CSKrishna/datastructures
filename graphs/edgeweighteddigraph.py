import sys, os
from argparse import ArgumentParser
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.bag import Bag

class Edge:
    def __init__(self, tuple, wt) -> None:
        self.tuple = tuple
        self.wt = wt
        
    def get_head(self):
        return self.tuple[0]

    def get_tail(self):
        return self.tuple[1]

    def get_wt(self):
        return self.wt
        
    def __str__(self):
        return str(self.get_tail())


class DiGraph:
    def __init__(self, V):
        if V < 0:
            raise ValueError("Number of vertices must be non-negative")
        self.V = V
        self.out_adj = [Bag() for _ in range(V)] #array of bag of outbound  edges from a vertex
        self.in_adj = [Bag() for _ in range(V)] #array of bag of inbound edges to a vertex

        """
        for _ in range(V):
            self.out_adj.append(Bag())
            self.in_adj.append(Bag())
        """
        self.E = 0

    def add(self, Edge):
        u = Edge.get_head()   
        v = Edge.get_tail()
        self.out_adj[u].add(Edge)
        self.in_adj[v].add(Edge)

    def get_outboundedges(self, u):
        return self.out_adj[u]
    
    def V(self):
        return self.V

    @classmethod
    def fromfile(cls, file):
        V = int(file.readline())
        digraph = cls(V)

        E = int(file.readline())
        if E < 0:
            raise ValueError("Number of vertices must be non-negative")  
        digraph.E = E

        for _ in range(E):
            u, v = file.readline().split()
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
    parser = ArgumentParser()
    parser.add_argument('--filepath', default= "none", type=str)
    args = parser.parse_args()
    if args.filepath == "none":
        file = sys.stdin
        g = DiGraph.fromfile(file)
    else:
        with open(args.filepath) as file:
            g = DiGraph.fromfile(file)
    
    print(g)