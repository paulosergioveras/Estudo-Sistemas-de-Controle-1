import math
import matplotlib.pyplot as plt
from scipy import signal


class SistemaSegundaOrdem():
    def __init__ (self, a=None, b=None, zeta=None, wn=None):
        if a != None and b != None:
            self.wn = math.sqrt(b) # frequência natural
            self.zeta = (a/2) / wn # frequência de amortecimento
        else:
            self.wn = wn
            self.zeta = zeta
    
    # Encontrar b usando frequência natural wn:
    @property
    def find_b(self):
        return (self.wn)**2
    
    # Encontrar a usando frequência de amortecimento zeta:
    @property
    def find_a(self):
        return 2*self.zeta*self.wn
    
    # Descobrir tipo de amortecimento do sistema
    @property
    def tipo_amortecimento(self):

        if self.zeta == 0:
            return "Não amortecido. Polos complexos = 0"
        elif self.zeta > 0 and self.zeta < 1:
            return "Subamortecido. Polos complexos != 0"
        elif self.zeta == 1:
            return "Criticamente Amortecido. Polos reais iguais."
        else:
            return "Superamortecido. Polos reais diferentes."
    
    def plot_resposta_ao_degrau(self):
        """Gera o gráfico da resposta ao degrau unitário."""
        
        # Define os coeficientes da Função de Transferência: G(s) = num/den
        num = [self.wn**2]
        den = [1, 2 * self.zeta * self.wn, self.wn**2]
        
        sys = signal.TransferFunction(num, den)
        
        # Calcula a resposta ao degrau
        t, y = signal.step(sys)
        
        # Criação do gráfico
        plt.figure(figsize=(8, 5))
        plt.plot(t, y, label=f'zeta={self.zeta:.2f}', color='darkblue', linewidth=2)
        plt.axhline(1, color='red', linestyle='--', label='Set-point (1.0)')
        
        plt.title(f'Resposta ao Degrau - Sistema {self.tipo_amortecimento}')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Amplitude')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()

    def __str__(self):
        # Calculando os componentes da função de transferência
        num = self.wn**2
        den_s1 = 2 * self.zeta * self.wn  # Coeficiente de S
        den_s0 = self.wn**2               # Termo constante
        
        # Formatação da string G(S)
        return (f"G(S) = {num:.2f} / (S^2 + {den_s1:.2f}*S + {den_s0:.2f})\n"
                f"Classificação: {self.tipo_amortecimento}")
    
sistema = SistemaSegundaOrdem(zeta=0, wn=3)
print(sistema)
sistema.plot_resposta_ao_degrau()
