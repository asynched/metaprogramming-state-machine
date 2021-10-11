from mutation.exceptions.mutation import MutationError as _MutationError
from mutation.utils.lists import unique as _unique


class StateMachine(type):
    DEBUG = False

    def __new__(cls, name, bases, attrs):
        methods = [method for method in attrs['MUTATION_SCHEMA']]

        state_mutations = StateMachine.map_state_mutations(methods)

        for mutation_name in state_mutations:
            mutation_structure = state_mutations[mutation_name]

            mutation = StateMachine.make_mutation(
                mutation_name,
                mutation_structure['destination'],
                mutation_structure['states'],
            )

            attrs[mutation_name] = mutation

        attrs['__init__'] = StateMachine.make_initializer_method(attrs['INITIAL_STATE'])

        return type(name, bases, attrs)

    def make_initializer_method(initial_state: any):
        def initializer_method(self):
            self.state = initial_state

        return initializer_method

    def map_state_mutations(methods: list) -> dict:
        state_mutations = {}

        for method in methods:
            if (method_name := method['trigger']) in state_mutations:
                state_mutation = state_mutations[method_name]
                state_mutation['states'].append(method['source'])
            else:
                state_mutations[method['trigger']] = {
                    'states': [method['source']],
                    'destination': method['destination'],
                }

        return state_mutations

    def make_mutation(method_name: str, mutation: any, states: list):
        def method(self):
            allowed_mutations = _unique(states)

            if StateMachine.DEBUG:
                print(f'{method.__name__.upper()}:')
                print(f'{self.state=}')
                print(f'{mutation=}')
                print(f'{allowed_mutations=}', end='\n\n')

            if self.state in allowed_mutations:
                self.state = mutation
                return
            else:
                raise _MutationError(self.state, mutation)

        method.__name__ = method_name

        return method
