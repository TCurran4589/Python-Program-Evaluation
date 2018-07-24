import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''

# TO DO:
    * Document Code
    * Add Function and variable descriptions in function
    * Unit Test
    * Error Handling

'''




def manski_bounds(treatment_status, before, after, graph = True):

    treated = []

    untreated = []

    prob_d1 = sum(treatment_status) / len(treatment_status)

    prob_d0 = (1 - prob_d1)

    collection = list(zip(treatment_status, before, after))

    for i in range(0, len(collection)):
        if(collection[i][0] == 1):
            treated.append(collection[i][2])
        else:
            untreated.append(collection[i][2])

    treated_expVal = np.mean(treated)
    untreated_expVal = np.mean(untreated)

    ##### Upper Bound #####

    treated_bounds = []
    untreated_bounds = []
    i = 0

    while i <= 1:
        bnds_t = prob_d1 * treated_expVal + prob_d0*i
        treated_bounds.append(bnds_t)
        bnds_ut = prob_d1 * i + prob_d0*untreated_expVal
        untreated_bounds.append(bnds_ut)

        i += 1

    if graph == True:

        plt.plot(np.array(["Treated", "Treated"]), treated_bounds)
        plt.plot(np.array(['Untreated', 'Untreated']), untreated_bounds, color = 'red')
        plt.title(r"Manski Bounds for Treated and Untreated Groups")
        plt.text(.01, treated_bounds[1], ("Treated Upper Bound: "+str(round(treated_bounds[1],2))))
        plt.text(.01, treated_bounds[0], ("Treated Lower Bound: "+str(round(treated_bounds[0],2))))
        plt.text(.55, untreated_bounds[1], "Treated Upper Bound: "+str(round(untreated_bounds[1],2)))
        plt.text(.55, untreated_bounds[0], "Treated Lower Bound: "+str(round(untreated_bounds[0],2)))
        plt.ylabel("Treatment Effect")

    ate_ub = treated_bounds[1] - untreated_bounds[0]
    ate_lb = treated_bounds[0] - untreated_bounds[1]

    print("Average Treatment Effect Upper Bound: {}".format(round(ate_ub,4)))
    print("Average Treatment Effect Lower Bound: {}".format(round(ate_lb,4)))

    return(treated_bounds, untreated_bounds, ate_ub, ate_lb)
