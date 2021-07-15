import os
import random

trans_coll_dev_10 = '/scratch/mezzat/supervised-audio-data-8k/test-data-8k/coll-dev-10/coll-dev-10.trans.txt'

coll_dev_10 = []

with open(trans_coll_dev_10, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        coll_dev_10.append((id, path, trans))


coll_dev_10_path = 'data/coll-dev-10'
os.makedirs(coll_dev_10_path, exist_ok=True)

with open(os.path.join(coll_dev_10_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(coll_dev_10_path, 'text'), 'w') as text_f, open(os.path.join(coll_dev_10_path, 'utt2spk'), 'w') as utt2spk:
    for wave in coll_dev_10:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

