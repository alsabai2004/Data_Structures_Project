from .graph import Graph


def graph_oprea():
    print("\n" + "=" * 50)
    print("              GRAPH SETUP")
    print("=" * 50)
    print("1. Undirected Graph")
    print("2. Directed Graph")
    print("=" * 50)

    while True:
        graph_type = input("Choose graph type: ").strip()

        if graph_type == "1":
            graph = Graph(directed=False)
            print("Undirected Graph selected.")
            break

        elif graph_type == "2":
            graph = Graph(directed=True)
            print("Directed Graph selected.")
            break

        else:
            print("Invalid choice. Please choose 1 or 2.")

    while True:
        print("\n" + "=" * 50)
        print("                    GRAPH")
        print("=" * 50)
        print("1.  Add Vertex")
        print("2.  Remove Vertex")
        print("3.  Add Edge")
        print("4.  Remove Edge")
        print("5.  Display Graph")
        print("6.  Display Vertices")
        print("7.  BFS Traversal")
        print("8.  DFS Traversal")
        print("9.  BFS Path")
        print("10. Get Neighbors")
        print("11. Check Vertex")
        print("12. Check Edge")
        print("13. Vertex Count")
        print("14. Edge Count")
        print("15. Vertex Degree")
        print("16. Check if Empty")
        print("17. Check Connectivity")
        print("18. Clear Graph")
        print("19. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            vertex = input("Enter vertex: ").strip()

            if not vertex:
                print("Vertex cannot be empty.")
                continue

            if graph.add_vertex(vertex):
                print(f"Vertex '{vertex}' added successfully.")
            else:
                print(f"Vertex '{vertex}' already exists.")

        elif choice == "2":
            vertex = input("Enter vertex to remove: ").strip()

            if graph.remove_vertex(vertex):
                print(f"Vertex '{vertex}' removed successfully.")
            else:
                print(f"Vertex '{vertex}' was not found.")

        elif choice == "3":
            vertex1 = input("Enter first vertex: ").strip()
            vertex2 = input("Enter second vertex: ").strip()

            if not vertex1 or not vertex2:
                print("Vertices cannot be empty.")
                continue

            graph.add_edge(vertex1, vertex2)
            print(f"Edge added: {vertex1} -> {vertex2}")

        elif choice == "4":
            vertex1 = input("Enter first vertex: ").strip()
            vertex2 = input("Enter second vertex: ").strip()

            if graph.remove_edge(vertex1, vertex2):
                print(f"Edge removed: {vertex1} -> {vertex2}")
            else:
                print("Edge was not found.")

        elif choice == "5":
            graph.display()

        elif choice == "6":
            graph.display_vertices()

        elif choice == "7":
            start = input("Enter starting vertex for BFS: ").strip()

            result = graph.bfs(start)

            if result:
                print("BFS:", " -> ".join(result))
            else:
                print(f"Vertex '{start}' was not found.")

        elif choice == "8":
            start = input("Enter starting vertex for DFS: ").strip()

            result = graph.dfs(start)

            if result:
                print("DFS:", " -> ".join(result))
            else:
                print(f"Vertex '{start}' was not found.")

        elif choice == "9":
            start = input("Enter starting vertex: ").strip()
            target = input("Enter target vertex: ").strip()

            path = graph.bfs_path(start, target)

            if path:
                print("Path:", " -> ".join(path))
            else:
                print("No path found.")

        elif choice == "10":
            vertex = input("Enter vertex: ").strip()

            if graph.has_vertex(vertex):
                neighbors = graph.get_neighbors(vertex)

                if neighbors:
                    print(
                        f"Neighbors of '{vertex}':",
                        " -> ".join(neighbors)
                    )
                else:
                    print(f"Vertex '{vertex}' has no neighbors.")
            else:
                print(f"Vertex '{vertex}' was not found.")

        elif choice == "11":
            vertex = input("Enter vertex: ").strip()

            if graph.has_vertex(vertex):
                print(f"Vertex '{vertex}' exists.")
            else:
                print(f"Vertex '{vertex}' does not exist.")

        elif choice == "12":
            vertex1 = input("Enter first vertex: ").strip()
            vertex2 = input("Enter second vertex: ").strip()

            if graph.has_edge(vertex1, vertex2):
                print(f"Edge '{vertex1} -> {vertex2}' exists.")
            else:
                print(f"Edge '{vertex1} -> {vertex2}' does not exist.")

        elif choice == "13":
            print("Number of vertices:", graph.vertex_count())

        elif choice == "14":
            print("Number of edges:", graph.edge_count())

        elif choice == "15":
            vertex = input("Enter vertex: ").strip()

            if graph.has_vertex(vertex):
                print(
                    f"Degree of '{vertex}':",
                    graph.degree(vertex)
                )
            else:
                print(f"Vertex '{vertex}' was not found.")

        elif choice == "16":
            if graph.is_empty():
                print("Graph is empty.")
            else:
                print("Graph contains vertices.")

        elif choice == "17":
            if graph.is_connected():
                print("Graph is connected.")
            else:
                print("Graph is not connected.")

        elif choice == "18":
            graph.clear()
            print("Graph cleared successfully.")

        elif choice == "19":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    graph_oprea()
