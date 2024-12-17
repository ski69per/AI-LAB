def __init__(self):
self.adjacency_list = {}
def add_edge(self, u, v):
if u not in self.adjacency_list:
self.adjacency_list[u] = []
self.adjacency_list[u].append(v)
def depth_limited_dfs(self, node, goal, limit, visited):
if limit < 0:
return False
if node == goal:
return True
visited.add(node)
for neighbor in self.adjacency_list.get(node, []):
if neighbor not in visited:
if self.depth_limited_dfs(neighbor, goal, limit - 1, visited):
return True
visited.remove(node) # Allow revisiting for the next iteration
return False
def iddfs(self, start, goal, max_depth):
for depth in range(max_depth + 1):
visited = set()
if self.depth_limited_dfs(start, goal, depth, visited):
return True
return False
def main():
graph = Graph()
# Input number of edges
num_edges = int(input("Enter the number of edges: "))
# Input edges
for _ in range(num_edges):
edge = input("Enter an edge (format: A B): ").split()
graph.add_edge(edge[0], edge[1])
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
max_depth = int(input("Enter the maximum depth for IDDFS: "))
if graph.iddfs(start_node, goal_node, max_depth):
print(f"Goal node {goal_node} found!")
else:
print(f"Goal node {goal_node} not found within depth {max_depth}.")
if __name__ == "__main__":
main()
