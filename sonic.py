# MARTINEZ_ERICK
import retro
import pygame
import json
import os.path as path
import random
from pygame.locals import *

largo = 1000 
num = 100 
pressure = 50 
mutation_chance = 0.3 
valor_estatico = 0

def individual(min,max):
    #["B", "A", "MODE", "START", "UP", "DOWN", "LEFT", "RIGHT", "C", "Y", "X", "Z"]
    #return[random.randint(min,max) for i in range(largo)]
    return (random.randint(min,max), valor_estatico, valor_estatico, valor_estatico, valor_estatico, valor_estatico, random.randint(min,max), random.randint(min,max), valor_estatico, valor_estatico, valor_estatico, valor_estatico)


def create_poblation():

    poblacion = []
    for i in range(num):
        individuo = dict()
        individuo['movimientos'] = []
        individuo['fitness'] = 0
        for j in range(largo):
            individuo['movimientos'].append(individual(0,1))
        poblacion.append(individuo)
    return poblacion

def calcularFitness(dist):
    fitness=0
    for i in range(len(individual)):
        fitness = 0
        for i in range(len(individual)):
            if dist == model and model <= 3253:
                model += random.randint(0,50)
                fitness += 1
                print ("fitness")
    return fitness

def selection_and_reproduction(population):
    puntuados = [ [i['fitness'], i] for i in population]
    puntuados = [i[1] for i in sorted(puntuados)]
    population = puntuados


    selected =  puntuados[(len(puntuados)-pressure):]
    #print ("selected")

    for i in range(len(population)-pressure):
        punto = random.randint(1,largo-1)
        padre = random.sample(selected, 2)
        population[i]['movimientos'][:punto] = padre[0]['movimientos'][:punto]
        population[i]['movimientos'][punto:] = padre[1]['movimientos'][punto:]
    print ("nueva poblacion")
    print (len(population))
    return population

def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(1,largo-1)



            population[i]['movimientos'][punto] = individual(0,1)

    return population



def evaluar_poblacion(env, poblacion):

    for individuo in poblacion:

        for action in individuo['movimientos']:
            env.render()
            video_size = env.observation_space.shape[1], env.observation_space.shape[0]
            screen = pygame.display.set_mode(video_size)
            _obs, _rew, done, _info = env.step(action)
            if _info['lives'] < vidas:
                continue
            if done:
                break
            individuo['fitness'] = _info['x']
        print (individuo['fitness'])
    return poblacion


env = retro.make(game='SonicTheHedgehog-Genesis', state='GreenHillZone.Act2')
fitness = 0
poblacion = create_poblation()
vidas = 3


for i in range (1000):
    _obs = env.reset()
    poblacion = evaluar_poblacion(env, poblacion)
    poblacion = selection_and_reproduction(poblacion)
    poblacion= mutation(poblacion)
