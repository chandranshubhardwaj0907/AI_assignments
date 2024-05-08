class Graph:
  def __init__(self, graph, heuristic_list, start):
    self.graph = graph
    self.heuristic = heuristic_list
    self.start = start
    self.parent = {}
    self.status = {}
    self.solution = {}

  def apply_AO(self):
    """Starts the A* search with AO* optimization."""
    self.ao_star(self.start, False)

  def neighbor(self, v):
    """Returns the neighbors of a node."""
    return self.graph.get(v, [])

  def get_status(self, v):
    """Returns the processing state of a node."""
    return self.status.get(v, 0)

  def set_status(self, v, val):
    """Updates the processing state of a node."""
    self.status[v] = val

  def get_heuristic_val(self, n):
    """Retrieves the heuristic value for a node."""
    return self.heuristic.get(n, 0)

  def set_heuristic_val(self, n, value):
    """Updates the heuristic value for a node."""
    self.heuristic[n] = value

  def min_cost_node(self, v):
    """Finds the child node with the minimum cost."""
    min_cost = float('inf')
    children = []
    for neighbors in self.neighbor(v):
      cost = 0
      child_nodes = []
      for child, weight in neighbors:
        cost += self.get_heuristic_val(child) + weight
        child_nodes.append(child)
      if cost < min_cost:
        min_cost = cost
        children = child_nodes
    return min_cost, children
  def ao_star(self, v, backtrack):
    """Recursive core of the A* search with AO* optimization."""
    print("heuristic value:", self.heuristic)
    print("solution:", self.solution)
    print("processing node:", v)
    if self.get_status(v) >= 0:
      min_cost, child_nodes = self.min_cost_node(v)
      self.set_heuristic_val(v, len(child_nodes))
      solved = True
      for child in child_nodes:
        self.parent[child] = v
        if self.get_status(child) != -1:
          solved = False & solved
      if solved:
        self.set_status(v, -1)
        self.solution[v] = child_nodes
        if v != self.start:
          self.ao_star(self.parent[v], True)
      if not backtrack:
        if child_nodes:
          for child in child_nodes:
            self.set_status(child, 0)
            self.ao_star(child, False)


h1 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph1 = {
  'A': [[('B', 1), ('C', 1)], [('D', 1)]],
  'B': [[('G', 1)], [('H', 1)]],
  'D': [[('E', 1), ('F', 1)]]
}
g1 = Graph(graph1, h1, 'A')
g1.apply_AO()
