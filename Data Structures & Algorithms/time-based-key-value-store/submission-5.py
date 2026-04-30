class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self,key : str,value : int,timestamp: int):
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.store.get(key,[])
        if value:
            l = 0
            r = len(value) -1
            while l <= r:
                m = (l+r)//2
                if timestamp >= value[m][1]:
                    res = value[m][0]
                    l = m +1
                else:
                    r = m-1
        return res


































        
