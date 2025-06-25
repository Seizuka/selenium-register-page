📄 Selenium Register Page – Alfakarir
Automated end-to-end testing of the candidate registration process at alfakarir.alfamart.co.id/register, using Python, Selenium, and the Page Object Model (POM) pattern.

📂 Project Structure
bash
Salin
Edit
selenium-register-page/
├── pages/
│   └── register_page.py     # Page Object class for the registration form
├── test_cases/
│   └── register.py          # Main test case
├── data/
│   └── register_data.json   # Test data input
├── utils/
│   └── crypto_utils.py      # Utility for password encryption/decryption
├── main.py                  # Entry point to run the test
├── requirements.txt         # Python dependencies
└── README.md
⚙️ Prerequisites
Python 3.7 or higher

Install dependencies:

bash
Salin
Edit
pip install -r requirements.txt
requirements.txt:
nginx
Salin
Edit
selenium
cryptography
🧪 Test Data
Test input is stored in data/register_data.json, for example:

json
Salin
Edit
{
  "full_name": "Test Name",
  "id_number": 1234567890123456,
  ...
  "university": "UNIVERSITAS GAJAH MADA",
  "major": "TEKNIK INFORMATIKA",
  "graduate_year": "2021"
}
Make sure to provide valid paths for photo and resume files.

🛠️ Special Handling
University (Select2 dropdown): Click on span#select2-institution_name-container, input text to search, wait for the match, then click the option.

Date of Birth & Graduation Year: Inputs are read-only and populated using JavaScript injection.

City/Subdistrict/Village Dropdowns: Wait for dynamic options to load before selecting with select_by_visible_text.

🚀 Running the Test
Install dependencies:

bash
Salin
Edit
pip install -r requirements.txt
Run the test:

bash
Salin
Edit
python main.py
or directly:

bash
Salin
Edit
python test_cases/register.py
✅ Verification
After completing the education step, the test checks for the presence of an alert <h2> with the text "Berhasil!" (Success).

If the element and text appear, the test is considered passed.

📦 What Is Automated
Open the homepage and click Register

Upload profile photo

Fill in personal profile information ✓

Select gender, religion, DOB, marital status, upload resume ✓

Click Next to proceed to Address page

Fill province, city, subdistrict, village, home status, and full address ✓

Click Next to proceed to Education page

Select education level, university (via Select2), major, and graduation year (using JS injection) ✓

Submit form and verify success alert ("Berhasil!") ✓

🧩 Page Object Model (POM)
This project uses the Page Object Model design to separate logic and UI interactions. The RegisterPage class in register_page.py encapsulates all web element interactions like fill_profile(), select_university(), etc., improving maintainability.

🔑 Key Files & Roles
main.py / test_cases/register.py: script to run the test

pages/register_page.py: handles all UI element interactions

data/register_data.json: stores input test data

utils/crypto_utils.py: encrypt/decrypt password if needed

✅ Summary
This test suite automates the registration process on Alfakarir using Selenium + POM with a data-driven approach (JSON) and advanced techniques like JavaScript injection and dynamic dropdown waits. A good reference for testing similar multi-step forms.