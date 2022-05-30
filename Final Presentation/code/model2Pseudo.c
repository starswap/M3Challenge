P(W_p and A and R)_Est = function (person1):
    // person1 is of type Person (custom OOP)
    baseRate = overall pre-pandemic WFH proportion from ONS
    currentRate = baseRate
    for characteristic in person1: //industry, sex, FT/HT etc.
        charRate = 2019 WFH rate for people with characteristic from ONS
        charRate = charRate / baseRate // to normalise
        currentRate = currentRate * charRate //affects their chance
    endfor
    //continuous factors: commute distance and age
    currentRate = currentRate * tanh(person1.commuteDistance)
    currentRate = currentRate * (1.5-0.5 e^((person.Age-20)/80))
    return currentRate