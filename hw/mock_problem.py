"""
399


usd -> yen
yen -> aus
mile - > km


? usd -> aus ==>
usd -> yen * yen --> aus  ==>


? yen -> usd ==>
 1 / (usd/yen)


 Basic idea:

 model the sources and destinations as nodes in a graph, the ratio is a weight on the edge,
 this is a Directed Graph,

 then a query is process as looking for one of the following:
 1) source node - > target node path (until connected nodes are finished)
 or if 1) is not found, then
 2) target node -> source node (until connejctedl...) and get the 1/x of the edges' mulitiplication value

By finding the path we can do DFS / BFS

"""
from collections import defaultdict, deque
import functools

class Solution:
    def __init__(self, src_dest_list):
        """
        Process the list to generate a graph, in the format of
        dict of (src, set((dest, ratio)))
        dict of { node: indegrees } --> need or not? maybe not.
        :param sour_dest_list: list of tuples like (source, dest, ratio)
        """
        self.data = self._process(src_dest_list)

    def _process(self, src_dest_list):
        data = defaultdict(set)
        for s, d, r in src_dest_list:
            data[s].add((d, r))
        return data

    def query(self, src, dest):
        """
        return the float / double ratio
        :param source:
        :param destination:
        :return:
        """
        if src not in self.data or dest not in self.data:
            return None
        visited = set()
        queue = deque()
        queue.append(src)
        ratios = [1]
        self.helper(visited, src, dest, ratios)
        if len(ratios) > 1:
            return functools.reduce(ratios, lambda = x : x * x)

