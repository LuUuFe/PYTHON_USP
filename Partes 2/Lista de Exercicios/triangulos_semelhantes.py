class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def semelhantes(self,triangulo):
        t1 = []
        t2 = []
        t1.append(triangulo.a), t1.append(triangulo.b), t1.append(triangulo.c)
        t2.append(self.a), t2.append(self.b), t2.append(self.c)
        razao = 0
        i = 0
        while i < len(t1):
            if t1[i] / t2[i] == razao or razao == 0:
                razao = t1[i] / t2[i]
                i += 1
            else:
                return False
        return True
            
