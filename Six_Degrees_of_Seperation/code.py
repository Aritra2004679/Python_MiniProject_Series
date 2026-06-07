import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# Read Connections
with open("connections.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        person1, person2 = line.split(",")
        G.add_edge(person1.strip(), person2.strip())

print("=" * 50)
print("SIX DEGREES OF SEPARATION")
print("=" * 50)

start_person = input("Enter your name: ")
target_person = input("Enter favourite person: ")

try:
    # Find Shortest Path
    path = nx.shortest_path(G, start_person, target_person)

    print("\nConnection Found!\n")

    for i in range(len(path)):
        print(path[i])

        if i != len(path) - 1:
            print("↓")

    print("\nDegrees of Separation :", len(path) - 1)

    # Highlight Path Edges
    path_edges = list(zip(path, path[1:]))

    # Draw Network
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=2000
    )
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=8
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray"
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        width=3,
        edge_color="red"
    )

    plt.title("Six Degrees of Separation")
    plt.savefig("network_graph.png")
    plt.show()

except nx.NetworkXNoPath:
    print("\nNo connection exists.")

except nx.NodeNotFound:
    print("\nPerson not found in the network.")