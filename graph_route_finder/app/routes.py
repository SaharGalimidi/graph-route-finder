from flask import Blueprint, render_template, request
import json
from .graph import Graph
import os

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    file_path = os.path.join(os.path.dirname(__file__), 'graph_example.json')
    with open(file_path) as file:
        json_data = json.load(file)
    graph = Graph(json_data)
    shortest_path = []
    path_distance = None
    closest_vertex = None

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'find_shortest_path':
            start = request.form.get('start')
            end = request.form.get('end')
            shortest_path, path_distance = graph.find_shortest_path(start, end)
            if shortest_path:
                graph.show_graph(shortest_path)

        elif action == 'find_closest_vertex':
            vertex = request.form.get('closest')
            vertex = tuple(map(float, vertex.replace(
                '(', '').replace(')', '').split(',')))
            closest_vertex = graph.find_closest_vertex(vertex)
            if closest_vertex:
                graph.show_graph(
                    closest_vertex_info=closest_vertex, source_vertex=vertex)

    return render_template('index.html', vertices=graph.adjacency_dict.keys(),
                           shortest_path=shortest_path, path_distance=path_distance, closest_vertex=closest_vertex)
