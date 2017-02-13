#!/bin/python3

import sys

def solution(cityCount, stations):
    stationIndex = 0
    distances    = []

    for city in range(cityCount):
        east = stations[stationIndex]
        west = stations[stationIndex - 1] if stationIndex > 0 else east
        
        distEast = abs(city - east)
        distWest = abs(city - west)

        distances.append(min(distEast, distWest))

        if distWest >= distEast and stationIndex + 1 < len(stations):
            stationIndex += 1

    return distances

n, m = map(int, input().split())
c    = list(map(int, input().split()))
d    = solution(n, sorted(c))

print(max(d))
