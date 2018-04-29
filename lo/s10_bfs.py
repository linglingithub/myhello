from collections import deque

class Solution:
    def bfs(self, root):
        # Assumptions: graph is connected
        if not root:
            return
        queue = deque()
        node = root
        queue.append(node)
        visited = {}
        visited[root] = True
        while queue:
            node = queue.popleft()
            # print the node
            self.print_node(node)
            # get nei
            for nei in node.neighbors:      # expand
                if visited.get(nei, False):
                    continue
                visited[nei] = True
                queue.append(nei)           # generate

    def print_node(self, node, node_breaker=" "):
        print(node.val, node_breaker)

    # follow up 1, print in level order
    def bfs_level(self, root):
        # Assumptions: graph is connected
        if not root:
            return
        queue = deque()
        node = root
        queue.append(node)
        visited = {}
        visited[root] = True
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                # print the node
                self.print_node(node)
                # get nei
                for nei in node.neighbors:
                    if visited.get(nei, False):
                        continue
                    visited[nei] = True
                    queue.append(nei)
            print("======== level breaker here ========")


    # follow up 2, return root --> node's level counts
    def bfs_level_countSelf(self, root, target):
        # Assumptions: graph is connected
        if not root:
            return 0
        queue = deque()
        node = root
        queue.append(node)
        visited = {}
        visited[root] = True
        dist = 0
        while queue:
            dist += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node == target:
                    print("Found: ", dist)
                    return dist
                # get nei
                for nei in node.neighbors:
                    if visited.get(nei, False):
                        continue
                    visited[nei] = True
                    queue.append(nei)
            print("======== level breaker here ========")
        return -1


    def bfs_level_count(self, root, target):
        # Assumptions: graph is connected
        if not root:
            return 0
        if target == root:                          # since check target at generating, then should corner case the root
            return 0
        queue = deque()
        node = root
        queue.append(node)
        visited = {}
        visited[root] = True
        dist = 0
        while queue:
            dist += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                # get nei
                for nei in node.neighbors:
                    if nei == target:               # !!! check target when generating node, earlier than self version
                        return dist + 1             # so should return dist + 1
                    if visited.get(nei, False):
                        continue
                    visited[nei] = True
                    queue.append(nei)
            print("======== level breaker here ========")
        return -1

    # follow up: find shortest path
    def bfs_shortest_path(self, init, goal):
        # 1. remove

