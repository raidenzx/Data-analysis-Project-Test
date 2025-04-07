# 📈 Sales Balance Automation

This project automates the generation of a detailed monthly sales report and sends it via email automatically.  
It uses **Pandas** for data processing and **smtplib** and **email.message** for sending emails.

## ✨ Features

- Processes sales data from a file (e.g., `.csv` or `.xlsx`)
- Generates a detailed monthly report
- Automatically sends the report via email

## 🛠 Technologies Used

- [Pandas](https://pandas.pydata.org/) — data manipulation
- [smtplib](https://docs.python.org/3/library/smtplib.html) — email sending
- [email.message](https://docs.python.org/3/library/email.message.html) — email content creation

## 📋 How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repository.git
```

2. **Install the dependencies:**

```bash
pip install pandas
```

3. **Configure your email settings inside the script:**

```python
SENDER_EMAIL = "your-email@example.com"
PASSWORD = "your-password"
RECEIVER_EMAIL = "receiver@example.com"
```

4. **Run the script:**

```bash
python sales_balance_automation.py
```

The report will be automatically sent to the configured recipient.

## 💑 Report Example

The report includes:
- Total sales for the month
- Best-selling product
- Total revenue
- Growth analysis (if applicable)

## 🔒 Security Notes

- Avoid hardcoding your credentials inside the script.
- It is highly recommended to use environment variables or a `.env` file to securely store sensitive information.

