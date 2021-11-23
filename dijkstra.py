'''
Elek adatszerkezete:
3d lista:
1->melyik pont szomszedai
2-> [int neighbour,float dist]

a kód olvasasa komoly energiakat igenyel, főleg az algoritmusnal,
az adatszerkezeteket a feltoltesek utan tobbszor atirtam, az indexelest meg hozzatakoltam,
ennek eredmenye ez a mernoki csoda
'''

import math

def calc_distance(x1, x2,  y1,  y2):
    return math.hypot(x2 - x1, y2 - y1)

routes = []
points = []
edges = []

p=int(input())
n=int(input())
e=int(input())

alt_edges = []
for i in range(n):
    alt_edges.append([])

line = input()

for i in range(p):
    line = input().split("\t")
    routes.append([int(line[0]), int(line[1])])

line = input()

for i in range(n):
    line = input().split('\t')
    points.append([int(line[0]), int(line[1])])

line = input()

for i in range(e):
    line = input().split('\t')
    distance = calc_distance(points[int(line[0])][0],points[int(line[1])][0],points[int(line[0])][1],points[int(line[1])][1])
    alt_edges[int(line[0])].append([int(line[1]), distance])
    alt_edges[int(line[1])].append([int(line[0]), distance])
    
route_distances= []

for route in routes:
    
    current_point = route[0]
    end = route[1]
    
    visited = [False] * len(points)
    distance_from_point=[99999999999999]* n
    visited_neighbours = []
    
    visited_neighbours.append(current_point)
    distance_from_point[current_point] = 0
    
    while(not visited[end]):
        for i in range(len(alt_edges[current_point])):
            if  not (visited[alt_edges[current_point][i][0]]) :
                if distance_from_point[current_point] + alt_edges[current_point][i][1] < distance_from_point[alt_edges[current_point][i][0]]:
                    distance_from_point[alt_edges[current_point][i][0]] = distance_from_point[current_point] + alt_edges[current_point][i][1]
                    if alt_edges[current_point][i][0] not in visited_neighbours:
                        visited_neighbours.append(alt_edges[current_point][i][0])

        visited[current_point]= True
        visited_neighbours.pop(visited_neighbours.index(current_point))
        
        min_val = 9999999999999999
        for i in visited_neighbours:
            if  distance_from_point[i] < min_val:
                min_val = distance_from_point[i]
                current_point= i
        
    route_distances.append(round(distance_from_point[end],2))

for i in route_distances:
    print(i,end="\t")


