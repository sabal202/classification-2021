from .vp9 import decoder as vp9_decoder
from .mpeg import decoder as mpeg_decoder

print('Import {}, {}'.format(__name__, __package__))

def play():
    vp9_decoder.decode()
    mpeg_decoder.decode()