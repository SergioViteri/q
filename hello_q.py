#!/usr/bin/env python3
# coding: utf-8

import sys, os
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

#
# Creación del cricuito
#
circuit = QuantumCircuit(1, 1)
circuit.barrier()
circuit.barrier()
circuit.measure(0, 0)

#
# Guarda la imagen del esquema en el disco
#
circuit.draw(output = 'mpl').savefig(os.path.join(os.path.dirname(__file__), 'img', 'hello_q.jpg'))

#
# Ejecuta el circuito en el simulador y muestra los resultados
#
sim = Aer.get_backend('aer_simulator') 
result = sim.run(circuit).result()
counts = result.get_counts()
print(counts)


