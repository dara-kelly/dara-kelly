import networkx as nx
G=nx.Graph()
G.add_edges_from([(1,2),(1,3),(1,4),(3,4)])
G
>>> <networkx.classes.graph.Graph object at 0x128a930>
G.nodes(data=True)
>>> [(1, {}), (2, {}), (3, {}), (4, {})]
G.node[1]['attribute']='value'
G.nodes(data=True)
>>> [(1, {'attribute': 'value'}), (2, {}), (3, {}), (4, {})]
nx.write_graphml(G,'so.graphml')
