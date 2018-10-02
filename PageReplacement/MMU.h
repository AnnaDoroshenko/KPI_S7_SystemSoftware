#ifndef MMU_H
#define MMU_H


#include <vector>
#include <algorithm>
#include "Process.h"


class MMU {
    struct Row;
    struct Page;
    const unsigned int AMOUNT_OF_RAM_PAGES;
    std::vector<unsigned int> freeQueue;
    std::vector<unsigned int> takenQueue;
    std::vector<Row> tableOfPresence;
    std::vector<std::vector<Page>> pages;

    public:
    MMU(unsigned int pageAmount, const std::vector<Process*>& bunchOfProcesses);
    void workWith(unsigned int processNo, unsigned int pageNo);

    private:
    void fillDefaultFreeQueue();
    bool hasFreePages();
    void pushToFreeQueue(unsigned int address);
    void eraseFromFreeQueue(unsigned int address);
    unsigned int pushToTakenQueue();
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
