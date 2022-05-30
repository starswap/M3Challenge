procedure recursiveGen(amount,city,prev,step,year):
  //Recursively generates a representative population. 
  //    amount : remaining population size
  //    prev : characteristics determined on previous calls
  //    step : which characteristic we are currently deciding
  
  if step == 0:
    for sex in sexes:
      recursiveGen(sexPercent[city][sex]*amount,city,prev+[sex],step+1,year) //for all possible sexes with representative probability (by reducing amount)
  else if step == 1:
    for ethnicity in ethnicities:
      recursiveGen(ethnicityPercent[city][ethnicity]*amount,city,prev+[ethnicity],step+1,year) //for all possible ethnicities with representative probability (by reducing amount)
  else if step == 2:
    for industry in industries:
      recursiveGen(industryPercent[year][city][industry]*amount,city,prev+[industry],step+1,year) //for all possible industries with representative probability (by reducing amount)
 // ... for other characteristics (omitted for brevity)
  else: //base case
    for person in range(int(amount)): 
        total = total + model2Probability for a person with these characteristics
        //Here we also incorporate the age, post pandemic attitudes constant, and commute distance factors.