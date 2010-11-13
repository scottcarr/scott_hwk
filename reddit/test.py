import pdb
import heapq
import membership
import cluster_aff
from operator import itemgetter

N_LARGEST = 10
ACC_THRESHOLD = 0.5

memberships = membership.build_membership('affinities.clabel','clusters')

clusters = cluster_aff.sum_cluster_affinities(memberships, 'my_publicvotes-20101018_affinities.dump')

largest = heapq.nlargest(N_LARGEST, clusters[1].iteritems(),itemgetter(1))

#this chunk will give all the UIDs of a particular cluster
#need to figure out a way of testing if the members of the cluster really
# like the most popular subreddits of that cluster
cluster_members = []
for c_member in memberships:
	if memberships[c_member] == '1':
		cluster_members.append(c_member)

#this code needs to be redone:
#for subreddit in largest:	
#	good = 0
#	fail = 0
#	for user in cluster_members:
#		pdb.set_trace()
#		if memberships[user][subreddit] > THRESHOLD:
#			good += 1
#		else:
#			fail += 1
#print "For subreddit", subreddit, good, "passes and", fail, "fails"	

pdb.set_trace()
