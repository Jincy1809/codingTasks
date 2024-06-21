# AmazonCapstone

The final capstone project for HyperionDev bootcamp

# Description

The SpaCy library is used to implement sentiment analysis on Amazon product reviews
Data file link: https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products

# Table of Contents

1. Installation
2. Getting started
3. Usage
4. Contact Information
   
1. Installation

The following libraries are required to run this code:

SpaCy
SpacyTextBlob
pandas

2. Getting Started

To get started, you can simply clone this repo and run the main file. Make necessary changes to suit your own needs.

3. Usage

Firstly, data needs to be collected to train the model. In this case, data is downloaded as a .csv file from Kaggle - find the link to the file in the description. To adjust the usage of this program, feel free to replace the .csv file with any data you want to implement sentiment analysis on.

The data is then preprocessed and the en_core_web_sm model is loaded from the SpaCy library. The preprocessing that occurs includes: dropping NaN values; removing stop words; converting to lower case and stripping whitespace.

Finally, polarity score is calculated as the data passed through the model and compared to a base score. A value of Positive, Negative or Neutral is returned.

4. Contact Information

Please direct any questions to any of the following:

• Email: jincy.perutty@gmail.com
• LinkedIn: www.linkedin.com/in/jincy-perutty-ba14a9237
