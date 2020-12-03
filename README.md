# Face detection_and_Gender_Classification

# Project Overview

# Objective: 
            Developing Machine learning model for Face detection and Gender_Classification, and integrate it to flask App.
            
# Deliverables:
           1. Develop flask app and integrate machine learning model
           2. User will upload an image and app has to detect the face and identify gender.
           
           
# Dataset: 
          https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar
           
           
# Machine learning model Application folow:

         1. Input image
         2. Data preperation (Crop Image)
         3. Data prepprocessing
         4. Feature exraction
         5. Building Machine leaning model
         6. Making Pipeline model
         7. deploying machine leaning model using flask
         8. Output 
         
         
Note : to replicate this project, please download data from google drive and keep it same directory which are preset in jupyter notebooks.
       https://drive.google.com/file/d/1Wji7xRByWMGvNF9JPThozrNevs8j-YV_/view?usp=sharing
       
      
   # Performance of different machine learning model
   
| Model               | Accuracy | Precision | recall | f1-score | kappa score | AUC Score |
|---------------------|----------|-----------|--------|----------|-------------|-----------|
| SVM_without_PCA     | 0.793    | 0.784     | 0.895  | 0.836    | 0.559       | 0.9       |
| SVM_with PCA        | 0.84     | 0.863     | 0.867  | 0.865    | 0.67        | 0.91      |
| Naïve base          | 0.762    | 0.791     | 0.81   | 0.8      | 0.507       | 0.84      |
| KNN                 | 0.759    | 0.796     | 0.794  | 0.795    | 0.502       | 0.75      |
| Logistic Regression | 0.772    | 0.796     | 0.824  | 0.81     | 0.526       | 0.84      |
| Decision Trees      | 0.657    | 0.687     | 0.765  | 0.724    | 0.274       | 0.68      |
| Deep learning_CNN   | 0.854    | 0.872     | 0.88   | 0.876    | 0.698       | 0.91      |

         
i have build above machine learning models, out of all, SVM with PCA in which prinicipal component analysis has done before building machine leanring model is giving better result. i have chosen SVM with PCA for deployment.

later i tried with Deep learning as well, it is giving compared with SVM with PCA.


       

