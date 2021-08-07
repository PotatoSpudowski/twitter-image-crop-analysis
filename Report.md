## Team Name: 
Bahushruth

## About You:
Hi, my name is Bahushruth. I recently graduated from "Manipal University, Jaipur" with a bachelors in Computer and communication engineering. I am currently a GRM Research Intern at IBM Research India. My research interests lie in NLP, Multimodal Research, Social Network Analysis, and AI Ethics. To know more about me, check my [portfolio](https://bahushruth.in) :)

## Readme:
Below are the list of different experiments performed and harms identified. 


1. **Erasure of Leftmost Face in a Group Picture** 

**Harm type: Erasure**

Similar to the dataset that the Twitter team used in this [paper](https://arxiv.org/abs/2105.08667) to identify bias between 2 Race, I used the [FairFace dataset](https://github.com/joojs/fairface) to perform bias analysis on an additional 2 races (Indians and East asians) to obtain the following ranking results of different groups(based on race and gender) as seen in this [notebook](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/notebooks/Demographic-Bias-Analysis-FairFace.ipynb). 

However, when the "pairing across all group" experiment was performed, I noticed an interesting pattern. The left-most group exhibited very low saliency compared to the other groups. Hence I re-ran the experiment a few times with different ordering of the group in the image and found the same result.

Here are some results of the experiment.
![h11](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-1.png)
![h12](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-2.png)
![h13](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-3.png)
![h14](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-4.png)
![h15](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-5.png)
![h16](https://github.com/PotatoSpudowski/twitter-image-crop-analysis/blob/main/images/harm1-6.png)

[Describes your results, the harm you have identified (categorized according to a taxonomy provided below), a description of why it is important, and a description of your findings including the qualitative and quantitative methods you used to evaluate this harm’s potential impact on people. ]

## Evidence/Reproducibility:
[Evidence / Python Code (preferably a GitHub link) that demonstrates the harm including the data / image file(s) needed to reproduce/verify the harm you identified using your methodology.

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

**Please add the following to "Impact" field below:**

##Self-Grading Recommendation: 
Description of Harm
Decision to grade as intentional or unintentional harm
**- Harm Base Score:** [Numeric Score]  [Brief rationale]
**- Affected Users: ** [Numeric Score]  [Brief rationale]
**- Likelihood or Exploitability: ** [Numeric Score]  [Brief rationale]
**- Justification: ** [Numeric Score]  [Brief rationale]
**- Clarity: ** [Numeric Score]  [Brief rationale]
**- Creativity: ** [Numeric Score]  [Brief rationale]
**- Total Score: ** [Total Score]

