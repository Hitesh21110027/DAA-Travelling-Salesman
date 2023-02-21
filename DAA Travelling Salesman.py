
from sys import maxsize
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s):

	# stores all nodes apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# stores minimum weight for Hamiltonian Cycle
    
	min_path = maxsize
	next_permutation=permutations(vertex)
    #finds all possible orders of the nodes in list form
	for i in next_permutation:

		# store current Path weight
		current_pathweight = 0

		# calculate current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		
	return min_path




graph = [[0, 10, 15, 20], [10, 0, 35, 25],
[15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(travellingSalesmanProblem(graph, s))
#passes function