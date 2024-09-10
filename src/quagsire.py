"""quagsire.py

Feed me thermal image data of plants and I'll feed you info about water content.

@date 09/09/2024
"""
import argparse
import cv2
import numpy as np


# Setup.
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

# Data ingestion.
def gray16_to_gray8(gray16: np.array) -> np.array:
    """Convert an image into a Numpy array representing"""
    gray8 = np.zeros((160, 120), dtype=np.uint8)
    gray8 = cv2.normalize(gray16, gray8, 0, 255, cv2.NORM_MINMAX)
    gray8 = np.uint8(gray8)

def img_read(ipath: str) -> [np.array, np.array]:
    """Convert an image file into some iterable object.
    """
    # Convert image into a gray8 format.
    try:
        gray16 = cv2.imread(ipath, cv2.IMREAD_ANYDEPTH)
        gray8 = gray16_to_gray8(gray16)
    except TypeError as e:
        gray16 = np.zeros((160, 120), dtype=np.uint16) 
        gray8 = np.zeros((160, 120), dtype=np.uint8) 
        print(e)
    return gray8, gray16


# Display.
def display(
        img: np.array,
        title: str = "Test"
    ):
    try:
        cv2.imshow(title, img)
        cv2.waitKey(0)
    except cv2.error as e:
        print(e)
        print("Hi nub.")

def clean_up():
    cv2.destroyAllWindows()

# Main.
def quagsire(args: argparse.Namespace):
    """
    Ingest thermal imagery and spit out info on water content.
    """
    img, therm = img_read(args.input)
    display(img)
    clean_up()

if __name__ == "__main__":
    args = parse_args()
    quagsire(args)
