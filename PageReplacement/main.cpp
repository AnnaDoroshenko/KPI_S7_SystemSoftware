#include <iostream>
#include <vector>
#include <algorithm>
#include "Process.h"
#include "MMU.h"


int main() {
    srand(time(0));

    const unsigned int TICKS = 200;
    const unsigned int AMOUNT_OF_RAM_PAGES = 6;
    const unsigned int AMOUNT_OF_PROCESSES = 5;

    std::vector<Process*> bunchOfProcesses;
    bunchOfProcesses.reserve(AMOUNT_OF_PROCESSES);
    unsigned int tick = 0;

    for (unsigned int i = 0; i < AMOUNT_OF_PROCESSES; i++) {
        bunchOfProcesses.push_back(new Process(tick));
    }

    MMU mmu(AMOUNT_OF_RAM_PAGES, bunchOfProcesses);
    std::cout << "here1" << std::endl;

    while (tick < TICKS) {
        const unsigned int PROCESS_No = rand() % AMOUNT_OF_PROCESSES;
        const unsigned int PAGE_No = bunchOfProcesses[PROCESS_No]->getExecutingPage();
        const bool MODIFICATION = ((rand() % 2) == 0);
        std::cout << "here2" << std::endl;
        mmu.workWith(PROCESS_No, PAGE_No, MODIFICATION);
        std::cout << "here3" << std::endl;

        /* for (unsigned int i = 0; i < bunchOfProcesses.size(); i++) { */
        /*     if (!bunchOfProcesses[i].isAlive(tick)) { */
        /*         bunchOfProcesses.erase(bunchOfProcesses.begin() + i); */
        /*     } */
        /* } */

        tick++;
    }


    return 0;
}
