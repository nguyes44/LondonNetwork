import pyperf
import random
import sys
sys.path.append('.\src\Graph_Builder')  # noqa: W605
sys.path.append('.\src\Metric_Extractor')  # noqa: W605
sys.path.append('.\_dataset')  # noqa: W605
from CsvLine import csvReaderLines  # noqa: E402
from CsvStation import csvReaderStations  # noqa: E402
from CsvConnection import csvReaderConnections  # noqa: E402
from GraphBuilder import GraphBuilder  # noqa: E402
from A_StarBenchmark import a_star  # noqa: E402
from DijkstraBenchmark import dijkstra  # noqa: E402


def main():
    graph = graph_generation()
    randomNodes = random_nodes(graph)
    do_bench(randomNodes, graph)


def random_nodes(graph):
    stations = list(graph.get_stationsDict().values())  # syntax
    upper_bound = len(stations) - 1
    i = random.randint(0, upper_bound)
    j = random.randint(0, upper_bound)
    return [stations[i].get_id(), stations[j].get_id()]


def graph_generation():
    londonLines = "_dataset/london.lines.csv"
    londonStations = "_dataset/london.stations.csv"
    londonConnections = "_dataset/london.connections.csv"

    tempStations = csvReaderStations(londonStations)
    tempLines = csvReaderLines(londonLines)
    tempConnections = csvReaderConnections(
        londonConnections, tempLines, tempStations)

    graph = GraphBuilder(tempStations, tempLines, tempConnections)
    graph.load_graph()
    return graph


def do_bench(nodes, graph):
    runner = pyperf.Runner()
    runner.bench_func('a_star', a_star, graph, nodes[0], nodes[1])

    print('Nodes visited:')

    i = 0
    runs = 20  # pyperf runs the algorithm 20 times per instance
    average = []
    temp = 0

    while (i < runs):
        temp = dijkstra(graph, nodes[0], nodes[1])
        average.append(temp)
        i += 1
    print(sum(average)/runs)
    runner.bench_func('dijkstra', dijkstra, graph, nodes[0], nodes[1])


main()
