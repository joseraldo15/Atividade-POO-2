from datetime import datetime

lista_candidatos = []
votos_nulos = 0


class Candidato:

    def __init__(self, nome, partido, numero):
        self.__nome = nome
        self.__partido = partido
        self.__numero = numero
        self.votos = []

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_numero(self):
        return self.__numero

    @property
    def get_votos(self):
        return len(self.votos)


class Eleitor:

    def __init__(self, nome, cpf):
        self.__cpf = cpf

    @property
    def get_cpf(self):
        return self.__cpf

    def votar(self, numero_candidato=0):
        if numero_candidato != 0:
            for x in lista_candidatos:
                if x.get_numero == numero_candidato:
                    if self.get_cpf not in x.votos:
                        x.votos.append({'eleitor': self.__cpf, 'horario': datetime.now().strftime("%H:%M:%S")})
                    else:
                        print('Você já votou nesse candidato.')
                        break
        else:
            global votos_nulos
            votos_nulos += 1


c1 = Candidato('Zeraldo', 'PT', 123)
lista_candidatos.append(c1)

c2 = Candidato('Gustavo', 'PSDB', 321)
lista_candidatos.append(c2)

c3 = Candidato('Joao Vitor', 'PSOL', 423)
lista_candidatos.append(c3)

e1 = Eleitor('Zezin', 12345667890)
e2 = Eleitor('Zezao', 12345667895)
e3 = Eleitor('Zefinha', 67854312609)

e1.votar(c1.get_numero)
e2.votar(c2.get_numero)
e3.votar()

for x in lista_candidatos:
    print(f'{x.get_nome} conseguiu {x.get_votos} votos, {x.votos}')
print(f'Houveram {votos_nulos} votos nulos')
