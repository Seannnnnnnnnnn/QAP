Exploring hueristics for the QAP problem. 


All hueristics are implemented in an `OOP` manner, and derived from a base class 
called `QAP_Hueristic`. Due to computational restrictions in our testing environment, 
we cap all CPU time for our heuristics to 60 seconds. 


```bash
├── C++
│   └── SimulatedAnnealing.cpp
├── QAPInstances 
│   ├── { QAP instanaces from QAPLib}
├── QAPSolns
│   ├── { solutions to instances in ../QAPInstances }
├── README.md
├── hueristics
│   ├── QAP.code-workspace
│   ├── QAP_heuristic.py
│   ├── genetic.ipynb
│   ├── ils.ipynb
│   ├── randomized greedy.ipynb
│   ├── simmulated annealing.ipynb
│   └── tabu search.ipynb
└── results
    ├── SimmulatedAnnealing.csv
    ├── TabuSearch.csv
    └── ils.csv
```