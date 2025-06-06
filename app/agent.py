from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import requests # Added for A2A communication

# Simulated configuration for other agents in an A2A system
# In a real system, these would be actual service endpoints or discovery mechanisms.
SUB_AGENT_SERVICES = {
    "intake_agent": {"endpoint": "http://localhost:8002"}, # Updated to base URL of ADK server
    "document_agent": {"endpoint": "http://localhost:8003"},
    "conflict_check_agent": {"endpoint": "http://localhost:8004"},
    "billing_agent": {"endpoint": "http://localhost:8005"},
    "case_agent": {"endpoint": "http://localhost:8006"},
}

def call_sub_agent_tool(agent_name: str, tool_name: str, tool_args: dict) -> dict:
    """
    Delegates a tool call to a hypothetical sub-agent for legal client onboarding.

    Args:
        agent_name (str): The name of the sub-agent to call (e.g., "intake_agent", "document_agent").
        tool_name (str): The name of the tool to call on the sub-agent (e.g., "collect_client_info", "draft_initial_agreement").
        tool_args (dict): A dictionary of arguments for the sub-agent's tool.

    Returns:
        dict: A dictionary simulating or containing the actual response from the sub-agent.
    """
    if agent_name not in SUB_AGENT_SERVICES:
        return {"error": f"Sub-agent '{agent_name}' not found in configuration."}

    base_endpoint = SUB_AGENT_SERVICES[agent_name]["endpoint"]
    delegation_url = f"{base_endpoint}/run_tool"
    print(f"[A2A Orchestrator] Delegating call to {agent_name} ({delegation_url}) for tool '{tool_name}' with args: {tool_args}")

    # --- Actual HTTP delegation for intake_agent ---
    if agent_name == "intake_agent":
        try:
            payload = {"tool_name": tool_name, "tool_args": tool_args}
            response = requests.post(delegation_url, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            return {"status": "success", "agent": agent_name, "tool": tool_name, "result": response.json()}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Failed to delegate to {agent_name} for tool {tool_name}: {str(e)}"}

    # --- Simulated responses for other agents (not yet implemented as separate services) ---
    elif agent_name == "document_agent":
        try:
            payload = {"tool_name": tool_name, "tool_args": tool_args}
            response = requests.post(delegation_url, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            return {"status": "success", "agent": agent_name, "tool": tool_name, "result": response.json()}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Failed to delegate to {agent_name} for tool {tool_name}: {str(e)}"}

    elif agent_name == "conflict_check_agent":
        try:
            payload = {"tool_name": tool_name, "tool_args": tool_args}
            response = requests.post(delegation_url, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            return {"status": "success", "agent": agent_name, "tool": tool_name, "result": response.json()}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Failed to delegate to {agent_name} for tool {tool_name}: {str(e)}"}

    elif agent_name == "billing_agent":
        try:
            payload = {"tool_name": tool_name, "tool_args": tool_args}
            response = requests.post(delegation_url, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            return {"status": "success", "agent": agent_name, "tool": tool_name, "result": response.json()}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Failed to delegate to {agent_name} for tool {tool_name}: {str(e)}"}

    elif agent_name == "case_agent":
        try:
            payload = {"tool_name": tool_name, "tool_args": tool_args}
            response = requests.post(delegation_url, json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            return {"status": "success", "agent": agent_name, "tool": tool_name, "result": response.json()}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": f"Failed to delegate to {agent_name} for tool {tool_name}: {str(e)}"}

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
                "1. To **collect initial client information (basic onboarding questions)**, use `agent_name='intake_agent'` and `tool_name='collect_client_info'` with a `'client_name'`, `'contact_info'`, and `'case_type'` in `tool_args`. This simulates gathering name, contact, and case type."
                "2. To **perform an internal KYC/AML check**, use `agent_name='intake_agent'` and `tool_name='perform_internal_kyc_aml'` with a `'client_id'` and `'client_name'` in `tool_args`."
                "3. To **draft an initial client agreement**, use `agent_name='document_agent'` and `tool_name='draft_initial_agreement'` with `'client_id'` and `'agreement_type'` (e.g., 'retainer', 'engagement letter') in `tool_args`."
                "4. To **perform a conflict of interest check**, use `agent_name='conflict_check_agent'` and `tool_name='check_conflicts'` with a `'client_name'` in `tool_args`."
                "5. To **set up client billing**, use `agent_name='billing_agent'` and `tool_name='setup_client_billing'` with `'client_id'` and `'fee_structure'` (e.g., 'hourly', 'flat_fee') in `tool_args`."
                "6. To **create a new case entry**, use `agent_name='case_agent'` and `tool_name='create_new_case_entry'` with `'client_id'` and `'case_title'` in `tool_args`."
                "When responding, summarize the delegated task and its simulated results, guiding the user on the next steps in the onboarding process."
)
    
root_agent = base_agent
