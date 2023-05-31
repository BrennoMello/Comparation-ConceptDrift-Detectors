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


EvaluatePrequentialUFPEforDetectors -l (drift.SingleClassifierDrift -l
trees.HoeffdingTree -d RDDM) -s (ConceptDriftStream -s
(ConceptDriftStream -s (ConceptDriftStream -s (ConceptDriftStream -s
(generators.AgrawalGenerator -f 1 -p 1.0) -d
(generators.AgrawalGenerator -f 2) -p 2000 -w 1) -d
(generators.AgrawalGenerator -f 3) -p 4000 -w 1) -d
(generators.AgrawalGenerator -f 4) -p 6000 -w 1) -d
(generators.AgrawalGenerator -f 5) -p 8000 -w 1) -r 30 -c -i 10000 -f 10 -q 10 -b 40

