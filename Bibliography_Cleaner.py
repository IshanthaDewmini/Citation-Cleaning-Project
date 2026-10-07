from pathlib import Path
import re

file = Path("export.bib")
with open(file, "r", encoding="utf-8") as f:
    data = f.read()

#Count the number of references
references = data.count("@")
print(f"Number of references: {references}")

#Split the BibTeX file into individual references
references = re.findall(
    r'@\w+\s*\{.*?(?=\n@|\Z)',
    data,
    flags=re.DOTALL
)
print(f"Number of references after split: {len(references)}")

#Check for missing authors, year, DOI numbers, duplicate titles
print("\nChecking for missing authors and years:")
for i, reference in enumerate(references, start=1):

    if "author =" not in reference:
        print(f"\nReference {i} is missing an author.")

    if "year =" not in reference:
        print(f"Reference {i} is missing a year.")

    if "doi =" not in reference or "doi = {}" in reference:
        print(f"Reference {i} is missing a DOI number.")

#Check for duplicate titles
print("\nChecking for duplicate titles:")
titles = []
for reference in references:

    match = re.search(r'title\s*=\s*\{(.*?)\}', reference, re.DOTALL)

    if match:
        title = match.group(1).strip()

        if title in titles:
            print(f"Duplicate title found: {title}")

        else:
            titles.append(title)

#Save incomplete references to a seperate file
with open("incomplete_references.bib", "w", encoding="utf-8") as f:
    for i, reference in enumerate(references, start=1):
        if "author =" not in reference or "year =" not in reference or "doi =" not in reference or "doi = {}" in reference:
            f.write(reference + "\n")
print("\nIncomplete references have been saved to 'incomplete_references.bib'.")

#Create a report of incomplete references
with open("incomplete_references_report.txt", "w", encoding="utf-8") as f:
    for i, reference in enumerate(references, start=1):
        missing = []
        if "author =" not in reference:
            missing.append("author")
        if "year =" not in reference:
            missing.append("year")
        if "doi =" not in reference or "doi = {}" in reference:
            missing.append("DOI number")
        if missing:
            f.write(f"Reference {i}\n")
            f.write(f"Missing: {', '.join(missing)}\n\n")
            f.write(reference.strip())
            f.write("\n\n")
print("\nIncomplete references report has been saved to 'incomplete_references_report.txt'.")

#Complete information for reference 5 and 2

author = "Dent, N.J."
year = "1994"
title = "European Regulatory Compliance Issues: Good Research Practices"
journal = "Journal of the American College of Toxicology"
volume = "13"
issue = "1"
pages = "79-85"
doi = "10.3109/10915819409140658"         

author = "Zolkarnain, N.; Ishak, S.A.; Shaari, A.L.; Roslan, N.A.; Ghazali, R."
year = "2019"
title = "Good Laboratory Practice (GLP) for Greater Compliance in an Increasingly Regulated Market"
journal = "Palm Oil Developments"
volume = "71"
pages = "33-40"

#Create Harvard Refencing style for reference 5 and 2
harvard_ref_5 = f"{author} ({year}) '{title}', {journal},{volume}({issue}), pp. {pages}. doi: {doi}."
harvard_ref_2 = f"{author} ({year}) '{title}', {journal},{volume}, pp. {pages}."

print("\nHarvard reference:")
print(harvard_ref_5)
print(harvard_ref_2)

#Identify the reference type 
print("\nIdentifying reference types:")
for i, reference in enumerate(references, start=1):
    match = re.search(r'@(\w+)\s*\{', reference)
    if match:
        reference_type = match.group(1)
        print(f"Reference {i}: {reference_type}")

#Show info in miscellaneous references
print("\nMiscellaneous references:")
for i, reference in enumerate(references, start=1):
    if "@misc" in reference:
        print(f"\nReference {i}:")
        print(reference[:1000])

#Show the fields available in each refernce
print("\nFields found in each reference:")

for i, reference in enumerate(references, start=1):
    fields = re.findall(r'^\s*([A-Za-z_]+)\s*=', reference, re.MULTILINE)
    print(f"Reference {i}: {', '.join(fields)}")

    #Conclusion
#There are 15 references
#13 have usable bibliographic information
#2 are incomplete. But extracted righ info online
#What fields are available for each reference
#What some @misc entries are actually journal articles

#Verified Refence detais
verified_references = {
    2: {
        "author": "Zolkarnain, N.; Ishak, S. A.; Shaari, A. L.; Roslan, N. A.; Ghazali, R.",
        "title": "Good Laboratory Practice (GLP) for Greater Compliance in an Increasingly Regulated Market",
        "journal": "Palm Oil Developments",
        "year": "2019",
        "volume": "71",
        "pages": "33-40"
    },
    5: {
        "author": "Dent, N. J.",
        "title": "European Regulatory Compliance Issues: Good Research Practices",
        "journal": "Journal of the American College of Toxicology",
        "year": "1994",
        "volume": "13",
        "issue": "1",
        "pages": "79-85",
        "doi": "10.3109/10915819409140658"
    }
}

#Generate ACS style refernces
def get_field(reference, field):
    match = re.search(
        rf'^\s*{field}\s*=\s*\{{(.*?)\}}',
        reference,
        re.DOTALL | re.MULTILINE
    )

    if match:
        return match.group(1).strip()

    return None
print("\nACS-style references:")
acs_references = []
for i, reference in enumerate(references, start=1):

#Use verified information for References 2 and 5
    if i in verified_references:

        data = verified_references[i]

        author = data["author"]
        title = data["title"]
        journal = data["journal"]
        year = data["year"]
        volume = data.get("volume")
        issue = data.get("issue")
        pages = data.get("pages")
        doi = data.get("doi")

    else:

        author = get_field(reference, "author")
        title = get_field(reference, "title")
        journal = get_field(reference, "journal")
        booktitle = get_field(reference, "booktitle")
        year = get_field(reference, "year")
        volume = get_field(reference, "volume")
        issue = get_field(reference, "issue")
        pages = get_field(reference, "pages")
        doi = get_field(reference, "doi")

#Check for missing essential information
    if not author or not title or not year:
        acs_references.append(
            f"Reference {i}: Incomplete information"
        )
        continue

#Format the reference
    reference_text = f"{author}. {title}."

    if journal:
        reference_text += f" {journal}"

        if year:
            reference_text += f" {year}"

        if volume:
            reference_text += f", {volume}"

        if issue:
            reference_text += f" ({issue})"

        if pages:
            reference_text += f", {pages}"

        reference_text += "."

    elif booktitle:
        reference_text += f" In {booktitle}"

        if year:
            reference_text += f", {year}"

        if pages:
            reference_text += f", {pages}"

        reference_text += "."

    if doi:
        reference_text += f" https://doi.org/{doi}"

    acs_references.append(
        f"{i}. {reference_text}"
    )

#Display the references
for reference in acs_references:
    print(reference)

#Creating PDF
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import cm

pdf_file = "ACS_Bibliography.pdf"
document = SimpleDocTemplate(
    pdf_file,
    pagesize=A4,
    rightMargin=2 * cm,
    leftMargin=2 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm
)
styles = getSampleStyleSheet()
title_style = styles["Title"]
title_style.alignment = TA_CENTER
reference_style = styles["BodyText"]
reference_style.fontSize = 10
reference_style.leading = 14
story = []
story.append(Paragraph("ACS-Style Bibliography", title_style))
story.append(Spacer(1, 0.5 * cm))
for reference in acs_references:
    story.append(Paragraph(reference, reference_style))
    story.append(Spacer(1, 0.3 * cm))
document.build(story)

print(f"\nPDF created successfully: {pdf_file}")