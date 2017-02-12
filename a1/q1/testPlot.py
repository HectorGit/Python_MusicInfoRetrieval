#import mir.py
import numpy as np
import wave
import os
import struct
import matplotlib.pyplot as plt


class Task1():

	#@staticmethod
	def plotMyGraph(arr1,arr2):
		plt.title('Graph title');
		plt.ylabel('this_is_ylabel');
		plt.xlabel('this_is_xlabel');
		plt.plot(arr1,arr2);
		plt.show();
		

	def main():
	
		#arr1 = np.arange(0,1000,1,np.int); #x's
		arr1 = np.linspace(0,249,249); #x's
		print arr1.shape;
		
		arr2 = np.random.random_integers(-10,10,249); #y's
		print arr2.shape;
		
		#plt.title('Graph title');
		#plt.ylabel('this_is_ylabel');
		#plt.xlabel('this_is_xlabel');
		#plt.plot(arr1,arr2);
		#plt.show();
		#task = self.Task1();
		plotMyGraph(arr1,arr2);
		
		return 0;

	if __name__ == "__main__": main()