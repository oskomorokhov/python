class TimeMap:

    def __init__(self):

        self.ts = {}
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.ts.keys():

            self.ts[key].append(timestamp)
            self.values[key].append(value)

        else:

            self.ts[key] = [timestamp]
            self.values[key] = [value]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.ts.keys():
            return ""

        else:

            if timestamp >= self.ts[key][-1]:
                return self.values[key][-1]
            elif timestamp == self.ts[key][0]:
                return self.values[key][0]
            elif timestamp < self.ts[key][0]:
                return ""

            return self.values[key][bisect.bisect(self.ts[key], timestamp)-1]
