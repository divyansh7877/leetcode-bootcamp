class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        '''
        
        '''
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target or max_stop < source:
            return -1

        n = len(routes)
        minbuseslist = [float('inf')] * (max_stop + 1)
        minbuseslist[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, minbuseslist[stop])
                mini += 1
                for stop in route:
                    if minbuseslist[stop] > mini:
                        minbuseslist[stop] = mini
                        flag = True
               
        return minbuseslist[target] if minbuseslist[target] < float('inf') else -1