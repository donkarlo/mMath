import unittest
from unittest import TestCase

from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.SerieBuilder import SerieBuilder
from mMath.data.timeSerie.stochasticProcess.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.FromStateSerieBuilder import FromStateSerieBuilder
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.TransitionMatrix import TransitionMatrix

if __name__ == '__main__':
    unittest.main()


class TestTransitionMatrix(TestCase):
    def test_get_next_most_probable_state_by_state(self):
        '''

        :return:
        '''
        state1 = State()
        state2 = State()
        state3 = State()
        stateSerieBuilder = SerieBuilder()

        stateSerieBuilder.appendState(state1)
        stateSerieBuilder.appendState(state3)

        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)

        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state3)

        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)

        stateSerieBuilder.appendState(state1)
        stateSerieBuilder.appendState(state1)

        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)

        self.__stateSerie: Serie = stateSerieBuilder.getSerie()
        transMatrixBuilder = FromStateSerieBuilder(self.__stateSerie)
        dict = transMatrixBuilder.getTransitionNpMatrix()

        stateTrMat = TransitionMatrix(dict)
        nextMostProbableStateId = stateTrMat.getNextMostProbableStateIdByState(state3.getId())
        self.assertEqual(nextMostProbableStateId, state2.getId())


