
import os
from loguru import logger as log


def run_abrupt_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW1_Abrupt.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW1_Abrupt.csv'
                        
                    log.info(command)
                    os.system(command)

def run_gradual_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW1_Gradual.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_agraw1/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW1_Gradual.csv'           
                    
                    log.info(command)
                    os.system(command)


def run_abrupt_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW2_Abrupt.csv'
                        

                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW2_Abrupt.csv'
                            
                    log.info(command)
                    os.system(command)

def run_gradual_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW2_Gradual.csv'
                        
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                    -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_agraw2/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_AGRAW2_Gradual.csv'
                            
                    log.info(command)
                    os.system(command)

def run_abrupt_led(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""): 
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_LED_Abrupt.csv'
                        
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_LED_Abrupt.csv'
                            
                    log.info(command)
                    os.system(command)

def run_gradual_led(repetitions, learning_algorithms, drift_detectors_params, data_stream):


    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""): 
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                        -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                        -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                        -p {size["drift_position"][3]} -w 500) \
                                        -p {size["drift_position"][2]} -w 500) \
                                        -p {size["drift_position"][1]} -w 500) \
                                        -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_LED_Gradual.csv'
                                    
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_led/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_LED_Gradual.csv'
                            
                    log.info(command)
                    os.system(command)


def run_abrupt_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_MIXED_Abrupt.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_MIXED_Abrupt.csv'                                
                    log.info(command)
                    os.system(command)


def run_gradual_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_MIXED_Gradual.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_mixed/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_MIXED_Gradual.csv'            
                    
                    log.info(command)
                    os.system(command)

def run_abrupt_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_RANDOM_RBF_Abrupt.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_RANDOM_RBF_Abrupt.csv'       
                    
                    log.info(command)
                    os.system(command)

def run_gradual_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_RANDOM_RBF_Gradual.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                    -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_randomRBF/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_RANDOM_RBF_Gradual.csv'
                                                        
                    log.info(command)
                    os.system(command)


def run_abrupt_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_SINE_Abrupt.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_SINE_Abrupt.csv'        
                    log.info(command)
                    os.system(command)


def run_gradual_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_SINE_Gradual.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_sine/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_SINE_Gradual.csv'
                    log.info(command)
                    os.system(command)

def run_abrupt_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (generators.WaveformGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_WAVEFORM_Abrupt.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.WaveformGenerator -i {iter}) -d (generators.WaveformGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 1) \
                                    -p {size["drift_position"][2]} -w 1) \
                                    -p {size["drift_position"][1]} -w 1) \
                                    -p {size["drift_position"][0]} -w 1) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/abrupt_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_WAVEFORM_Abrupt.csv'                
                    log.info(command)
                    os.system(command)


def run_gradual_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream):

    for learning_algorithm in learning_algorithms:
        for size in data_stream:
            for drift_algorithm in drift_detectors_params:
                for iter in range(repetitions):
                    if(drift_algorithm["params"] != ""):
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d ({drift_algorithm["drift_name"]} {drift_algorithm["params"]})) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_WAVEFORM_Gradual.csv'
                    else:
                        command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm["drift_name"]}) \
                                    -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                    -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                    -p {size["drift_position"][3]} -w 500) \
                                    -p {size["drift_position"][2]} -w 500) \
                                    -p {size["drift_position"][1]} -w 500) \
                                    -p {size["drift_position"][0]} -w 500) -e (BasicClassificationPerformanceEvaluator) -i {size["data_size"]} -f 1000" > results/gradual_waveform/{learning_algorithm}_{drift_algorithm["id"]}_{size["data_size"]}_{iter}_WAVEFORM_Gradual.csv'
                    
                    log.info(command)
                    os.system(command)

if __name__ == "__main__":
    
    
    # Full Experiments        
    # repetitions = 30
    # learning_algorithms = ["bayes.NaiveBayes", "trees.HoeffdingTree"]
    # data_stream = [{"data_size": 10000, "drift_position":  [2000, 4000, 6000, 8000]}, \
    #                {"data_size": 20000, "drift_position": [4000, 8000, 12000, 16000]}, \
    #                {"data_size": 50000, "drift_position": [10000, 20000, 30000, 40000]}, \
    #                {"data_size": 100000, "drift_position":[20000, 4000, 6000, 8000]}]
                              
    # drift_detectors_params = [{"id": "DDM", "drift_name": "DDM", "params": ""},    \
    #                           {"id": "EDDM", "drift_name": "EDDM", "params": ""},   \
    #                           {"id": "ADWIN", "drift_name": "ADWIN", "params": ""},  \
    #                           {"id": "ECDD", "drift_name": "ECDD", "params": ""},   \
    #                           {"id": "STEPD", "drift_name": "STEPD", "params": ""},  \
    #                           {"id": "SeqDrift2", "drift_name": "SeqDrift2", "params": ""},  \
    #                           {"id": "SEED", "drift_name": "SEED", "params": ""},   \
    #                           {"id": "HDDM_A_Test", "drift_name": "HDDM_A_Test", "params": ""},  \
    #                           {"id": "HDDM_W_Test", "drift_name": "HDDM_W_Test", "params": ""},  \
    #                           {"id": "FHDDM", "drift_name": "FHDDM", "params": ""},  \
    #                           {"id": "FTDD", "drift_name": "FTDD", "params": ""},   \
    #                           {"id": "RDDM_30", "drift_name": "RDDM", "params": "-n 30 -w 2 -o 3"}, \
    #                           {"id": "RDDM","drift_name": "RDDM", "params": ""},   \
    #                           {"id": "WSTD","drift_name": "WSTD", "params": ""}
    #                           ]
    
    # Test Experiments
    repetitions = 30
    learning_algorithms = ["bayes.NaiveBayes"]
    data_stream = [{"data_size": 10000, "drift_position":  [2000, 2000, 2000, 2000]}, \
                   {"data_size": 20000, "drift_position": [4000, 4000, 4000, 4000]}, \
                   #{"data_size": 50000, "drift_position": [10000, 10000, 10000, 10000]}, \
                   #{"data_size": 100000, "drift_position":[20000, 20000, 20000, 20000]}
                   ]
                              
    drift_detectors_params = [
                              {"id": "DDM", "drift_name": "DDM", "params": ""},    \
                              {"id": "EDDM", "drift_name": "EDDM", "params": ""},   \
                              {"id": "ADWIN", "drift_name": "ADWINChangeDetector", "params": ""},  \
                              {"id": "ECDD", "drift_name": "EWMAChartDM", "params": ""},   \
                              {"id": "STEPD", "drift_name": "STEPD", "params": ""},  \
                              {"id": "SeqDrift2", "drift_name": "SeqDrift2ChangeDetector", "params": ""},  \
                              {"id": "SEED", "drift_name": "SEEDChangeDetector", "params": ""},   \
                              {"id": "HDDM_A_Test", "drift_name": "HDDM_A_Test", "params": ""},  \
                              {"id": "HDDM_W_Test", "drift_name": "HDDM_W_Test", "params": ""},  \
                              #{"id": "FHDDM", "drift_name": "FHDDM", "params": ""},  \
                              #{"id": "FTDD", "drift_name": "FTDD", "params": ""},   \
                              {"id": "RDDM_30", "drift_name": "RDDM", "params": "-n 30 -w 2 -o 3"}, \
                              {"id": "RDDM","drift_name": "RDDM", "params": ""},   \
                              #{"id": "WSTD","drift_name": "WSTD", "params": ""}
                              ]
    

    log.info(f'Runnig abrupt_agraw1')
    run_abrupt_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_agraw1')
    run_gradual_agraw1(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig abrupt_agraw2')
    run_abrupt_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig  gradual_agraw2')
    run_gradual_agraw2(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig abrupt_led')
    run_abrupt_led(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_led')
    run_gradual_led(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig abrupt_mixed')
    run_abrupt_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_mixed')
    run_gradual_mixed(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig brupt_randomRBF')
    run_abrupt_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_randomRBF')
    run_gradual_randomRBF(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig abrupt_sine')
    run_abrupt_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_sine')
    run_gradual_sine(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig abrupt_waveform')
    run_abrupt_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    log.info(f'Runnig gradual_waveform')
    run_gradual_waveform(repetitions, learning_algorithms, drift_detectors_params, data_stream)
    