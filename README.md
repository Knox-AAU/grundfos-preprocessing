# KNOX Preprocessing
This project is part of the KNOX multiproject and is located in layer one. The goal of this module is to extract and segment information from PDF-documents provided by Grundfos.

The module is able to extract text, titles, images and tables from PDF-files and produce a folder containing the extracted information. The module contains three components in addition to a few utilities:
- The **Text Segmenter** component recursively scans the document to find and segment text into their correct sections or subsections.
- The **Miner** component analyzes the lines in the document to find tables and figures.
- The **Inference** component which uses computer vision to find tables and images (as well as text, lists and titles if desired).


# Installation
1. Clone the repository using ``` git clone https://git.its.aau.dk/Knox/grundfos-preprocessing.git ```
2. Create a new virtual environment using your preferred tool for example Conda. For Conda: ``` conda create -n grundfos-preprocessing python=3.8 ```
3. Activate the virtual environment. For Conda: ```conda activate grundfos-preprocessing```
4. Install required dependencies with pip: ``` pip install -r requirements.txt ```
5. To use the machine-intelligence component download the model from ```https://drive.google.com/file/d/1Jx2m_2I1d9PYzFRQ4gl82xQa-G7Vsnsl/view?usp=sharing``` and place it in the *classification* folder.

# Usage

To segment a document run the *segment.py* file in the root folder of the repository using the following command:
```
python segment.py INPUT_FOLDER OUTPUT_FOLDER
```

To learn what flags and commands are available run:
```python segment.py --help``` or ```python segment.py -h```