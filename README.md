#VEHICLE COLLISION DETECTION WITH ALERT SYSTEM USING CNN:

1:**Demonstration**
  ![collision](https://github.com/Robinr0027/vechicle-collision/assets/133769370/58d9749e-59a1-4547-b912-3c8b260fc7c9)


2.**What is Accident Detection System?**
This repository focuses on using Deep Learning to detect road accidents through CCTV footage and implementing an alert system using Twilio. Road accidents are a global problem with fatal consequences. By employing CCTV accident detection and integrating Twilio's messaging capabilities, we aim to promptly alert relevant parties about accidents and minimize the impact of such incidents.

3.**Prerequisites**
-Python 3.10.9
-Basic knowledge of Python scripting, Machine Learning, and Deep Learning
-Familiarity with Twilio API and messaging services.

4.**Getting Started - How to use it?**
Clone this repository:https://github.com/Robinr0027/vechicle-collision.git

To install all the packages required to run this python program pip install -r requirements.txt

**Note:** This project requires a camera. So make sure you have a connected camera to your device. You can also use a downloaded video if not using a camera.

**To run the program:**
Before running the program, you need to run the accident-classification.ipynb file which will create the model_weights.h5 file. Then, to run this python program, you need to execute the main.py python file.
streamlit run main.py.

To use Twilio in your application, follow these steps:
-Sign up for a Twilio account at the Twilio website.
-Once you have an account, you will be provided with authentication credentials, including an Account SID and an Auth Token.
-paste these in keys.py file.

5.**Description**
This program includes 4 things:
1.data: Kaggle dataset on Accident Detection from CCTV footage.
2.accident-classification.ipynb: This is a jupyter notebook that generates a model to classify the above data. This file generates two important files model.json and model_weights.h5.
3.detection.py: This file loads the Accident Detection system with the help of model.json and model_weights.h5 files.
4.camera.py: It packs the camera and executes the detection.py file on the video dividing it frame by frame and displaying the percentage of the prediction in the accident (if present) in the frame.
