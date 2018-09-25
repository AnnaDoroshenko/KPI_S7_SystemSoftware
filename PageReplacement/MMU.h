#ifndef MMU_H
#define MMU_H


#include <vector>


class MMU {
    std::vector<unsigned int> freeQueue;
    std::vector<unsigned int> takenQueue;

    public:
    void fillDefaultFreeQueue();

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
    };
};

#endif
