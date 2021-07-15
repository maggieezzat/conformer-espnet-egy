import os
import random

trans_msa = '/scratch/mezzat/supervised-audio-data-8k/modern-standard-arabic-8k/msa/msa.trans.txt'
trans_msa_speed = '/scratch/mezzat/supervised-audio-data-8k/modern-standard-arabic-8k/msa_speed_08_12/msa_speed_08_12.trans.txt'
trans_msa_noise = '/scratch/mezzat/supervised-audio-data-8k/modern-standard-arabic-8k/msa_noise_05/msa_noise_05.trans.txt'

msa = []
msa_speed = []
msa_noise = []

with open(trans_msa, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        msa.append((id, path, trans))

with open(trans_msa_speed, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        msa_speed.append((id, path, trans))

with open(trans_msa_noise, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        msa_noise.append((id, path, trans))

msa_path = 'data/msa'
os.makedirs(msa_path, exist_ok=True)

with open(os.path.join(msa_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(msa_path, 'text'), 'w') as text_f, open(os.path.join(msa_path, 'utt2spk'), 'w') as utt2spk:
    for wave in msa:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

msa_speed_path = 'data/msa_speed'
os.makedirs(msa_speed_path, exist_ok=True)

with open(os.path.join(msa_speed_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(msa_speed_path, 'text'), 'w') as text_f, open(os.path.join(msa_speed_path, 'utt2spk'), 'w') as utt2spk:
    for wave in msa_speed:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')


msa_noise_path = 'data/msa_noise'
os.makedirs(msa_noise_path, exist_ok=True)

with open(os.path.join(msa_noise_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(msa_noise_path, 'text'), 'w') as text_f, open(os.path.join(msa_noise_path, 'utt2spk'), 'w') as utt2spk:
    for wave in msa_noise:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

