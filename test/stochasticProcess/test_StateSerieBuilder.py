from mMath.data.timeSerie.stochasticProcess.state.Serie import Serie
from mMath.data.timeSerie.stochasticProcess.state.SerieBuilder import SerieBuilder
from mMath.data.timeSerie.stochasticProcess.state.State import State
from mMath.test.stochasticProcess.transitionMatrix.test_FromStatesSerieBuilder import TestFromStatesSerieBuilder


class TestStateSerieBuilder:
    stateSerie: Serie

    def getSerie(self) -> Serie:
        state1 = State()
        state2 = State()
        state3 = State()
        stateSerieBuilder = SerieBuilder()
        stateSerieBuilder.appendState(state1)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state1)
        TestFromStatesSerieBuilder.stateSerie = stateSerieBuilder.getSerie()
        return TestFromStatesSerieBuilder.stateSerie

    def test_getSeire(self):
        state1 = State()
        state2 = State()
        state3 = State()
        stateSerieBuilder = SerieBuilder()
        stateSerieBuilder.appendState(state1)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state1)
        self.__stateSerie: Serie = stateSerieBuilder.getSerie()
        self.assertEqual(self.__stateSerie.getLength(), 7)

    def test_appendState(self):
        state1 = State()
        state2 = State()
        state3 = State()
        stateSerieBuilder = SerieBuilder()
        stateSerieBuilder.appendState(state1)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state3)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state2)
        stateSerieBuilder.appendState(state1)
        self.__stateSerie: Serie = stateSerieBuilder.getSerie()
        self.assertEqual(self.__stateSerie.getLength(), 8)