import csv
import mir_eval
import numpy as np

def getTimesFromCsv(filename):
	
	mode = 'r';
	output = [];

	with open(filename, mode) as f:
		reader = csv.DictReader(f);
		for row in reader:
			output.append([float(row['startTime']), float(row['endTime'])]);
			
	return output;
	
def getF_Measure(reference,estimated):
	p,r,f_measure = mir_eval.segment.detection(reference,estimated);
	return f_measure;