import pdb
import membership
import cluster_aff

N_LARGEST = 10
ACC_THRESHOLD = 0.5
N_CLUSTERS = 50

# memberships is a dict, i.e. memberships['user_id'] = cluster_to which_the_user_belongs
memberships = membership.build_membership('affinities.clabel','clusters')

# cluster is a dict where the keys are cluster ids 1...50 and the values are a list of users that
# belong to that cluster
clusters = cluster_aff.sum_cluster_affinities(memberships, 'my_publicvotes-20101018_affinities.dump')

#this does the actual testing and printing
cluster_aff.test_clusters(memberships,'my_publicvotes-20101018_affinities.dump', ACC_THRESHOLD, clusters, N_LARGEST)
