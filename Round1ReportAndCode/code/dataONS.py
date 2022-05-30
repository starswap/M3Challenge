#General numbers of people working from home (millions, 2019)
kNoWFH_2019 = 23.769735
kWFH_2019 = 8.615113

#Sex (2019) - WFH Percentage 
kNoWFH_men_2019 = 12.559057
kWFH_men_2019 =  4.59726200 
kNoWFH_women_2019 = 11.210678
kWFH_women_2019 = 4.01785100 
sexWFH = {"men":kWFH_men_2019/(kWFH_men_2019+kNoWFH_women_2019),"women": kWFH_women_2019/(kWFH_men_2019+kNoWFH_women_2019)}

#Ethnicity (2019) - WFH Percentage 
ethnicityWFH = {"white":1-0.726982116699218,"mixed":1-0.677182853221893,"asian":1-0.786816716194152,"black":1-0.825749695301055,"other":1-0.78287649154663}

#Industry (2019)
#Note: Wanted to use BLS categories but the ONS data was given as percentages making combining difficult without the raw totals.
industryFT_WFH = {"AgricultureForestryFishing":1-0.622196853160858,
"MiningUtilities":1-0.760932683944702,
"Manufacturing":1-0.788643658161163,
"Construction":1-0.751720190048217,
"WholesaleRetailRepairOfVehicles":1-0.822654724121093,
"TransportStorage":1-0.883512794971466,
"AccommodationFoodServices":1-0.856739997863769,
"InformationCommunication":1-0.530150711536407,
"FinancialServicesRealEstate":1-0.638728022575378,
"ProfScientificTechnicalActiv":1-0.590569615364074,
"AdminSupportServices":1-0.747599959373474,
"PublicAdminDefence":1-0.708281695842742,
"Education":1-0.60731154680252,
"HealthSocialWork":1-0.771711289882659,
"OtherServices": 1-0.660328805446624}

industryPT_WFH = {
"AgricultureForestryFishing":1-0.744184255599975,
"MiningUtilities":1-0.653858661651611,
"Manufacturing":1-0.721013069152832,
"Construction":1-0.657320737838745,
"WholesaleRetailRepairOfVehicles":1-0.917843580245971,
"TransportStorage":1-0.865761935710906,
"AccommodationFoodServices":1-0.93391728401184,
"InformationCommunication":1-0.497111767530441,
"FinancialServicesRealEstate":1-0.628497898578643,
"ProfScientificTechnicalActiv":1-0.505080223083496,
"AdminSupportServices":1-0.806695878505706,
"PublicAdminDefence":1-0.744857549667358,
"Education":1-0.728527069091796,
"HealthSocialWork":1-0.824699640274047,
"OtherServices":1-0.748933792114257
}

#Education
educationWFH = {
  "noQualifications":1-0.892920076847076,
  "entryLevel":1-0.837141454219818,
  "gcseOrEquiv":1-0.780677258968353,
  "aLevelOrEquiv":1-0.722423911094665,
  "degreeOrEquiv":1-0.649750053882598,
  "higherDegree":1-0.573047816753387
}


industryFT_WFH = {"AgricultureForestryFishing":1-0.622196853160858,
"MiningUtilities":1-0.760932683944702,
"Manufacturing":1-0.788643658161163,
"Construction":1-0.751720190048217,
"WholesaleRetailRepairOfVehicles":1-0.822654724121093,
"TransportStorage":1-0.883512794971466,
"AccommodationFoodServices":1-0.856739997863769,
"InformationCommunication":1-0.530150711536407,
"FinancialServicesRealEstate":1-0.638728022575378,
"ProfScientificTechnicalActiv":1-0.590569615364074,
"AdminSupportServices":1-0.747599959373474,
"PublicAdminDefence":1-0.708281695842742,
"Education":1-0.60731154680252,
"HealthSocialWork":1-0.771711289882659,
"OtherServices": 1-0.660328805446624}

#D3 remote work data -> matched up against industries from the ONS.
P_RIndustry = {"AgricultureForestryFishing":0.01,
"MiningUtilities":0.01,
"Manufacturing":0.01,
"Construction":0.01,
"WholesaleRetailRepairOfVehicles":0.28,
"TransportStorage":0.03,
"AccommodationFoodServices":0.05,
"InformationCommunication":1,
"FinancialServicesRealEstate":0.88,
"ProfScientificTechnicalActiv":0.98,
"AdminSupportServices":0.65,
"PublicAdminDefence":0.97,
"Education":0.98,
"HealthSocialWork":0.37,
"OtherServices":0.25}
