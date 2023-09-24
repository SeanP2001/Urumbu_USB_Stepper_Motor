# test.py
#
# Fab KiCad library integrity test script
#
# Created by Krisjanis Rijnieks 1 May 2020
# (c) Krisjanis Rijnieks 2020
#
# This work may be reproduced, modified, distributed,
# performed, and displayed for any purpose, but must
# acknowledge this project. Copyright is retained and
# must be preserved. The work is provided as is; no
# warranty is provided, and users accept all liability.

import os.path
from os import path
import mmap

libraryName = 'fab'
errorCount = 0

def errorOnLine(lineNum, message):
	global errorCount
	errorCount = errorCount + 1
	print('\033[1;31;40mERROR LINE', str(lineNum) + ':\033[0;37;40m', message)

def error(message):
	global errorCount
	errorCount = errorCount + 1
	print('\033[1;31;40mERROR:\033[0;37;40m', message)

def checkPartName(partDEFName, partF1Name):
	if partF1Name != partDEFName:
		errorOnLine(lineNum, 'Part DEF name and F1 name do not match')

def checkFootprint(lineNum, footprintField):
	if footprintField == '':
		return

	parts = footprintField.split(':')

	if parts[0] != libraryName:
		errorOnLine(lineNum, 'Footprint library name is wrong')

	if len(parts) > 1:
		footprintPath = libraryName + '.pretty/' + parts[1] + '.kicad_mod'
		footFileExists = path.exists(footprintPath)
		if footFileExists != True:
			errorOnLine(lineNum, 'Footprint file does not exist: ' + footprintPath)

def checkDescription(symbolName):
	with open(libraryName + '.dcm', 'r') as file, \
		mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
		if s.find(symbolName.encode('utf8')) != -1:
			return True
		f.close()
	errorOnLine(lineNum, 'Part description not found in .dcm file:' + symbolName)

# Read the library file
with open(libraryName + '.lib', 'r') as f:
	lines = f.readlines()
	f.close()

if len(lines) == 0:
	print('Failed to read contents of library file')
	exit(1)

lineNum = 0
for l in lines:
	lineNum += 1
	line = l.strip()
	words = line.split()
	if words[0] == 'DEF':
		partDefName = words[1]
		checkDescription(partDefName)
	if words[0] == 'F1':
		checkPartName(partDefName, words[1].strip('"'))
	if words[0] == 'F2':
		checkFootprint(lineNum, words[1].strip('"'))

def checkSymbolMapping(footprintName):
	with open(libraryName + '.lib', 'r') as f, \
		mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
		if s.find(footprintName.encode('utf8')) != -1:
			return True
		f.close()
	error('Symbol mapping not found for footprint ' + footprintName)

# Read all footprints in *.pretty directory
files = os.listdir(libraryName + '.pretty')
for f in files:
	footprintName = f.replace('.kicad_mod', '')
	checkSymbolMapping(footprintName)

if errorCount > 0:
	print('TOTAL ERRORS in ' + libraryName + '.lib:', errorCount)
	exit(1)

print(libraryName + '.lib is \033[1;32;40mOK!')

exit(0)
