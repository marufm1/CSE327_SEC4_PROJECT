# CSE327_SEC4_PROJECT

Here is the guide to installing all the dependencies required to run the program.
We are using Anaconda with Python 3.6.5 and Tensorflow CPU v1.5 

# Description:

Our project is about detecting different types of fruits with the help of deep learning using the object detection Tensorflow API and also OpenCV for image processing via images, webcam, recorded video file (mov). In this project, we used Tensorflow to train multiple objects which are fruits in our case (example: Mango, Banana, Orange etc). We had to figure out to use the Tensoflow CPU version instead of using the faster GPU version as we don’t have access to a good enough GPU. At first, we used the Faster_rcnn model but then we switched to SSD_mobilenet which had lower accuracy but faster detection. The training process for each object took about 20+ hours. After the training process was done we could run our script to see the detected object with the help of some image processing done through OpenCV.



# Downloads

# For just running the program:

1. Download this current repo.
2. Copy the repo downloaded to C drive make sure that the directory of the repo looks like: C:/tensorflow1/models/research/object_detection/...

3. Then open the Ananconda command prompt to RUN AS ADMINISTRATOR.

     a)Activate tensorflow1 virtual environment
     
     b)Then cd to object detection folder and set the path by issuing the command:
       set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim
       
4.After that type "idle" and enter.This will open IDLE and now you can run any of the scripts. 
For eg. Object_detection_mango_image.py and press Run or F5.It will initialize for 10 seconds and then display a window showing any objects it’s detected in the image!
        
  



# For Training:

1. Download the following repo as it will be required for training process: https://github.com/tensorflow/models/tree/079d67d9a0b3407e8d074a200780f3835413ef99
Make sure to download exactly this commit from Feb 6. And rename it to models only rather than models-xxxxx... 


We need to copy the repo downloaded in the downloads step to the C:
We need to make sure that the directory of the repo looks like: C:/tensorflow1/models/research/object_detection/...

2. Download this current repo.
Then copy the contents of the object_detection folder downloaded in step 2 of downloads and replace with the previously dowbloaded files in C:/tensorflow1/models/research/object_detection/...



# Installation

1. First Install Anaconda with Python 3.6.5 if you don't have already.
2. We need to copy the repo downloaded in the downloads step to the C:
3. Install Tensorflow by issuing the following command: pip install tensorflow==1.5

We need to open the Ananconda Prompt as Run as Administrator and do the following:

Create a new acnaconda virtual environment:

C:\> conda create -n tensorflow1 pip python=3.5
Then activate the environment by issuing:

Then we simply activate the environment:

C:\> activate tensorflow1

Install tensorflow in this environment by issuing:

(tensorflow1) C:\> pip install tensorflow==1.5


Install the other necessary packages by issuing the following commands:

(tensorflow1) C:\> conda install -c anaconda protobuf==3.6.1
(tensorflow1) C:\> pip install pillow==5.0.0
(tensorflow1) C:\> pip install lxml==4.1.1
(tensorflow1) C:\> pip install Cython
(tensorflow1) C:\> pip install jupyter==1.0.0
(tensorflow1) C:\> pip install matplotlib
(tensorflow1) C:\> pip install pandas==0.22.0
(tensorflow1) C:\> pip install opencv-python==3.4.0.12

Use command: cd C:/tensorflow1/models/research
to change your current directory.

Now we have to set the path by issuing:

set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim

You can check the set pythonpath by using: echo %PYTHONPATH%

Finally, run the following commands from the C:\tensorflow1\models\research directory:

(tensorflow1) C:\tensorflow1\models\research> python setup.py build
(tensorflow1) C:\tensorflow1\models\research> python setup.py install

Use command: cd C:/tensorflow1/models/research/object_detection

Now we can run the command: idle
Which will open up the python IDE and then we can open the file "Object_detection_Image.py" from C:/tensorflow1/models/research/object_detection/
Then running it will show open up a OpenCv prompt to show the results of the detection.
