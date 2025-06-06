from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import yfinance as yf

def get_stock_price(ticker: str) -> float:
    """
    Fetch the current price of a stocck price for a given ticker symbol.

    Args:
         ticker (str): The stock ticker symbol.

    Returns:
        float: The current price of the stock.
    """
    stock = yf.Ticker(ticker)
    price = stock.info.get("currentPrice", "Price not available")
    return {"price": price, "ticker": ticker}


base_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[get_stock_price], 
    name='root_agent',
    description="A helpful agent that gets stock price.",
    instruction="You are a stock price assistant. Always use the get_stock_price tool."
                "include the ticker symbol in your response."
)

root_agent = base_agent
