#include "Process.h"


Process::Process (unsigned int birthTime) :
    AMOUNT_OF_PAGES((rand() % 10) + 1), 
    WORKING_SET(generateWorkingSet()), 
    LIFE_TIME((rand() % 20) + 1), 
    BIRTH_TIME(birthTime) {}


std::vector<unsigned int> Process::generateWorkingSet() {
    const unsigned int SIZE_OF_WORKING_SET = 0.3 * AMOUNT_OF_PAGES;
    std::vector<unsigned int> workingSet;
    workingSet.reserve(SIZE_OF_WORKING_SET);
    // FIXME: find some another approach to fill working set
    for (unsigned int i = 0; i < SIZE_OF_WORKING_SET; i++) {
        workingSet.push_back(i);
    }

    return workingSet;
}


unsigned int Process::getExecutingPage() {
    const unsigned int randNumber = (rand() % 10) + 1;
    /* const unsigned int size = WORKING_SET.size(); */
    unsigned int page = 0;
    if (randNumber <= 5) {
        // page = rand() % WORKING_SET.size();
        page = rand() % 3;
    } else {
        page = (rand() % AMOUNT_OF_PAGES) + WORKING_SET.size();
    }

    return page;
}


// bool Process::isAlive (unsigned int currentTime) const {
//     return ((currentTime - BIRTH_TIME) < LIFE_TIME);
// }


unsigned int Process::getPageAmount(){
    return AMOUNT_OF_PAGES;
}
