import os
import random

trans_coll = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/Colloquial-Waves/Colloquial-Waves.trans.txt'
trans_coll_speed = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/Colloquial-Waves-Speed-08-12/Colloquial-Waves-Speed-08-12.trans.txt'
trans_coll_noise = '/scratch/mezzat/supervised-audio-data-8k/egyptian-colloquial-arabic-8k/Colloquial-Waves-Noise-05/Colloquial-Waves-Noise-05.trans.txt'


coll = []
coll_speed = []
coll_noise = []

with open(trans_coll, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        coll.append((id, path, trans))


dev_ids = {}
random.seed(575)
random.shuffle(coll)
dev_waves = coll[:5000]
dev_waves = list(set(dev_waves))
coll = coll[5000:]

for item in dev_waves:
    dev_ids[item[0]] = item[0]


with open(trans_coll_speed, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        base_id = id.split("_speed")[0]
        if base_id in dev_ids:
            dev_waves.append((id, path, trans))
        else:
            coll_speed.append((id, path, trans))

with open(trans_coll_noise, 'r') as f:
    for line in f:
        line = line.strip().split(" ", 1)
        path = line[0]
        trans = line[1]
        id = path.split("/")[-1]
        id = id[:-4]
        base_id = id.split("_noisy")[0]
        if base_id in dev_ids:
            dev_waves.append((id, path, trans))
        else:
            coll_noise.append((id, path, trans))


dev_path = 'data/coll-dev-new'
os.makedirs(dev_path, exist_ok=True)
with open(os.path.join(dev_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(dev_path, 'text'), 'w') as text_f, open(os.path.join(dev_path, 'utt2spk'), 'w') as utt2spk:
    for wave in dev_waves:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')


coll_path = 'data/colloquial'
os.makedirs(coll_path, exist_ok=True)
with open(os.path.join(coll_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(coll_path, 'text'), 'w') as text_f, open(os.path.join(coll_path, 'utt2spk'), 'w') as utt2spk:
    for wave in coll:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

coll_speed_path = 'data/colloquial-speed'
os.makedirs(coll_speed_path, exist_ok=True)
with open(os.path.join(coll_speed_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(coll_speed_path, 'text'), 'w') as text_f, open(os.path.join(coll_speed_path, 'utt2spk'), 'w') as utt2spk:
    for wave in coll_speed:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')

coll_noise_path = 'data/colloquial-noise'
os.makedirs(coll_noise_path, exist_ok=True)
with open(os.path.join(coll_noise_path, 'wav.scp'), 'w') as wav_scp, open(os.path.join(coll_noise_path, 'text'), 'w') as text_f, open(os.path.join(coll_noise_path, 'utt2spk'), 'w') as utt2spk:
    for wave in coll_noise:
        wav_scp.write(wave[0] + ' ' + wave[1] + '\n')
        text_f.write(wave[0] + ' ' + wave[2] + '\n')
        utt2spk.write(wave[0] + ' ' + wave[0] + '\n')



