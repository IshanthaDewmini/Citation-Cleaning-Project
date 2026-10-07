Bibliography and Citation Cleaner Using Python

This is a project based on checking and organising bibliographic references exported from Mendeley. The references were saved in Mendeley Reference Manager for writing a report based on Pharmaceutical legislation guidelines in the EU. The project uses a BibTeX file exported from Mendeley containing 15 references.

The Python script

1. Reads a BibTeX bibliography exported from Mendeley
2. Identifies individual reference records
3. Checks for missing authors, years, DOIs
4. Checks for duplicates
5. Identifies different BibTeX reference types
6. Extracts bibliographic fields from the records
7. Allows incomplete references to be reviewed and verified
8. Formats references in ACS style
9. Generates a PDF bibliography

These records were subsequently reviewed and additional bibliographic information was verified.
Missing information was extracted from reliable resources online.

Methodology and Libraries Used

Python
Regular Expressions
BibTeX
ReportLab
Mendeley
Git & GitHub

Results

The BibTex had 15 bibliographic references exported from Mendeley. Thirteen references contained usable bibliographic information, while two references were identified as incomplete with missing author, year, or DOI information. The incomplete references were saved separately for further review and verification. The missing information was retrieved from the legit internet sources. Additional bibliographic information was verified for the two incomplete records, and an ACS-style bibliography containing the processed references was generated as a PDF. The script also identified the different BibTeX reference types and displayed the bibliographic fields available for each reference.


Discussion

This project demonstrates a practical application of Python to scientific literature and research data management. During research with a large set of references, it is hard to identify which references have missing details for final reference management. Python can be used to extract all information and assess the reliability of the reference materials. The project combines text processing, bibliographic data extraction, validation, and document generation into a small research-oriented workflow.
