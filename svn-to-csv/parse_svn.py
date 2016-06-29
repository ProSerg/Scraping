#!/usr/bin/env python3

import sys
import argparse
import re
import csv

infile = "null"
outfile = "null"
indata = "nothing"
outdata = "nothing"

def HandlerArgs():
	parser = argparse.ArgumentParser(description="The program for \
	parsing information from `svn status`  ", )
	parser.add_argument('-f', '--file', nargs='?', type=argparse.FileType('r'), default=sys.stdin )
	parser.add_argument('-o', '--out', nargs='?', type=argparse.FileType('w'), default="data.cvs" )
	options = parser.parse_args()
	return options
	
def HandlerOpts(options):
	global infile
	global outfile
	infile = options.file
	outfile = options.out
	
def ReadFile():	
	if infile:
		indata = infile.read()
	return indata
	
def Parsing(indata):
	outdata = indata
	count = 1
	rows=[] 
	p = re.compile('(.*)\s+([\d\-]+)\s+(\d+)\s+(\w+)\s+([\w\\\.\_\-\=\+\-]*)')
	for line in indata.split("\n"):
		line = re.sub(r'\s+', ' ', line)
		matchs = p.match(line)
		if matchs:
#			array.append(match.group(1))
#			print( " {0} => {1} ".format(count, line) )
#			print("Flags:  |" + matchs.group(1))
#			print("ID1:  |" + matchs.group(2))
#			print("ID2:  |" + matchs.group(3))
#			print("author: |" + matchs.group(4))
#			print("file:  |" + matchs.group(5))
#			print()
			rows.append({
            'flags': matchs.group(1),
            'ID1': matchs.group(2),
            'ID2': matchs.group(3),
            'author': matchs.group(4),
            'file': matchs.group(5)
			})
			count = count + 1
		else:	
			print( "!!!ignor: " + line)
			print()
	return rows
	

def WriteFile(outdata):
	writer = csv.writer(outfile)
	writer.writerow(('Flags', 'ID1', 'ID2', 'author', 'file' ))
	writer.writerows(
		( row['flags'], row['ID1'], row['ID2'], row['author'], row['file'] ) for row in outdata
	)

def main():
	options = HandlerArgs()
	HandlerOpts(options)
	indata = ReadFile()
	outdata = Parsing(indata)
	WriteFile(outdata)
	
if  __name__ == "__main__":
	main()

