import csv

def sum_cluster_affinities(memberships, aff_filename):
	#takes the user_id, cluster_id pairs from memberships
	# and sums the affinities for every subreddit that a user
	# of a given cluster has voted on
	# output form: clusters['cluster_id']['subreddit_id'] = sumed_affinity
	
	f_aff = open(aff_filename)

	aff_reader = csv.reader(f_aff,delimiter='\t')

	clusters = {}
	for row in aff_reader:
		#each for in aff file is a tuple, so need to get the parts
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
					#must be the first time for  the cluster_id		
					clusters[c_id] = { sr_id : affinity } 
		except KeyError:
			#apparently not all UIDs in clabel are in the output of srrecs.r	 
			print user_id, "in affinities.clabel but not in srrecs.r output"
	return clusters
