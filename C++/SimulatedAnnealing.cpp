#include <iostream>
#include <vector>
#include <random>


using namespace std;

// class def 
class SimulatedAnnealing {
    private:
        int rate;
        int Tmin;
        int T0;
        vector<vector<int>> W;
        vector<vector<int>> D; 
        int n; 
        
        int cost(vector<int> cost);
        vector<int> generate_init_soln();
        vector<int> generate_neighbor(vector<int> perm);
    public:
        SimulatedAnnealing::SimulatedAnnealing(vector<vector<int>> W, vector<vector<int>> D, int rate, int Tmin, int T0);
        SimulatedAnnealing::~SimulatedAnnealing();
        void SimulatedAnnealing::solve(int n_iter);
};


// implementation
SimulatedAnnealing::SimulatedAnnealing(vector<vector<int>> W, vector<vector<int>> D, int rate, int Tmin, int T0){
    this->D = D;
    this->W = W;
    this->rate = rate;
    this->Tmin = Tmin; 
    this->T0 = T0;
    n = D.size();
}

SimulatedAnnealing::~SimulatedAnnealing(){}


int SimulatedAnnealing::cost(vector<int> X){
    // TODO: CHECK THE FORMULA FOR THE BELOW 
    int sum = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++){
            sum += D[i][j];
        }
    }
}


vector<int> SimulatedAnnealing::generate_init_soln(){
    return vector{n};
}


void SimulatedAnnealing::solve(int n_iters){
    // intit a random soln 
    vector<int> soln = generate_init_soln();

    auto curr_perm = soln; 
    int curr_cost = cost(curr_perm); 
    
    int best_cost = curr_cost;
    auto best_perm = curr_perm;

    while (T0 > Tmin) {
        
        for (int i; i<n_iters; i++){
            
            auto new_perm = generate_neighbor(curr_perm);
            int  new_cost = cost(new_perm);

            int Delta = new_cost - curr_cost;

            // TODO: ADD THE RANDOM CHECK CONDITION
            if (Delta <= 0) {
                curr_perm = new_perm;
                curr_cost = new_cost;

                if (curr_cost < best_cost){
                    best_cost = curr_cost;
                    best_perm = new_perm;
                }
            }
        }
    }
}