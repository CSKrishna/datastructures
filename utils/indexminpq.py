"""
A rough Python equivalent of the the IndexMinPQ class from https://algs4.cs.princeton.edu/24pq/IndexMinPQ.java.html
"""



class IndexMinPQ:
    def __init__(self, maxN: int) -> None:
        """
        :maxN: # of elements in PQ
        """
        self.keys = [None for _ in range(maxN)] #stores the keys for the objects in the priority queye
        self.pq = [-1] # maps priority of obect to object's index (0 based indexing), initiate with a dummy entry
        self.qp = [maxN for _ in range(maxN)] #maps index of object to its priority
        self.maxN = maxN

    def _validateIndex(self, index: int):
        if (index < 0) or (index >= self.maxN):
            raise Exception("Invalid index")

    def insert(self, index, key):
        self._validateIndex(index)
        self.pq.append(index)
        n = len(self.pq) -1
        self.qp[index] = n
        self.keys[index] = key
        self.swim(n)
    

    def swim(self, priority):
        while (priority > 1) and self.greater(priority//2, priority):
            self.swap(priority//2, priority)
            priority = priority//2


    def greater(self, i, j):
        bool = self.keys[self.pq[i]] > self.keys[self.pq[j]]
        return bool
    
    def swap(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
    
    def getindex_val(self, u):
        self._validateIndex(u)
        return self.keys[u]

    def getMin(self):
        if not self.isEmpty():
            return self.keys[self.pq[1]]
        else:
            raise Exception("Underflow")

    def delMin(self):
        n = len(self.pq) - 1
        i = self.pq[1]       
        min = self.keys[i]

        self.swap(1, n)
        self.pq.pop() #this reduces the length of pq
        self.qp[i] = self.maxN # this indicates that the object indexed by i has been deleted
        self.keys[i] = None

        self.sink(1) #to maintain the Heap property
        return i, min

    
    def sink(self, i):
        n = len(self.pq) - 1
        while (2*i <= n):
            j = 2*i
            if j < n and self.greater(j, j+1):
                 j += 1
          
            if not self.greater(i, j):
                break
            self.swap(i, j)
            i = j


    def changeindex(self, i, key):
        self._validateIndex(i)
        self.keys[i] = key
        p = self.qp[i]
        self.swim(p)
        self.sink(p)
    
    def isEmpty(self):
        return len(self.pq) <= 1

    def size(self):
        return len(self.pq) - 1 