import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define processes and resources
processes = ["P0", "P1", "P2"]
resources = ["A", "B", "C", "D", "E", "F"]

# Add nodes
G.add_nodes_from(processes, shape="circle")
G.add_nodes_from(resources, shape="square")

# Define edges (requests and allocations)
edges = [
    ("P0", "A"), ("P0", "B"), ("P0", "C"),  
    ("A", "P0"), ("B", "P0"), ("C", "P0"),

    ("P1", "D"), ("P1", "E"), ("P1", "B"),  
    ("D", "P1"), ("E", "P1"), ("B", "P1"),

    ("P2", "C"), ("P2", "F"), ("P2", "D"),  
    ("C", "P2"), ("F", "P2"), ("D", "P2")  
]

G.add_edges_from(edges)

# Define positions
pos = {
    "P0": (-2, 2), "P1": (0, 2), "P2": (2, 2),
    "A": (-3, 0), "B": (-1, 0), "C": (1, 0), 
    "D": (-1, -2), "E": (1, -2), "F": (3, -2)
}

# Assign colors to distinguish processes and resources
node_colors = ["lightblue" if n in processes else "lightgray" for n in G.nodes]

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="black", node_size=1500, arrowsize=15)
plt.title("Resource Allocation Graph (RAG)")
plt.show()
