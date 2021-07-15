#!/bin/bash

sets="coll-dev-10 colloquial colloquial-speed mgb3_adapt_noise mgb3-dev msa_noise coll-dev-new colloquial-noise mgb3_adapt mgb3_adapt_speed msa msa_speed"

for x in $sets; do
    spk2utt=data/${x}/spk2utt
    utt2spk=data/${x}/utt2spk
    text=data/${x}/text
    wav_scp=data/${x}/wav.scp
    sort -o $utt2spk $utt2spk
    sort -o $text $text
    sort -o $wav_scp $wav_scp
    utils/utt2spk_to_spk2utt.pl <$utt2spk >$spk2utt || exit 1
    utils/validate_data_dir.sh --no-feats data/${x} || exit 1
done