from flask import Flask
from flask import request, make_response
from flask_cors import CORS
import os
import json
import networkx as nx
from collections import Counter


ROOT_PATH = 'database/data'

def readJson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def writeTxt(file_path, edges_list):
    with open(os.path.join(ROOT_PATH, file_path.split('.')[0] + '.txt'), 'w', encoding='utf-8') as f:
        for edge in edges_list:
            f.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test_ping():
    app.logger.info("Ping Success")
    return "Ping Success"

@app.route('/get_data_list', methods=['GET'])
def get_data_list():
    file_names = []
    for root, dirs, files in os.walk(ROOT_PATH):
        for file in files:
            if file.endswith('.json'):
                file_names.append(file.split('.')[0])
    file_names = list(set(file_names))
    return file_names

@app.route('/upload', methods=['POST', 'OPTIONS'])
def save_file():
    if request.method == 'OPTIONS':  # 处理OPTIONS请求
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    file = request.files['file']
    file_name = file.filename
    file.save(os.path.join(ROOT_PATH, file_name))
    
    # data process
    pre_data = readJson(os.path.join(ROOT_PATH, file_name))
    try:
        graph = []
        edges_list = pre_data['links']
        for edge in edges_list:
            source = edge['source']
            target = edge['target']
            graph.append([source, target])
        print(len(graph))
        print(graph[0])
        writeTxt(file_name, graph)
    except Exception as e:
        print(e)
        return "error"
    return "success"

@app.route('/algorithm', methods=['GET'])
def cal_degree():
    data_name = request.args.get('data_name')
    data_path = os.path.join(ROOT_PATH, data_name + '.txt')
    graph = nx.read_edgelist(data_path, delimiter=' ', nodetype=int)
    graph.remove_edges_from(nx.selfloop_edges(graph))
    
    features_set = {}

    # 对于大图（节点大于1000）进行下采样，按照degree降序采样1000个
    if len(graph.nodes()) > 1000:
        degrees = dict(graph.degree())
        sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
        nodes_list = []
        for i in range(400):
            nodes_list.append(sorted_degrees[i][0])
        subgraph = graph.subgraph(nodes_list)
    
    # 计算degree
    degrees = dict(graph.degree())
    degree_counts = Counter(degrees.values())
    sorted_degree_counts = dict(sorted(degree_counts.items()))
    degrees_list = list(sorted_degree_counts.keys())
    counts_list = list(sorted_degree_counts.values())
    integrated_dict = {
        'degree': degrees_list,
        'count': counts_list
    }
    features_set['degree'] = integrated_dict
    
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
    features_set['coreness'] = integrated_dict
    
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
    features_set['triangle'] = integrated_dict

    # 计算所有节点的最短路径
    if len(graph.nodes()) > 1000:
        graph = subgraph

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
    features_set['shortest_path'] = integrated_dict
    
    # 计算 clustering coefficient
    clustering_coefficient = nx.clustering(graph)
    clustering_coefficient_counts = Counter(clustering_coefficient.values())
    sorted_clustering_coefficient_counts = dict(sorted(clustering_coefficient_counts.items()))
    clustering_coefficient_list = list(sorted_clustering_coefficient_counts.keys())
    clustering_coefficient_list = [round(x, 3) for x in clustering_coefficient_list]
    counts_list = list(sorted_clustering_coefficient_counts.values())
    integrated_dict = {
        'clustering_coefficient': clustering_coefficient_list,
        'count': counts_list
    }
    # 去除key为0的项
    integrated_dict['clustering_coefficient'] = integrated_dict['clustering_coefficient'][1:]
    integrated_dict['count'] = integrated_dict['count'][1:]
    features_set['clustering_coefficient'] = integrated_dict
    print(features_set)
    return features_set

if __name__ == '__main__':
    app.run(port=8280, debug=True)