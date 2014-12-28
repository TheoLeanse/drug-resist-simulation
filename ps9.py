# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b2 import *
#from ps8b_precompiled_27 import *
from pylab import *


#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    timeRange={
        300: '300 steps before drug',
        150: '150 steps before drug',
        75: '75 steps before drug',
        0: '0 steps before drug'
        }
    allViruses = []
    for e in timeRange:
        numViruses = []
        for i in range(numTrials):
            numViruses.append(singleSimulation(e))# call helper to run one simulation for one time range, and return virus population
        allViruses.append(numViruses)

##    print allViruses
    
    subplot(221)
    pylab.hist(allViruses[0],)
    grid(True)
    title('timesteps before adminstrating drug')
    ylabel('300 steps')
    
    subplot(222)
    pylab.hist(allViruses[1],)
    grid(True)
    ylabel('150 steps')

    subplot(223)
    pylab.hist(allViruses[2],)
    grid(True)
    ylabel('75 steps')
    xlabel('number of viruses')
    
    subplot(224)
    pylab.hist(allViruses[3],)
    grid(True)
    ylabel('0 steps')
##    
    pylab.show()
##    
def singleSimulation(timeRange):
    """
    takes as input a number of initial trials to run, before administering drug 'guttagonal'
    and running an additonal 150 timesteps
    """
    viruses = []
    for i in range(100):
        viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))
        
    patient1 = TreatedPatient(viruses, 1000)

    numViruses = 0
    for i in xrange(0, timeRange + 150):
##        print patient1.getTotalPop()
        if i == timeRange:
            patient1.addPrescription('guttagonal')
        try:
            viruses.append(patient1.update())
        except AssertionError:
            pass
    return viruses[-1]





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
