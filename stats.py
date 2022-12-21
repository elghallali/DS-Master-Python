class Stats:
    def __init__(self, distribution):
        self.distribution = distribution

    def show(self):
        return self.distribution

    def moyenne(self):
        somme = 0
        for i in self.distribution:
            somme+=i
        return somme/len(self.distribution)

    def min(self):
        min = self.distribution[0]
        for i in range(1,len(self.distribution)):
            if min > self.distribution[i]:
                min = self.distribution[i]
        return min

    def max(self):
        max = self.distribution[0]
        for i in range(1,len(self.distribution)):
            if max > self.distribution[i]:
                max = self.distribution[i]
        return max


stat = Stats(distribution)