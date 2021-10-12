from mutation import StateMachine as _StateMachine
from mutation.interfaces import AbstractStateMachine as _AbstractStateMachine


def state_machine(base: _AbstractStateMachine):
    methods = [method for method in base.MUTATION_SCHEMA]

    state_mutations = _StateMachine.map_state_mutations(methods)

    for mutation_name in state_mutations:
        mutation_structure = state_mutations[mutation_name]

        mutation = _StateMachine.make_mutation(
            mutation_name,
            mutation_structure['destination'],
            mutation_structure['states'],
        )

        setattr(base, mutation_name, mutation)

    base.__init__ = _StateMachine.make_initializer_method(base.INITIAL_STATE)

    return base
