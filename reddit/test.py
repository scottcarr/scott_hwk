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
cluster_members = {}
c_id = '1'
for c_member in memberships:
	if memberships[c_member] == c_id:
		cluster_members[c_member] = { 'good' : 0, 'bad' : 0, 'belongs' : 1 }
		

cluster_aff.find_affs_in_cluster(cluster_members, largest, 'my_publicvotes-20101018_affinities.dump',ACC_THRESHOLD)

