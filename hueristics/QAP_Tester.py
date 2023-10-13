"""
class for testing a QAP Hueristic. Take as input the hueristic, and file paths
to perform tests 
"""
import csv
import os
import numpy as np


class QAP_Hueristic_Tester:
    def __init__(self, heuristic: object, instance_path:str, soln_path:str, write_to_path:str) -> None:
        assert os.path.exists(soln_path) and os.path.exists(instance_path)
        self.heuristic     = heuristic
        self.instance_path = instance_path
        self.soln_path     = soln_path
        self.write_to_path = write_to_path


    def __read_integers(self, filename):
        with open(filename) as f:
            return [int(elem) for elem in f.read().split()]
        

    def __open_solution(self, filename: str):
        file_it = iter(self.__read_integers(filename))
        _ = next(file_it)   # this is just how the files within the lib are formatted
        return next(file_it)


    def test_hueristic(self, n_iters: int, n_trials: int, 
                       tai_only=False, bur_only=False, **kwargs):
        """
        tests the hueristic over specified number of trials and iterations. 
        records avg gap, std. dev, max gap, min gap for each trial
        """
        results_filename = self.write_to_path + str(self.heuristic)

        if tai_only: results_filename += '-tai.csv'
        if bur_only: results_filename += '-bur.csv'
        if not tai_only and not bur_only: filename += '.csvs'

        with open(results_filename, mode='w') as results:  
            
            writer = csv.writer(results)
            writer.writerow(['instance', 'avg gap', 'std_dev', 
                             'max gap', 'min gap', 'trials'])


            for filename in os.listdir(self.instance_path): 
                
                 # skips any instances that are not Tai
                if tai_only and 'tai' not in filename: continue    
                if bur_only and 'bur' not in filename: continue

                file_it = iter(self.__read_integers(self.instance_path+filename))

                # open QAP instance param's 
                n = next(file_it)
                w = np.array([[next(file_it) for j in range(n)] for i in range(n)])
                d = np.array([[next(file_it) for j in range(n)] for i in range(n)])

                # generate an instance 
                heuristic = self.heuristic(w,d,**kwargs)

                soln_file = filename[:-4]+'.sln' # this removes the .dat from filename

                try:
                    
                    gaps = []
                    qap_soln = self.__open_solution(self.soln_path+soln_file)

                    for _ in range(n_trials): 
                        huerstic_soln = heuristic.solve(n_iters)
                        gap = 100*(heuristic.cost(huerstic_soln) - qap_soln)/qap_soln
                        gaps.append(gap)

                    writer.writerow([filename, np.mean(gaps), np.std(gaps), 
                                     max(gaps), min(gaps), n_trials])
                
            # any instances without corresponding solution files are deleted
                except FileNotFoundError:
                    os.remove(self.instance_path+filename)        
        return