# MOA HoeffdingTree
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask LearnModel -l trees.HoeffdingTree -s generators.WaveformGenerator -m 1000000 \
-O results/model1.moa

#MOA NaiveBayes
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask LearnModel -l bayes.NaiveBayes -s generators.WaveformGenerator -m 1000000 -O results/model1.moa

#MOA EvaluatePrequential does not work
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "EvaluatePrequential -l bayes.NaiveBayes -s (ConceptDriftStream -s (gen- erators.SEAGenerator -f 3) -d (generators.SEAGenerator -f 2) -p 50000 -w 1) -i 100000 -f 1000"

#Abrupt Concept Drift
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "EvaluatePrequential -l bayes.NaiveBayes -s (ConceptDriftStream -s (generators.SEAGenerator -f 3) \
-d (generators.SEAGenerator -f 2) -p 50000 -w 20000) -i 10000 -f 1000"

#Abrupt Concept Drift
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "EvaluatePrequential -l bayes.NaiveBayes \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 1) -d (generators.AgrawalGenerator -f 2) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 3) -d (generators.AgrawalGenerator -f 4) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 5) -d (generators.AgrawalGenerator -f 1) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 2) -d (generators.AgrawalGenerator -f 3) \
    -p 2000 -w 1) \
    -p 4000 -w 1) \
    -p 6000 -w 1) \
    -p 8000 -w 1) -i 10000 -f 1000" > results/NaiveBayes_AgrawalGenerator_Abrupt_Concept_Drift.csv


#Abrupt Concept Drift
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l bayes.NaiveBayes -d DDM) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 1) -d (generators.AgrawalGenerator -f 2) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 3) -d (generators.AgrawalGenerator -f 4) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 5) -d (generators.AgrawalGenerator -f 1) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 2) -d (generators.AgrawalGenerator -f 3) \
    -p 2000 -w 1) \
    -p 4000 -w 1) \
    -p 6000 -w 1) \
    -p 8000 -w 1) -i 10000 -f 1000" > results/NaiveBayes_AgrawalGenerator_Abrupt_Concept_Drift.csv


#Save File Abrupt Concept Drift
java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "WriteStreamToARFFFile \
-s (ConceptDriftStream -s (generators.AgrawalGenerator -f 2) -d (generators.AgrawalGenerator -f 4) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 3) -d (generators.AgrawalGenerator -f 5) -p 2000 -w 1) \
    -p 4000 -w 1) -f stream_test.arff -m 10000"

java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l bayes.NaiveBayes -d DDM) 
-s (ConceptDriftRealStream -s generators.AgrawalGenerator -d (ConceptDriftStream 
-s (generators.AgrawalGenerator -f 2) -d (ConceptDriftStream 
-s (generators.AgrawalGenerator -f 3) -d (ConceptDriftStream 
-s (generators.AgrawalGenerator -f 4) -d (generators.AgrawalGenerator -f 5) -p 8000 -w 1) -p 6000 -w 1) -p 4000 -w 1) -p 2000 -w 1) -i 10000 -f 1000"