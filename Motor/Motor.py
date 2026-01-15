import RandomM

MotorID = RandomM.id
Tipo = RandomM.tipo
Estado = RandomM.estado

class Motor:
    def __init__(self,MotorID,Tipo,Estado):
        self.MotorID = MotorID 
        self.Tipo = Tipo
        self.Estado = Estado
    
    def __caracteristicasderendimiento__(self, Potencia, Torque, Velocidad, Eficiencia, Respuesta, Durabilidad):
        self.Potencia = Potencia
        self.Torque = Torque
        self.Velocidad = Velocidad
        self.Eficiencia = Eficiencia
        self.Respuesta = Respuesta
        self.Durabilidad = Durabilidad
    
    def __caracteristicaselectricas__(self, Voltaje, Corriente, Frecuencia):
        self.Voltaje = Voltaje
        self.Corriente = Corriente
        self.Frecuencia = Frecuencia

print("Motor ID:", MotorID, "Tipo:", Tipo, "Estado:", Estado)

