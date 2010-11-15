import array
import pdb

x_filename = './data/x.dat'
y_filename = './data/y.dat'

def read_x_data():
	temp = []
	with open(x_filename) as file:
		for line in file:
			tuple = line.rpartition(" ")
			temp.append( [ float(tuple[0]), float(tuple[2]) ] )
	return temp

def read_y_data():
	temp = []
	with open(y_filename) as file:
		for line in file:
			temp.append(float(line))
	return temp

x = read_x_data()
y = read_y_data()
