# Canny Edge Detector

## Overview

* Year: 2020
* Language(s): Python
* Discipline(s): Computer Vision, Edge Detection
* Keywords: canny-edge-detection, computer-vision, derivative-masks, gaussian-smoothing, edge, edge-detection, hysteresis-thresholding, non-maximum-suppression

## Description

Canny Edge Detector is an implementation of the edge detection method defined by John Canny in 1986. This is done by performing the following computational steps:

1. Perform Gaussian smoothing on the image.
2. Compute the gradient magnitude and orientation using derivative masks.
3. Perform non-maximum suppression.
4. Perform hysteresis thresholding.

The input of this program is the file path to an image of your choice.

## Build Instructions

1. Clone the repository.
2. Open the directory with Terminal.
3. Run the program with the following instruction: `python run.py <path_to_image>`
