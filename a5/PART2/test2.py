import mir_eval
import auxFunctions

segmentino_gloria = mir_eval.io.load_intervals('segmentino_gloria_2.csv', delimiter=',');
segmenter_gloria = mir_eval.io.load_intervals('segmenter_gloria_2.csv', delimiter=',');
segmentino_turca = mir_eval.io.load_intervals('segmentino_turca_2.csv', delimiter=',');
segmenter_turca = mir_eval.io.load_intervals('segmenter_turca_2.csv', delimiter=',');
hector_gloria = mir_eval.io.load_intervals('hector_gloria_2.csv', delimiter=',');
hector_turca = mir_eval.io.load_intervals('hector_turca_2.csv', delimiter=',');

print "-----No.1 - Gloria in Excelsis Deo -----------------------------------------------"

f_measureSegmentinoGloria = auxFunctions.getF_Measure(hector_gloria,segmentino_gloria);
print("f_measure for Segmentino: %f" % f_measureSegmentinoGloria);

f_measureSegmenterGloria = auxFunctions.getF_Measure(hector_gloria,segmenter_gloria);
print("f_measure for Segmenter : %f" % f_measureSegmenterGloria);

print "------No.2 - Rondo Alla Turca------------------------------------------------------"

f_measureSegmentinoTurca = auxFunctions.getF_Measure(hector_turca,segmentino_turca);
print("f_measure for Segmentino: %f" % f_measureSegmentinoTurca);

f_measureSegmenterTurca = auxFunctions.getF_Measure(hector_turca,segmenter_turca);
print("f_measure for Segmenter: %f" % f_measureSegmenterTurca);