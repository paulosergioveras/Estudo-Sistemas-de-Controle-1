import math

class SegundaClasseSubamortecido:
    def __init__(self, wn, zeta=None, up_percentual=None):
        """
        Inicializa o sistema subamortecido. 
        Você deve fornecer a frequência natural (wn) e UMA das duas opções:
        zeta ou up_percentual (%UP).
        """

        self.wn = wn
        
        if zeta is not None:
            if not (0 < zeta < 1):
                raise ValueError("Para um sistema subamortecido, o zeta deve estar entre 0 e 1.")
            self.zeta = zeta
        elif up_percentual is not None:
            self.zeta = self.calcular_zeta_por_up(up_percentual)
        else:
            raise ValueError("Você deve fornecer o 'zeta' ou o 'up_percentual'.")

    @staticmethod
    def calcular_zeta_por_up(up_percentual):
        """Calcula o Zeta a partir da Ultrapassagem Percentual (%UP)"""

        up_frac = up_percentual / 100
        ln_up = math.log(up_frac)
        
        numerador = -ln_up
        denominador = math.sqrt(math.pi**2 + ln_up**2)
        return numerador / denominador

    def instante_de_pico(self):
        """Calcula o Instante de Pico (Tp)"""

        return math.pi / (self.wn * math.sqrt(1 - self.zeta**2))

    def ultrapassagem_percentual(self):
        """Calcula a Ultrapassagem Percentual (%UP)"""

        expoente = -(self.zeta * math.pi) / math.sqrt(1 - self.zeta**2)
        return math.exp(expoente) * 100

    def tempo_de_acomodacao(self):
        """Calcula o Tempo de Acomodação (Ts) para o critério de 2%"""

        return 4 / (self.zeta * self.wn)

    def __str__(self):
        """Exibe um resumo completo do sistema"""
        
        return (
            f"=== Sistema Subamortecido ===\n"
            f"Parâmetros: Wn = {self.wn:.2f} rad/s, Zeta = {self.zeta:.4f}\n"
            f" - Instante de Pico (Tp): {self.instante_de_pico():.4f} s\n"
            f" - Ultrapassagem Máxima (%UP): {self.ultrapassagem_percentual():.2f} %\n"
            f" - Tempo de Acomodação (Ts 2%): {self.tempo_de_acomodacao():.4f} s\n"
            f"============================="
        )

# --- Exemplo de Uso ---

# Exemplo 1: Criando a partir de Wn e Zeta
print("Exemplo 1: Fornecendo Zeta")
sys1 = SegundaClasseSubamortecido(wn=10, zeta=0.5)
print(sys1)

print("\n" + "-"*30 + "\n")

# Exemplo 2: Criando a partir de Wn e %UP (Ultrapassagem Percentual)
# Isso é muito útil em projetos onde o professor diz: "Projete um sistema com no máximo 16% de overshoot"
print("Exemplo 2: Fornecendo Ultrapassagem Percentual (%UP)")
sys2 = SegundaClasseSubamortecido(wn=5, up_percentual=16.3) # Um %UP de ~16.3% equivale a um zeta de ~0.5
print(sys2)
