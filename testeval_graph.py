import matplotlib.pyplot as plt
import time
import random
from PIL import Image

import collections

#15, 9, 21, 11, 8, 15, 21, 18, 3, 7, 17, 21, 16, 22, 16, 6, 7, 2, 6, 22
wrong_cha = input("Please enter the chapter or section you got wrong for every \nquestion you got wrong in the form of a list without the brackets.\nMake sure to have a comma and a space after it Ex: 1, 1, 4, 8, 8 Not: 1,1,3,8,8. --> ").split(', ')
title = input('What do you want the title of the graph to be? ')
while True:
	save = input('Do you want to save the graph as a file (to desktop)? (y or n) lowercase: ')
	if(save == 'y' or save == 'n'):
		break
	else:
		print('Error, please say y (lowercase y) for yes and n (lowercase n) for no.')
if save == 'y':
	file_name = input('What do you want to name the file? ')
while True:
	colorful = input('Do you want the graph to be colorful? (y or n) lowercase: ')
	if(colorful == 'y' or colorful == 'n'):
		break
	else:
		print('Error, please say y (lowercase y) for yes and n (lowercase n) for no.')
wrong_chap = list(map(lambda x: int(x), wrong_cha))
wrong_chap.sort()
graph = collections.Counter(wrong_chap)
a = {}
for i in dict(graph).items():
    a[f'Ch {i[0]}'] = i[1]
plt.xlabel('Chapter')
plt.ylabel('Frequency (# Wrong)')
plt.title(title)
if (colorful=='y'):
	plt.bar(a.keys(), a.values(), .5, color=['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'purple', 'mediumturquoise'])
else:
	plt.bar(a.keys(), a.values(), .5)
plt.xticks(rotation=45)

'''
Trying to add number on top of bar to represent value... Not done yet.

for value, index in enumerate(a.values()):
    plt.text(value, index, str(value))
'''

plt.tight_layout()
if save == 'y':
	plt.savefig(f'/Users/satyapandya/Desktop/{file_name}.png')
plt.show()

	
