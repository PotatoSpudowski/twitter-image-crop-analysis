# Image Crop Analysis

This repo is based off of the work done by [Twitter research](https://github.com/twitter-research/image-crop-analysis). 

My report for the [Twitter Algorithmic bias Bounty challenge](https://hackerone.com/twitter-algorithmic-bias?type=team&view_policy=true) can be found [here](Report.md).



# Instructions

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) and then follow these steps:
  * create a conda environment using `conda env create -f environment.yml`
  * activate the environment using `conda activate image-crop-analysis`
- Put datsets at `data/`

## Docker Run

* Install docker 
* Run the following commands in this root directory of this project:

```bash
docker build -t "image_crop" -f docker/Dockerfile .
docker run -p 9000:9000 -p 8900:8900 -it image_crop
```
* Open the jupyter lab URL shown in terminal. 

