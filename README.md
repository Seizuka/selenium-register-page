# 📄 Selenium Register Page – Alfakarir

Automated end-to-end testing of the candidate registration process at [alfakarir.alfamart.co.id/register](https://alfakarir.alfamart.co.id/register), using **Python**, **Selenium**, and the Page Object Model (POM) pattern.

---

## 📂 Project Structure

selenium-register-page/
├── pages/
│   └── register_page.py # Page Object class for the registration form
├── test_cases/
│   └── register.py # Main test case
├── data/
│ └── register_data.json # Test data input
├── encrypt_password.py # Script to encrypt plaintext password
├── main.py # Entry point to run the test
└── README.md # Project overview



## ⚙️ Prerequisites

- Python 3.7 or higher
- Google Chrome + ChromeDriver
- Install dependencies:

```bash

Install cryptography
pip install cryptography

pip install -r requirements.txt

selenium
cryptography



🧪 Test Data
{
  "full_name": "Test Name",
  "id_number": 1234567890123456,
  "email": "test@example.com"
}


🚀 Running the Test
python main.py


✅ What’s Automated

• Click "Daftar" from homepage
• Upload profile photo 
• Fill in:
• Full name, ID number, emails, password
• Phone number, place/date of birth, WA, gender, religion
• Marital status, weight/height, resume
• Click Next to Address Section:
• Province, City, Subdistrict, Village (with dynamic wait)
• Home status, home address, postal code
• Click Next to Education Section:
• Education level, university (Select2 dropdown), major, graduation year
• Submit form
• Verify success popup with Berhasil! heading

🔍 Special Handling

• Select2 Dropdowns (e.g. university):
    Click → input value → wait → select matched option
    Date Inputs (Read-only):
    Use JavaScript injection to populate DOB and graduation year

• Dynamic Dropdowns:
    Use .wait_until_*_loaded() before selecting City, Subdistrict, or Village


🧩 Page Object Model (POM)

This project uses the Page Object Model design to separate logic and UI interactions. The RegisterPage class in register_page.py encapsulates all web element interactions like fill_profile(), select_university(), etc., improving maintainability.

Example usage:
• register_page.fill_profile(...)
• register_page.select_university("UNIVERSITAS INDONESIA")
• register_page.set_graduate_year("2025")


📦 File Highlights

| File                 | Purpose                                  |
| -------------------- | ---------------------------------------- |
| `main.py`            | Entry point                              |
| `register.py`        | Executes full registration test          |
| `register_page.py`   | Handles web element logic                |
| `register_data.json` | External test data                       |
| `crypto_utils.py`    | Optional password encryption (if needed) |


📌 Notes

• This test uses Chrome browser by default.
• Add wait conditions carefully for dynamic fields.
• Retry university selection if default value ("Lain-lain") appears.
• Tested with site: https://alfakarir.alfamart.co.id/register
