#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: ARICA ACHARYA
# DATE CREATED:   01/24/2019                               
# REVISED DATE: 04/18/2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

filename_list = listdir("pet_images/")

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    # Creates list of files in directory
    in_files = listdir(image_dir)   
    # Creates empty dictionary for the labels
    petlabels_dic = dict()
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it
       # isn't an pet image file
       if in_files[idx][0] != ".":
           # Uses split to extract words of filename into list image_name
           image_name = in_files[idx].split("_")
           # Creates temporary label variable to hold pet label name extracted
           pet_label = ""         
           for word in image_name:
               # Only add to pet_label if word is all letters add blank at end
               if word.isalpha():
                   pet_label += word.lower() + " "
           # strips off trailing whitespace
           pet_label = pet_label.strip()         
           if in_files[idx] not in petlabels_dic:
              petlabels_dic[in_files[idx]] = pet_label
           else:
               print("Warning: Duplicate files exist in directory",
                     in_files[idx])
    # returns dictionary of labels
    return(petlabels_dic)

