# **README: LSTMF File Results & Cherokee Ground Truth Data**  

## **Overview**  
This folder generates **LSTMF training data** and **Cherokee ground truth (GT) files** to support **OCR model training** for the **Cherokee language** using **Tesseract LSTM**. The **LSTMF files** contain processed training samples used to refine the recognition model, while the **ground truth files** ensure accurate text-image alignment for supervised learning.  

## **LSTMF File Results**  
- **LSTMF files** are created during the training process using `trainins-tess.py`.  
- These files contain **character sequences mapped to image features**, allowing the model to improve text recognition.  
- They serve as **input for Tesseract’s LSTM training**, guiding the AI model in learning Cherokee script structures.  
- Stored in: `G:\Cherokee\ltmsf`  

## **Cherokee Ground Truth Results**  
- Created by `cherokee_ground_truth_template.py`, these files provide **labeled transcriptions** for each training image.  
- They contain **word-level alignments** of Cherokee text, symbols, and English translations.  
- The GT data is used to **validate OCR outputs** and **refine accuracy during training**.  
- Stored in: `G:\Cherokee\cherokee_ground_truth`  

## **Purpose & Next Steps**  
- These datasets are used to **train and test** a **Cherokee OCR model**, ensuring better **text recognition accuracy**.  
- The **LSTMF files** refine the model’s **understanding of script patterns**, while **GT files** provide a **benchmark for evaluation**.  
- Once trained, the final model can be used to **extract Cherokee text** from historical documents and digital archives.  
