# Summary

In this lab, we used KBinsDiscretizer from Scikit-learn to perform vector quantization on a sample image of a raccoon face. We used 8 gray levels to represent the image, which can be compressed to use only 3 bits per pixel. We compared the uniform and k-means clustering strategies to map the pixel values to the 8 gray levels. We found that the k-means clustering strategy provided a more balanced distribution of the pixel values. We also checked the memory usage of the compressed images and found that the compressed image took 8 times more memory than the original image due to the use of a 64-bit float representation for the compressed image.