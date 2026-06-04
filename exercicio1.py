class CalcularSalario:
    def __init__(self, valorHora, horasTrabalhadas, filhos):
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.filhos = filhos
        
    def calcularSalarioBruto(self):
        salarioBruto = self.horasTrabalhadas * self.valorHora
        return salarioBruto
        
    def calcularSalarioFamilia(self):
        salarioBruto = self.calcularSalarioBruto()
        
        if salarioBruto <= 788.00:
            cota = 30.50
        elif salarioBruto <= 1100.00:
            cota = 18.50
        else: 
            cota = 11.90
        salarioFamilia = cota * self.filhos
        return salarioFamilia
        
    def calcularSalarioLiquido(self):
        return self.calcularSalarioBruto() + self.calcularSalarioFamilia() 
        