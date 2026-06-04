class Fibonacci:
    def __init__(self, n):
        self.n = n

    def sequenciaFibonacci(self):
        sequencia = []
        a = 1
        b = 1

        for i in range(self.n):
            sequencia.append(a)
            a = b
            b = a + b

        return sequencia

    def pertenceFibonacci(self):
        a = 1
        b = 1

        while a < self.n:
            a = b
            b = a + b

        return a == self.n

