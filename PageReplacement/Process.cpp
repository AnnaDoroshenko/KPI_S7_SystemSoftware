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
    unsigned int page = 0;
    if (randNumber <= 9) {
        // get page from the working set
    } else {
        // get any page, that isn't included to the working set
    }

    return page;
}


bool Process::isAlive (unsigned int currentTime) const {
    return ((currentTime - BIRTH_TIME) < LIFE_TIME);
}


unsigned int Process::getPageAmount(){
    return AMOUNT_OF_PAGES;
}
