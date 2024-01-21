% Read the original and masked images
originalImage = imread('Orignal Image.jpeg');
maskedImage = imread('Mask Image.jpg');


% Resize images to the same dimensions
originalImage = imresize(originalImage, size(maskedImage, [1, 2]));

% Convert images to grayscale for simplicity
originalGray = rgb2gray(originalImage);
maskedGray = rgb2gray(maskedImage);

% Compute the absolute difference between the original and masked images
difference = imabsdiff(originalGray, maskedGray);

% Threshold the difference image to create a binary mask
threshold = 75;  % Adjust this threshold based on your images
binaryMask = difference > threshold;

% Display the binary mask
imshow(binaryMask);
title('Binary Mask');

% Optional: Save the binary mask
% imwrite(binaryMask, 'binary_mask.jpg');
