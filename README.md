# Breast Cancer Prediction using Logistic Regression

This project implements a Logistic Regression model to predict whether a breast tumor is benign or malignant based on various medical features from the **breast_cancer.csv** dataset. The project achieved an accuracy of **96%** using K-Fold Cross Validation.

## Dataset

The dataset contains features related to breast cancer cell measurements:
- **Clump Thickness**
- **Uniformity of Cell Size**
- **Uniformity of Cell Shape**
- **Marginal Adhesion**
- **Single Epithelial Cell Size**
- **Bare Nuclei**
- **Bland Chromatin**
- **Normal Nucleoli**
- **Mitoses**

The target variable `Class` has two possible values:
- `2` for **Benign** (non-cancerous)
- `4` for **Malignant** (cancerous)

## Project Structure

- `breast_cancer.csv` - Dataset used for training the model.
- `cancer.pkl` - Saved model file using pickle for later use.
- `cancer.ipynb` - Main Python script with model training, evaluation, and prediction
- `breast.py` - Main Python script Streamlit web interface.
- `README.md` - This documentation file.

## Dependencies

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should include:
```
pandas
scikit-learn
pickle
streamlit
```

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the `breast.py` script to see on Web developed using Streamlit .
3. The model is saved as `cancer.pkl` for future predictions.
4. To predict a tumor's class using the trained model, input a sample as follows:

```python
# Example prediction
cy = model.predict([[5,1,1,1,2,1,3,1,1]])
print(cy)  # Output will be either 2 (Benign) or 4 (Malignant)
```

## Results

- **Accuracy**: 96%
- **Confusion Matrix**: Displays the model's performance in terms of correctly/incorrectly classified instances.
- **Cross-Validation**: K-Fold Cross Validation is used to estimate the model’s accuracy and variability.

## Future Improvements

- Explore other models like SVM, Random Forest, etc.
- Implement feature scaling for potential performance improvements.
- Build a web interface using Flask or Streamlit for easy interaction.

---

You can modify this based on additional features you add or remove from the project.
