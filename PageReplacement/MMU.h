#ifndef MMU_H
#define MMU_H


#include <vector>
#include <algorithm>
#include "Process.h"


class MMU {
    struct Row;
    const unsigned int AMOUNT_OF_RAM_PAGES;
    std::vector<unsigned int> freeQueue;
    std::vector<unsigned int> takenQueue;
    std::vector<Row> tableOfPresence;

    public:
    MMU(unsigned int pageAmount, std::vector<Process*>& bunchOfProcesses);
    void workWith(unsigned int processNo, unsigned int pageNo);

    private:
    void fillDefaultFreeQueue();
    bool hasFreePages();
    void pushToFreeQueue(unsigned int address);
    void eraseFromFreeQueue(unsigned int address);
    void pushToTakenQueue();
    void eraseFromTakenQueue(unsigned int address);

    struct Page {
        bool presenceFlag = false;
        bool accessFlag = false;
        bool modificationFlag = false;
        unsigned int RamAddress = 0;
    };

    struct Row {
        unsigned int processNo;
        unsigned int pageNo;
        unsigned int age;

    Row (unsigned int processNo, unsigned int pageNo, unsigned int age);
    unsigned int getAge();
    };
};


#endif
