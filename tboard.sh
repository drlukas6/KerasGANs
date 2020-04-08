echo "Starting Tensorboard on tf_logs/$1"
tensorboard --logdir=./tf_logs/"$1" --port=6007
