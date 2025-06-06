# ADK Stock Price Agent

This project contains a simple ADK agent that fetches the current price of a given stock ticker symbol using the `yfinance` library.

## Setup Instructions

To get this project up and running on your local machine, follow the instructions for your operating system.

### Prerequisites

Ensure you have Python 3.9+ installed. This project uses `uv` for dependency management. If you don't have `uv` installed, you can install it using pip:

```bash
pip install uv
```

### Ollama Setup

This project uses Ollama to run the `llama3.2:latest` model. Please ensure you have Ollama installed and the model pulled:

1.  **Install Ollama:**
    Follow the instructions on the [Ollama website](https://ollama.com/download) to install Ollama for your operating system.

2.  **Pull the Llama 3.2 model:**
    Once Ollama is installed, open your terminal and run:
    ```bash
    ollama pull llama3.2:latest
    ```

### General Steps (All Operating Systems)

1.  **Clone the repository:**

    ```bash
    git clone <https://github.com/OSOSerious/Google-ADK-Agents.git>
    cd ADK_AI
    ```

2.  **Install dependencies:**

    ```bash
    uv pip install -r requirements.txt
    ```

### Apple (macOS) / Linux

After completing the general steps, you can run the ADK web server:

```bash
adk web --port 8001
```

Access the web UI at `http://localhost:8001`.

### Windows

After completing the general steps, you can run the ADK web server:

```powershell
adk web --port 8001
```

Access the web UI at `http://localhost:8001`.

### Docker Setup

Alternatively, you can run the ADK Stock Price Agent using Docker. Ensure you have Docker installed and running on your system.

1.  **Build the Docker Image:**

    Navigate to the root directory of this project (`ADK_AI`) in your terminal and run:

    ```bash
    docker build -t adk-stock-agent .
    ```

2.  **Run the Docker Container:**

    ```bash
    docker run -p 8001:8001 adk-stock-agent
    ```

    **Important Note on Ollama:**
    The Docker container runs your ADK agent, but it *does not* run the Ollama server itself. You need to ensure your Ollama server (with the `llama3.2:latest` model) is running and accessible from where your Docker container will be running. If Ollama is running on your host machine, you might need to configure LiteLLM in your agent (e.g., in `app/agent.py` or via an environment variable) to use `http://host.docker.internal:11434` (for Docker Desktop on macOS/Windows) or your host machine's actual IP address instead of `localhost` or `127.0.0.1`.

    Access the web UI at `http://localhost:8001`.

## Project Structure

-   `app/agent.py`: Contains the ADK agent definition and the `get_stock_price` tool.
-   `requirements.txt`: Lists the Python dependencies.
-   `README.md`: This file.
-   `main.py`, `pyproject.toml`, `uv.lock`: Other project files.

## Legal Automation Orchestrator

This project now features a specialized ADK agent designed to orchestrate legal client onboarding tasks through a private, local agent-to-agent (A2A) system. The `root_agent` acts as an orchestrator, delegating tasks to specialized, hypothetical internal legal sub-agents.

### Core Client Onboarding Services (Simulated Delegation)

The `app/agent.py` file has been updated to include a generic `call_sub_agent_tool` that simulates interaction with various internal legal sub-agents. These interactions are for **local use only** and do not involve actual external API calls, reinforcing the private AI aspect. The orchestrator can delegate the following tasks:

1.  **Collect Initial Client Information:**
    -   **Tool:** `call_sub_agent_tool(agent_name='intake_agent', tool_name='collect_client_info', tool_args={'client_name': '...'})
    -   **Purpose:** Simulates gathering basic client details like name, contact, and case type.

2.  **Draft Initial Client Agreement:**
    -   **Tool:** `call_sub_agent_tool(agent_name='document_agent', tool_name='draft_initial_agreement', tool_args={'client_id': '...', 'agreement_type': '...'})
    -   **Purpose:** Simulates drafting an initial client agreement (e.g., retainer, engagement letter).

3.  **Perform Conflict of Interest Check:**
    -   **Tool:** `call_sub_agent_tool(agent_name='conflict_check_agent', tool_name='check_conflicts', tool_args={'client_name': '...'})
    -   **Purpose:** Simulates checking for conflicts of interest against internal firm records.

4.  **Perform Internal KYC/AML Check:**
    -   **Tool:** `call_sub_agent_tool(agent_name='intake_agent', tool_name='perform_internal_kyc_aml', tool_args={'client_id': '...'})
    -   **Purpose:** Simulates an internal Know Your Client (KYC) and Anti-Money Laundering (AML) check.

5.  **Setup Client Billing:**
    -   **Tool:** `call_sub_agent_tool(agent_name='billing_agent', tool_name='setup_client_billing', tool_args={'client_id': '...', 'fee_structure': '...'})
    -   **Purpose:** Simulates setting up the client's billing account and defining the fee structure.

6.  **Create New Case Entry:**
    -   **Tool:** `call_sub_agent_tool(agent_name='case_agent', tool_name='create_new_case_entry', tool_args={'client_id': '...', 'case_title': '...'})
    -   **Purpose:** Simulates creating a new case or matter within the firm's internal case management system.

### Interacting with the Legal Orchestrator Agent

Once the ADK Web Server is running, you can interact with this specialized agent through the web UI. Prompt it to perform client onboarding tasks by specifying the `agent_name`, `tool_name`, and `tool_args` as described above. The agent will respond with simulated results for each delegated task.
