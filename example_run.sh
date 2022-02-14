# This script runs first lightl-magic and then executes coreset on the embedded
# images. The full dataset and sampled images can then be explored in the
# Lightly WebApp.
# 
# Required environment variables:
# - TOKEN
#
# Optional environment variables:
# - LIGHTLY_SERVER_LOCATION 
#   Can be used to change the server location, is `https://api.lightly.ai` by default.
#   Set, for example, to `http://api.lightly-docker` for local usage.


# train, embed and upload the data
lightly-magic token=${TOKEN} input_dir="/datasets/my-dataset" new_dataset_name="my-dataset-name" trainer.max_epochs=1 loader.num_workers=8

# run coreset sampling
# Important: 
# - Use the same dataset name as before
# - Remember to set a new tag name
# - The --output-file option is optional
# - You can also use --dataset-id instead of --dataset-name
python run_coreset.py --token=${TOKEN} --dataset-name="my-dataset-name" --new-tag-name="my-tag-name" --num-samples=5 --output-file=filenames.txt