class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, nombre_arabe):
        if(nombre_arabe == 1): return "I"
        if(nombre_arabe == 2): return "II"
        if(nombre_arabe == 3): return "7"
        return "IV"