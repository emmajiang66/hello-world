#!/bin/bash

TIMEOUT=10


for LAMBDA in 0.1 0.01 0.001
do
  for LR in 0.1 0.01 0.001
  do
    for NS in 10 20 30 40 50 60 70 80 90 100
        python ca3.py --timeout $TIMEOUT --lambda $LAMBDA --w_size $NS --lr $LR gd >> runs.json
        python ca3.py --timeout $TIMEOUT --lambda $LAMBDA --w_size $NS --lr $LR PGD >> runs.json
        python ca3.py --timeout $TIMEOUT --lambda $LAMBDA --w_size $NS --lr $LR BCD >> runs.json
        for BATCH_SIZE in 1
        do
          python ca3.py --timeout $TIMEOUT --lambda $LAMBDA --w_size $NS --lr $LR sgd --batch_size $BATCH_SIZE >> runs.json

          for EPOCH_SIZE in 1 2 3 4 5 6 7 8 9 10
          do
            python ca3.py --timeout $TIMEOUT --lambda $LAMBDA --w_size $NS --lr $LR svrg --batch_size $BATCH_SIZE --epoch_size $EPOCH_SIZE >> runs.json
          done
        done
    done
  done

done
