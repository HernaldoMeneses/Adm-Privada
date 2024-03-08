'''
Mundo
    Sociedade-Institucionalizadas
        Organizações
            Produções
                Bens(produtos)
                Serviçoes
                    Planejadas
                    Coordenadas
                    Dirigidas
                        Recursos
                            Humanos (Pessoas)
                            Não Humanos
                                Físicos
                                Materias
                                Financeiros
                                Tecnológicos

'''

'''
    A Vida das pessoas depende intimamente das Organizações
    E as Organizações dependem das pessoas
'''

'''
    As Organizações são extremamente heterogêneas e diversificadas
        Tamanhos
        Características
        Estruturas
        Objetivos
            Finalidades
                Lucrativas (Empresas)
                Não Lucrativas
                    Exército
                    Igreja
                    Serviçoes Públicos
                    Entidades Filantrópicas
                    ONGS - Não Governamentais
'''

TO = 'Teoria Geral das Organizações'
class Topico:
    def __init__(self, tema, tese, solution, brain_storm, frases):
        self.tema = tema
        self.tese = tese
        self.solution = solution
        self.brain_storm = brain_storm
        self.frases = frases

    def definir_tema(self, new_tema):
        self.tema = new_tema

    def definir_tese(self, new_tese):
        self.tese = new_tese
    
    def definir_solution(self, new_solution):
        self.solution = new_solution
    
    def definir_brain_srotm(self, new_brain_srotm):
        self.brain_storm = new_brain_srotm

    def definir_brain_srotm(self, new_frases):
        self.frases = new_frases

    def imprimir_informacoes(self):
        print(f"Tema: {self.tema}, \n Tese: {self.tese}")
        print(f"Solution: {self.solution}")
        print(f"Brain_Storm: {self.brain_storm}")
        print(f"Frases: {self.frases}")
        cout =1
        for i in (self.frases):
            print(f"Frase: {cout} {i}")
            cout = cout +1

# Exemplo de uso da classe
tema_ = 'Tema - '
tese_ = 'Tese - '
solution_ = 'Solution - '
brain_storm_ = ['Word1','Word2']
frases_ = ['frase1','frase2']
topic1 = Topico(
    tema=tema_, 
    tese=tese_, 
    solution=solution_, 
    brain_storm=brain_storm_,
    frases=frases_)
topic1.imprimir_informacoes()


#pg.30/650
#file:///L:/Linear_/Base-Jump_08/ADMINISTRA%C3%87%C3%83O%20-%20Idalberto%20Chiavenato%20-%20Introdu%C3%A7%C3%A3o%20A%20Teoria%20Geral%20Da%20Administra%C3%A7%C3%A3o.pdf