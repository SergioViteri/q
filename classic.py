#!/usr/bin/env python3
# coding: utf-8

import sys, os
import random

def sum (faces, quantity):
	res = 0
	for i in range(quantity):
		res += random.randint(1, faces)

	return res

def estimate():
	count = {14: 0, 15:0, 4: 0, 24: 0}
	prob = {14: 0, 15:0, 4: 0, 24: 0}
	for i in range(0, 1000000000):
		res = sum(6, 4)
		if res in count:
			count[res] += 1
			prob[res] = 100*count[res]/i

		if (i % 10000000) == 0:
			print(i, count, prob)

	print (count, prob)

def exact():
	count = {}
	prob = {}
	for num in range (4, 25):
		count[num] = 0

	total = 0
	for d1 in range(1, 7):
		for d2 in range(1, 7):
			for d3 in range(1, 7):
				for d4 in range(1, 7):
					total += 1
					num = d1+d2+d3+d4
					count[num] += 1

	for num in range (4, 25):
		prob[num] = round(100*count[num]/total, 4)
	print(count, prob, total)


exact()