"""Un ejemplo clasico de instrospeccion con Python"""

class intro():
    def __init__(self, valor):
        self.valor = valor
        
        def segundo(self):
            print("Segundo")
            
        def tercero(self):
            print("tercero")
            
dato = intro("Valor")
print(isinstance(dato, intro))