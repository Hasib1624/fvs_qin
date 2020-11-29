import numpy as np

# from copy import copy


class AdjNode:
    def __init__(self, name, value):
        self.name = name
        self.vertex = value
        self.next = None

    def __str__(self):
        return str(self.name)


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d, d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s, s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Initialize legal set
    def initialize(self, T_0=0.6):
        self.L = []
        choice = np.random.choice(self.V)
        #         print(choice)
        node = AdjNode(choice, choice)
        self.L.append((choice, node))
        self.FVS = [(i, AdjNode(i, i)) for i in range(self.V) if i != choice]
        self.T = T_0
        self.print_status()

    # Get energy of L:
    def get_energy(self):
        return self.V - len(self.L)

    def gen_rank(self):
        rank = {}
        for i, nd in enumerate(reversed(self.L)):
            rank[nd[0]] = i
        self.rank = rank
#         print(self.rank)

    def get_conflict(self):
        self.gen_rank()
        conflict_l = []
        for i in range(self.V):
            sum_ = 0
            temp = self.graph[i]
            while temp:
                try:
                    if (self.rank[i] - self.rank[temp.vertex]) > 0:
                        sum_ += 1
                except KeyError as e:
                    pass
                temp = temp.next
            if sum_ > 1:
                conflict_l.append(i)
        return conflict_l

    def run(self):
        # Choose a random vertex form FVS
        v = np.random.choice(len(self.FVS))
        # Find the first vertex it is neighbor with
        temp = self.graph[self.FVS[v][1].vertex]
        print(self.FVS[v])
        # Find its neighbors
        neighbor_L = []
        while temp:
            print(temp)
            for i, node in enumerate(self.L):
                print('\t', node)
                if node[1].vertex == temp.vertex:
                    print("Neighbor found")
                    neighbor_L.append(i)
            temp = temp.next
#         temp = self.FVS[v]
        print(neighbor_L)
        
        neighbor_n = len(neighbor_L)
        if neighbor_n == 0:
            print("First Case")
            self.L.append(self.FVS[v])
            self.FVS.pop(v)
        elif neighbor_n == 1:
            print("Second Case")
            self.L.insert(neighbor_L[0], self.FVS[v])
            self.FVS.pop(v)
        else:
            print("Third Case")
            idx = max(neighbor_L)
            self.L.insert(neighbor_L.index(idx), self.FVS[v])
            self.FVS.pop(v)
            
            conflict_l = self.get_conflict()

            if len(conflict_l) > 0:
                for i, nd in enumerate(self.L):
                    if nd[1].vertex in conflict_l:
                        self.FVS.append(self.L[i])
                        self.L.pop(i)      
            else:
                rnd = np.random.uniform()
                if rnd <= np.exp(-(-1 + len(conflict_l)) / self.T):
                    for i, nd in enumerate(self.L):
                        if nd.vertex in conflict_l:
                            self.FVS.append(self.L[i])
                            self.L.pop(i)
        self.print_status()
        print()
        
        return self.FVS, self.get_energy()

    # Print the graph

    def print_status(self):
        print("FVS : ", end='\t')
        for i, node in self.FVS:
            print(i, end=', ')
        print()
        print("L : ", end='\t')
        for i, node in self.L:
            print(i, end=', ')
        print()

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def print_set(self, set_):
        for node in set_:
            print(node)
        print()


if __name__ == "__main__":
    V = 6

    # Create graph and edges
    graph = Graph(V)
    for i in range(V):
        for j in range(i + 1, V):
            if i == j:
                continue
            if np.random.uniform() < 0.5:
                graph.add_edge(i, j)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(0, 3)
    # graph.add_edge(1, 2)

    graph.print_agraph()
    graph.initialize()

    N_t = 50
    fvs_l = []
    energy_l = []
    for _ in range(N_t):
        fvs, energy = graph.run()
        fvs_l.append(fvs)
        energy_l.append(energy)
