def get_formants(file_path):

    import numpy
    import wave
    import math
    from scipy.signal import lfilter, hamming
    from scipy import signal
    import librosa
    import matplotlib.pyplot as plt
    import librosa.display
    from IPython.display import Audio

    # y = librosa.load('/home/themiszwang/Documentos/IFPI/APRAX/codigoPraat/v1/audios/audio01.wav')
    # window = signal.hamming(len(y[0]), sym=False)
    # window = window.reshape((-1, 1))
    # windowed = y * window

    # Pega o .wav como parâmetro
    audio = wave.open(file_path, 'r')
    # audio = librosa.load(file_path)
    
    # Get file as numpy array.
    x = audio.readframes(-1)
    x = numpy.frombuffer(x, dtype=numpy.int16)

    # Janela de Hamming
    N = len(x)
    w = numpy.hamming(N)

    # Apply window and high pass filter.
    x1 = x * w
    x1 = lfilter([1], [1., 0.63], x1)

    # Get LPC.
    Fs = 44100 # 44100 frequência padrão
    ncoeff = int(2 + Fs / 1000)
    lpc = librosa.lpc(x1, ncoeff)

    # Get roots.
    root = numpy.roots(lpc)
    root = [r for r in root if numpy.imag(r) > 0]

    # Get angles.
    angles = numpy.arctan2(numpy.imag(root), numpy.real(root))

    # Get frequencies.
    frqs = sorted(angles * (Fs / (2 * math.pi)))
    # print('\n')

    # while frqs[0] < 1:  # para retirar os falsos negativos 0.0
    #     del frqs[0]

    return frqs


print(get_formants(
    f'/home/themiszwang/Documentos/IFPI/APRAX/codigoPraat/v1/audios/audio02.wav'))

# def listarF1():

#     lista_f1 = []
#     for i in range (1,8):
#         lista_f1.append(get_formants(f'/home/themiszwang/Documentos/IFPI/APRAX/codigoPraat/v1/audios/audio0{i}.wav')[0]) #pegar apenas f1

#     return lista_f1

# print(listarF1())
