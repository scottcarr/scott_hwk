import csv
import pdb

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
	f_aff.close()
	return clusters

def find_affs_in_cluster(members, top_srs, aff_filename, threshold):		
	f_aff = open(aff_filename)
	aff_reader = csv.reader(f_aff,delimiter='\t')
	
	total_good = 0
	total_bad = 0		
	
	for row in aff_reader:
		#each for in aff file is a tuple, so need to get the parts
		user_id = row[0]
		sr_id = row[1]
		affinity = float(row[2])
		
		try:
			if members[user_id]['belongs'] == 1:
			
				#pdb.set_trace()
				good = 0
				bad = 0
	
				for sr in top_srs:
					#pdb.set_trace()
					if sr[0] == sr_id:
						#print affinity, threshold
						if affinity > threshold:
							members[user_id]['good'] += 1
							total_good += 1
						else:	
							members[user_id]['bad'] += 1
							total_bad += 1
		except KeyError:
			#do nothing
			x = 1

	for user in members:
		print user, members[user]['good'], "good and ", members[user]['bad'], "bad"	
	
	print "Totals:", total_good,"good and", total_bad, "bad"
