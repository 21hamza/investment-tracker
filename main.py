from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import yfinance as yf
app=FastAPI()

class Investment(BaseModel):
    ticker: str
    amount: float
    date: date
    buy_prices:float=0.0
    shares:float=0.0

portfolio=[]
@app.get("/")
def root():
    return {"message":"Hello World"}
@app.post("/invest")
def add_investment(investment: Investment):
    stock=yf.Ticker(investment.ticker)
    hist=stock.history(start=investment.date,end=investment.date)
    if hist.empty:
        return {"error":"No data"}
    buy_prices=hist['Close'].iloc[0]
    shares=investment.amount/buy_prices
    investment.buy_prices=round(buy_prices,2)
    investment.shares=round(shares,2)
    portfolio.append(investment)
    return {"message": "Investment added","data": investment}
@app.get("/investments")
def get_investments():
    result=[]
    for inv in portfolio:
        try:
            stock=yf.Ticker(inv.ticker)
            data=stock.history(period="1d")
            if data.empty:
                current_price=None
                profit=None
            else:
                current_price=data['Close'].iloc[-1]
                profit=(current_price-inv.buy_prices)*inv.shares
                result.append({
                    "ticker":inv.ticker,
                    "amount_invested":inv.amount,
                    "buy_price":inv.buy_prices,
                    "shares":inv.shares,
                    "current_price":round(current_price,2) if current_price else None,
                    "profit_or_loss":round(profit,2) if profit else "N/A"
                })
        except Exception as e:
            result.append({"error":str(e)})
    return {"portfolio":portfolio}

@app.get("/price/{ticker}")
def get_price(ticker: str):
    try:
        stock=yf.Ticker(ticker)
        data=stock.history(period="1d")

        if data.empty:
            return {"error":"No data"}

        price=data["Close"].iloc[-1]
        return {
            "ticker":ticker.upper(),
            "price":round(price,2)
        }

    except Exception as e:
        return {"error":str(e)}


