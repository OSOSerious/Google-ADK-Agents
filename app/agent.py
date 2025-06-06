from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Simulated configuration for other agents in an A2A system
# In a real system, these would be actual service endpoints or discovery mechanisms.
SUB_AGENT_SERVICES = {
    "intake_agent": {"endpoint": "http://localhost:8002/legal_intake_api"},
    "document_agent": {"endpoint": "http://localhost:8003/legal_docs_api"},
    "conflict_check_agent": {"endpoint": "http://localhost:8004/legal_conflict_api"},
    "billing_agent": {"endpoint": "http://localhost:8005/legal_billing_api"},
    "case_agent": {"endpoint": "http://localhost:8006/legal_case_api"},
}

def call_sub_agent_tool(agent_name: str, tool_name: str, tool_args: dict) -> dict:
    """
    Delegates a tool call to a hypothetical sub-agent for legal client onboarding.

    Args:
        agent_name (str): The name of the sub-agent to call (e.g., "intake_agent", "document_agent").
        tool_name (str): The name of the tool to call on the sub-agent (e.g., "collect_client_info", "draft_initial_agreement").
        tool_args (dict): A dictionary of arguments for the sub-agent's tool.

    Returns:
        dict: A dictionary simulating the response from the sub-agent.
    """
    if agent_name not in SUB_AGENT_SERVICES:
        return {"error": f"Sub-agent '{agent_name}' not found in configuration."}

    target_endpoint = SUB_AGENT_SERVICES[agent_name]["endpoint"]
    print(f"[A2A Orchestrator] Delegating call to {agent_name} ({target_endpoint}) for tool '{tool_name}' with args: {tool_args}")

    # Simulate responses for legal client onboarding tasks
    if tool_name == "collect_client_info":
        client_name = tool_args.get("client_name", "Unnamed Client")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "client_id": f"LCL-001-{client_name.replace(' ', '-')}",
                "onboarding_status": "initial_data_collected",
                "next_step": "Draft initial client agreement and perform conflict check.",
                "details": f"Initial client information for {client_name} successfully collected. Key questions answered: Name, Contact, Case Type. Next: Document drafting and conflict check.",
                "source": f"Simulated {agent_name}"
            }
        }
    elif tool_name == "draft_initial_agreement":
        client_id = tool_args.get("client_id", "N/A")
        agreement_type = tool_args.get("agreement_type", "client agreement")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "document_id": f"DOC-{client_id}-{agreement_type.replace(' ', '-')}",
                "onboarding_status": "agreement_drafted",
                "next_step": "Review draft and send to client.",
                "details": f"Drafted initial {agreement_type} for client {client_id}. Standard clauses included. Requires review by paralegal/attorney.",
                "source": f"Simulated {agent_name}"
            }
        }
    elif tool_name == "check_conflicts":
        client_name = tool_args.get("client_name", "Unnamed Client")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "conflicts_found": False,
                "onboarding_status": "conflict_check_complete",
                "details": f"Conflict check for {client_name} completed against internal records. No direct conflicts found at this stage. Proceed with caution and further due diligence.",
                "source": f"Simulated {agent_name}"
            }
        }
    elif tool_name == "perform_internal_kyc_aml":
        client_id = tool_args.get("client_id", "N/A")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "kyc_aml_status": "cleared_internal",
                "details": f"Internal KYC/AML check for client {client_id} completed. No immediate red flags found based on available internal data. Further external checks may be required based on firm policy.",
                "source": f"Simulated {agent_name}"
            }
        }
    elif tool_name == "setup_client_billing":
        client_id = tool_args.get("client_id", "N/A")
        fee_structure = tool_args.get("fee_structure", "hourly")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "billing_account_id": f"BILL-{client_id}",
                "status": "billing_setup_complete",
                "details": f"Billing account for client {client_id} setup with {fee_structure} fee structure. Ready for time entry and invoicing.",
                "source": f"Simulated {agent_name}"
            }
        }
    elif tool_name == "create_new_case_entry":
        client_id = tool_args.get("client_id", "N/A")
        case_title = tool_args.get("case_title", "New Legal Matter")
        return {
            "status": "success",
            "agent": agent_name,
            "tool": tool_name,
            "result": {
                "case_id": f"CASE-{client_id}-{case_title.replace(' ', '-')}",
                "status": "case_entry_created",
                "details": f"New case entry '{case_title}' created for client {client_id} in the internal case management system. Ready for document association and task assignment.",
                "source": f"Simulated {agent_name}"
            }
        }
    else:
        return {"status": "error", "message": f"Simulated sub-agent tool '{tool_name}' not recognized for {agent_name}."}


base_agent = Agent(
    model=LiteLlm(model="ollama_chat/llama3.2:latest"),
    tools=[call_sub_agent_tool], 
    name='root_agent',
    description="A specialized legal automation orchestrator agent for client onboarding.",
    instruction="You are a legal automation orchestrator. Your primary goal is to assist law firms and paralegals with client onboarding by delegating tasks to specialized internal legal agents."
                "Use call_sub_agent_tool to delegate onboarding tasks. You must specify the 'agent_name', 'tool_name', and 'tool_args' (a dictionary) for the delegation."
                "Here are the core client onboarding services you can orchestrate:"
                "1. To **collect initial client information (basic onboarding questions)**, use `agent_name='intake_agent'` and `tool_name='collect_client_info'` with a `'client_name'` in `tool_args`. This simulates gathering name, contact, and case type."
                "2. To **draft an initial client agreement**, use `agent_name='document_agent'` and `tool_name='draft_initial_agreement'` with `'client_id'` and `'agreement_type'` (e.g., 'retainer', 'engagement letter') in `tool_args`."
                "3. To **perform a conflict of interest check**, use `agent_name='conflict_check_agent'` and `tool_name='check_conflicts'` with a `'client_name'` in `tool_args`."
                "4. To **perform an internal KYC/AML check**, use `agent_name='intake_agent'` and `tool_name='perform_internal_kyc_aml'` with a `'client_id'` in `tool_args`."
                "5. To **set up client billing**, use `agent_name='billing_agent'` (hypothetical, add to SUB_AGENT_SERVICES) and `tool_name='setup_client_billing'` with `'client_id'` and `'fee_structure'` (e.g., 'hourly', 'flat_fee') in `tool_args`."
                "6. To **create a new case entry**, use `agent_name='case_agent'` (hypothetical, add to SUB_AGENT_SERVICES) and `tool_name='create_new_case_entry'` with `'client_id'` and `'case_title'` in `tool_args`."
                "When responding, summarize the delegated task and its simulated results, guiding the user on the next steps in the onboarding process."
)
    
root_agent = base_agent
