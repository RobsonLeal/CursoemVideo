# tocando um som wav


print('### EXERCÍCIO 21 # AULA 08 ###')
print('==============================')

import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("021.wav")
play_obj = wave_obj.play()
play_obj.wait_done()