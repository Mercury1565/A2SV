class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        visited = set()
        walls = set(map(tuple , walls))
        guards = set(map(tuple , guards))

        for guard in guards:
            pt = list(guard)
            visited.add(tuple(pt))

            while pt[1] > 0: # Left
                pt[1] -= 1
                if tuple(pt) in walls or tuple(pt) in guards:
                    break

                visited.add(tuple(pt))
                

            pt = list(guard)
            while pt[1] < (n - 1): # Right
                pt[1] += 1
                if tuple(pt) in walls or tuple(pt) in guards:
                    break
            
                visited.add(tuple(pt))
                

            pt = list(guard)
            while pt[0] < (m - 1): # Down
                pt[0] += 1
                if tuple(pt) in walls or tuple(pt) in guards:
                    break
             
                visited.add(tuple(pt))
                

            pt = list(guard)
            while pt[0] > 0: # Up
                pt[0] -= 1
                if tuple(pt) in walls or tuple(pt) in guards:
                    break
            
                visited.add(tuple(pt))
    
        return (m*n) - len(visited) - len(walls)
