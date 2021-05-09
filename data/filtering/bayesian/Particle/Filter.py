from typing import List
from mmath.data.filtering.Filter import Filter as MainFilter
from mmath.data.filtering.bayesian.Particle import ParticlePosVel
from mmath.data.filtering.bayesian.Particle.Particle import Particle
from mmath.data.probability.ConditionalPdf import ConditionalPdf
from mmath.linearalgebra.Matrix import Matrix
from mmath.linearalgebra.tensor.Kernel import Kernel
from state import State
from state.stateProcess.MeasurementEquation import MeasurementEquation
from state.stateProcess.StateEquation import StateEquation


class Filter(MainFilter):
    ''''''

    def __init__(self
                 , initState: State
                 , regionOfIntrestDistribution:Matrix
                 , particlesNum:int
                 , conditionalPdf:ConditionalPdf
                 ,kernel0:Kernel
                 ,kernel1:Kernel):
        '''
        @todo ROI can be a distribution too

        Parameters
        -----------

        '''
        self.__initState: State = initState
        self.__currentParticles = None
        self.__particlesNum = particlesNum
        self.__regionOfInterestDistribution = regionOfIntrestDistribution
        self.__conditionalPDf = conditionalPdf

        self.__kernel0: Kernel = kernel0
        self.__kernel1: Kernel = kernel1

        super().__init__()

    def initialize(self):
        pass

    # def __senseFunction(self, particle: Particle)->float:
    #     '''z(x_t)~\sum f(x|mean(x),var(x)) and f=mmath.data.pdf.Normal(mean(x),var(x))
    #     measures particle's (position,velocity) likelihood based on observation
    #     x is the  measured distance between the particle and the given landmarke
    #     x_t is the particle
    #     \mu is the theoretical distance between the measured distance and the landmark
    #     '''
    #     pass

    def __generateCurrentParticles(self,size:int)->None:
        ''''''
        pass

    def __getCurrentParticles(self)->List[ParticlePosVel]:
        ''''''
        if self.__currentParticles is None:
            self.__generateCurrentParticles()
        return self.__currentParticles

    def moveParticlesTowardCurrentStateByStateEquation(self,stateEquation:StateEquation):
        ''''''
        currentPredictedState:State = stateEquation.getCurrentState()
        particle:Particle
        for particle in self.__getCurrentParticles():
            moveRate:float=particle.getState().getDistanceFrom(currentPredictedState)/100
            particle.getState().moveTowardVecByRate(currentPredictedState,moveRate)

    def getpPredictedObservationFromPredictedStateByMeasurementEquation(self
                                                                        ,measurementEquation:MeasurementEquation
                                                                        ,predictedState:  State):
        ''''''
        pass

    def updateCurrentParticlesBelief(self):
        ''''''
        for particle in self.__currentParticles:
            pass

    def resampleCurrentParticlesAccordingImportanceWeightBelief(self):
        ''''''
        pass

    def computeBestParticleInCurrentParticles(self):
        ''''''
        pass

    def __getParticleWeight(self, particle)->float:
        ''''''
        thisParticleKernel = self.__kernel0.getValue(particle.getMeasuredObservation() - particle.getPredictedObservation())

        kernelSum = 0
        particleInLoop:Particle
        for particleInLoop in self.__currentParticles:
            kernelSum += self.__kernel0.getValue(particleInLoop.__measuredObservation - particleInLoop.__predictedObservation)

        return thisParticleKernel/kernelSum


    def getEstimatedDensity(self,x):
        ''''''
        sum = 0
        particleInLoop:Particle
        for particleInLoop in self.__currentParticles:
            sum += self.__getParticleWeight(particleInLoop)*self.__kernel1.getValue(x - particleInLoop.getPredictedState())








