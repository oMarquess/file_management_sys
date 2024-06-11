# File Management System

## Overview
This File Management System is designed to automate the extraction of structured data from various document formats. It creates summaries, critiques of PowerPoint presentations, visualizes complex data trapped in PDFs, and ensures outputs are trustworthy and relevant to user queries. This system is ideal for users needing to manage and analyze large volumes of document data efficiently.

## Features

- **Data Extraction**: Automatically extract structured data from diverse document formats.
- **PowerPoint Processing**: Generate summaries and critiques of PowerPoint presentations.
- **Data Visualization**: Convert complex data from PDFs into visual representations.
- **Trustworthy Outputs**: Ensures the accuracy and relevance of outputs to user queries.

## Experimental Notebooks

The system includes three Jupyter notebooks that handle different file types:

1. **PowerPoint Files**: `pptx_data.ipynb` - Handles the extraction and analysis of data from `.pptx` files.
2. **PDF Files**: `pdf_data.ipynb` - Focuses on extracting and visualizing data from `.pdf` files.
3. **CSV Files**: `csv_data.ipynb` - Efficiently processes and analyses `.csv` files, favored for its reliability and ease of use.

## Backend

The system leverages a separate Django Rest Framework (DRF) app to handle queries and processing for any file type. This backend is designed to provide flexibility and robustness in managing a variety of document formats. It enables data analytic Retriever-And-Generator (RAG) operations on any uploaded file through an API. This feature is optional and can be integrated based on specific user needs.

To utilize this backend:

1. **API Integration**: The backend can be accessed via an API, allowing users to perform operations on uploaded files directly through API calls.
2. **Data Analytics**: Implements a Retriever-And-Generator approach for data extraction and analysis, providing advanced insights and summaries based on the content of the files.
3. **Optional Use**: This backend module is optional and can be enabled or disabled as required by the user, ensuring that resources are utilized efficiently only when needed.

For API documentation and setup instructions, refer to the `api_docs.md` file included in the backend directory.

## Evaluation Report

- **CSV Files**: The system performs exceptionally well with CSV files, providing reliable and efficient data processing.
- **PDF Files**: While the system generally handles PDFs effectively, there are instances where the visualization code may not execute correctly, requiring the user to refine the code manually.
- **PowerPoint Files**: The PowerPoint handling is robust, offering detailed summaries and critiques that add value to presentation analysis.

## Getting Started

To get started with the File Management System, clone the repository and install the required dependencies:

```bash
git clone [repository-url]
cd file-management-system
pip install -r requirements.txt


To run any of the notebooks, use:
`jupyter notebook [notebook-name.ipynb]`