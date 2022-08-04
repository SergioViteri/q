#!/usr/bin/env python3
# coding: utf-8

import sys, os
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram


circuit = QuantumCircuit(1, 1)

circuit.barrier()

#ops

circuit.barrier()

circuit.measure(0, 0)

circuit.draw(output = 'mpl').savefig(os.path.join(os.path.dirname(__file__), 'img', 'hello_q.jpg'))


sim = Aer.get_backend('aer_simulator') 
result = sim.run(circuit).result()
counts = result.get_counts()
print(counts)


