

class Graph:
    def __init__(self,order,directed=False,costs=False,labels=None):
        self.order=order
        self.directed=directed
        self.adjList= [[] for _ in range(self.order)]
        if costs:
            self.costs=[]
        else:
            self.costs=None
        self.labels=labels
    def add_node(self):
        self.adjList.append([])
        self.order+=1
        if self.costs:
            self.costs.append([])

    def add_edge(self,src,dst,cost=None):
        self.adjList[src].append(dst)
        if not self.directed:
            self.adjList[dst].append(src)

    def graph_to_csv(self):
        with open("graph.csv", "w") as f:
            for i in range(len(self.adjList)):
                f.write(self.labels[i]+";")
                f.write("")
                for j in self.adjList[i]:
                    f.write(self.labels[j]+",")
                f.write("\n")