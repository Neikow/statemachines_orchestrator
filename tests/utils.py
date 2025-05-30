from statemachine import StateMachine, State

from statemachines_orchestrator.orchestrator import Orchestrator


class MachineA(StateMachine):
    S1 = State("S1", initial=True)
    S2 = State("S2")
    S3 = State("S3", final=True)
    s1_to_s2 = S1.to(S2)
    s2_to_s3 = S2.to(S3)


class MachineB(StateMachine):
    X1 = State("X1", initial=True)
    X2 = State("X2", final=True)
    x1_to_x2 = X1.to(X2)


class OrchestratorAB(Orchestrator):
    a: MachineA
    b: MachineB


class Dummy:
    pass
