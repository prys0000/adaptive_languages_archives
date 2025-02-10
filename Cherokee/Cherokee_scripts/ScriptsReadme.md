
# **Cherokee Language Training and Deployment Scripts**  

## **Overview**  
This repository contains a **closed AI network** designed for **Cherokee language processing** using **Tesseract OCR and metadata standardization**. These scripts facilitate:  

1. **Data preparation** (Generating training images, ground truth, and structured language data)  
2. **Model training** (Training Tesseract OCR with Cherokee text)  
3. **Model deployment** (Recognizing Cherokee text in images and extracting text)  

Unlike open-internet models, this **only uses Indigenous-reviewed materials** and operates within a **controlled environment** to ensure **linguistic accuracy, cultural integrity, and historical context**.  

---

## **Script Organization**  

### **1. Data Preparation**  
Before training the AI, we must generate and organize the data. These scripts handle **Cherokee word-image creation, ground truth extraction, and training list generation**.  

#### **a) `language_template.py`** (Generates labeled images from Cherokee language data)  
- Reads a **CSV file** containing **English words, Cherokee symbols, and Cherokee words**  
- Generates **images** containing labeled Cherokee text  
- Saves output to a specified directory  

#### **b) `cherokee_ground_truth_template.py`** (Creates ground truth text files for OCR training)  
- Reads the **same CSV file**  
- Creates **.gt.txt (ground truth) files** corresponding to the generated images  
- Stores them in `cherokee_ground_truth/` for training  

#### **c) `lists-cherokee_template.py`** (Generates training data lists for OCR)  
- Scans the **ground truth directory**  
- Converts images and corresponding text into **Tesseract training format**  
- Prepares the dataset for model training  

---

### **2. Model Training**  
Once the dataset is prepared, we train the Cherokee OCR model.  

#### **d) `trainins-tess.py`** (Trains Tesseract OCR with Cherokee text)  
- Uses **Tesseract lstmtraining**  
- Loads the **Cherokee `.traineddata` model**  
- Processes **training and evaluation lists**  
- Iterates until convergence to refine accuracy  

---

### **3. Model Deployment**  
Once the AI model is trained, it can recognize Cherokee text in new images.  

#### **e) `cherokee_lang_deploy.py`** (Deploys the trained OCR model)  
- Uses **Tesseract OCR**  
- Processes **input images**  
- Extracts **Cherokee text** and saves results in `.txt` files  

#### **f) `cherokee_lang_deploy_template.py`** (Customizable deployment script for different datasets)  
- Functions the same as `cherokee_lang_deploy.py` but allows users to **modify input and output paths**  

---

## **How to Use the Scripts**  

### **Step 1: Prepare Training Data**  
1. Update the **CSV file** with Cherokee words.  
2. Run `language_template.py` to generate labeled images.  
3. Run `cherokee_ground_truth_template.py` to create `.gt.txt` files.  
4. Run `lists-cherokee_template.py` to prepare training data lists.  

### **Step 2: Train the OCR Model**  
1. Ensure Tesseract is installed.  
2. Run `trainins-tess.py` to train the model.  

### **Step 3: Deploy the OCR Model**  
1. Move the trained `.traineddata` file to the **Tesseract tessdata directory**.  
2. Run `cherokee_lang_deploy.py` to process new images.  

---

## **Conclusion**  
This closed AI network ensures **Cherokee language preservation** using training within a **controlled, Indigenous-led framework**. By structuring the scripts in this order, we can efficiently develop, train, and deploy **Cherokee text recognition models** for archival research. 
