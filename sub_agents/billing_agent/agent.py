from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def setup_client_billing(client_id: str, fee_structure: str) -> dict:
    """
    Sets up billing for a new client.

    Args:
        client_id (str): The unique ID of the client.
        fee_structure (str): The agreed-upon fee structure (e.g., "hourly", "flat_fee", "contingency").

    Returns:
        dict: Details of the billing setup.
    """
    print(f"[Billing Agent] Setting up billing for client ID: {client_id} with fee structure: {fee_structure}")
    billing_account_id = f"BILL-{client_id}"
    # In a real system, this would integrate with an accounting or billing software
    return {
        "status": "success",
        "billing_account_id": billing_account_id,
        "onboarding_status": "billing_setup_complete",
        "details": f"Billing account for client {client_id} setup with {fee_structure} fee structure. Ready for time entry and invoicing.",
        "source": "Billing Agent"
    }

billing_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[setup_client_billing],
    name='billing_agent',
    description="A specialized agent for setting up client billing and managing financial aspects of legal cases.",
    instruction="You are a legal billing agent. Your role is to set up financial arrangements for new clients."
                "Use setup_client_billing to configure a client's billing, providing their ID and the agreed fee structure."
                "Always provide the billing account ID and confirmation of setup."
) 