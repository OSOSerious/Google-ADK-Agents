from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def collect_client_info(client_name: str, contact_info: str, case_type: str) -> dict:
    """
    Collects initial client information for onboarding.

    Args:
        client_name (str): The name of the client.
        contact_info (str): Client's contact details (e.g., email, phone).
        case_type (str): The type of legal case (e.g., "contract dispute", "real estate").

    Returns:
        dict: Details of the collected information and next steps.
    """
    print(f"[Intake Agent] Collecting info for {client_name}, Contact: {contact_info}, Case Type: {case_type}")
    client_id = f"LCL-001-{client_name.replace(' ', '-')}"
    # In a real system, this would save to a database or CRM
    return {
        "status": "success",
        "client_id": client_id,
        "onboarding_stage": "initial_data_collected",
        "details": f"Initial information collected for client {client_name}. Contact: {contact_info}, Case Type: {case_type}.",
        "next_steps": "Proceed to internal KYC/AML check and document preparation."
    }

def perform_internal_kyc_aml(client_id: str, client_name: str) -> dict:
    """
    Performs an internal Know Your Client (KYC) and Anti-Money Laundering (AML) check.

    Args:
        client_id (str): The unique ID of the client.
        client_name (str): The name of the client.

    Returns:
        dict: The result of the internal KYC/AML check.
    """
    print(f"[Intake Agent] Performing internal KYC/AML for client ID: {client_id}, Name: {client_name}")
    # In a real system, this would query internal databases or compliance systems
    return {
        "status": "success",
        "client_id": client_id,
        "kyc_aml_status": "cleared_internal",
        "details": f"Internal KYC/AML check for {client_name} ({client_id}) completed. No immediate red flags found based on firm's internal records. Further external checks may be necessary based on firm policy.",
        "onboarding_stage": "kyc_aml_checked"
    }


intake_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"), # This agent can also use an LLM if needed for its specific tasks
    tools=[collect_client_info, perform_internal_kyc_aml],
    name='intake_agent',
    description="A specialized agent for collecting client information and performing internal KYC/AML checks during legal client onboarding.",
    instruction="You are a legal intake and compliance agent. Your role is to collect initial client information and conduct internal KYC/AML checks."
                "Use collect_client_info to gather a new client's name, contact information, and case type."
                "Use perform_internal_kyc_aml to conduct an internal compliance check for a client once their ID and name are known."
                "Always provide clear summaries of the information collected or the status of the compliance check."
) 