#Drift v1
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l bayes.NaiveBayes -d DDM)
-s (ConceptDriftStream -s (generators.AgrawalGenerator -i 29) -d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 2) 
-d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 3) -d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 4) 
-d (generators.AgrawalGenerator -i 29 -f 5)                                 
-p 2000 -w 1)                                 
-p 2000 -w 1)                                 
-p 2000 -w 1)                                 
-p 2000 -w 1) -i 10000 -f 1000" > results/abrupt_agraw1/bayes.NaiveBayes_DDM_10000_29_AGRAW1_Abrupt.csv

#Drift v2
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l bayes.NaiveBayes -d DDM)
-s (ConceptDriftStream -s (generators.AgrawalGenerator -i 29) -d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 2) 
-d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 3) 
-d (ConceptDriftStream -s (generators.AgrawalGenerator -i 29 -f 4) 
-d (generators.AgrawalGenerator -i 29 -f 5) 
-p 8000 -w 1)
-p 6000 -w 1)
-p 4000 -w 1)
-p 2000 -w 1) -i 10000 -f 1000" > results/abrupt_agraw1/bayes.NaiveBayes_DDM_10000_29_AGRAW1_Abrupt.csv


"EvaluatePrequential -l (drift.SingleClassifierDrift -l bayes.NaiveBayes -d ADWINChangeDetector)
-s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s 
(generators.AgrawalGenerator -f 1 -p 1.0 -i 17) -d 
(generators.AgrawalGenerator -f 2 -i 17) -p 2000 -w 1) -d 
 (generators.AgrawalGenerator -f 3 -i 17) -p 4000 -w 1) -d 
 (generators.AgrawalGenerator -f 4 -i 17) -p 6000 -w 1) -d 
 (generators.AgrawalGenerator -f 5 -i 17) -p 8000 -w 1) -e (WindowClassificationPerformanceEvaluator) -q 10 -i 10000 -f 10"


 EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l trees.HoeffdingTree) 
 -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 4) 
 -d (generators.AgrawalGenerator -f 5) -p 8000 -w 1) -d (generators.AgrawalGenerator -f 3) -p 6000 -w 1) 
 -d (generators.AgrawalGenerator -f 2) -p 4000 -w 1) -d (ConceptDriftStream -s (generators.AgrawalGenerator -f 2) 
 -d (ConceptDriftStream -s (generators.AgrawalGenerator -f 3) -d (ConceptDriftStream -d (ConceptDriftStream -s (generators.AgrawalGenerator -f 4) 
 -d (ConceptDriftStream -s (generators.AgrawalGenerator -f 5) -d generators.AgrawalGenerator))))) -p 2000 -w 1)

 java -cp "moa-release-2018.6.1/src/moa2014.jar:moa-release-2018.6.1/lib/*" -javaagent:"moa-release-2018.6.1/lib/sizeofag-1.0.0.jar" moa.DoTask "EvaluatePrequentialUFPEforDetectors -l (drift.SingleClassifierDrift -l trees.HoeffdingTree -d ADWINChangeDetector) -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 1 -p 1.0) -d (generators.AgrawalGenerator -f 2) -p 2000 -w 1) -d (generators.AgrawalGenerator -f 3) -p 4000 -w 1) -d (generators.AgrawalGenerator -f 4) -p 6000 -w 1) -d (generators.AgrawalGenerator -f 5) -p 8000 -w 1) -r 30 -c -i 10000 -f 10 -q 10 -b 40"


"EvaluatePrequential -l (drift.SingleClassifierDrift -l bayes.NaiveBayes -d DDM)                                     
-s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream 
-s (generators.LEDGeneratorDrift -d 7 -i 29) 
-d (generators.LEDGeneratorDrift -d 7 -i 29) -p 2000 -w 1) 
-d (generators.LEDGeneratorDrift -d 7 -i 29) -p 4000 -w 1) 
-d (generators.LEDGeneratorDrift -d 7 -i 29) -p 6000 -w 1) 
-d (generators.LEDGeneratorDrift -d 7 -i 29) -p 8000 -w 1) -e (WindowClassificationPerformanceEvaluator) -q 10 -i 10000 -f 10" 