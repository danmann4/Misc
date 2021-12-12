# Specral Processing and Graident Descent Example

## Spectral background and cosmic ray removal

These are just two algorithms that came quite in handy for spectral signal processing:
    1. bgrem.m is a matlab function to remove the fluorescent background from spectral data using the 1st order SNIP algorithm. This will facilitate interpretation of relative peak intensities, and chemical composition in the case of Raman Spectrsocopy. Applicable for infrared spectroscopies as well. bgrem example.png shows an example of taking a sample input (blue), calculating the fluorescent background (orange), and the resulting removal of the background (yellow). 
    2. removeCosmicRays.m is a matlab function to remove cosmic rays from CCD measurements. Depending on the image capture duration the CCD camera can get quite saturated with noise from cosmic rays tripping capacitors. This function will facilitate distinguishing cosmic rays from the rest of the data, and ultimately removing them from the data set.

## Gradient descent multivariate ordinary least squares linear regression
Gradient Descent Example.py is a simple example of using python to create a housing price predicting function 
based on various inputs. The data for this example is contained in the Housingprices.csv file.