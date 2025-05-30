import pytest

from statemachines_orchestrator.exceptions import (
    StateFieldIsNotUnique,
    NoMachinesOnOrchestrator,
    AnnotationIsNotAStateMachine,
)
from statemachines_orchestrator.orchestrator import Orchestrator
from tests.utils import Dummy, OrchestratorAB, MachineA, MachineB


def test_unique_state_field_enforcement():
    dummy = Dummy()
    with pytest.raises(StateFieldIsNotUnique):
        OrchestratorAB(
            a=MachineA(model=dummy),
            b=MachineB(model=dummy),
        )
    with pytest.raises(StateFieldIsNotUnique):
        OrchestratorAB(
            a=MachineA(model=dummy, state_field="same"),
            b=MachineB(model=dummy, state_field="same"),
        )


def test_no_machines_on_orchestrator():
    with pytest.raises(NoMachinesOnOrchestrator):

        class EmptyOrchestrator(Orchestrator):
            pass


def test_annotation_is_not_a_statemachine():
    with pytest.raises(AnnotationIsNotAStateMachine):

        class BadOrchestrator(Orchestrator):
            foo: str
