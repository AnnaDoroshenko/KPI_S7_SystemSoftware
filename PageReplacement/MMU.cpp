#include "MMU.h"


MMU::MMU(unsigned int pageAmount, std::vector<Process*>& bunchOfProcesses) : 
    AMOUNT_OF_RAM_PAGES(pageAmount) {
        fillDefaultFreeQueue();
        tableOfPresence.reserve(AMOUNT_OF_RAM_PAGES);
}


void MMU::fillDefaultFreeQueue() {
    for (unsigned int i = 0; i < AMOUNT_OF_RAM_PAGES; i++) {
        freeQueue.push_back(i);
    }
}


bool MMU::hasFreePages() {
    return (freeQueue.size() != 0) ? true : false;
}


void MMU::pushToFreeQueue(unsigned int address) {
    freeQueue.push_back(address);
}


void MMU::eraseFromFreeQueue(unsigned int address) {
    freeQueue.erase(
            std::remove(freeQueue.begin(), freeQueue.end(), address), freeQueue.end());
}


void MMU::pushToTakenQueue() {
    unsigned int address = freeQueue.at(freeQueue.size() - 1);
    takenQueue.push_back(address);
    freeQueue.pop_back();
}


void MMU::eraseFromTakenQueue(unsigned int address) {
    takenQueue.erase(
            std::remove(takenQueue.begin(), takenQueue.end(), address), takenQueue.end());
}

void MMU::workWith(unsigned int processNo, unsigned int pageNo) {
    if (hasFreePages()) {
        pushToTakenQueue();
        // create new row and push it into tableOfPresence
    } else {
        unsigned int age = MMU::tableOfPresence[0].getAge();
        unsigned int index = 0;
        for (unsigned int i = 1; i < tableOfPresence.size(); i++) {
            const unsigned int currentAge = tableOfPresence[i].getAge();
            if (currentAge < age) {
                age = currentAge;
                index = i;
            }
        }
        // go to tableOfPresence.at(index) and change it
        // replaceInTakenQueue()
    }
}


MMU::Row::Row(unsigned int processNo, unsigned int pageNo, unsigned int age) : 
    processNo(processNo), pageNo(pageNo), age(age) {}


unsigned int MMU::Row::getAge() {
    return age;
}
