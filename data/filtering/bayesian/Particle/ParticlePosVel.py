from mmath.linearalgebra.Vector import Vector

from state.control import Input
from state.control.InputSerie import ActionSerie
from state.control.InputSerieBuilder import ActionSerieBuilder
from state.observation.Observation import Observation
from state.observation.ObservationsSerie import ObservationsSerie
from state.observation.ObservationSerieBuilder import ObservationSerieBuilder


class Particle:
    def __init__(self):
        self.__time = None
        #belief function over particle, is proportionate likelihood that the robot is in refVec
        self.__importanceWeightBelief:float = 0

        #a vector from region of intrest - dustribution in GNG - a point in map - (position,velocity)
        self.__estimatedPose:Vector = None
        self.__estimatedVelocity:Vector = None

        self.__observationSerie:ObservationsSerie = None
        self.__actionSerie:ActionSerie = None

        #Builders
        self.__observationSerieBuilder:ObservationSerieBuilder = ObservationSerieBuilder()
        self.__actionSerieBuilder:ActionSerieBuilder = ActionSerieBuilder()

    # def getParticleLikelihood(self, newObservation:Observation, newAction:Action, proportionRate:float)->float:
    #     self.appendNewObservation(newObservation)
    #     self.appendNewAction(newAction)
    #     a:float = proportionRate *self.__importanceWeightBelief* self.__conditionalPDf(self.__refVec
    #                                                      ,  [self.__observationSerieBuilder.getObservationSerie
    #                                                      , self.__actionSerieBuilder.getActionsSerie()])
    #
    #     return a

    def appendNewAction(self, newAction: Input)->None:
        self.__actionSerieBuilder.appendAction(newAction)

    def appendNewObservation(self,newObservation:Observation)->None:
        self.__observationSerieBuilder.appendObservation(newObservation)

    def getObservationSerie(self)->ObservationsSerie:
        return self.__observationSerieBuilder.getObservationSerie()

    def getActionSerie(self)->ActionSerie:
        return self.__actionSerieBuilder.getActionsSerie()

    def __setApproximatedAction(self)-> Input:
        '''by velcoty changes'''

    def __setUpdatedPosition(self):
        ''''''

    def evaluateImportanceWeightBeliefBasedOnMapRestrictions(self)->float:
        ''''''
        #todo evaluation of weights from here



