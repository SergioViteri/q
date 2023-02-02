#!/usr/bin/env python3
# coding: utf-8

import sys, os
import csv

def equals (dice):
	"""Busca parejas, tríos y críticos. Devuelve el total de éxitos."""
	dice.sort()

	pairs = 0
	trios = 0
	idx = 0	
	watched = []
	for value in dice:
		j = 0
		equals = 0
		for j in range(idx+1, len(dice)):
			compareTo = dice[j]
			if j not in watched:
				if value == compareTo:
					watched.append(j)
					equals += 1
					if equals == 1:
						pairs += 1
					if equals == 2:
						trios += 1 
					if equals == 3:
						return 5 # ¡¡¡ crítico !!!
				
			j += 1
		idx += 1

	#print(f"pairs: {pairs}; trios: {trios}")
	return pairs + trios

def sequences (dice):
	"""Busca secuencias. Devuelve el total de éxitos."""
	dice.sort()
	hits = 0

	watched = []
	idx = 0
	for value in dice:
		sequenceLength = 0
		for j in range(idx, len(dice)-1):
			jp = j+1
			if (dice[idx]+sequenceLength+1 == dice[jp]):
				if jp not in watched:
					watched.append(jp)
					sequenceLength += 1
					if sequenceLength >= 2:
						hits += 1
			elif dice[idx]+sequenceLength == dice[jp]:
				pass
			else:
				break
		idx += 1

	return hits

def hits(dice):
	return equals(dice) + sequences(dice)

def calc():
	totals = {}
	hitCount = {}
	hitProb = {}
	for diceNumber in range(2,9):
		totals[diceNumber] = 0
		hitCount[diceNumber] = {}
		hitProb[diceNumber] = {}
		for hitIdx in range(0,9):
			hitCount[diceNumber][hitIdx] = 0

	for dice1 in range(1, 7):
		for dice2 in range(1, 7):
			totals[2] += 1
			numberOfHits = hits([dice1, dice2])
			hitCount[2][numberOfHits] += 1
			for dice3 in range(1, 7):
				totals[3] += 1
				numberOfHits = hits([dice1, dice2, dice3])
				hitCount[3][numberOfHits] += 1
				for dice4 in range(1, 7):
					totals[4] += 1
					numberOfHits = hits([dice1, dice2, dice3, dice4])
					hitCount[4][numberOfHits] += 1
					for dice5 in range(1, 7):
						totals[5] += 1
						numberOfHits = hits([dice1, dice2, dice3, dice4, dice5])
						hitCount[5][numberOfHits] += 1
						for dice6 in range(1, 7):
							totals[6] += 1
							numberOfHits = hits([dice1, dice2, dice3, dice4, dice5, dice6])
							hitCount[6][numberOfHits] += 1
							for dice7 in range(1, 7):
								totals[7] += 1
								numberOfHits = hits([dice1, dice2, dice3, dice4, dice5, dice6, dice7])
								hitCount[7][numberOfHits] += 1
								for dice8 in range(1, 7):
									totals[8] += 1
									numberOfHits = hits([dice1, dice2, dice3, dice4, dice5, dice6, dice7, dice8])
									hitCount[8][numberOfHits] += 1


	for diceNumber in range(2, 9):
		for hit in hitCount[diceNumber]:
			hitProb[diceNumber][hit] = hitCount[diceNumber][hit] / totals[diceNumber]

	return hitProb

try:
	fileName = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <file_name>")

data = calc()

with open(fileName, 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow([
		'N. de dados',
		'0 éxitos', 
		'1 éxito',
		'2 éxitos', 
		'3 éxitos', 
		'4 éxitos', 
		'5 éxitos', 
		'6 éxitos', 
		'7 éxitos', 
		'8 éxitos'
	])
	for diceNumber in data:
		writer.writerow([
			diceNumber, 
			data[diceNumber][0], 
			data[diceNumber][1], 
			data[diceNumber][2], 
			data[diceNumber][3], 
			data[diceNumber][4], 
			data[diceNumber][5], 
			data[diceNumber][6], 
			data[diceNumber][7], 
			data[diceNumber][8]
		])


