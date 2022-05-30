Determine projected population sizes in 2024 and 2027 for each city // (Part I)
For each city and each possible industry, ethnicity, education level etc  project percentage of people in that city with that characteristic in each year // (Part I & Research)


for year in years: //For both 2024 and 2027
  for city in cities: //For all cities
    total = 0 //total people WFH starts at 0.
    recursiveGen(population[year][city],city,[],0,year) //we use a global to save memory (avoiding copying)
    print("City : " + city + ", year : " + year)
    print(total/population[year][city]*100) // % of people for this city
