import re

with open(r"c:\Users\devpa\Downloads\portfolio\index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Define the replacements for each project title block
replacements = [
    ("Automatic Paper Cutter with Smart IoT Automation", "https://github.com/pawani04/SmartPaperCutter"),
    ("Next-Gen City Waste Management System", "https://github.com/pawani04/Waste-Management-System"),
    ("PharmaGo: Cross-Platform Healthcare App", "https://github.com/pawani04/PharmaGo"),
    ("Smart Gadget E-Commerce Marketplace", "https://github.com/pawani04/Smart-Gadget-Store"),
    ("Cloud-Based Smart POS System", "https://github.com/pawani04/Smart_POS_System"),
    ("Smart Tourist Safety & Emergency Tracking", "https://github.com/pawani04/tourist_safety_app"),
    ("Telco AI Customer Churn Predictor", "https://github.com/pawani04/Telco-Churn-Predictor"),
    ("Wander Ceylon Tourism Platform", "https://github.com/pawani04/Wander_Ceylon"),
    ("Lotus Care BI & Data Warehouse Solution", "https://github.com/pawani04/DW-AL-Student-results-analyse")
]

# We need to replace the very next <a href="https://github.com/pawani04"... after each project title
for title, link in replacements:
    # Find the index of the title
    title_idx = html_data.find(title)
    if title_idx != -1:
        # Find the next href="https://github.com/pawani04"
        href_idx = html_data.find('href="https://github.com/pawani04"', title_idx)
        if href_idx != -1 and href_idx < title_idx + 2000:
            # Replace it
            html_data = html_data[:href_idx] + f'href="{link}"' + html_data[href_idx + len('href="https://github.com/pawani04"'):]

with open(r"c:\Users\devpa\Downloads\portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html_data)

print("Done updating GitHub links!")
