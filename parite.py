#! /usr/bin/env python3
# coding: utf-8

import argparse
# import pdb; pdb.set_trace()

import analysis.csv as c_an
import analysis.xml as x_an

def parse_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML ?""")
	return parser.parse_args()

def main():
	args = parse_argument()
	
	if args.extension == 'csv':
		c_an.launch_analysis('nosdeputes.csv')
	elif args.extension == 'xml':
		x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
	main()