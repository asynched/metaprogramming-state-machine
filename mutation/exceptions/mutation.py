class MutationError(Exception):
    def __init__(self, source, destination):
        print(
            f'Current state "{source}" has no mutation defined to "{destination}"'
            '\nIf you want to define a new mutation, please add it to your "MUTATION_SCHEMA"'
        )
