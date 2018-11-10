import pprint

class Graph :
	def __init__(self, vertices) :
		self.v = vertices
		self.graph = [ [0 for c in range(self.v)] for r in range(self.v) ]

	def dijkstra(self, n) :

		dist = [10000]*self.v
		dist[n] = 0
		done = [False]*self.v

		q = []

		q.append(n)

		while len(q) > 0 :
			elem = q.pop(0) 
			done[elem] = True
			for idx, val in enumerate(self.graph[elem]) :
				if val > 0 and not done[idx]:
					q.append(idx)
					dist[idx] = min(dist[idx], dist[elem] + self.graph[elem][idx])

		print(dist)
		print(done)

	def dijkstra_path(self, n, end) :

		dist = [10000]*self.v
		parent = [None]*self.v

		dist[n] = 0
		done = [False]*self.v

		q = []

		q.append(n)

		while len(q) > 0 :
			elem = q.pop(0) 
			done[elem] = True
			for idx, val in enumerate(self.graph[elem]) :
				if val > 0 and not done[idx]:
					q.append(idx)
					e_d = dist[idx]
					n_d = dist[elem] + self.graph[elem][idx]

					if n_d < e_d :
						dist[idx] = n_d
						parent[idx] = elem

		print(dist)
		print(parent)

		c = end
		while True :
			print(c)
			if parent[c] == None :
				print(parent[c])
				break
			else :
				c = parent[c]

g  = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 

g.dijkstra_path(0, 0)