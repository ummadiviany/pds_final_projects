# Final Projects for CS60013 : Programming and Data Structures
## Project 4 : Medical Image Visualization and Analysis
### Introduction
1.in this project ,we visualize and analyze the medical images. The dataset is located in the `data/medical_images/` directory.The datasets of medical file is in Nifti format.And by the use of python coding and with the application of various libraries like 
    1.nibabel to read that nifti file
    2.numpy to Visualize
    3.matplotlib to plot that image
    4.nilearn to Visualize that numpy array, without extract data from it.
    5.skimage.

2.The dataset has Nifti file of :
   1. `Hippocampus MRI` 
   2. `Heart MRI` 
   3. `Prostate MRI` 
   4. `Abdomen CT` 

## Step that we done to Read, Visualize and Analysis
1. First we read that Nifti file which is end with ".nii.gz" with the help of Nibabel library.
2. To view metadata we use .header in readed file that contains a variety of information about the file.
3. To access data in the NIfTI object:-we use the method get_fdata() and this data is in NumPy array.
4. To view the middle scan slice along each dimension to convert 3D image to 2D image.
5. Then we plot that image into matplotlib.
6. For more visualization: Plot with NiLearn, and it  was designed to work with neuroimaging data.
7. Then we done statistical analysis by using of NumPy and Scipy library.in which we calculate Mean,Median,Mode,Standard deviation,Standard variation of visulised image.
8. Then we simply apply segmentation of that visualised image.
9. Then we provide switch case in that to ease the implmentation of code.

## Reference
1. GeeksforGeeks
2. W3shcools
