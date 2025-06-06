from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def create_new_case_entry(client_id: str, case_title: str) -> dict:
    """
    Creates a new case entry in the firm's case management system.

    Args:
        client_id (str): The unique ID of the client associated with the case.
        case_title (str): The title or brief description of the new legal case.

    Returns:
        dict: Details of the newly created case entry.
    """
    print(f"[Case Agent] Creating new case entry for client ID: {client_id} with title: {case_title}")
    case_id = f"CASE-{client_id}-{case_title.replace(' ', '-')}"
    # In a real system, this would integrate with a case management software
    return {
        "status": "success",
        "case_id": case_id,
        "onboarding_status": "case_entry_created",
        "details": f"New case entry '{case_title}' created for client {client_id} in the internal case management system. Ready for document association and task assignment.",
        "source": "Case Agent"
    }

case_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[create_new_case_entry],
    name='case_agent',
    description="A specialized agent for creating and managing legal case entries.",
    instruction="You are a legal case management agent. Your role is to create and update case entries within the firm's system."
                "Use create_new_case_entry to log a new legal matter for a client, providing their ID and a title for the case."
                "Always provide the new case ID upon successful creation."
) 