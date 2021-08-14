#Quiz #2 IA
#Elaborado por
#Leiwis Contreras 1028020195 Grupo 1
#Ibio Escobar Gomez 1038816379 Grupo 3
#Luis Carmona Grupo 3


#implementacion de librerias
import random
import string

cadena = "Ingeniería informática, inteligencia artificial"  # cadena estipulada para el codigo del quiz#2
modelo=[] #para el calculo del material genetico
num = 10  # La cantidad de individuos que habra en la poblacion
pressure = 3  # Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
mutation_chance = 0.2  # La probabilidad de que un individuo mute

#Ciclo para la muestra del modelo a seguir
for i in range(len(cadena)):
    modelo.append(cadena[i])
print("\n\nModelo: %s\n" % (modelo)," \n")  # Mostrar el modelo, con un poco de espaciado

def individual():
    """
        Crea un individual
    """
 #Permite el uso de tildes
    return [random.choice(string.ascii_letters + " áéíóúÁÉÍÓÚ") for i in range(len(cadena))]


def crearPoblacion():
    """
        Crea una poblacion nueva de individuos
    """
    return [individual() for i in range(num)]


def calcularFitness(individual):
    """
        Calcula el fitness de un individuo concreto.
    """
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1

    return fitness


def selection_and_reproduction(population):
    """
        Evala todos los elementos de la poblacion (population) y se queda con los mejores
        guardandolos dentro de 'selected'.
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).

        Por ultimo muta a los individuos.

    """
    puntuados = [(calcularFitness(i), i) for i in
                 population]  # Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
    puntuados = [i[1] for i in sorted(puntuados)]  # Ordena los pares ordenados y se queda solo con el array de valores
    population = puntuados

    selected = puntuados[(len(
        puntuados) - pressure):]  # Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'

    # Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population) - pressure):
        punto = random.randint(1, len(cadena) - 1)  # Se elige un punto para hacer el intercambio
        padre = random.sample(selected, 2)  # Se eligen dos padres

        population[i][:punto] = padre[0][:punto]  # Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][punto:] = padre[1][punto:]

    return population  # El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven


def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(population) - pressure):
        if random.random() <= mutation_chance:  # Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0, len(cadena) - 1)  # Se elgie un punto al azar
            nuevo_valor = random.choice(string.ascii_letters + " áéíóúÁÉÍÓÚ")  # y un nuevo valor para este punto

            # Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.choice(string.ascii_letters + " áéíóúÁÉÍÓÚ")

            # Se aplica la mutacion
            population[i][punto] = nuevo_valor

    return population


population = crearPoblacion()  # Inicializar una poblacion
print("Poblacion Inicial:\n%s" % (population))  # Se muestra la poblacion inicial
for i in range(600):
    population = selection_and_reproduction(population)
    population = mutation(population)

print("\nPoblacion Final:\n%s" % (population))  # Se muestra la poblacion evolucionada
print("\n\n")
