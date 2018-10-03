#include "MMU.h"


MMU::MMU(unsigned int pageAmount, const std::vector<Process*>& bunchOfProcesses) : 
    AMOUNT_OF_RAM_PAGES(pageAmount),
    tableOfPresence(std::vector<Row>(AMOUNT_OF_RAM_PAGES, Row(0, 0, 0))) {
        fillDefaultFreeQueue();
        pages.reserve(bunchOfProcesses.size());
        for (unsigned int i = 0; i < bunchOfProcesses.size(); i++) {
            const unsigned int pageAmount = bunchOfProcesses[i]->getPageAmount();
            std::vector<Page> pagesOfCurrentProcess;
            pagesOfCurrentProcess.reserve(pageAmount);
            for (unsigned int j = 0; j < pageAmount; j++) {
                pagesOfCurrentProcess.push_back(Page());
            }
            pages.push_back(pagesOfCurrentProcess);
        }
    }


void MMU::fillDefaultFreeQueue() {
    for (unsigned int i = 0; i < AMOUNT_OF_RAM_PAGES; i++) {
        freeQueue.push_back(i);
    }
}


bool MMU::hasFreePages() {
    return (freeQueue.size() != 0);
}


/* void MMU::pushToFreeQueue(unsigned int address) { */
/*     freeQueue.push_back(address); */
/* } */


/* void MMU::eraseFromFreeQueue(unsigned int address) { */
/*     freeQueue.erase( */
/*             std::remove(freeQueue.begin(), freeQueue.end(), address), freeQueue.end()); */
/* } */


unsigned int MMU::pushToTakenQueue() {
    unsigned int address = freeQueue.at(freeQueue.size() - 1);
    takenQueue.push_back(address);
    freeQueue.pop_back();
    return address;
}


/* void MMU::eraseFromTakenQueue(unsigned int address) { */
/*     takenQueue.erase( */
/*             std::remove(takenQueue.begin(), takenQueue.end(), address), takenQueue.end()); */
/* } */


void MMU::workWith(unsigned int processNo, unsigned int pageNo, bool modified) {
    Page currentPage = pages[processNo][pageNo];
    if (!currentPage.isPresent()) {
        if (hasFreePages()) {
            unsigned int addr = pushToTakenQueue();
            tableOfPresence[addr] = Row(processNo, pageNo, 0);
        } else {
            unsigned int age = MMU::tableOfPresence[0].age;
            unsigned int index = 0;
            for (unsigned int i = 1; i < tableOfPresence.size(); i++) {
                const unsigned int currentAge = tableOfPresence[i].age;
                if (currentAge < age) {
                    age = currentAge;
                    index = i;
                }
            }
            Row unusedPageRow = tableOfPresence[index];
            Page unusedPage = pages[unusedPageRow.processNo][unusedPageRow.pageNo];
            unusedPage.present(false);
            unusedPage.access(false);
            unusedPage.modify(false);
            // cout about paging
            tableOfPresence[index] = Row(processNo, pageNo, 0);
        }
        currentPage.present(true);
    }
    updateAge(processNo, pageNo);
    currentPage.access(true);
    if (modified) {
        currentPage.modify(true);
    }
    showTableOfPresence();
}


void MMU::updateAge(unsigned int processNo, unsigned int pageNo) {
    for (unsigned int i = 0; i < tableOfPresence.size(); i++) {
        Row& currentRow = tableOfPresence[i];
        if ((currentRow.processNo == processNo) && (currentRow.pageNo == pageNo)) {
            currentRow.age |= 0x80000000;
        }
        currentRow.age >>= 1;
    }
}


void MMU::showTableOfPresence() {
    for (Row row : tableOfPresence) {
        std::cout << "Process " << row.processNo;
        std::cout << " Page " << row.pageNo;
        std::cout << " Age: " << row.age << std::endl;
    }
}


bool MMU::Page::isPresent() {
    return presenceFlag;
}


void MMU::Page::present(bool state) {
    presenceFlag = state;
}


void MMU::Page::access(bool state) {
    accessFlag = state;
}


void MMU::Page::modify(bool state) {
    modificationFlag = state;
}


MMU::Row::Row(unsigned int processNo, unsigned int pageNo, unsigned int age) : 
    processNo(processNo), pageNo(pageNo), age(age) {}
