## Team Name: 
Bahushruth

## About You:
Hi, my name is Bahushruth. I recently graduated from "Manipal University, Jaipur" with a bachelors in Computer and communication engineering. I am currently a GRM Research Intern at IBM Research India. My research interests lie in NLP, Multimodal Research, Social Network Analysis, and AI Ethics. To know more about me, check my [portfolio](https://bahushruth.in) :)

## Readme:
Below are the list of different experiments performed and harms identified. 


1. **Erasure of Leftmost Face in a Group Picture** 

**Harm type: Erasure**

Similar to the dataset that the Twitter team used in this [paper](https://arxiv.org/abs/2105.08667) to identify bias between 2 Race, I used the [FairFace dataset](https://github.com/joojs/fairface) to perform bias analysis on an additional 2 races (Indians and East asians) to obtain the following ranking results of different groups(based on race and gender) as seen in this [notebook](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/notebooks/Demographic-Bias-Analysis-FairFace.ipynb). 

However, when the "pairing across all group" experiment as seen in the [notebook](https://github.com/twitter-research/image-crop-analysis/blob/main/notebooks/Demographic%20Bias%20Analysis.ipynb) released by twitter was performed, I noticed an interesting pattern. The left-most group exhibited very low saliency compared to the other groups. Hence I re-ran the experiment a few times with different ordering of the group in the image and found the same result.

Here are the results of the experiment.
![h11](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-1.png)
![h12](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-2.png)
![h13](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-3.png)
![h14](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-4.png)
![h15](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-5.png)
![h16](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-6.png)

This seems similar to a recent [controversy](https://www.buzzfeednews.com/article/ikrd/vanessa-nakate-greta-thunberg-davos) involving a Ugandan activist who was cropped out of a news agency photograph.

2. **Manipulating Image Saliency by adding Image Artifacts**

**Harm type: Stereotyping**

I used the [Fatkun Chrome Extension](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) to download png images of objects like guns, handcuffs, luxury/cheap cars, expensive watches, etc. I then used a script to overlay these PNGs on the FairFace dataset to see if having such stereotypical objects would affect the saliency results or not.

Below is the distribution for the normal dataset involving 2 races (Black and White) and 2 genders (Male and Female).

![h21](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-2.png)

The groups entered are: [('Black', 'Female'), ('Black', 'Male'), ('White', 'Female'), ('White', 'Male')]

The statistic is: [496. 266. 665. 573.]


Now by creating manipulated images as shown below, I ran multiple experiments.

![h22](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-1.png)

**With Gun Artifacts**

![h23](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-3.png)

The statistic is: [546. 294. 640. 520.]

**With HandCuff Artifacts**

![h24](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-4.png)

The statistic is: [531. 302. 628. 539.]

**With Luxury Watches Artifacts**

![h25](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-5.png)

The statistic is: [539. 302. 640. 519.]

**With Cheap Cars Artifacts**

![h26](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-6.png)

The statistic is: [587. 291. 567. 555.]

**With Luxury Cars Artifacts**

![h27](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-7.png)

The statistic is: [559. 300. 593. 548.]

Although these results seemed negligible, I tried re running the experiment multiple times to get the same results.
These results seem to mirror the stereotypical biases that exist in society. 
Such as crime is more associated with one gender over other. Same for wealth.

In order to get a better understanding I performed further tests. 

**Black males:- Handcuffs vs Luxury watches**

![h28](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-8.png)

**White Females:- Handcuffs vs Luxury watches**

![h29](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm2-9.png)

I performed the same experiment with Cheap cars vs Luxury Cars and got the same result. This maybe due to the difference in contrast of expensive and cheap items but such a bias pushes the sterotype that one group is better than the other, and is more suited with the finer things. This severely hurts the underrepresented demographic.




## Evidence/Reproducibility:

Link to the [Github repository](https://github.com/PotatoSpudowski/twitter-image-crop-analysis)

Link to the Datasets I used for the experiments:
* [FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age](https://github.com/joojs/fairface)

* PNG Artifact images of guns, handcuffs, luxury watches, etc were downloaded using [Fatkun Chrome Extension](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en). Link to the [dataset](https://drive.google.com/file/d/1KHOMhNPyslhr5UggtL4z2GTZ-2JjQ5Bt/view?usp=sharing).

Download all the dataset files and extract them in the data folder to perform all the experiments.

* **Visual Images to BMI dataset** was obtained from contacting the authors of the [paper](https://ieeexplore.ieee.org/document/8666768)

## Supporting Material/References:
Link to notebook for the experiment

* [Erasure of Leftmost Face in a Group Picture](https://github.com/twitter-research/image-crop-analysis/blob/main/notebooks/Demographic%20Bias%20Analysis.ipynb)

**Please add the following to "Impact" field below:**

## Self-Grading Recommendation: 

1. **Erasure of Leftmost Face in a Group Picture**

Decision to grade as intentional or unintentional harm: **Unintentional harm**

**- Harm Base Score:** 15 

As seen by the latest controversy involving a Ugandan activist who was cropped out of a news agency photograph. This unintentional harm can have a serious impact on the individual being cropped out. Making them feel inferior compared to the other people in the picture. Based on the severity of the problem I recommended the above base score.

**- Affected Users:** 1.3

Anyone can be affected

**- Likelihood or Exploitability:** 1.0 

**- Justification:** 1.0 

**- Clarity:** 1.25  

