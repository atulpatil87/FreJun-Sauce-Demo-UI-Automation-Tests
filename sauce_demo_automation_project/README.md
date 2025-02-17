# Sauce Demo UI Automation Tests

## 📌 Project Overview
This project contains automated UI tests for [Sauce Demo](https://www.saucedemo.com/) using **Selenium** with the **Pytest** framework.

✅ Login (valid & invalid cases)  
✅ Sorting of items  
✅ Verifying product display  
✅ Adding items to cart & verifying payment values  
✅ Checkout process  
✅ Logout  
✅ Negative cases (wrong credentials, empty cart checkout, etc.)  

---

## 🛠 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone <your-github-repo-url>
cd sauce_demo_tests
```

### **2️⃣ Create & Activate Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
Install required Python packages:
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up WebDriver**
ChromeDriver is automatically managed by **pytest-selenium**, so no need to download manually.

---

## 🚀 Running the Tests

### **Run All Tests**
```bash
pytest -v --tb=short
```

### **Run Specific Test File**
```bash
pytest tests/test_login.py
```

### **Run Tests in Parallel (Requires pytest-xdist)**
```bash
pytest -n 2
```

### **Generate HTML Report (Requires pytest-html)**
```bash
pytest --html=report.html --self-contained-html
```

---
### For HTML Reports
pytest -v --html=report.html


## 📂 Project Structure
```
sauce_demo_tests/
│── tests/
│   ├── test_login.py
│   ├── test_sorting.py
│   ├── test_product_display.py
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│   ├── test_negative_cases.py
│── pages/
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│── conftest.py
│── requirements.txt
│── README.md
│── pytest.ini
```

### **📌 Explanation:**
- `tests/` → Contains all test cases.
- `pages/` → Page Object Model (POM) files for modular automation.
- `conftest.py` → Common fixtures & setup configurations.
- `requirements.txt` → Lists required dependencies.
- `pytest.ini` → Pytest configuration file.

---

## 📌 Assumptions & Constraints
1. The tests assume the site is **stable** and elements do not change frequently.
2. ChromeDriver is **automatically handled** by `pytest-selenium`, so no need to download it manually.
3. The login test uses a **standard test user**: `standard_user` with `secret_sauce`.
4. The framework is extendable for other test scenarios as needed.

---

## 🛠 Dependencies
- Python 3.x
- Pytest
- Selenium
- pytest-xdist (for parallel execution)
- pytest-html (for HTML reports)
- pytest-selenium (for automatic WebDriver management)
- PyChart (for visualization and reporting)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## 📬 Contribution
Feel free to **fork** this repository and raise a pull request for any enhancements or bug fixes.

📧 **For any issues, contact:** _your-email@example.com_

Happy Testing! 🚀

