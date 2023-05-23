class Deportista:
    def __init__(self, años_practicando):
        self._deporte = "Futbol"
        self._años_practicando = años_practicando

    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._años_practicando
    
    def setAñosPracticando(self, años_practicando):
        self._años_practicando = años_practicando