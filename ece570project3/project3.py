import Image
import random
import matplotlib.pyplot as plt

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
        

Nv=200 #Number of vehicles
Lsx=100
Lsy=100
Ldx=450
Ldy=450

my_map = Image.open('localmap.gif')
map_list = list(my_map.getdata())

zeros_list = find_zeros_and_ones(map_list)

x_coords, y_coords = transform_indexes(zeros_list, my_map.size[0])

plt.scatter(x_coords, y_coords)
plt.show()

#Generate randon distribution of vehicles.






xs = []
ys = []


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
