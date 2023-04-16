class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def retangulo(self):
        triangulo = []
        triangulo.append(self.a), triangulo.append(self.b), triangulo.append(self.c)
        hipotenusa = 0
        for lado in triangulo:
            if lado > hipotenusa or hipotenusa == 0:
                hipotenusa = lado
        triangulo.remove(hipotenusa)
        if triangulo[0]**2 + triangulo[1]**2 == hipotenusa**2:
            return True
        else:
            return False
        
            
            
