import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
        description="stocks"
    )
    parser.add_argument("-t", "--ticker_directory_path", type=str,
                        help="Path for ticker symbols directory", default="./tickers")
    parser.add_argument(
        "-o",
        "--output_directory_path",
        type=str,
        default="./results",
        help="Path of the output directory (creates directory if not present)",
    )
    args = parser.parse_args()
    return args


def setup_env(args):
    if not os.path.exists(args.output_directory_path):
        os.makedirs(args.output_directory_path)
