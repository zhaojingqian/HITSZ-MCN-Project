import networkx as nx
from collections import Counter

graph = nx.read_edgelist('/home/zhaojingqian/CNModelProject/database/data/cora_data.txt', delimiter=' ', nodetype=int)
degrees = dict(graph.degree())
# Count the occurrences of each degree
degree_counts = Counter(degrees.values())
# Extract the degrees and their corresponding counts
sorted_degree_counts = dict(sorted(degree_counts.items()))
degrees_list = list(sorted_degree_counts.keys())
counts_list = list(sorted_degree_counts.values())
integrated_dict = {
    'degree': degrees_list,
    'count': counts_list
}
print(integrated_dict)

# 计算coreness
coreness = nx.core_number(graph)
coreness_counts = Counter(coreness.values())
sorted_coreness_counts = dict(sorted(coreness_counts.items()))
coreness_list = list(sorted_coreness_counts.keys())
counts_list = list(sorted_coreness_counts.values())
integrated_dict = {
    'coreness': coreness_list,
    'count': counts_list
}
print(integrated_dict)

# 计算triange
triange = nx.triangles(graph)
triange_counts = Counter(triange.values())
sorted_triange_counts = dict(sorted(triange_counts.items()))
triange_list = list(sorted_triange_counts.keys())
counts_list = list(sorted_triange_counts.values())
integrated_dict = {
    'triange': triange_list,
    'count': counts_list
}

# 计算所有节点的最短路径
shortest_path = dict(nx.all_pairs_shortest_path_length(graph))
shortest_path_list = []
for key in shortest_path.keys():
    for key2 in shortest_path[key].keys():
        if key == key2:
            continue
        shortest_path_list.append(shortest_path[key][key2])
shortest_path_counts = Counter(shortest_path_list)
sorted_shortest_path_counts = dict(sorted(shortest_path_counts.items()))
shortest_path_list = list(sorted_shortest_path_counts.keys())
counts_list = list(sorted_shortest_path_counts.values())
integrated_dict = {
    'shortest_path': shortest_path_list,
    'count': counts_list
}

print(integrated_dict)