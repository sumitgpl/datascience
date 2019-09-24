#
# Problem description

Your goal is to predict the binary class heart\_disease\_present, which represents whether or not a patient has heart disease:

- 0 represents no heart disease present
- 1 represents heart disease present

- **Features**
- [List of features](https://www.drivendata.org/competitions/54/machine-learning-with-a-heart/page/109/#features_list)
- [Example of features](https://www.drivendata.org/competitions/54/machine-learning-with-a-heart/page/109/#features_eg)

- **Performance metric**
- [Example](https://www.drivendata.org/competitions/54/machine-learning-with-a-heart/page/109/#metric)

- **Submission Format**
- [Format example](https://www.drivendata.org/competitions/54/machine-learning-with-a-heart/page/109/#sub_values)

##
# Dataset

There are 14 columns in the dataset, where the patient\_id column is a unique and random identifier. The remaining 13 features are described in the section below.

- slope\_of\_peak\_exercise\_st\_segment (type: int): the slope of the peak exercise [ST segment](https://en.wikipedia.org/wiki/ST_segment), an electrocardiography read out indicating quality of blood flow to the heart
- thal (type: categorical): results of [thallium stress test](https://www.ucsfbenioffchildrens.org/tests/007201.html) measuring blood flow to the heart, with possible values normal, fixed\_defect, reversible\_defect
- resting\_blood\_pressure (type: int): resting blood pressure
- chest\_pain\_type (type: int): chest pain type (4 values)
- num\_major\_vessels (type: int): number of major vessels (0-3) colored by flourosopy
- fasting\_blood\_sugar\_gt\_120\_mg\_per\_dl (type: binary): fasting blood sugar \&gt; 120 mg/dl
- resting\_ekg\_results (type: int): resting electrocardiographic results (values 0,1,2)
- serum\_cholesterol\_mg\_per\_dl (type: int): serum cholestoral in mg/dl
- ldpeak\_eq\_st\_depression (type: float): oldpeak = [ST depression](https://en.wikipedia.org/wiki/ST_depression) induced by exercise relative to rest, a measure of abnormality in electrocardiograms
- sex (type: binary): 0: female, 1: male
- age (type: int): age in years
- max\_heart\_rate\_achieved (type: int): maximum heart rate achieved (beats per minute)
- exercise\_induced\_angina (type: binary): exercise-induced chest pain (0: False, 1: True)

### Feature data example

Here&#39;s an example of one of the rows in the dataset so that you can see the kinds of values you might expect in the dataset. Some are binary, some are integers, some are floats, and some are categorical. There are no missing values.

| **field** | **value** |
| --- | --- |
| **slope\_of\_peak\_exercise\_st\_segment** | 2 |
| **thal** | normal |
| **resting\_blood\_pressure** | 125 |
| **chest\_pain\_type** | 3 |
| **num\_major\_vessels** | 0 |
| **fasting\_blood\_sugar\_gt\_120\_mg\_per\_dl** | 1 |
| **resting\_ekg\_results** | 2 |
| **serum\_cholesterol\_mg\_per\_dl** | 245 |
| **oldpeak\_eq\_st\_depression** | 2.4 |
| **sex** | 1 |
| **age** | 51 |
| **max\_heart\_rate\_achieved** | 166 |
| **exercise\_induced\_angina** | 0 |

##
# Performance metric

Performance is evaluated according to binary [log loss](https://en.wikipedia.org/wiki/Loss_functions_for_classification#Cross_entropy_loss_(Log_Loss)).

##
# Submission format

The format for the submission file is two columns with the patient\_id and heart\_disease\_present. This competition uses log loss as its evaluation metric, so the heart\_disease\_present values you should submit are the  **probabilities that a patient has heart disease**  (not the binary label).

For example, if you predicted...

| **patient\_id** | **heart\_disease\_present** |
| --- | --- |
| **olalu7** | 0.5 |
| **z9n6mx** | 0.5 |
| **5k4413** | 0.5 |
| **mrg7q5** | 0.5 |
| **uki4do** | 0.5 |
| **...** | ... |
| **bwoyg6** | 0.5 |
| **j8i7ve** | 0.5 |
| **t2zn1n** | 0.5 |
| **oxf8kj** | 0.5 |
| **aeiv0y** | 0.5 |

Your .csv file that you submit would look like:

patient\_id,heart\_disease\_present

olalu7,0.5

z9n6mx,0.5

5k4413,0.5

mrg7q5,0.5

uki4do,0.5

kev1sk,0.5

9n6let,0.5

jxmtyg,0.5

51s2ff,0.5

...

5bbknr,0.5

hr6pjx,0.5

r4hsar,0.5

4cezdf,0.5

palhcc,0.5

bwoyg6,0.5

j8i7ve,0.5

t2zn1n,0.5

oxf8kj,0.5

aeiv0y,0.5

##
