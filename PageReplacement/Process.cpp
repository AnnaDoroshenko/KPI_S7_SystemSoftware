#include "Process.h"


Process::Process (float birthTime) :
    // AMOUNT_OF_PAGES()
        /* unsigned int amountOfPages,  */
        /* std::vector<unsigned int> workingSet,  */
        float birthTime {
        /* float lifeTime) { */
    srand(time(0));
    amountOfPages = static_cast <unsigned int> (rand()) / static_cast <unsigned int> (RAND_MAX);
    workingSet = generateWorkingSet(amountOfPages);
    birthTime = birthTime;
    lifeTime = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
};


std::vector<unsigned int> Process::generateWorkingSet(const unsigned int& amountOfPages) {
    // TODO Have no idea yet :(
}


unsigned int Process::getExcecutingPage() {}


bool Process::isAlive (float currentTime) {
    return ((currentTime - birthTime) < lifeTime) ? true : false;
}
