"""
Simple graph implementation
"""
from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # # adding this makes the edges and nodes bidirectional in nature
            # self.vertices[v2].add(v1)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # instantiate a Queue object
        q = Queue()
        # instantiate empty list of all the nodes we have already traversed
        traversed = []
        # enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # while the queue still has values in it
        while q.size() > 0:
            # set the current_val as dequeue so the algorithm can start
            current_val = q.dequeue()
            # append the current_val to the traversed lsit
            traversed.append(current_val)
            # for a given val in the value of the specified vertex
            for val in self.vertices[current_val]:
                # if the value is not in traversed
                if val not in traversed:
                    # add it to the queue via enqueue
                    q.enqueue(val)
            # print the current_val
            print(current_val)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        DFT is the same as BFT just using a Stack
        instead of a Queue.
        """
        # instantiate a Stack object
        s = Stack()
        # traversed is equal to the starting_vertex in a list
        traversed = [starting_vertex]
        # push the starting_vertex
        s.push(starting_vertex)
        # while the stack still has values in it
        while s.size() > 0:
            # pop the current value off the stack
            current_val = s.pop()
            # print the current_val
            print(current_val)
            # for a specified val in the value of the specified vertex
            for val in self.vertices[current_val]:
                # if the val has not already been traversed
                if val not in traversed:
                    # append it to the traversed list
                    traversed.append(val)
                    # push the stack val
                    s.push(val)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # define a recusive function
        def recurse(graph, traversed, vertex):
            # if vertex is in traversed (already visted that vertex or node)
            if vertex in traversed:
                # return nothing
                return
            # print the vertex
            print(vertex)
            # if the vertex has not already been traversed
            if vertex not in traversed:
                # append it to the traversed list
                traversed.append(vertex)
            # loop through the val(s) in the specified graph vertex value
            for val in graph[vertex]:
                # recursively call the function 
                recurse(graph, traversed, val)
        # calling recurse function inside of the dft_recursive function:
        # takes a graph attribute, traversed list (empty), and a starting vertex
        recurse(self.vertices, [], starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # instantiate a Queue object
        q = Queue()
        # reverse lookup table
        traversed = {1: None}
        # set the current_val equal to None
        current_val = None
        # start enqueue on the starting_vertex
        q.enqueue(starting_vertex)
        # while the queue contains values
        while current_val != destination_vertex:
            # dequeue the current_val
            current_val = q.dequeue()
            # for a val in the vertices attribute of the current_val
            for val in self.vertices[current_val]:
                # if the val has not been traversed
                if val not in traversed:
                    # set the value of the traversed val at the dict val as the 
                    # current_val
                    traversed[val] = current_val
                    # enqueue the val
                    q.enqueue(val)
        
        # instantiate a new empty list to map backwards
        returnlist = []
        # while the current_val is not None
        while current_val is not None:
            # append the current_val to the returnlist
            returnlist.append(current_val)
            # set the traversed valueequal to the current_val
            current_val = traversed[current_val]
        # reverse the list
        returnlist.reverse()
        # return returnlist
        return returnlist

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # instantiate Stack object
        s = Stack()
        # reverse lookup table
        traversed = {1: None}
        # set the current_val equal to None
        current_val = None
        # push the starting_vertex
        s.push(starting_vertex)
        # while the queue contains values
        while current_val != destination_vertex:
            # pop the current_val off
            current_val = s.pop()
            # loop through the values in the vertices atrtibute at the specified
            # current_val
            for val in self.vertices[current_val]:
                # if the val is not traversed (already been seen)
                if val not in traversed:
                    # add the current_val to the traversed value at the specified
                    # val
                    traversed[val] = current_val
                    # push to the next val
                    s.push(val)
        # instantiate a new empty list to map backwards
        returnlist = []
        # while the current_val is not None
        while current_val is not None:
            # append the current_val to the returnlist
            returnlist.append(current_val)
            # set the current_val equal to the value at the specified index
            current_val = traversed[current_val]
        # reverse the list
        returnlist.reverse()
        # return returnlist
        return returnlist

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # recurse function
        def recurse(graph, traversed, goal, vertex):
            # if the vertex is already in traversed
            if vertex in traversed:
                # return none because there is nothing left
                return None
            # is the vertex is equal to what we are looking for
            if vertex == goal:
                # return list to append on to map on the way back
                return [vertex]
            # if the vertex is not in traversed
            if vertex not in traversed:
                # append it to traversed since we have now seen it
                traversed.append(vertex)
            # loop through the val in the specified graph vertex
            for val in graph[vertex]:
                # result is queal to the recurse
                result = recurse(graph, traversed, goal, val)
                # is the result is not None
                if result is not None:
                    # append the vertex to result
                    result.append(vertex)
                    # return result
                    return result
            # catch, return nothing if all dead ends
            return None
        
        # get result from recursion and reverse
        result = recurse(self.vertices, [], destination_vertex, starting_vertex)
        # reverse the result
        result.reverse()
        # return result
        return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)

    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
