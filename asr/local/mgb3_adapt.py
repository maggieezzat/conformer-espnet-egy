import os
import random

trans_mgb3 = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/mgb3-adapt/mgb3-adapt.trans.txt'
trans_mgb3_speed = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/mgb3-adapt-speed-08-12/mgb3-adapt-speed-08-12.trans.txt'
trans_mgb3_noise = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/mgb3-adapt-noise-05/mgb3-adapt-noise-05.trans.txt'

mgb3 = []
mgb3_speed = []
mgb3_noise = []

with open(trans_mgb3, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        mgb3.append((id, path, trans))

with open(trans_mgb3_speed, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        mgb3_speed.append((id, path, trans))

with open(trans_mgb3_noise, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        mgb3_noise.append((id, path, trans))

mgb3_path = 'data/mgb3_adapt'
os.makedirs(mgb3_path, exist_ok=True)

with open(os.path.join(mgb3_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(mgb3_path, 'text'), 'w') as text_f, open(os.path.join(mgb3_path, 'utt2spk'), 'w') as utt2spk:
    for wave in mgb3:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

mgb3_speed_path = 'data/mgb3_adapt_speed'
os.makedirs(mgb3_speed_path, exist_ok=True)

with open(os.path.join(mgb3_speed_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(mgb3_speed_path, 'text'), 'w') as text_f, open(os.path.join(mgb3_speed_path, 'utt2spk'), 'w') as utt2spk:
    for wave in mgb3_speed:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')


mgb3_noise_path = 'data/mgb3_adapt_noise'
os.makedirs(mgb3_noise_path, exist_ok=True)

with open(os.path.join(mgb3_noise_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(mgb3_noise_path, 'text'), 'w') as text_f, open(os.path.join(mgb3_noise_path, 'utt2spk'), 'w') as utt2spk:
    for wave in mgb3_noise:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

