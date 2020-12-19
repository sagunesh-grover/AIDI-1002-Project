# Malaria Detector

The deployed flask web application can be found [here](https://malaria-detector-aidi1002.herokuapp.com/). Inorder to test the web app sample images can be found [here](https://github.com/sagunesh-grover/AIDI-1002-Project/tree/main/4-Delivery%20%26%20Acceptance/Input_Cell_Images)

![](https://github.com/sagunesh-grover/AIDI-1002-Project/blob/main/4-Delivery%20%26%20Acceptance/Deployed-Web-App-Code/project_demo.gif)



## Problem Description
According to World Health Organization (WHO), Malaria is a preventable and curable life-threatening disease caused by parasites that is transmitted to people through the bites of infected female Anopheles mosquitoes. In 2018, there were an estimated 228 million cases of malaria, aggregating to an estimated death count of 4,05,000 worldwide. Malaria control and elimination alone estimated to US$ 2.7 billion in funding, of which 30% (US$ 900 million) amounted to contributions from governments of endemic countries. As years pass by, these numbers continue to rise.
Moreover the process of blood smear workflow for Malaria detection involves intensive examination of the blood smear at a 100X magnification, where people manually count red blood cells that contain parasites out of 5000 cells which alone signifies the motivation for the development of a robust tool which eases and affectively automate this cumbersome process of blood smear workflow for Malaria detection enabling researchers and on-site infectious disease physicians to arrive at a quick and accurate diagnosis.

## Data Source
The following dataset was acquired from [National Library of Medicine (NLM)](https://lhncbc.nlm.nih.gov/publication/pub9932). It contains a total of 27,558 images consisting of:
* Infected / Parasitized
*	Uninfected



## Data Modeling
The results of various [Machine Learning Models](https://github.com/sagunesh-grover/AIDI-1002-Project/blob/main/3-ML%20Modeling%20%26%20Evaluation/Final%20Model%20Code-Sagunesh%20Grover.ipynb) on the test set are:

|      Model Name     |   Score  |
|:-------------------:|:--------:|
|    **Random Forest**    | **0.899673** |
| Logistic Regression | 0.898222 |
|         SVM         | 0.897678 |
|         KNN         | 0.880987 |

