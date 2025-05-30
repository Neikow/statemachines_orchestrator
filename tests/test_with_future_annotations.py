from __future__ import annotations

from statemachines_orchestrator.orchestrator import Orchestrator
from tests.utils import MachineA


def test_orchestrator_with_state_machine_type_annotation_should_compile():
    class _StateMachineOrchestrator(Orchestrator):
        machineA: MachineA
