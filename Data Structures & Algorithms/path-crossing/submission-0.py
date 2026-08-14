class Solution:
    def isPathCrossing(self, path: str) -> bool:
        origin = [0,0]
        hashmap = {(0,0)}
        for p in path:
            if p == 'N':
                origin[1] += 1
            elif p == 'E':
                origin[0] -= 1
            elif p == 'S':
                origin [1] -= 1
            else:
                origin[0] += 1
            
            if tuple(origin) in hashmap:
                return True
            
            hashmap.add((origin[0],origin[1]))
        return False
