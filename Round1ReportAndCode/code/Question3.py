#import necessary modules
from math import exp
from dataONS import * #2019 ONS Data https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/datasets/homeworkingintheukworkfromhomestatus which we have converted to python dictionary format
from Question2 import * #we reuse question 2 model here in question3.
import numpy as np#for normal distribution
import random

mu, sigma = 35, 10 # age mean and standard deviation
c = 1.4 #Pandemic attitudes constant

def tanh(x):
  """the tanh function"""
  return (exp(x) - exp(-x))/(exp(x)+exp(-x))

#Projected populations based on regression
population = {"2024":{"Barry":56805,"Liverpool":754024,"Omaha":504872,"Seattle":1780424,"Scranton":2461378},"2027":{"Barry":58410,"Liverpool":772777,"Omaha":515231,"Seattle":1846727,"Scranton":2461550}}

#Possible characteristics of a person
years = ["2024","2027"]
cities = ["Barry","Liverpool","Omaha","Seattle","Scranton"]
sexes = ["men","women"]
ethnicities = ["white","mixed","asian","black","other"]
educations = ["noQualifications","entryLevel","gcseOrEquiv","aLevelOrEquiv","degreeOrEquiv","higherDegree"]
industries = ["AgricultureForestryFishing","MiningUtilities","Manufacturing","Construction","WholesaleRetailRepairOfVehicles","TransportStorage","AccommodationFoodServices","InformationCommunication","FinancialServicesRealEstate","ProfScientificTechnicalActiv","AdminSupportServices","PublicAdminDefence","Education","HealthSocialWork","OtherServices"] 
times = ["Full Time","Part Time"]
houses = [True,False]

#For each city and sometimes for each year, percentage of people having each tag
sexPercent = {"Barry":{"men":0.5,"women":0.5},"Liverpool":{"men":0.5,"women":0.5},"Omaha":{"men":0.5,"women":0.5},"Seattle":{"men":0.5,"women":0.5},"Scranton":{"men":0.5,"women":0.5}}

ethnicityPercent = {"Barry":{"white":0.961,"mixed":0.016,"asian":0.018,"black":0.004,"other":0.01},"Liverpool":{"white":0.91,"mixed":0.02,"asian":0.041,"black":0.019,"other":0.01},"Omaha":{"white":0.7747,"mixed":0.034,"asian":0.0384,"black":0.1232,"other":0.0297},"Seattle":{"white":0.657,"mixed":0.051,"asian":0.138,"black":0.079,"other":0.126},"Scranton":{"white":0.8309,"mixed":0.0439,"asian":0.0467,"black":0.0585,"other":0.02}}

industryPercent = {"2024":{"Barry":{"AgricultureForestryFishing":0.025,"MiningUtilities":0.025,"Manufacturing":0.083,"Construction":0.025,"WholesaleRetailRepairOfVehicles":0.010,"TransportStorage":0.010,"AccommodationFoodServices":0.194,"InformationCommunication":0.0656,"FinancialServicesRealEstate":0.058,"ProfScientificTechnicalActiv":0.054,"AdminSupportServices":0.114,"PublicAdminDefence":0.114,"Education":0.087,"HealthSocialWork":0.087,"OtherServices":0.0514},"Liverpool":{"AgricultureForestryFishing":0.067,"MiningUtilities":0.067,"Manufacturing":0.135,"Construction":0.067,"WholesaleRetailRepairOfVehicles":0.095,"TransportStorage":0.095,"AccommodationFoodServices":0.084,"InformationCommunication":0.103,"FinancialServicesRealEstate":0.042,"ProfScientificTechnicalActiv":0.029,"AdminSupportServices":0.029,"PublicAdminDefence":0.029,"Education":0.014,"HealthSocialWork":0.014,"OtherServices":0.111},"Omaha":{"AgricultureForestryFishing":0.020,"MiningUtilities":0.020,"Manufacturing":0.063,"Construction":0.020,"WholesaleRetailRepairOfVehicles":0.090,"TransportStorage":0.090,"AccommodationFoodServices":0.101,"InformationCommunication":0.018,"FinancialServicesRealEstate":0.091,"ProfScientificTechnicalActiv":0.074,"AdminSupportServices":0.105,"PublicAdminDefence":0.105,"Education":0.085,"HealthSocialWork":0.085,"OtherServices":0.038},"Seattle":{"AgricultureForestryFishing":0.020,"MiningUtilities":0.020,"Manufacturing":0.080,"Construction":0.020,"WholesaleRetailRepairOfVehicles":0.095,"TransportStorage":0.095,"AccommodationFoodServices":0.092,"InformationCommunication":0.075,"FinancialServicesRealEstate":0.047,"ProfScientificTechnicalActiv":0.078,"AdminSupportServices":0.104,"PublicAdminDefence":0.104,"Education":0.071,"HealthSocialWork":0.071,"OtherServices":0.},"Scranton":{"AgricultureForestryFishing":0.013,"MiningUtilities":0.013,"Manufacturing":0.093,"Construction":0.013,"WholesaleRetailRepairOfVehicles":0.130,"TransportStorage":0.130,"AccommodationFoodServices":0.086,"InformationCommunication":0.009,"FinancialServicesRealEstate":0.050,"ProfScientificTechnicalActiv":0.058,"AdminSupportServices":0.084,"PublicAdminDefence":0.084,"Education":0.108,"HealthSocialWork":0.108,"OtherServices":0.0301}},"2027":{"Barry":{"AgricultureForestryFishing":0.0252,"MiningUtilities" :0.0252,"Manufacturing" :0.0818,"Construction" :0.0252,"WholesaleRetailRepairOfVehicles" :0.010,"TransportStorage" :0.010,"AccommodationFoodServices" :0.197,"InformationCommunication" :0.0643,"FinancialServicesRealEstate" :0.0584,"ProfScientificTechnicalActiv" : 0.114,"AdminSupportServices" :0.114,"PublicAdminDefence" :0.027,"Education" :0.0874,"HealthSocialWork" :0.08735,"OtherServices" :0.0507},"Liverpool":{"AgricultureForestryFishing" :0.065,"MiningUtilities": 0.065,"Manufacturing" :0.138,"Construction" :0.065,"WholesaleRetailRepairOfVehicles" :0.095,"TransportStorage" :0.095,"AccommodationFoodServices" :0.081,"InformationCommunication" :0.103,"FinancialServicesRealEstate" :0.043,"ProfScientificTechnicalActiv" :0.057,"AdminSupportServices" :0.042,"PublicAdminDefence" :0.042,"Education" :0.013,"HealthSocialWork" :0.013,"OtherServices" :0.110},"Omaha":{"AgricultureForestryFishing" :0.020,"MiningUtilities" :0.020,"Manufacturing" :0.062,"Construction" :0.020,"WholesaleRetailRepairOfVehicles" :0.086,"TransportStorage" :0.086,"AccommodationFoodServices" :0.102,"InformationCommunication" :0.017,"FinancialServicesRealEstate" :0.092,"ProfScientificTechnicalActiv": 0.075,"AdminSupportServices" :0.106,"PublicAdminDefence" :0.106,"Education" :0.088,"HealthSocialWork" :0.088,"OtherServices" :0.039},"Seattle":{"AgricultureForestryFishing" :0.020,"MiningUtilities" :0.020,"Manufacturing":0.076,"Construction" :0.020,"WholesaleRetailRepairOfVehicles" :0.095,"TransportStorage" :0.095,"AccommodationFoodServices" :0.092,"InformationCommunication" :0.081,"FinancialServicesRealEstate" :0.046,"ProfScientificTechnicalActiv": 0.080,"AdminSupportServices" :0.103,"PublicAdminDefence" :0.103,"Education" :0.072,"HealthSocialWork" :0.072,"OtherServices" :0.037},"Scranton":{"AgricultureForestryFishing":0.013,"MiningUtilities":0.013,"Manufacturing":0.087,"Construction":0.013,"WholesaleRetailRepairOfVehicles":0.133,"TransportStorage":0.133,"AccommodationFoodServices":0.087,"InformationCommunication":0.008,"FinancialServicesRealEstate":0.050,"ProfScientificTechnicalActiv":0.059,"AdminSupportServices":0.057,"PublicAdminDefence":0.057,"Education":0.110,"HealthSocialWork":0.110,"OtherServices":0.110}}}
#(Determined in model 1)

#percentage chance that a person in each city can/cannot work from home due to their house (not) being suitable
housePercent = {"Barry":{True:0.9,False:0.1},"Liverpool":{True:0.9,False:0.1},"Omaha":{True:0.9,False:0.1},"Seattle":{True:0.9,False:0.1},"Scranton":{True:0.9,False:0.1}}

educationPercent = {"Barry":{"noQualifications":0.063,"entryLevel":0.189,"gcseOrEquiv":0.393,"aLevelOrEquiv":0.193,"degreeOrEquiv":0.064,"higherDegree":0.098}
,"Liverpool":{"noQualifications":0.064,"entryLevel":0.192,"gcseOrEquiv":0.332,"aLevelOrEquiv":0.077,"degreeOrEquiv":0.232,"higherDegree":0.103}
,"Omaha":{"noQualifications":0.025,"entryLevel":0.075,"gcseOrEquiv":0.206,"aLevelOrEquiv":0.31,"degreeOrEquiv":0.246,"higherDegree":0.131}
,"Scranton":{"noQualifications":0.046,"entryLevel":0.138,"gcseOrEquiv":0.293,"aLevelOrEquiv":0.277,"degreeOrEquiv":0.149,"higherDegree":0.095}
,"Seattle":{"noQualifications":0.027,"entryLevel":0.082,"gcseOrEquiv":0.154,"aLevelOrEquiv":0.295,"degreeOrEquiv":0.269,"higherDegree":0.173}}

timePercent = {"Barry":{"Full Time":0.75,"Part Time":0.25},"Liverpool":{"Full Time":0.75,"Part Time":0.25}
,"Omaha":{"Full Time":0.75,"Part Time":0.25}
,"Seattle":{"Full Time":0.75,"Part Time":0.25}
,"Scranton":{"Full Time":0.75,"Part Time":0.25}}


totalWFH = 0 #total people WFH starts at 0.

def recursiveGen(amount,city,prev,step,year):
  """Recursively generates a population of size amount for city, assuming the existing
     characteristics already determined outlined in prev, for year year.
     The step indicates which characteristic we are currently deciding"""
  
  global totalWFH
  
  if step == 0:
    for sex in sexes:
      recursiveGen(sexPercent[city][sex]*amount,city,prev+[sex],step+1,year) #for all possible sexes with probability (by reducing amount)
  elif step == 1:
    for ethnicity in ethnicities:
      recursiveGen(ethnicityPercent[city][ethnicity]*amount,city,prev+[ethnicity],step+1,year) #for all possible ethnicities with probability (by reducing amount)
  elif step == 2:
    for industry in industries:
      recursiveGen(industryPercent[year][city][industry]*amount,city,prev+[industry],step+1,year) #for all possible industries with probability (by reducing amount)
  elif step == 3:
    for education in educations:
      recursiveGen(educationPercent[city][education]*amount,city,prev+[education],step+1,year) #for all possible educations with probability (by reducing amount)
  elif step == 4:
    for time in times:
      recursiveGen(timePercent[city][time]*amount,city,prev+[time],step+1,year)#for all possible times with probability (by reducing amount)
  elif step == 5: 
    for house in houses:
      recursiveGen(housePercent[city][house]*amount,city,prev+[house],step+1,year) #for all possible house characteristics with probability (by reducing amount)
  else: #base case
    for person in range(int(amount)): #actually generate all of the people and determine the chance of them working from home post pandemic
      #Here we incorporate the age, post pandemic attitudes constant, and commute distance factors.
      totalWFH += max(0,
                      min(
                        c*PWp_n_A_R(Person(
                          prev[0],prev[1],prev[2],prev[3],prev[4],
                          random.randint(0,10000),
                          prev[5],
                          max(min(
                            np.random.normal(mu, sigma),80),
                              20))),
                      1)) #applying model 2

for year in years: #For both 2024 and 2027
  print("For year: " + str(year))
  for city in cities: #For all cities
    print("For city: " + city)
    
    totalWFH = 0 #total people WFH starts at 0.
    recursiveGen(population[year][city],city,[],0,year) #generate a representative population and sum the wfh over the population.
    print(totalWFH/population[year][city]*100) #Obtain percentage of people that will now WFH.
