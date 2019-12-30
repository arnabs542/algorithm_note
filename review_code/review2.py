# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# Q1.1 copy linked list with a random pointer
class Solution138:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # the copied head, only with val
        if head == None:
            return None
        
        newhead = Node(head.val, None, None)
        curr = newhead
        
        # the hashmap will include the original node and the copied node
        hashmap = {head: newhead}
        
        curr = newhead
        
        # in our while loop, we will firstly copy the next and then copy the random, and if there is no previous built cloned node, we will also create one
        while curr:
            
            # we copy the next pointer, so we need to copy the Node
            if head.next not in hashmap:
                if head.next:
                    hashmap[head.next] = Node(head.next.val, None, None)
                else:
                    hashmap[head.next] = None
                    
            curr.next = hashmap[head.next]
            
            # we copy the random pointer, so we need to copy the random Node
            if head.random not in hashmap:
                if head.random:
                    hashmap[head.random] = Node(head.random.val, None, None)
                else:
                    hashmap[head.random] = None
                
            curr.random = hashmap[head.random]
            
            head = head.next
            curr = curr.next
                
        return newhead


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# Q1.2 copy graph that might have circles
class Solution131:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        # newnode = Node(node.val, [])
        
        # hashmap to record the original node and the cloned node
        hashmap = {}
        
        def dfs(node, hashmap):
            # 2 base cases
            if node in hashmap:
                return hashmap[node]
            
            # because the node is not in the hashmap, we add the ndoe into the hashmap
            # and we need to copy it
            # firstly copy the val
            hashmap[node] = Node(node.val, [])
            
            # then we want to copy the neighbors
            for nei in node.neighbors:
                # (wrong, why?)if we want to copy the neighbors, we need to copy the neighbor nodes at first
                # if nei not in hashmap:
                #     hashmap[nei] = Node(nei.val, [])
                
                # if not none, we add the copied neighbors into the copied node's neighbors
                hashmap[node].neighbors.append(dfs(nei, hashmap))
                    
            return hashmap[node]
        
        dfs(node, hashmap)
        
        return hashmap[node]