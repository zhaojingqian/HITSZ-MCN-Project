import networkx as nx
from collections import Counter

graph = nx.read_edgelist('/home/zjq/CNModelProject/database/data/cora_data.txt', delimiter=' ', nodetype=int)
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
print(integrated_dict)