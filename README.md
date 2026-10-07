Bibliography and Citation Cleaner Using Python

This is a project based on checking and organising bibliographic references exported from Mendeley. The refernces were saved on Mendeley refernce manager for writing a report based on Pharmaceutical legislation guideline in the EU. The project uses a BibTeX file exported from Mendeley containing 15 references.

The Python script 
1. Reads a BibTex bibliography exported from Mendeley
2. Identifies individual reference records
3. Check for missing authors, years, DOIs
4. Check for duplicates
5. Identifies different BibTeX reference types
6. Extracts bibliographic fields from the records
7. Allows incomplete references to be reviewed and verified
8. Formats references in ACS style
9. Generates a PDF bibliography

These records were subsequently reviewed and additional bibliographic information was verified.
Missing information was extracted form reliable resources online. 

Methodology and Libraries Used
Python
Regular Expressions
BibTeX
ReportLab
Mendeley
Git & GitHub

Discussion
This project demonstrates a practical application of Python to scientific literature and research data management. During a research with a large set of references it is hard to guess which references have missing details for the final referencing management. Python can be used to extract all information and decide the reliability of the reference materials. The project combines text processing, bibliographic data extraction, validation, and document generation into a small research oriented workflow.