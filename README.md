# Lightly Sampling Automation

Utility code to trigger a coreset sampling through the Lightly API. 

An example of the workflow is provided in [`example_run.sh`](https://github.com/lightly-ai/sampling-automation/blob/main/example_run.sh), 
including the initial dataset creation, model training, data embedding, 
data upload, and coreset sampling.

### Requirements

[Lightly](https://github.com/lightly-ai/lightly) must be installed:
```
pip install lightly
```

### Usage

First, a dataset must be created and embeddings uploaded to Lightly. This is best
done with the [Lightly Magic Command](https://docs.lightly.ai/getting_started/command_line_tool.html#training-embedding-and-uploading-in-a-go-magic).

Let's say you created a dataset with the name "my-dataset-name". We can then run 
a sampling on the dataset as follows:
```
python run_coreset.py --token=${TOKEN} --dataset-name="my-dataset-name" --new-tag-name="my-tag-name" --num-samples=5
```

The `--token` is your Lightly API access token. `--dataset-name` is the name of the
dataset you want to subsample. `--new-tag-name` is the name of the tag that 
should be created after sampling and will contain all the sampled images.
`--num-samples` is the number of images that should be sampled.

### Configuration

#### Server Location

The Lightly Server location is controlled by the `LIGHTLY_SERVER_LOCATION` 
environment variable (`'https://api.lightly.ai'` by default). Make sure to set
it before running the script if you have a local deployment, for example:
```
export LIGHTLY_SERVER_LOCATION='http://api.lightly-docker'
python run_coreset.py ...
```

#### Dataset Name/Dataset ID

The script allows you to either specify the dataset by name (`--dataset-name`)
or the by id (`--dataset-id`). It does not matter which one you use, just make
sure that it refers to the dataset you uploaded before to the Lightly platform.

#### Saving the sampled filenames

The `--output-file` option allows you to save the filenames of the sampled
images to a file. The fill will contain one filename per line:
```
img1.png
img4.png
img10.png
```

#### run_coreset.py options

Output from `python run_coreset.py --help`:

```
usage: Coreset Sampling [-h] [--token TOKEN] (--dataset-name DATASET_NAME | --dataset-id DATASET_ID) --new-tag-name NEW_TAG_NAME --num-samples NUM_SAMPLES [--output-file OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         API token. If not specified the TOKEN environment variable is used instead.
  --dataset-name DATASET_NAME
                        The name of the dataset from which to create the sampling.
  --dataset-id DATASET_ID
                        The dataset id from which to create the sampling.
  --new-tag-name NEW_TAG_NAME
                        The name of the tag that gets created by the sampling.
  --num-samples NUM_SAMPLES
                        Number of samples to select, must be larger than 0.
  --output-file OUTPUT_FILE
                        File in which sampled filenames should be stored.
```