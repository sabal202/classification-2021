
from .vorbis import decode as vorbis_decoder
from .mpeg import decode as mpeg_decoder

print('Import {}, {}'.format(__name__, __package__))

def play():
    vorbis_decoder()
    mpeg_decoder()