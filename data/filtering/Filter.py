import abc

from mmath.data.probability.Event import Event
from mmath.data.probability.Pdf import Pdf
from state import State
from state.Serie import Serie
from state.observation.ObservationsSerie import ObservationsSerie
from state.observation.Observation import Observation


class Filter(metaclass=abc.ABCMeta):
    ''' In each filtering our goal is to compute the posterior which is state estimation after observation (self.getPosterior)
     first we predict () then we observe and update according to what is observed
    What is the PDF of state with a given set of observation
    if the variables are normally distributed and the transitions are linear, the Bayes filtering becomes equal to the Kalman filtering.
    '''

    def __init__(self):
        #Estimations improve by receiving more observation
        self.__observationSerie:ObservationsSerie = None
        #p(z_k|x_k)
        self.__getLikelihood:float = None
        #p(x_k|z_{1:k-1})
        self.__currentPrior:float = None
        #Acts as a normalizer, a constant which could be regarded as the probability of the measurement, sum(p(z_{1:k}))
        self.__currentMarginalLikelihood:float = None

        self.__stateSerie = None

    def addObservation(self, observation: Observation) -> None:
        '''Whenever a new observation is added prediction and then update should run again'''
        self.__observationSerie.appendObservation(observation)
        self.__stateSerie:Serie = None
        self._predict()
        self._update()

    def _predict(self) -> State:
        '''First setp: predict prior to observation using the StateEquation'''
        self._updatePrior()
        self._updateLikelihood()

    @abc.abstractmethod
    def _update(self, observationSerie: Observation) -> State:
        '''Second step: Update prediction, refining the _pridct sing bayes theorem'''
        pass

    @abc.abstractmethod
    def getPosterior(self):
        '''No stop condition is needed. the last observation is the s'''
        self.__posterior = (self._getLikelihood() * self._getPrior()) / self._getMarginalLikelihood()
        return self.__posterior

    @abc.abstractmethod
    def _getPrior(self)->float:
        ''''''
        pdf = Pdf()
        priorSum:float=0
        stateCounter = 0
        for state in self.__stateSerie:
            priorSum += pdf.getValueByEvent(Event(state).conditionedOn(Event(self.__stateSerie.getByIndex(stateCounter - 1))))
            stateCounter +=1
        self.__currentPrior = priorSum
        return priorSum

    @abc.abstractmethod
    def _getLikelihood(self)->float:
        '''A knowledge which we aquire from characterstics of the sensor
        p(z_k|z:1k-1)
        '''

    def _getMarginalLikelihood(self)->float:
        ''''''
        pdf = Pdf()
        likelihoodSum: float = 0
        stateCounter = 0
        for state in self.__stateSerie:
            likelihoodSum += pdf.getValueByEvent(
                Event(self.__observationSerie.getLastObservation()).conditionedOn(state)) \
                             * pdf.getValueByEvent(Event(state).conditionedOn(
                self.__observationSerie.getObservationSlice(0, self.__observationSerie.getLastObservationIndex() - 1)))
            stateCounter += 1
        self.__currentMarginalLikelihood = likelihoodSum
