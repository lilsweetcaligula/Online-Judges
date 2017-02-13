#!/bin/python3

import sys

def solution(topics):
    import collections

    topicCounts = []
    
    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            topicCounts.append(bin(int(topics[i], base=2) | int(topics[j], base=2))[2:].count('1'))

    maxTopicCount = max(topicCounts)
    maxGroupCount = collections.Counter(topicCounts)[maxTopicCount]

    return maxTopicCount, maxGroupCount
            

n, m    = map(int, input().split())
topic   = []
topic_i = 0

for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)
    
maxTopicCount, maxGroupCount = solution(topic)

print(maxTopicCount)
print(maxGroupCount)
