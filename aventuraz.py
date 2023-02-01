#!/usr/bin/env python3
# coding: utf-8

import sys, os
import random

def critical (dice):
	ret = 0

	idx = 0
	checked = []
	for value in dice:
		idx += 1
		if idx not in checked:
			checked.append(idx)
			j = 0
			equals = 0
			for value2 in dice:
				j += 1
				if j not in checked:
					#checked.append(j)
					#print(value, value2)
					if value == value2:
						equals += 1
						print(idx, j, equals)
						if equals == 3:
							return 5 
	return 0

def trio (dice):
	ret = 0

	idx = 0
	checked = []
	for value in dice:
		idx += 1
		if idx not in checked:
			checked.append(idx)
			j = 0
			equals = 0
			for value2 in dice:
				j += 1
				if j not in checked:
					#checked.append(j)
					#print(value, value2)
					if value == value2:
						equals += 1
						print(idx, j, equals)
						if equals == 2:
							ret += 1 
							break

	return ret

def pair (dice):
	ret = 0

	idx = 0
	checked = []
	for value in dice:
		idx += 1
		if idx not in checked:
			checked.append(idx)
			j = 0
			for value2 in dice:
				j += 1
				if j not in checked:
					#checked.append(j)
					#print(value, value2)
					if value == value2:
						checked.append(j)
						ret += 1
						break

	return ret

def sequence (dice):
	dice.sort()
	print(dice)
	ret = 0

	checked = []
	idx = 0
	for value in dice:
		sequenceLength = 0
		if idx < len(dice)-1:
			tmpChecked = []
			tmpPrev = 0
			for j in range(idx, len(dice)-1):
				jp = j+1
				if jp in checked and jp < len(dice)-1:
					jp += 1
				#print(f"{j}.{jp} j:{jp} {dice[j]+1} == {dice[jp]} {tmpPrev} and {tmpPrev+1} == {dice[jp]} sequenceLength:{sequenceLength}")
				if (not tmpPrev and dice[j]+1 == dice[jp]) or (tmpPrev and tmpPrev+1 == dice[jp]):
					if not jp in checked:
						if (jp) not in tmpChecked:
							tmpChecked.append(jp)
						sequenceLength += 1
						print(f"sequenceLength: {sequenceLength}")
						if sequenceLength >= 2:
							for item in tmpChecked:
								if item not in checked:
									checked.append(item)
							print(checked)
							ret += 1
							#break
					else:
						tmpPrev = dice[j]+1
				elif dice[j] == dice[jp]:
					#print(f"{idx+1}c")
					pass
				else:
					#print("BREAK")
					break

			#if dice[j] == value +1:
			#	print(value, dice[idx+1] )
		idx += 1

	return ret

dice = [1,7,2,3,2,6,2,3,4,5,4,5]

ret = sequence(dice)
print(ret)
