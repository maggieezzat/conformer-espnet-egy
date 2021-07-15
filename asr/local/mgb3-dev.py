import os
import random

trans_mgb3_dev = '/scratch/mezzat/supervised-audio-data-8k/test-data-8k/mgb3-dev/mgb3-dev.trans.txt'

mgb3_dev = []

with open(trans_mgb3_dev, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        mgb3_dev.append((id, path, trans))


mgb3_dev_path = 'data/mgb3-dev'
os.makedirs(mgb3_dev_path, exist_ok=True)

with open(os.path.join(mgb3_dev_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(mgb3_dev_path, 'text'), 'w') as text_f, open(os.path.join(mgb3_dev_path, 'utt2spk'), 'w') as utt2spk:
    for wave in mgb3_dev:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

