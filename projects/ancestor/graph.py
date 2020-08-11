
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


"""
Simple graph implementation
"""
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
        # ## ALT CODE: v1
        # # instantiate a Queue object
        # q = Queue()
        # # instantiate empty list of all the nodes we have already traversed
        # traversed = []
        # # enqueue the starting_vertex
        # q.enqueue(starting_vertex)
        # # while the queue still has values in it
        # while q.size() > 0:
        #     # set the current_val as dequeue so the algorithm can start
        #     current_val = q.dequeue()
        #     # append the current_val to the traversed lsit
        #     traversed.append(current_val)
        #     # for a given val in the value of the specified vertex
        #     for val in self.vertices[current_val]:
        #         # if the value is not in traversed
        #         if val not in traversed:
        #             # add it to the queue via enqueue
        #             q.enqueue(val)
        #     # print the current_val
        #     print(current_val)


        ## ALT CODE: v2
        # instantiate Queue
        q = Queue()
        # make a set to track if we've been here before
        visited = set()
        # enqueue the starting node
        q.enqueue(starting_vertex)
        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of our line, 
            # this is our current node
            current_node = q.dequeue()
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # loop through each of the neighbors
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        DFT is the same as BFT just using a Stack
        instead of a Queue.
        """
        ## ALT CODE: v1
        # # instantiate a Stack object
        # s = Stack()
        # # traversed is equal to the starting_vertex in a list
        # traversed = [starting_vertex]
        # # push the starting_vertex
        # s.push(starting_vertex)
        # # while the stack still has values in it
        # while s.size() > 0:
        #     # pop the current value off the stack
        #     current_val = s.pop()
        #     # print the current_val
        #     print(current_val)
        #     # for a specified val in the value of the specified vertex
        #     for val in self.vertices[current_val]:
        #         # if the val has not already been traversed
        #         if val not in traversed:
        #             # append it to the traversed list
        #             traversed.append(val)
        #             # push the stack val
        #             s.push(val)


        ## ALT CODE: v2
        # make a stack
        s = Stack()
        # make a set to track if we've been here before
        visited = set()
        # push on our starting node
        s.push(starting_vertex)
        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever is on top, this is the current node
            current_node = s.pop()
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # ## ALT CODE: v1
        # # define a recusive function
        # def recurse(graph, traversed, vertex):
        #     # if vertex is in traversed (already visted that vertex or node)
        #     if vertex in traversed:
        #         # return nothing
        #         return
        #     # print the vertex
        #     print(vertex)
        #     # if the vertex has not already been traversed
        #     if vertex not in traversed:
        #         # append it to the traversed list
        #         traversed.append(vertex)
        #     # loop through the val(s) in the specified graph vertex value
        #     for val in graph[vertex]:
        #         # recursively call the function 
        #         recurse(graph, traversed, val)
        # # calling recurse function inside of the dft_recursive function:
        # # takes a graph attribute, traversed list (empty), and a starting vertex
        # recurse(self.vertices, [], starting_vertex)

        ## ALT CODE: v2
        # if not visited
        if not visited:
            # instantiate set variable visited
            visited = set()
        # if starting_vertex not in visited
        if starting_vertex not in visited:
            # mark this vertex as visited
            visited.add(starting_vertex)
            # print starting_vertex
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            # for each neighbor 
            for neighbor in neighbors:
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # ## ALT CODE: v1
        # # instantiate a Queue object
        # q = Queue()
        # # reverse lookup table
        # traversed = {1: None}
        # # set the current_val equal to None
        # current_val = None
        # # start enqueue on the starting_vertex
        # q.enqueue(starting_vertex)
        # # while the queue contains values
        # while current_val != destination_vertex:
        #     # dequeue the current_val
        #     current_val = q.dequeue()
        #     # for a val in the vertices attribute of the current_val
        #     for val in self.vertices[current_val]:
        #         # if the val has not been traversed
        #         if val not in traversed:
        #             # set the value of the traversed val at the dict val as the 
        #             # current_val
        #             traversed[val] = current_val
        #             # enqueue the val
        #             q.enqueue(val)
        
        # # instantiate a new empty list to map backwards
        # returnlist = []
        # # while the current_val is not None
        # while current_val is not None:
        #     # append the current_val to the returnlist
        #     returnlist.append(current_val)
        #     # set the traversed valueequal to the current_val
        #     current_val = traversed[current_val]
        # # reverse the list
        # returnlist.reverse()
        # # return returnlist
        # return returnlist


        ## ALT CODE: v2
        # instantiate a Queue
        q = Queue()
        # make a set to track if we've been here before
        visited = set()
        # enqueue starting node
        q.enqueue([starting_vertex])
        # while our queue is not empty
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # check if the node equals the target
                if current_node == destination_vertex:
                    # if so, return the path
                    return path
                # return neighbors
                neighbors = self.get_neighbors(current_node)
                # loop through the neighbor in neighbors
                for neighbor in neighbors:
                    # new_path equal a list of path
                    new_path = list(path)
                    # append the neighbor to new_path
                    new_path.append(neighbor)
                    # enqueue new_path
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # ## ALT CODE: v1
        # # instantiate Stack object
        # s = Stack()
        # # reverse lookup table
        # traversed = {1: None}
        # # set the current_val equal to None
        # current_val = None
        # # push the starting_vertex
        # s.push(starting_vertex)
        # # while the queue contains values
        # while current_val != destination_vertex:
        #     # pop the current_val off
        #     current_val = s.pop()
        #     # loop through the values in the vertices atrtibute at the specified
        #     # current_val
        #     for val in self.vertices[current_val]:
        #         # if the val is not traversed (already been seen)
        #         if val not in traversed:
        #             # add the current_val to the traversed value at the specified
        #             # val
        #             traversed[val] = current_val
        #             # push to the next val
        #             s.push(val)
        # # instantiate a new empty list to map backwards
        # returnlist = []
        # # while the current_val is not None
        # while current_val is not None:
        #     # append the current_val to the returnlist
        #     returnlist.append(current_val)
        #     # set the current_val equal to the value at the specified index
        #     current_val = traversed[current_val]
        # # reverse the list
        # returnlist.reverse()
        # # return returnlist
        # return returnlist

         
        ## ALT CODE: v2
        # instantiate a Stack
        s = Stack()
        # make a set to track if we've been here before
        visited = set()
        # enqueue starting node
        s.push([starting_vertex])
        # while our stack is not empty
        while s.size() > 0:
            path = s.pop()
            current_node = path[-1]
            # if we haven't visited this node yet,
            if current_node not in visited:
                # print current node
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # check if the node equals the target
                if current_node == destination_vertex:
                    return path
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # ## ALT CODE: v1
        # # recurse function
        # def recurse(graph, traversed, goal, vertex):
        #     # if the vertex is already in traversed
        #     if vertex in traversed:
        #         # return none because there is nothing left
        #         return None
        #     # is the vertex is equal to what we are looking for
        #     if vertex == goal:
        #         # return list to append on to map on the way back
        #         return [vertex]
        #     # if the vertex is not in traversed
        #     if vertex not in traversed:
        #         # append it to traversed since we have now seen it
        #         traversed.append(vertex)
        #     # loop through the val in the specified graph vertex
        #     for val in graph[vertex]:
        #         # result is queal to the recurse
        #         result = recurse(graph, traversed, goal, val)
        #         # is the result is not None
        #         if result is not None:
        #             # append the vertex to result
        #             result.append(vertex)
        #             # return result
        #             return result
        #     # catch, return nothing if all dead ends
        #     return None
        
        # # get result from recursion and reverse
        # result = recurse(self.vertices, [], destination_vertex, starting_vertex)
        # # reverse the result
        # result.reverse()
        # # return result
        # return result


        # ## ALT CODE: v2
        # mark our node as visited
        if not visited:
            # instantiate visited set
            visited = set()
        # if no path
        if not path:
            # instantiate empty list for the path
            path = []
        # add the starting_vertex to the visited set
        visited.add(starting_vertex)
        # if the starting_vertex == destination_vertex
        if starting_vertex == destination_vertex:
            # return the path
            return path
        # if the len(path) == 0
        if len(path) == 0:
            # append the starting_vertex to path since that is the only vertex
            # in that specified path
            path.append(starting_vertex)
        # instantiate neighbors variable
        neighbors = self.get_neighbors(starting_vertex)
        # loop through the neighbor in neighbors
        for neighbor in neighbors:
            # if the neight not in visited
            if neighbor not in visited:
                # instantiate new_path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
                # if new_path
                if new_path:
                    # return new_path
                    return new_path






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
