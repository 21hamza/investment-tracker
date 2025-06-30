
# 📊 Investment Tracker API

A backend-only stock investment tracker built with **FastAPI** and **yfinance**, designed to calculate real-time **profit/loss** on stock investments.

> 🔧 Built as a showcase project for backend development and finance using Python.

---

## 🚀 Features

- 📈 Add stock investments with date and amount
- 💹 Get current live stock price using `yfinance`
- 💰 Calculates real-time profit/loss per investment
- 🧠 Auto-validated request structure using Pydantic
- 🧪 Swagger UI to test all endpoints instantly (`/docs`)

---

## ⚙️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.9+
- [yfinance](https://pypi.org/project/yfinance/)
- Pydantic

---

## 🧪 Installation & Run Locally

1. **Clone this repo:**

```bash
git clone https://github.com/your-username/investment-tracker.git
cd investment-tracker
```

2. **Install dependencies:**

```bash
pip install fastapi uvicorn yfinance
```

3. **Run the server:**

```bash
uvicorn main:app --reload
```

4. Open your browser:
- Swagger Docs: `http://127.0.0.1:8000/docs`
- Root: `http://127.0.0.1:8000/`

---

## 🔁 API Endpoints

### `POST /invest`

Add a new investment

**Body:**
```json
{
  "ticker": "AAPL",
  "amount": 1000,
  "date": "2025-06-01"
}
```

---

### `GET /investments`

Returns all stored investments along with:

- Buy price
- Current price
- Number of shares
- Profit or loss

---

### `GET /price/{ticker}`

Fetches the current price for any stock (e.g. `/price/TSLA`)

---

## 👤 Author

Made with ❤️ by **Hamza Alam**

- [GitHub](https://github.com/your-username)
- [LinkedIn](https://linkedin.com/in/your-link)

---

## 🏁 Future Improvements

- Connect to SQLite or PostgreSQL for real data storage
- Add authentication for users
- Build a React frontend for UI

---
