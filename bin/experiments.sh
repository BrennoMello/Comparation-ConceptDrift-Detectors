#Abrupt Concept Drift AGRAW1 DDM

java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" \
moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l bayes.NaiveBayes -d DDM) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 1) -d (generators.AgrawalGenerator -f 2) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 3) -d (generators.AgrawalGenerator -f 4) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 5) -d (generators.AgrawalGenerator -f 1) \
    -s (ConceptDriftStream -s (generators.AgrawalGenerator -f 2) -d (generators.AgrawalGenerator -f 3) \
    -p 2000 -w 1) \
    -p 4000 -w 1) \
    -p 6000 -w 1) \
    -p 8000 -w 1) -i 10000 -f 1000" > results/NaiveBayes_DDM_AGRAW1_Abrupt_CD.csv

