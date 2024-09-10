"""quagsire.py

Feed me thermal image data of plants and I'll feed you info about water content.

@date 09/09/2024
"""
import argparse
import cv2
import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        default="flights/flight.tif",
        help="Provide an input file for eating.",
        type=str
    )
    parser.add_argument(
        "-o",
        "--output",
        default="reports/report.md",
        help="Regurgitated output file.",
        type=str
    )
    return parser.parse_args()

def quagsire(args: argparse.Namespace):
    """
    Ingest thermal imagery and spit out info on water content.
    """
    print(args)

if __name__ == "__main__":
    args = parse_args()
    quagsire(args)
