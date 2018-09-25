#ifndef PROCESS_H
#define PROCESS_H


#include <vector>
#include <stdlib.h>


class Process {
    const unsigned int AMOUNT_OF_PAGES;
    const std::vector<unsigned int> WORKING_SET;
    const unsigned int LIFE_TIME;
    const unsigned int BIRTH_TIME;

    public:
    Process (unsigned int birthtime);

    private:
    std::vector<unsigned int> generateWorkingSet();
    unsigned int getExcecutingPage();
    bool isAlive (unsigned int currentTime) const;
};


#endif
