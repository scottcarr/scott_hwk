#!/usr/bin/python
import Image
import random
import matplotlib.pyplot as plt
import pdb
import networkx as nx

def find_zeros_and_ones(mylist):
    my_zeros = []

    i = -1
    try:
        while 1:
            i = mylist.index(0, i+1)
            my_zeros.append(i)
    except ValueError:
        pass

        i = -1
    try:
        while 1:
            i = mylist.index(1, i+1)
            my_zeros.append(i)
    except ValueError:
        pass
    return my_zeros

def transform_indexes(index_list, cols):

    x_coords = []
    y_coords = []

    for index in index_list:
        x_coords.append(index % cols)
        y_coords.append(index / cols)

    return x_coords, y_coords
        

def return_vehicles_in_range(this_vehicle,vehicles, s_range):

	vehicles_in_range = []
	for vehicle in vehicles:
 		if is_within_range(vehicles[0], vehicles[1], this_vehicle[0], this_vehicle[1], s_range):		
			vehicles_in_range.append(vehicle)
	return vehicles_in_range

def is_within_range(x1, y1, x2, y2, s_range):
	
	if (x1 <= x2 + s_range /2 ) and (x1 >= x2 - s_range / 2) and (y1 <= y2 + s_range /2) and (y1 >= y2 - s_range /2):
		return True
	else:
		return False
def get_node_attr(Graph, node_name, attr_name):
	return Graph.nodes(data=True)[Graph.nodes().index(node_name)][1][attr_name]

def run_simulation(draw_graph):
	Nv=200 #Number of vehicles
	Lsx=100
	Lsy=100
	Ldx=450
	Ldy=450
	s_range = 200

	my_map = Image.open('localmap.gif')
	map_list = list(my_map.getdata())

	zeros_list = find_zeros_and_ones(map_list)

	x_coords, y_coords = transform_indexes(zeros_list, my_map.size[0])

	xy_pairs = range(len(x_coords))

	for i in range(len(x_coords)):
		xy_pairs[i] = (x_coords[i], y_coords[i])

	vehicles = random.sample(xy_pairs, Nv)

	vehicles_x = []
	vehicles_y = []
	for pair in vehicles:
		vehicles_x.append(pair[0])
		vehicles_y.append(pair[1])

	G = nx.Graph()

	for vehicle in vehicles:
		v_x = vehicle[0]
		v_y = vehicle[1]
		name = str(v_x)
		name += str(v_y)
		G.add_node(name)
		G.node[name]['x'] = v_x
		G.node[name]['y'] = v_y
		G.nodes(data=True)

	G.add_node('source', x = Lsx, y = Lsy)
	G.add_node('destination', x = Ldx, y = Ldy)

	for node in vehicles:
		for other_node in vehicles:
			if is_within_range(node[0], node[1], other_node[0], other_node[1], s_range):	
				name1 = node
				name1 = str(node[0])
				name1 += str(node[1])
				name2 = other_node
				name2 = str(other_node[0])
				name2 += str(other_node[1])
				if name1 != name2:
					G.add_edge(name1, name2)

	for vehicle in vehicles:
		if is_within_range(vehicle[0], vehicle[1], Lsx, Lsy, s_range):
			name1 = vehicle
			name1 = str(vehicle[0])
			name1 += str(vehicle[1])
			G.add_edge('source', name1)

	for vehicle in vehicles:
		if is_within_range(vehicle[0], vehicle[1], Ldx, Ldy, s_range):
			name1 = vehicle
			name1 = str(vehicle[0])
			name1 += str(vehicle[1])
			G.add_edge('destination', name1)
			
	path = nx.shortest_path(G, source = 'source', target = 'destination')
	
	if draw_graph == True:
		plt.scatter(vehicles_x, vehicles_y, marker = 'o')
		plt.scatter(x_coords, y_coords, s = 1)
		plt.scatter(Lsx, Lsy, marker = '^', color = 'r')
		plt.scatter(Ldx, Ldy, marker = '^', color = 'r')
		plt.annotate('source', (Lsx, Lsy))
		plt.annotate('destination', (Ldx, Ldy))
		plt.show()

	for vehicle in path:
		plt.scatter(get_node_attr(G, vehicle, 'x'), get_node_attr(G,vehicle,'y'), marker='h', color = 'r')


	return len(path)

N_TRIALS = 100
results = []
for i in range(N_TRIALS):
	results.append(run_simulation(False))

print results

'''%change color for demonstration
[x,y]=find(map==0|map==1)
L=size(x,1)
for i=1:L:
    map(x(i),y(i))=40;
end

i=floor(rand(1,Nv)*L);
Lx=x(i);
Ly=y(i);
image(map);
hold on; 
scatter(Ly,Lx,'wo');
scatter(Lsx,Lsy,'rs','filled');
scatter(Ldx,Ldy,'rs','filled');
text(Lsx,Lsy+10,'Resource');
text(Ldx,Ldy+10,'Destination');'''
