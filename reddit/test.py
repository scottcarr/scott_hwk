import pdb
import csv

f_usr = open('affinities.clabel','r')
f_clust = open('clusters','r')
f_aff = open('my_publicvotes-20101018_affinities.dump')

aff_reader = csv.reader(f_aff,delimiter='\t')

usr = f_usr.readlines()

memberships = {}
i = 0
for line in f_clust:
	memberships[usr[i][:-1]] = line[:-1]
	i+=1

clusters = {}
for row in aff_reader:
	user_id = row[0]
	sr_id = row[1]
	affinity = float(row[2])
	try:
		c_id = int(memberships[user_id])
		try:
			#this will only work if the cluster_ID,sr_id exists
			clusters[c_id][sr_id] += affinity
		except KeyError:
			#either that cluster id or the sr_id didn't exist,
			#so we must initialize it
			try:
				clusters[c_id][sr_id] = affinity
			except KeyError:
				#this must be the first time we'ved seen the cluster_id		
				clusters[c_id] = { sr_id : affinity } 
	except KeyError:
 		print user_id

pdb.set_trace()
