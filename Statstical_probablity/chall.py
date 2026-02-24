pepole = 100
cancer_patients = 10
smokers = 40
smokers_with_cancer = 8

p_cancer_given_smoker = smokers_with_cancer / smokers
P_smoker_given_cancer = smokers_with_cancer / cancer_patients
print("P(Cancer | Smoker):", p_cancer_given_smoker)
print("P(Smoker | Cancer):", P_smoker_given_cancer)
