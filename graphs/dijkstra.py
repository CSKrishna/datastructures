import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.indexminpq import IndexMinPQ
from graphs.edgeweighteddigraph import DiGraph, Edge

class Dijkstra:
    def __init__(self, G, s) -> None:
        """
        G: Edge-weighted digraph
        s: vertex in G from which to compute shortest paths to all reachable vertices in G
        """
        self.G = G
        self.pq = IndexMinPQ(G.V())
        self.distto = []*G.V()
        self.vertex_sequence = []*G.V()
        self.x = {}
        self.v_x = {}
        for v in range(G.V()):
            self.distto[v] = float('inf')
            self.pq.insert(v, self.distto[v])
            self.v_x.add(v)
        self.distto[s] = 0.0
        self.pq.changeindex(s, self.distto[s])
        
    def scoop(self):
        i, dist = self.pq.delMin()
        self.x.add(i)
        self.vertex_sequence.append(i)
        self.distto.append(dist)
        self.v_x.remove(i)
        for edge in self.G.get_outboundedges(i):
            
            j = edge.get_tail()
            if j in self.v_x:
                wt = edge.get_wt()
                d = self.pq.getindex_val(j)
                if wt < d:
                    self.pq.changeindex(j, wt)

              
                   
    def runDijkstraSp(self) 


        



        




        pass