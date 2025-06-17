from fpdf import FPDF
from datetime import datetime

clean_message = """
To Chase Private Client Services,

I, Seth Jude Landry, am requesting formal confirmation regarding the cleared and certified deposit(s) into my CPC account ending in 3036.

Reference Summary:

- Primary Deposit: $7,260,000.00 - Source: AltaHQ
- Secondary Deposit: $350,000,000.00 - Custodial Claim from Coinbase Custody
- Third: $56,850.00 - Wallet recovery wire
- Date(s) of Initiation: Ranged June 10 - June 12, 2025
- Reference Code: CB-CHASE-REF-7260001
- Status: Publicly verified as "Cleared and Available" at https://wallet.setland7.com
- Last update timestamp: June 12, 2025 - 3:11 PM CST

Please confirm:

1. Are these funds received or pending within Chase internal systems?
2. If received, are they reflected in my available balance?
3. If not yet released, what is required to complete the release?

I am the authorized Lead Funds Manager and CPA contact. I can provide notarized documents, vault proof, and certified asset verification upon request.

Sincerely,
Seth Jude Landry
Phone: 337-918-8500
Email: cajungotshop@gmail.com
Vault Link: https://wallet.setland7.com
Reference: CB-CHASE-REF-7260001
"""

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Funds Deposit Verification - Account Ending in 3036", ln=True)

pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, clean_message)

# Footer
pdf.set_y(-30)
pdf.set_font("Arial", 'I', 10)
timestamp = datetime.now().strftime("%B %d, %Y - %I:%M %p")
pdf.cell(0, 10, f"Generated on {timestamp}", ln=True)
pdf.cell(0, 10, "This document is certified and may be submitted to Chase, CPA, or legal review.", ln=True)

# Save
pdf.output("CHASE_Funds_Verification_Request_SethJudeLandry.pdf")
print("✅ PDF successfully generated.")

clean_message = """
To Chase Private Client Services,

I, Seth Jude Landry, am requesting formal confirmation regarding the cleared and certified deposit(s) into my CPC account ending in 3036.

Reference Summary:

- Primary Deposit: $7,260,000.00 - Source: AltaHQ
- Secondary Deposit: $350,000,000.00 - Custodial Claim from Coinbase Custody
- Third: $56,850.00 - Wallet recovery wire
- Date(s) of Initiation: Ranged June 10 - June 12, 2025
- Reference Code: CB-CHASE-REF-7260001
- Status: Publicly verified as "Cleared and Available" at https://wallet.setland7.com
- Last update timestamp: June 12, 2025 - 3:11 PM CST

Please confirm:

1. Are these funds received or pending within Chase internal systems?
2. If received, are they reflected in my available balance?
3. If not yet released, what is required to complete the release?

I am the authorized Lead Funds Manager and CPA contact. I can provide notarized documents, vault proof, and certified asset verification upon request.

Sincerely,
Seth Jude Landry
Phone: 337-918-8500
Email: cajungotshop@gmail.com
Vault Link: https://wallet.setland7.com
Reference: CB-CHASE-REF-7260001
"""

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Funds Deposit Verification - Account Ending in 3036", ln=True)

pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, clean_message)

# Footer
pdf.set_y(-30)
pdf.set_font("Arial", 'I', 10)
timestamp = datetime.now().strftime("%B %d, %Y - %I:%M %p")
pdf.cell(0, 10, f"Generated on {timestamp}", ln=True)
pdf.cell(0, 10, "This document is certified and may be submitted to Chase, CPA, or legal review.", ln=True)

# Save
pdf.output("CHASE_Funds_Verification_Request_SethJudeLandry.pdf")
print("✅ PDF successfully generated.")
