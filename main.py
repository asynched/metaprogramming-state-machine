from mutation import StateMachine
from mutation.decorators import state_machine
from mutation.interfaces import AbstractStateMachine


@state_machine
class VideoState(AbstractStateMachine):
    PLAYING = 'playing'
    PAUSED = 'paused'
    STOPPED = 'stopped'

    INITIAL_STATE = STOPPED
    MUTATION_SCHEMA = [
        {
            'trigger': 'play',
            'source': PAUSED,
            'destination': PLAYING,
        },
        {
            'trigger': 'play',
            'source': STOPPED,
            'destination': PLAYING,
        },
        {
            'trigger': 'pause',
            'source': PLAYING,
            'destination': PAUSED,
        },
        {
            'trigger': 'stop',
            'source': PLAYING,
            'destination': STOPPED,
        },
        {
            'trigger': 'stop',
            'source': PAUSED,
            'destination': STOPPED,
        },
    ]


if __name__ == '__main__':
    StateMachine.DEBUG = True

    video = VideoState()
    video.play()
    video.pause()
    video.stop()
    video.pause()
