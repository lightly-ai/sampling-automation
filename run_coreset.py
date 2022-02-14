import argparse
import os

import lightly
from lightly.active_learning.config import SamplerConfig
from lightly.openapi_generated.swagger_client import SamplingMethod


parser = argparse.ArgumentParser("Coreset Sampling")

parser.add_argument(
    "--token",
    default=os.environ.get("TOKEN"),
    help=(
        "API token. If not specified the TOKEN environment variable is used "
        "instead."
    )
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    '--dataset-name',
    type=str,
    help="The name of the dataset from which to create the sampling."
)
group.add_argument(
    '--dataset-id',
    type=str,
    help="The dataset id from which to create the sampling."
)
parser.add_argument(
    '--new-tag-name',
    type=str,
    required=True,
    help="The name of the tag that gets created by the sampling.",
)
parser.add_argument(
    '--num-samples',
    type=int,
    required=True,
    help="Number of samples to select, must be larger than 0."
)
parser.add_argument(
    "--output-file",
    help="File in which sampled filenames should be stored."
)


def main(args):
    if args.num_samples < 1:
        raise ValueError(f"--num-samples must be > 0 but is {args.num_samples}")

    print('Connecting to the API')
    client = lightly.api.ApiWorkflowClient(
        token=args.token,
        dataset_id=args.dataset_id,
    )
    
    if args.dataset_name:
        client.set_dataset_id_by_name(args.dataset_name)
    
    sampler_config = SamplerConfig(
        method=SamplingMethod.CORESET,
        n_samples=args.num_samples,
        name=args.new_tag_name,
    )
    print('Running CORESET sampling')
    new_tag_data = client.sampling(sampler_config=sampler_config)
    if args.output_file:
        print(f'Saving filenames to {args.output_file}')
        filenames = client.get_filenames_in_tag(tag_data=new_tag_data)
        with open(args.output_file, 'w') as file:
            for filename in filenames:
                file.write(f"{filename}\n")
    print('Done!')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
