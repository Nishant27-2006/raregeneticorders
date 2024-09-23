
# Gene Expression Analysis using K-Means Clustering

This project performs a basic machine learning analysis on a gene expression dataset, specifically applying K-Means clustering to normalized gene expression values. The dataset used in this analysis was sourced from GEO (GSE38959), which contains breast cancer gene expression data.

## Steps Performed:
1. **Data Preprocessing**: 
   - Extracted and normalized the gene expression values.
   - Cleaned the data by removing missing values.
2. **K-Means Clustering**: 
   - Applied K-Means clustering to identify groups of genes with similar expression profiles.
   - Visualized the clusters using scatter plots and density plots.
3. **Exploratory Data Analysis**: 
   - Plotted the distribution of normalized gene expression values.
   - Visualized the clusters.

## Dataset:
- **Source**: GEO (GSE38959) - [Download Link](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE38959&format=file)

## Requirements:
- Python 3.x
- pandas
- scikit-learn
- seaborn
- matplotlib

## How to Run:
1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the analysis script:
    ```bash
    python main.py
    ```

## Output:
The script generates two visualizations:
- A scatter plot showing the clusters based on normalized gene expression values.
- A density plot illustrating the distribution of gene expression values by cluster.

