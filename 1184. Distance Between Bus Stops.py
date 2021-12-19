#Runtime: 40 ms, faster than 95.38% of Python3 online submissions for Distance Between Bus Stops.
#Memory Usage: 15 MB, less than 75.27% of Python3 online submissions for Distance Between Bus Stops.

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        outloop = 0
        inloop = 0
        for i in range(len(distance)):
            if i < start or i >= destination:
                outloop += distance[i]
            else:
                inloop += distance[i]
        return min(inloop, outloop)
