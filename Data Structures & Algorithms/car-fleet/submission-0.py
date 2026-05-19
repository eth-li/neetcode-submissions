class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(position)):
            d[position[i]]=speed[i]
        stack = sorted(d.items())
        
        fleets = len(stack)
        prev_time = (target - stack[-1][0])/stack[-1][1]
        for i in reversed(range(len(stack)-1)):
            time = (target - stack[i][0])/stack[i][1]
            if time <= prev_time:
                fleets -=1
            else:
                prev_time = time
        return fleets

