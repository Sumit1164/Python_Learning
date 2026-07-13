class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    def __sub__(self, other):
        return self.n -other.n
    

n = Number(10)
m = Number(2)

print(n+m)
print(n-m)