
import os
from loguru import logger as log


def run_abrupt_agraw1(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_agraw1/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_AGRAW1_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)

def run_gradual_agraw1(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 2) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 3) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 4) -d (generators.AgrawalGenerator -i {iter} -f 5) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_agraw1/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_AGRAW1_Gradual.csv'
                        
                    #print(command)
                    os.system(command)


def run_abrupt_agraw2(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_agraw2/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_AGRAW2_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)

def run_gradual_agraw2(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.AgrawalGenerator -i {iter} -f 6) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 7) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 8) -d (ConceptDriftStream \
                                -s (generators.AgrawalGenerator -i {iter} -f 9) -d (generators.AgrawalGenerator -i {iter} -f 10) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_agraw2/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_AGRAW2_Gradual.csv'
                        
                    #print(command)
                    os.system(command)

def run_abrupt_led(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_led/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_LED_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)

def run_gradual_led(repetitions, learning_algorithms, drift_algorithms, data_size):


    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.LEDGenerator -i {iter}) -d (generators.LEDGenerator -i {iter}) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_led/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_LED_Gradual.csv'
                        
                    #print(command)
                    os.system(command)


def run_abrupt_mixed(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_mixed/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_MIXED_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)


def run_gradual_mixed(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.MixedGenerator -i {iter}) -d (generators.MixedGenerator -i {iter}) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_mixed/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_MIXED_Gradual.csv'
                        
                    #print(command)
                    os.system(command)

def run_abrupt_randomRBF(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_randomRBF/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_RANDOM_RBF_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)

def run_gradual_randomRBF(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (ConceptDriftStream \
                                -s (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) -d (generators.RandomRBFGenerator -i {iter} -c 6 -a 40 -n 50) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_randomRBF/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_RANDOM_RBF_Gradual.csv'
                        
                    #print(command)
                    os.system(command)


def run_abrupt_sine(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_sine/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_SINE_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)


def run_gradual_sine(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_sine/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_SINE_Gradual.csv'
                        
                    #print(command)
                    os.system(command)

def run_abrupt_waveform(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.WaveformGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.WaveformGenerator -i {iter}) -d (generators.WaveformGenerator -i {iter}) \
                                -p {size[4]} -w 1) \
                                -p {size[3]} -w 1) \
                                -p {size[2]} -w 1) \
                                -p {size[1]} -w 1) -i {size[0]} -f 1000" > results/abrupt_waveform/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_WAVEFORM_Abrupt.csv'
                        
                    #print(command)
                    os.system(command)


def run_gradual_waveform(repetitions, learning_algorithms, drift_algorithms, data_size):

    for learning_algorithm in learning_algorithms:
        for size in data_size:
            for drift_algorithm in drift_algorithms:
                for iter in range(repetitions):
                    command = f'java -cp src/moa-2023.04.0-sources.jar -javaagent:lib/sizeofag-1.0.4.jar -classpath "lib/*" moa.DoTask "EvaluatePrequential -l (drift.DriftDetectionMethodClassifier -l {learning_algorithm} -d {drift_algorithm}) \
                                -s (ConceptDriftStream -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (ConceptDriftStream \
                                -s (generators.SineGenerator -i {iter}) -d (generators.SineGenerator -i {iter}) \
                                -p {size[4]} -w 500) \
                                -p {size[3]} -w 500) \
                                -p {size[2]} -w 500) \
                                -p {size[1]} -w 500) -i {size[0]} -f 1000" > results/gradual_waveform/{learning_algorithm}_{drift_algorithm}_{size[0]}_{iter}_WAVEFORM_Gradual.csv'
                        
                    #print(command)
                    os.system(command)

if __name__ == "__main__":
    
    # Experiments
    #repetitions = 30
    #learning_algorithms = ["bayes.NaiveBayes", "trees.HoeffdingTree"]
    #drift_algorithms = ["DDM", "EDDM"]
    #data_size = [[10000, 2000, 4000, 6000, 8000], [20000, 4000, 8000, 12000, 16000], [50000, 10000, 20000, 30000, 40000], [100000, 20000, 4000, 6000, 8000]]

    # Test Experiments        
    repetitions = 30
    learning_algorithms = ["bayes.NaiveBayes"]
    drift_algorithms = ["DDM"]
    data_size = [[10000, 2000, 4000, 6000, 8000]]

    log.info(f'Runnig abrupt_agraw1')
    run_abrupt_agraw1(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_agraw1')
    run_gradual_agraw1(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig abrupt_agraw2')
    run_abrupt_agraw2(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig  gradual_agraw2')
    run_gradual_agraw2(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig abrupt_led')
    run_abrupt_led(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_led')
    run_gradual_led(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig abrupt_mixed')
    run_abrupt_mixed(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_mixed')
    run_gradual_mixed(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig brupt_randomRBF')
    run_abrupt_randomRBF(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_randomRBF')
    run_gradual_randomRBF(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig abrupt_sine')
    run_abrupt_sine(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_sine')
    run_gradual_sine(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig abrupt_waveform')
    run_abrupt_waveform(repetitions, learning_algorithms, drift_algorithms, data_size)
    log.info(f'Runnig gradual_waveform')
    run_gradual_waveform(repetitions, learning_algorithms, drift_algorithms, data_size)
    