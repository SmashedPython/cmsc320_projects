# Adjascency List representation in Python


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
    
    def test_bipartite(self):
        color = {}  
        for i in range(self.V):
            color[i] = 'grey'  # Initialize color to grey

        # BFS 
        for v in range(self.V):
            if color[v] is not 'grey':
                continue  # Skip visited vertices

            queue = []
            queue.append(v)
            color[v] = 'black'

            while queue:
                vertex = queue.pop(0)

                current_node = self.graph[vertex]
                while current_node:
                    neighbor = current_node.vertex

                    if color[neighbor] == color[vertex]:
                        return False 

                    elif color[neighbor] is 'grey':
                        color[neighbor] = 'black' if color[vertex] == 'white' else 'white'
                        queue.append(neighbor)

                    current_node = current_node.next

        return True 



if __name__ == "__main__":
   graph1 = Graph(3)
   graph1.add_edge(0,1)
   graph1.add_edge(1,2)
   graph1.add_edge(2,0)
   
   print('graph 1: ', graph1.test_bipartite())

   graph2 = Graph(4)
   graph2.add_edge(0,1)
   graph2.add_edge(1,2)
   graph2.add_edge(2,3)
   graph2.add_edge(3,0)

   print('graph 2: ', graph2.test_bipartite())
   
   graph3 = Graph(6)
   graph3.add_edge(0,1)
   graph3.add_edge(1,2)
   graph3.add_edge(2,3)
   graph3.add_edge(3,4)
   graph3.add_edge(4,5)
   graph3.add_edge(5,0)
   graph3.add_edge(1,5)
   graph3.add_edge(2,4)

   print('graph 3: ', graph3.test_bipartite())
   
   graph4 = Graph(8)
   graph4.add_edge(0,1)
   graph4.add_edge(1,2)
   graph4.add_edge(2,3)
   graph4.add_edge(0,3)
   graph4.add_edge(2,4)
   graph4.add_edge(4,5)
   graph4.add_edge(5,6)
   graph4.add_edge(6,7)
   graph4.add_edge(7,4)

   print('graph 4: ', graph4.test_bipartite())
     
   graph5 = Graph(8)
   graph5.add_edge(0,1)
   graph5.add_edge(1,2)
   graph5.add_edge(2,3)
   graph5.add_edge(3,4)
   graph5.add_edge(4,5)
   graph5.add_edge(5,6)
   graph5.add_edge(6,7)
   graph5.add_edge(7,4)
   graph5.add_edge(7,5)
   graph5.add_edge(7,4)
   graph5.add_edge(7,3)
   print('graph 5: ', graph5.test_bipartite())
   
   def cocktail(lst):
    begin = 0
    end = len(lst) - 1
    while begin <= end:
        newbegin = end
        newend = begin
        for i in range(begin,end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                newend = i
        
        end = newend - 1

        for i in range(end, begin, -1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]
                newbegin = i

        begin = newbegin + 1

    return lst

arr = [3, 1, 5, 2, 4]
print(cocktail(arr))