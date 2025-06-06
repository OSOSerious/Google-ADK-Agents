from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

def draft_initial_agreement(client_id: str, agreement_type: str) -> dict:
    """
    Drafts an initial legal agreement for a client.

    Args:
        client_id (str): The unique ID of the client.
        agreement_type (str): The type of agreement to draft (e.g., "retainer", "engagement letter").

    Returns:
        dict: Details of the drafted agreement.
    """
    print(f"[Document Agent] Drafting {agreement_type} for client ID: {client_id}")
    document_id = f"DOC-{client_id}-{agreement_type.replace(' ', '-')}"
    # In a real system, this would use a document generation engine or templates
    return {
        "status": "success",
        "document_id": document_id,
        "onboarding_status": "agreement_drafted",
        "next_step": "Review draft and send to client.",
        "details": f"Initial {agreement_type} drafted for client {client_id}. Standard clauses included. Requires review by paralegal/attorney.",
        "source": "Document Agent"
    }

document_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[draft_initial_agreement],
    name='document_agent',
    description="A specialized agent for drafting initial legal documents like client agreements.",
    instruction="You are a legal document drafting agent. Your role is to generate initial legal agreements for clients."
                "Use draft_initial_agreement to create a new agreement for a client, specifying the client's ID and the type of agreement."
                "Always provide the document ID and next steps after drafting."
) 