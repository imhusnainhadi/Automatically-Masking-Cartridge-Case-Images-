
Project Title: Automated Forensic Analysis of Cartridge Cases

Description:

This project aims to automate the tedious and time-consuming process of masking fired ammunition components in forensic investigations. The focus is on cartridge cases, specifically 9mm caliber, using a 3D microscope. The algorithm, implemented in MATLAB, performs the following steps:

1. Image Acquisition: Utilize a 3D microscope to capture high-resolution images of fired 9mm cartridge cases.

2. Preprocessing: Convert the acquired images to grayscale, apply GaussianBlur for noise reduction, and use the Canny edge detector for feature extraction.

3. Contour Detection: Identify contours in the image using OpenCV, and filter contours based on area to focus on potential features.

4. Mask Generation: Create a binary mask by drawing rectangles around regions corresponding to features like breech-face impressions, aperture shear, firing pin impressions, and firing pin drags.

5. Thresholding: Use a threshold to differentiate between original and masked regions, enhancing feature visibility.

6. Display and Save Results:** Display the binary mask for visual validation and save it for further analysis. Additionally, adjust parameters as needed for diverse image sets.

*Implementation Notes:

- The algorithm provides a foundation for automating the preparatory function currently performed manually, thereby streamlining the comparison process for forensic analysis.

- Experiment with different threshold values, contour area thresholds, and other parameters to optimize the algorithm for various scenarios.

- Consider integrating deep learning techniques for improved accuracy and adaptability to a broader range of cartridge case images.

By automating this preparatory phase, law enforcement agencies can significantly enhance the efficiency of forensic investigations related to firearm incidents. The MATLAB code provides a flexible and extensible solution for future enhancements and integration into forensic analysis workflows.
