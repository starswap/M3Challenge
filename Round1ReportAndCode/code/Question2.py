#import necessary modules
from math import exp
from dataONS import * #2019 ONS Data https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/datasets/homeworkingintheukworkfromhomestatus which we have converted to python dictionary format
import random

c = 1.4 #Pandemic attitudes constant

class Person:
  """Defines a single member of the population in the Monte Carlo simulation"""
  def __init__(self,sex,ethnicity,industry,education,time,commute,houseAllowsWFH,age):
    """Take in data about the person and save it to local state"""
    self.sex = sex
    self.ethnicity = ethnicity
    self.industry = industry
    self.education = education
    self.time = time
    self.commute = commute #IN METRES
    self.houseAllowsWFH = houseAllowsWFH
    self.age = age

def tanh(x):
  """the tanh function"""
  return (exp(x) - exp(-x))/(exp(x)+exp(-x))

def PWp_n_A_R(person):
  """Probability that a given person wanted (pre-pandemic) and was allowed to and was ready to WFH"""

  if person.houseAllowsWFH: #if their house does not allow WFH then they cannot WFH at all
    baseRate = kWFH_2019/(kWFH_2019+kNoWFH_2019) #For a generic person, the chance that they WFH pre pandemic
    
    currentRate = baseRate #Start with this but change it based on the person's characteristics
    currentRate *= sexWFH[person.sex]/baseRate #Do people of their sex WFH more or less than average?
    currentRate *= ethnicityWFH[person.ethnicity]/baseRate #Do people of their ethnicity WFH more or less than average?
    if person.time == "Full Time": #Do people of their full/part time WFH more or less than average?
      currentRate *= industryFT_WFH[person.industry]/baseRate
    else:
      currentRate *= industryPT_WFH[person.industry]/baseRate
    currentRate *= educationWFH[person.education]/baseRate #Do people of their education level WFH more or less than average?
    currentRate *= tanh(person.commute/1000) #If the person lives really close to the office they will be much less likely to work from home. If they live far away we want the impact of moving 1 mile away from already far away to be low so we use tanh.
    currentRate *= 1.5-0.5*exp((person.age-20)/80) #Steady decline in likelihood of WFH with age; starting at 1 for a 20 year old due to level of tech saviness. 
    return currentRate
  else:
    return 0
  
def P_R(person):
  """Based on the given industry, the probability that their job is remote ready"""
  return P_RIndustry[person.industry]
  
def PW_n_A_givenR(person):
  """Probability that they (post pandemic) want to WFH and are allowed to WFH given that their job is remote ready"""
  return max(0,min(c*PWp_n_A_R(person)/P_R(person),1))

print(PW_n_A_givenR(Person("men","white","InformationCommunication","degreeOrEquiv","Full Time",1000,True,40)))
print(PW_n_A_givenR(Person("men","white","InformationCommunication","degreeOrEquiv","Full Time",1000,True,80)))
print(PW_n_A_givenR(Person("women","white","InformationCommunication","degreeOrEquiv","Full Time",1000,True,40)))
print(PW_n_A_givenR(Person("men","asian","InformationCommunication","noQualifications","Full Time",1000,True,40)))
print(PW_n_A_givenR(Person("men","asian","WholesaleRetailRepairOfVehicles","aLevelOrEquiv","Full Time",1000,True,40)))




