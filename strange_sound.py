import soundfile as sf

data, samplerate = sf.read('StrangeSounds.wav')


isUp = False
start_index = 0

final = []
current = []

for index, value in enumerate(data):
    if isUp and value == 0:
        length = index - start_index
        if length > 100:
            current.append(str(int(length > 1000)))

        if len(current) == 8:
            final.append(current[:])
            current = []
        isUp = False

    elif not isUp and value != 0:
        start_index = index
        isUp = True

for x in final:
    print("".join(x))
