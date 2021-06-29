import os
import random

valid_percent = 0.01
test_percent = 0.01

#data_path = '/scratch/mezzat/supervised-audio-data/egyptian-colloquial-arabic/Colloquial-Waves'
trans_path_coll = '/scratch/mezzat/supervised-audio-data/egyptian-colloquial-arabic/Colloquial-Waves/Colloquial-Waves.trans.txt'
trans_path_msa = '/scratch/mezzat/supervised-audio-data/modern-standard-arabic/msa/waves.trans.txt'

msa = []
coll = []

with open(trans_path_msa, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        id = path.split("/")[-1]
        id = id[:-4]
        trans = line[1]
        msa.append((id, path, trans))

with open(trans_path_coll, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        id = path.split("/")[-1]
        id = id[:-4]
        trans = line[1]
        coll.append((id, path, trans))

random.seed(575)
random.shuffle(coll)
dev_waves = coll[:5000]
coll = coll[5000:]
test_waves = coll[:5000]
coll = coll[5000:]
train_waves = coll + msa

train_path = 'data/train'

with open(os.path.join(train_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(train_path, 'text'), 'w') as text_f, open(os.path.join(train_path, 'utt2spk'), 'w') as utt2spk:
    for train_wave in train_waves:
        wav_scp.write(train_wave[0] + ' ' + train_wave[1] + '\n')
        text_f.write(train_wave[0] + ' ' + train_wave[2] + '\n')
        utt2spk.write(train_wave[0] + ' ' + train_wave[0] + '\n')

dev_path = 'data/dev'

with open(os.path.join(dev_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(dev_path, 'text'), 'w') as text_f, open(os.path.join(dev_path, 'utt2spk'), 'w') as utt2spk:
    for dev_wave in dev_waves:
        wav_scp.write(dev_wave[0] + ' ' + dev_wave[1] + '\n')
        text_f.write(dev_wave[0] + ' ' + dev_wave[2] + '\n')
        utt2spk.write(dev_wave[0] + ' ' + dev_wave[0] + '\n')


test_path = 'data/test'

with open(os.path.join(test_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(test_path, 'text'), 'w') as text_f, open(os.path.join(test_path, 'utt2spk'), 'w') as utt2spk:
    for test_wave in test_waves:
        wav_scp.write(test_wave[0] + ' ' + test_wave[1] + '\n')
        text_f.write(test_wave[0] + ' ' + test_wave[2] + '\n')
        utt2spk.write(test_wave[0] + ' ' + test_wave[0] + '\n')

