## Setup
0. Clone the repository:
   ```bash
   git clone https://github.com/username/mimic-query-tool.git
   cd mimic-query-tool

# Mimic Query Tool

### About This Project

This project was originally designed for the MIMIC-III dataset, but due to HIPAA compliance requirements, we shifted to using the **CORD-19 Research Challenge dataset**. Naming things is hard, so the repository still references "mimic," even though it now focuses on COVID-19 research.

### Dataset

This project uses the [CORD-19 Research Challenge](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge) dataset. The dataset contains metadata and full-text research papers related to COVID-19.

#### Setting Up the Dataset

1. **Download the Dataset**:
   - Make sure you have Kaggle CLI installed. If not, install it:
     ```bash
     pip install kaggle
     ```
   - Download the dataset:
     ```bash
     kaggle datasets download -d allen-institute-for-ai/CORD-19-research-challenge
     ```

2. **Unzip the Dataset**:
   - Extract the files into a `data/` directory:
     ```bash
     mkdir data
     unzip CORD-19-research-challenge.zip -d data/
     ```

3. **Ignore the Dataset in Git**:
   - The `data/` folder and the zip file are ignored in `.gitignore` to keep the repository clean.

---

### **3. Updated Directory Structure**

Once you've unzipped the dataset, your project directory structure should look like this: