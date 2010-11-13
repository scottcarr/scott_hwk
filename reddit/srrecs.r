library('skmeans')
x <- readCM('affinities.cm')
mat <- skmeans(x, 50, 'lihc')
write(mat$cluster, file="clusters", ncolumns = 1)
