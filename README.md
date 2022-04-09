# Data Analysis Examples, Specral Processing Algorithms, and Advent of Code Solutions!

## Bayesian Linear Regression
Bayesian Linear Regression.ipynb is an example of how we can use python to conduct Bayesian linear regressions. In this case its used to predict
the uncertainty around estimated housing prices. The data set used (Housingprices.csv) is the same as that for the gradient descent example.  

## Digit Model
This is a tensorflow neural network for discerning images of hand-drawn digits. 
In this use case we want to identify digits that are only within drawn shapes in an image (test_image.jpg).
"digit model.ipynb" is the script to create the neural network from the built in tensorflow MNIST database and examples. 
"Image_process.ipynb" is the image processing script to feed the appropriate numbers into the digit_model.

## Gradient descent multivariate ordinary least squares linear regression
Gradient Descent Example.py is a simple example of using python to create a housing price predicting function 
based on various inputs. The data for this example is contained in the Housingprices.csv file.

## Spectral background and cosmic ray removal

These are just two algorithms that came quite in handy for spectral signal processing...

    1. bgrem.m is a matlab function to remove the fluorescent background from spectral data using the 
       1st order SNIP algorithm. This will facilitate interpretation of relative peak intensities, and
       chemical composition in the case of Raman Spectrsocopy. Applicable for infrared spectroscopies as well. 
       bgrem example.png shows an example of taking a sample input (blue), calculating the fluorescent background (orange), 
       and the resulting removal of the background (yellow). 
   
    2. removeCosmicRays.m is a matlab function to remove cosmic rays from CCD measurements.
       Depending on the image capture duration the CCD camera can get quite saturated with noise from cosmic rays tripping capacitors. 
       This function will facilitate distinguishing cosmic rays from the rest of the data, and ultimately removing them from the data set.

## Advent of Code Solutions
Just a collection of some of my solutions to the Advent of Code challenges from 2020 and 2021 so far.
A puzzle a day keeps the doctor away...
