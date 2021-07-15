#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print com$
set -e
set -u
set -o pipefail

train_set="colloquial"
valid_set="coll-dev-new"
test_sets="coll-dev-10 mgb3-dev"

#train_set="msa msa_noise msa_speed"

asr_config=conf/tuning/train_asr_conformer7_n_fft512_hop_length256.yaml
lm_config=conf/tuning/train_lm_transformer2.yaml
inference_config=conf/decode_asr.yaml

SECONDS=0
nodes=1
gpus=4
      
./asr.sh \
    --lang ar \
    --nbpe 5000 \
    --asr_config "${asr_config}" \
    --inference_config "${inference_config}" \
    --train_set "${train_set}" \
    --valid_set "${valid_set}" \
    --test_sets "${test_sets}" \
    --ngpu $gpus \
    --num_nodes $nodes \
    --feats_type 'fbank_pitch' \
    --use_lm false --stage 3 --stop_stage 3

#./asr.sh \
#    --lang en \
#    --nbpe 5000 \
#    --max_wav_duration 30 \
#    --asr_config "${asr_config}" \
#    --lm_config "${lm_config}" \
#    --inference_config "${inference_config}" \
#    --train_set "${train_set}" \
#    --valid_set "${valid_set}" \
#    --test_sets "${test_sets}" \
#    --lm_train_text "data/${train_set}/text data/local/other_text/text" \
#    --bpe_train_text "data/${train_set}/text" "$@" \
#    --ngpu $gpus \
#    --num_nodes $nodes \
#    --use_lm false

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed on $n node(s)"

