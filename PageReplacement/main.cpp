#include <iostream>
#include "Process.h"
#include "MMU.h"


int main() {
    srand(time(0));
    unsigned int tick = 0;

    const unsigned int AMOUNT_OF_PROCESSES = 5;

    std::vector<Process*> banchOfProcesses;
    banchOfProcesses.reserve(AMOUNT_OF_PROCESSES);

    for (unsigned int i = 0; i < AMOUNT_OF_PROCESSES; i++) {
        banchOfProcesses.push_back(new Process(tick));
    }
    

    return 0;
}
