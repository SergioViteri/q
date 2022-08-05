#!/usr/bin/env python3
# coding: utf-8

import sys, os
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

SHOTS=10
FACES=6

#
# Creación del cricuito
#
circuit = QuantumCircuit(5, 5)
circuit.h(0) # Puerta lógica cuántica H 
circuit.h(1) # Puerta lógica cuántica H 
circuit.h(2) # Puerta lógica cuántica H 
circuit.h(3) # Puerta lógica cuántica H 
circuit.h(4) # Puerta lógica cuántica H 
circuit.barrier()
circuit.barrier()
circuit.measure(0, 0)
circuit.measure(1, 1)
circuit.measure(2, 2)
circuit.measure(3, 3)
circuit.measure(4, 4)
circuit.draw(output = 'mpl').savefig(os.path.join(os.path.dirname(__file__), 'img', 'dice.jpg'))

#
# Ejecuta el circuito en el simulador y muestra los resultados
#
sim = Aer.get_backend('aer_simulator') 
result = sim.run(circuit, shots=SHOTS).result()
counts = result.get_counts()
print(counts)

#
# Interpreta el resultado
#
dice = {}
for x in range(FACES):
    dice[x+1] = 0
for bits in counts:
	result =  int(bits, 2) # convierte el binario a número decimal
	normalizedResult = int(result * FACES/32) # Normalizar el resultado al número de caras. 32 es el número de combinaciones posibles con 5 bits
	normalizedResult += 1 #Suma 1 al resultado (los dados no empiezan en 0)
	dice[normalizedResult] += counts[bits]
print (dice)



