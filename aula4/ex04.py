class Sensor:
    def __init__(self, temperatura_inicial):
        self.__temperatura = 0
        self.set_temperatura(temperatura_inicial)

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        if -50 <= temperatura <= 150:
            self.__temperatura = temperatura
        else:
            print(f"Erro: Temperatura {temperatura}°C fora do limite físico do sensor (-50°C a 150°C).")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

if __name__ == "__main__":
    sensor = Sensor(25)
    temperaturas_teste = [12, 67, 80, -60]
    
    print("--- Testando o Sensor ---")
    for temp in temperaturas_teste:
        sensor.set_temperatura(temp)
        print(f"Temperatura Atual: {sensor.get_temperatura()}°C | Status: {sensor.status()}")
        print("-" * 30)
