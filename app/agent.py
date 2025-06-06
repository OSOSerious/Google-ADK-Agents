from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import yfinance as yf
from web3 import Web3, HTTPProvider

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

def get_evm_balance(address: str, rpc_url: str = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID") -> dict:
    """
    Fetch the ETH balance of a given EVM address.

    Args:
        address (str): The EVM wallet address.
        rpc_url (str): The RPC URL of the EVM chain. Defaults to Ethereum Mainnet (Infura).
                       Replace 'YOUR_INFURA_PROJECT_ID' with your actual Infura Project ID.

    Returns:
        dict: A dictionary containing the address and its balance in Ether.
    """
    try:
        w3 = Web3(HTTPProvider(rpc_url))
        if not w3.is_connected():
            return {"error": f"Could not connect to EVM RPC at {rpc_url}"}
        
        checksum_address = w3.to_checksum_address(address)
        balance_wei = w3.eth.get_balance(checksum_address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        return {"address": address, "balance_eth": float(balance_eth), "rpc_url": rpc_url}
    except Exception as e:
        return {"error": f"Failed to get EVM balance for {address}: {str(e)}"}

def get_cosmos_balance_placeholder(address: str, chain_id: str, denom: str) -> dict:
    """
    Placeholder tool to demonstrate Cosmos chain interaction.
    In a real implementation, this would use a Cosmos SDK client or make direct API calls.

    Args:
        address (str): The Cosmos wallet address.
        chain_id (str): The ID of the Cosmos chain (e.g., "cosmoshub-4").
        denom (str): The denomination of the token (e.g., "uatom").

    Returns:
        dict: A dictionary containing the address, mock balance, chain_id, and denom.
    """
    print(f"[Cosmos Tool Placeholder] Attempting to get {denom} balance for {address} on {chain_id}")
    # In a real scenario, you'd use a Cosmos SDK client or direct API calls here.
    # Example: response = requests.get(f"https://some-cosmos-api.com/banks/{address}/balances")
    mock_balance = 123.456 # Replace with actual logic
    return {"address": address, "balance": mock_balance, "chain_id": chain_id, "denom": denom}


base_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[get_stock_price, get_evm_balance, get_cosmos_balance_placeholder], 
    name='root_agent',
    description="A helpful agent that gets stock or crypto prices.",
    instruction="You are a financial assistant. Always use the provided tools to get financial information."
                "Use get_stock_price for stock ticker symbols, including the ticker symbol in your response."
                "Use get_evm_balance to fetch ETH balances for EVM addresses, requiring an address and optionally an RPC URL."
                "Use get_cosmos_balance_placeholder for Cosmos chain balances, requiring an address, chain ID, and denomination."
                "When responding, include the relevant addresses, ticker symbols, chain IDs, and denominations."
)
    
root_agent = base_agent
