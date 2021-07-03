import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros
def main(numero_de_tiros,numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    
    probabilidad_tiros_con_1 = tiros_con_1/numero_de_intentos

    return probabilidad_tiros_con_1
    #print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_sin_1}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    dado_1 = main(numero_de_tiros,numero_de_intentos)
    dado_2 = main(numero_de_tiros,numero_de_intentos)

    probabilidad_en_dos_dados = dado_1 * dado_2
    print(f'La probabilidad de obtener por lo menos un 1 en dos dados al hacer  {numero_de_tiros} tiros = {probabilidad_en_dos_dados}')