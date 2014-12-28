# 6.00 Problem Set 9

import numpy
import random
import pylab
# from ps8b2 import *
#from ps8b_precompiled_27 import *
from pylab import *
from ps8decomp import *


#
# PROBLEM 1
#

def makeHist(numTrials):
    # for each timerange, call simulationDelayedTreatment
    virusList300 = simulationDelayedTreatment(numTrials, 300)
    virusList150 = simulationDelayedTreatment(numTrials, 150)
    virusList75 = simulationDelayedTreatment(numTrials, 75)
    virusList0 = simulationDelayedTreatment(numTrials, 0)

##    print '300:', virusList300
##    print '150:', virusList150
##    print '75:', virusList75
##    print '0:', virusList0
    # save simDelTreat's output into a list
    
    # plot a histogram with that list. Y-Axis is 0 - numTrials
    yAxis = range(numTrials, 20)
    subplot(221)
    pylab.hist(virusList300) #, yAxis, bins = 10)
    title('timesteps before adminstrating drug')
    ylabel('delay of 2nd drug: 300')
    
    subplot(222)
    pylab.hist(virusList150, 20) #, bins = 10)
    ylabel('delay of 2nd drug: 150')

    subplot(223)
    pylab.hist(virusList75, 20) #, yAxis, bins = 10)
    ylabel('delay of 2nd drug: 75')
    xlabel('number of viruses')
    
    subplot(224)
    pylab.hist(virusList0, 20)
    ylabel('delay of 2nd drug: 0')
    
    pylab.show()


def simulationDelayedTreatment(numTrials, timeRange):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    allViruses = []
    for i in range(numTrials):
        viruses = []
        for i in range(100):
            viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))
        patient1 = TreatedPatient(viruses, 1000)
        
        # run trial, administering drug at point t=timeRange
        for t in range(150 + timeRange + 150):
            if t == 150:
                patient1.addPrescription('guttagonol')
            if t == 150 + timeRange:
                patient1.addPrescription('grimpex')
            try:
                count = patient1.update()
            except AssertionError:
                pass
        allViruses.append(count)
    return allViruses
    


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
