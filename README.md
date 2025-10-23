# 📡 Telecom Network Optimization using Graph Algorithms

## 🔍 Overview
This project focuses on optimizing telecom cable network layouts using **graph theory algorithms**.  
It analyzes network connectivity, cost efficiency, and optimal cable routing between telecom stations.  
The project uses Python’s `networkx`, `matplotlib`, and `numpy` libraries for graph construction, visualization, and analysis.

---

## 🎯 Project Objectives
- Model telecom networks using **weighted undirected graphs**.
- Apply **Minimum Spanning Tree (MST)** algorithms (Kruskal’s and Prim’s) to minimize cable costs.
- Implement the **Chinese Postman Problem** (Route Optimization) to ensure each cable is traversed at least once with minimal total distance.
- Visualize and save all network graphs (original, MST, and optimized routes) as image outputs.

---

## 🧠 Algorithms Used

# **1. Kruskal’s Algorithm (MST)**
Finds the minimum-cost connection between all network nodes without forming cycles.

# **2. Prim’s Algorithm (MST)**
An alternative MST algorithm that grows the tree from a single starting node.

# **3. Chinese Postman Problem (Route Optimization)**
Ensures all cables are covered efficiently, converting the MST into an Eulerian multigraph to determine the shortest inspection route.

---

## 🧩 Implementation Details

# **Languages & Libraries**
- Python 3.x  
- Libraries:
  - `networkx` (for graph algorithms)
  - `matplotlib` (for visualization)
  - `numpy` (for numerical computations)

# **Project Structure**

cgt(pjt)/
│
├── src/
│ ├── demo.py # Main program (runs the full simulation)
│ ├── graph_utils.py # Handles graph generation and basic utilities
│ ├── mst.py # Kruskal’s and Prim’s MST implementations
│ ├── eulerian.py # Chinese Postman (Eulerian) route implementation
│
├── outputs/ # Graph plots and result images are saved here
│ ├── original_graph.png
│ ├── mst_graph.png
│ └── eulerian_route.png
│
├── requirements.txt # Required libraries
├── README.md # Documentation file
└── .gitignore # Files ignored by Git
