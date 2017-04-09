import auxFunctions
import numpy as np
import mir_eval
import csv

timesSegmentinoGloria = np.array(auxFunctions.getTimesFromCsv('segmentino_gloria.csv'));
timesSegmentinoTurca = np.array(auxFunctions.getTimesFromCsv('segmentino_turca.csv'));
timesSegmenterGloria = np.array(auxFunctions.getTimesFromCsv('segmenter_gloria.csv'));
timesSegmenterTurca = np.array(auxFunctions.getTimesFromCsv('segmenter_turca.csv'));
timesHectorGloria = np.array(auxFunctions.getTimesFromCsv('hector_gloria.csv'));
timesHectorTurca = np.array(auxFunctions.getTimesFromCsv('hector_turca.csv'));

print "-----No.1 - Gloria in Excelsis Deo -----------------------------------------------"

f_measureSegmentinoGloria = auxFunctions.getF_Measure(timesHectorGloria,timesSegmentinoGloria);
print("f_measure for Segmentino: %f" % f_measureSegmentinoGloria);

f_measureSegmenterGloria = auxFunctions.getF_Measure(timesHectorGloria,timesSegmenterGloria);
print("f_measure for Segmenter : %f" % f_measureSegmenterGloria);

print "------No.2 - Rondo Alla Turca------------------------------------------------------"

f_measureSegmentinoTurca = auxFunctions.getF_Measure(timesHectorTurca,timesSegmentinoTurca);
print("f_measure for Segmentino: %f" % f_measureSegmentinoTurca);

f_measureSegmenterTurca = auxFunctions.getF_Measure(timesHectorTurca,timesSegmenterTurca);
print("f_measure for Segmenter: %f" % f_measureSegmenterTurca);


