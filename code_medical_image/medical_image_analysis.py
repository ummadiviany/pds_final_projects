### Project 4 : Medical Image Visualization and Analysis


import os
from os import listdir

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import scipy.ndimage as ndi
from nilearn import plotting
from scipy import ndimage as ndi
from skimage import data
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from skimage.segmentation import clear_border


def abdomen_ct():

    img = []
    folder_dir = r"C:\Users\91799\pds_final_projects\data\medical_images\Abdomen_CT"
    for images in os.listdir(folder_dir):
 
    # check if the image ends with .gz
        if (images.endswith(".gz")):
            img.append(images)
    #To read the nifti file by nibabel 
            
    visulised_img=nib.load(os.path.join(folder_dir,img[3]))
    print (visulised_img)
    


    # view file metadata
    print(visulised_img.header)


    #data is a familiar NumPy array
    visulised_img_data=visulised_img.get_fdata()

    visulishedshape=visulised_img_data.shape

    #visualize a slice
    fig, axs = plt.subplots(1,3)
    fig.suptitle('Abdomen CT: (Middle Slices)')
    axs[0].imshow(visulised_img_data[visulishedshape[0]//2,:,:], cmap='gray')
    axs[1].imshow(visulised_img_data[:,visulishedshape[1]//2,:], cmap='gray')
    axs[2].imshow(visulised_img_data[:,:,visulishedshape[2]//2], cmap='gray')
    fig.tight_layout()
    plt.show()
     

    plotting.plot_img(visulised_img)
    plt.suptitle("Visulisation of Abdomen CT :by Nilearn")
    plt.show()

    
    plotting.plot_img(visulised_img, display_mode='mosaic', cmap='gray')
    plt.show()


    #statistical analysis 
    print("statistical Analysis of visulised image:Abdomen_CT")
    print("Mean:",visulised_img_data.mean())
    print("Max:",visulised_img_data.max())
    print("Min:",visulised_img_data.min())
    print("standard deviation:",np.std(visulised_img_data))
    print("standard deviation:",np.var(visulised_img_data))


    
    
    visulised_img_data.shape
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Abdomen CT')
    plt.pcolormesh(visulised_img_data[90])
    plt.colorbar
    plt.show()
    #sigmantation of image 
    mask=visulised_img_data<-320
    plt.suptitle('segmented image:Abdomen CT')
    plt.pcolormesh(mask[50])
    plt.colorbar()
    plt.show()

    mask_labeled=np.vectorize(label,signature='(n,m)->(n,m)')(mask)
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Abdomen CT')
    plt.pcolormesh(mask_labeled[50]) 
    plt.colorbar()  
    plt.show() 


    

   

def heart_mri():
    img = []
   
    folder_dir = r"C:\Users\91799\pds_final_projects\data\medical_images\Heart_MRI"
    for images in os.listdir(folder_dir):

    # check if the image ends with png
        if (images.endswith(".gz")):
           img.append(images)
    #To read the nifti file by nibabel 
    visulised_img=nib.load(os.path.join(folder_dir,img[3]))
    print (visulised_img)
    


    # view file metadata
    print(visulised_img.header)


    #data is a familiar NumPy array
    visulised_img_data=visulised_img.get_fdata()

    visulishedshape=visulised_img_data.shape

    #visualize a slice
    fig, axs = plt.subplots(1,3)
    fig.suptitle('Heart_MRI:(Middle Slices)')
    axs[0].imshow(visulised_img_data[visulishedshape[0]//2,:,:], cmap='gray')
    axs[1].imshow(visulised_img_data[:,visulishedshape[1]//2,:], cmap='gray')
    axs[2].imshow(visulised_img_data[:,:,visulishedshape[2]//2], cmap='gray')
    fig.tight_layout()
    plt.show()

    #Plot a series of slices
    fig_rows = 4
    fig_cols = 4
    n_subplots = fig_rows * fig_cols
    n_slice = visulised_img_data.shape[0]
    step_size = n_slice // n_subplots
    plot_range = n_subplots * step_size
    start_stop = int((n_slice - plot_range) / 2)

    fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

    for idx, img in enumerate(range(start_stop, plot_range, step_size)):
        axs.flat[idx].imshow(ndi.rotate(visulised_img_data[img, :, :], 90), cmap='gray')
        axs.flat[idx].axis('off')
    fig.suptitle('Heart_MRI:(Series of Slices)')    
    plt.tight_layout()
    plt.show()

    
    plotting.plot_img(visulised_img)
    plt.suptitle("Visulisation of Heart_MRI :by Nilearn")
    plt.show()

    
    plotting.plot_img(visulised_img, display_mode='mosaic', cmap='gray')
    plt.show()


    #statistical anylysis
    print("statistical Analysis of visulised image:Heart_MRI")
    print("Mean:",visulised_img_data.mean())
    print("Max:",visulised_img_data.max())
    print("Min:",visulised_img_data.min())
    print("standard deviation:",np.std(visulised_img_data))
    print("standard deviation:",np.var(visulised_img_data))

    
    visulised_img_data.shape
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Heart_MRI')
    plt.pcolormesh(visulised_img_data[154])
    plt.colorbar
    plt.show()


    mask=visulised_img_data<320
    plt.suptitle('segmented image:Heart_MRI')
    plt.pcolormesh(mask[150])
    plt.colorbar()
    plt.show()

    mask_labeled=np.vectorize(label,signature='(n,m)->(n,m)')(mask)
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Heart_MRI')
    plt.pcolormesh(mask_labeled[100]) 
    plt.colorbar()  
    plt.show()   

    
    



def hippocampus_mri():
    img = []
    folder_dir = r"C:\Users\91799\pds_final_projects\data\medical_images\Hippocampus_MRI"
    for images in os.listdir(folder_dir):
 
    # check if the image ends with png
        if (images.endswith(".gz")):
           img.append(images)
    visulised_img=nib.load(os.path.join(folder_dir,img[0]))
    print (visulised_img)
    


    # view file metadata
    print(visulised_img.header)


    #data is a familiar NumPy array
    visulised_img_data=visulised_img.get_fdata()

    visulishedshape=visulised_img_data.shape

    #visualize a slice
    fig, axs = plt.subplots(1,3)
    fig.suptitle('Hippocampus_MRI:(Middle Slices)')
    axs[0].imshow(visulised_img_data[visulishedshape[0]//2,:,:], cmap='gray')
    axs[1].imshow(visulised_img_data[:,visulishedshape[1]//2,:], cmap='gray')
    axs[2].imshow(visulised_img_data[:,:,visulishedshape[2]//2], cmap='gray')
    fig.tight_layout()
    plt.show()


    #Plot a series of slices
    fig_rows = 4
    fig_cols = 4
    n_subplots = fig_rows * fig_cols
    n_slice = visulised_img_data.shape[0]
    step_size = n_slice // n_subplots
    plot_range = n_subplots * step_size
    start_stop = int((n_slice - plot_range) / 2)

    fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

    for idx, img in enumerate(range(start_stop, plot_range, step_size)):
        axs.flat[idx].imshow(ndi.rotate(visulised_img_data[img, :, :], 90), cmap='gray')
        axs.flat[idx].axis('off')
    fig.suptitle('Hippocampus_MRI:(Series of Slices)') 
    plt.tight_layout()
    plt.show()

    plotting.plot_img(visulised_img)
    plt.suptitle("Visulisation of Hippocapus_MRI :by Nilearn")
    plt.show()


    plotting.plot_img(visulised_img, display_mode='mosaic', cmap='gray')
    plt.show()  


    
    #statistical anylysis
    print("statistical Analysis of visulised image:Hippocampus MRI")
    print("Mean:",visulised_img_data.mean())
    print("Max:",visulised_img_data.max())
    print("Min:",visulised_img_data.min())
    print("standard deviation:",np.std(visulised_img_data))
    print("standard deviation:",np.var(visulised_img_data))



    visulised_img_data.shape
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Hippocampus_MRI')
    plt.pcolormesh(visulised_img_data[20])
    plt.colorbar
    plt.show()

    mask=visulised_img_data<300
    plt.suptitle('segmented image:Hippocampus_MRI')
    plt.pcolormesh(mask[20])
    plt.colorbar()
    plt.show()

    mask_labeled=np.vectorize(label,signature='(n,m)->(n,m)')(mask)
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Hippocampus_MRI')
    plt.pcolormesh(mask_labeled[30]) 
    plt.colorbar()  
    plt.show()   




def prostate_mri157():
    img = []
    folder_dir = r"C:\Users\91799\pds_final_projects\data\medical_images\Prostate_MRI\157" 
    for images in os.listdir(folder_dir):
 
    # check if the image ends with png
        if (images.endswith(".gz")):
           img.append(images)
    visulised_img=nib.load(os.path.join(folder_dir,img[0]))
    print (visulised_img)
    


    # view file metadata
    print(visulised_img.header)


    #data is a familiar NumPy array
    visulised_img_data=visulised_img.get_fdata()

    visulishedshape=visulised_img_data.shape

    #visualize a slice
    fig, axs = plt.subplots(1,3)
    fig.suptitle('Prostate_MRI:(Middle Slices)')
    axs[0].imshow(visulised_img_data[visulishedshape[0]//2,:,:], cmap='gray')
    axs[1].imshow(visulised_img_data[:,visulishedshape[1]//2,:], cmap='gray')
    axs[2].imshow(visulised_img_data[:,:,visulishedshape[2]//2], cmap='gray')
    fig.tight_layout()
    plt.show()


    #Plot a series of slices
    fig_rows = 4
    fig_cols = 4
    n_subplots = fig_rows * fig_cols
    n_slice = visulised_img_data.shape[0]
    step_size = n_slice // n_subplots
    plot_range = n_subplots * step_size
    start_stop = int((n_slice - plot_range) / 2)

    fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

    for idx, img in enumerate(range(start_stop, plot_range, step_size)):
        axs.flat[idx].imshow(ndi.rotate(visulised_img_data[img, :, :], 90), cmap='gray')
        axs.flat[idx].axis('off')
    fig.suptitle('Prostatr_MRI:(Series of Slices)') 
    plt.tight_layout()
    plt.show()

    plotting.plot_img(visulised_img)
    plt.suptitle("Visulisation of Prostate_MRI :by Nilearn")
    plt.show()


    plotting.plot_img(visulised_img, display_mode='mosaic', cmap='gray')
    plt.show()

        
    
    #statistical anylysis
    print("statistical Analysis of visulised image:Prostate MRI")
    print("Mean:",visulised_img_data.mean())
    print("Max:",visulised_img_data.max())
    print("Min:",visulised_img_data.min())
    print("standard deviation:",np.std(visulised_img_data))
    print("standard deviation:",np.var(visulised_img_data))  


    visulised_img_data.shape
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(visulised_img_data[150])
    plt.colorbar
    plt.show()

    mask=visulised_img_data<320
    plt.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(mask[100])
    plt.colorbar()
    plt.show()

    mask_labeled=np.vectorize(label,signature='(n,m)->(n,m)')(mask)
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(mask_labeled[100]) 
    plt.colorbar()  
    plt.show() 
  




def prostate_mri158():
    img = []
    folder_dir = r"C:\Users\91799\pds_final_projects\data\medical_images\Prostate_MRI\158" 
    for images in os.listdir(folder_dir):
 
    # check if the image ends with png
        if (images.endswith(".gz")):
           img.append(images)
    

    #To read the nifti file by nibabel 
    visulised_img=nib.load(os.path.join(folder_dir,img[0]))
    print (visulised_img)
    


    # view file metadata
    print(visulised_img.header)


    #data is a familiar NumPy array
    visulised_img_data=visulised_img.get_fdata()

    visulishedshape=visulised_img_data.shape

    #visualize a slice
    fig, axs = plt.subplots(1,3)
    fig.suptitle('Prostate_MRI:(Middle Slices)')
    axs[0].imshow(visulised_img_data[visulishedshape[0]//2,:,:], cmap='gray')
    axs[1].imshow(visulised_img_data[:,visulishedshape[1]//2,:], cmap='gray')
    axs[2].imshow(visulised_img_data[:,:,visulishedshape[2]//2], cmap='gray')
    fig.tight_layout()
    plt.show()



    plotting.plot_img(visulised_img)
    plt.suptitle("Visulisation of Prostate_MRI :by Nilearn")
    plt.show()



    plotting.plot_img(visulised_img, display_mode='mosaic', cmap='gray')
    plt.show()

    
    #statistical anylysis
    print("statistical Analysis of visulised image:Prostate MRI")
    print("Mean:",visulised_img_data.mean())
    print("Max:",visulised_img_data.max())
    print("Min:",visulised_img_data.min())
    print("standard deviation:",np.std(visulised_img_data))
    print("standard deviation:",np.var(visulised_img_data))


    visulised_img_data.shape
    fig, axs = plt.subplots(1,1)
    fig.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(visulised_img_data[200])
    plt.colorbar
    plt.show()

    mask=visulised_img_data<320
    plt.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(mask[150])
    plt.colorbar()
    plt.show()

    mask_labeled=np.vectorize(label,signature='(n,m)->(n,m)')(mask)
    fig, axs = plt.subplots(1,1)
    plt.suptitle('segmented image:Prostate_MRI')
    plt.pcolormesh(mask_labeled[150]) 
    plt.colorbar()  
    plt.show()   







def image_visu_sat_analy(no):
    if(no==1):
        print(abdomen_ct())
    elif(no==2):
        print(heart_mri())
    elif(no==3):
        print(hippocampus_mri())
    elif(no==4):
        print(prostate_mri157())
    elif(no==5):
        print(prostate_mri158())    
    else:
        print("file is not availble please ,enter between 1 to 5")

n=int(input("Enter the no. file which you want to visulise ,statistical anlaysis:\n press:1 for Abdomen_CT \n press 2:for HeartMRI\n press:3 for Hippocampus_MRI\n press:4 for Prostate_MRI157\n press:5 for Prostate_MRI158 \n PRESS:"))     
print(image_visu_sat_analy(n))        
        

