from unittest import TestCase

from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.SerieBuilder import SerieBuilder
from mMath.data.timeSerie.stochasticProcess.state.State import State
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.FromStateSerieBuilder import FromStateSerieBuilder
from mMath.data.timeSerie.stochasticProcess.state.transitionMatrix.TransitionMatrix import TransitionMatrix


class TestFromStatesSerieBuilder(TestCase):

    def test_get_transition_dictionary(self):
        state1 = State()
        state2 = State()
        state3 = State()
        stateSet = (state1, state2, state3)

        stateSerieBuilder = SerieBuilder(stateSet)

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

        stateSerie: Serie = stateSerieBuilder.getSerie()
        transMatrixBuilder:FromStateSerieBuilder  = FromStateSerieBuilder(stateSerie,stateSet)
        transitionMatrix:TransitionMatrix = transMatrixBuilder.getTransitionMatrix()
        transDic = transitionMatrix.getTransitionDictionary()
        self.assertAlmostEqual(transDic[state2.getId()][state1.getId()], 0.083333333,5)
        self.assertAlmostEqual(transDic[state3.getId()][state2.getId()],0.16666666,5)
        self.assertEqual(transDic[state3.getId()][state1.getId()], 0)

