# ADK Law Firm Automation Agents

This project has evolved into an ADK agent system designed to automate legal firm operations, specifically focusing on client onboarding processes through an agent-to-agent (A2A) communication model. The `root_agent` acts as an orchestrator, delegating tasks to specialized local sub-agents.

## Setup Instructions

To get this project up and running on your local machine, follow the instructions below.

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
    git clone https://github.com/OSOSerious/Google-ADK-Agents.git
    cd Google-ADK-Agents
    ```

2.  **Install dependencies for the main orchestrator agent:**

    Navigate to the `ADK_AI` directory (the root of the project after cloning):
    ```bash
    cd ADK_AI
    uv pip install -r requirements.txt
    ```

3.  **Install dependencies for each sub-agent:**

    For each sub-agent, navigate to its directory and install its dependencies. Repeat this for `intake_agent`, `document_agent`, `conflict_check_agent`, `billing_agent`, and `case_agent`:

    ```bash
    cd sub_agents/intake_agent/
    uv pip install -r requirements.txt
    cd ../../ # Go back to ADK_AI root

    # Repeat for other agents:
    cd sub_agents/document_agent/
    uv pip install -r requirements.txt
    cd ../../

    cd sub_agents/conflict_check_agent/
    uv pip install -r requirements.txt
    cd ../../

    cd sub_agents/billing_agent/
    uv pip install -r requirements.txt
    cd ../../

    cd sub_agents/case_agent/
    uv pip install -r requirements.txt
    cd ../../
    ```

### Running the ADK Agents

For full functionality, all agents (the main orchestrator and all sub-agents) need to be running concurrently. Open separate terminal windows or use a process manager (like `tmux` or `screen`) to run each agent.

1.  **Start the Main Orchestrator Agent (ADK Web Server):**
    From the `ADK_AI` root directory:
    ```bash
    adk web --port 8001
    # Or using Python directly:
    # python main.py
    ```
    Access the web UI at `http://localhost:8001`.

2.  **Start the Intake Agent:**
    From the `ADK_AI` root directory:
    ```bash
    cd sub_agents/intake_agent/
    adk web --port 8002
    # Or using Python directly:
    # python main.py
    cd ../../ # Go back to ADK_AI root
    ```
    This agent listens on `http://localhost:8002`.

3.  **Start the Document Agent:**
    From the `ADK_AI` root directory:
    ```bash
    cd sub_agents/document_agent/
    adk web --port 8003
    # Or using Python directly:
    # python main.py
    cd ../../
    ```
    This agent listens on `http://localhost:8003`.

4.  **Start the Conflict Check Agent:**
    From the `ADK_AI` root directory:
    ```bash
    cd sub_agents/conflict_check_agent/
    adk web --port 8004
    # Or using Python directly:
    # python main.py
    cd ../../
    ```
    This agent listens on `http://localhost:8004`.

5.  **Start the Billing Agent:**
    From the `ADK_AI` root directory:
    ```bash
    cd sub_agents/billing_agent/
    adk web --port 8005
    # Or using Python directly:
    # python main.py
    cd ../../
    ```
    This agent listens on `http://localhost:8005`.

6.  **Start the Case Agent:**
    From the `ADK_AI` root directory:
    ```bash
    cd sub_agents/case_agent/
    adk web --port 8006
    # Or using Python directly:
    # python main.py
    cd ../../
    ```
    This agent listens on `http://localhost:8006`.

### Docker Setup

The provided `Dockerfile` is for the main orchestrator agent. To run the entire multi-agent system via Docker, you would typically build individual Docker images for each sub-agent and orchestrate them using `docker-compose`. This setup is beyond the scope of this `Dockerfile`, which is focused on the main application.

1.  **Build the Docker Image (for main orchestrator):**

    Navigate to the `ADK_AI` directory in your terminal and run:

    ```bash
    docker build -t adk-law-orchestrator .
    ```

2.  **Run the Docker Container (for main orchestrator):**

    ```bash
    docker run -p 8001:8001 adk-law-orchestrator
    ```

    **Important Note on Ollama:**
    The Docker container runs your ADK agent, but it *does not* run the Ollama server itself. You need to ensure your Ollama server (with the `llama3.2:latest` model) is running and accessible from where your Docker container will be running. If Ollama is running on your host machine, you might need to configure LiteLLM in your agent (e.g., in `app/agent.py` or via an environment variable) to use `http://host.docker.internal:11434` (for Docker Desktop on macOS/Windows) or your host machine's actual IP address instead of `localhost` or `127.0.0.1`.

    Access the web UI at `http://localhost:8001` for the main orchestrator.

## Project Structure

-   `app/agent.py`: Contains the main ADK orchestrator agent definition and the `call_sub_agent_tool` for delegating to sub-agents.
-   `sub_agents/`: Directory containing specialized sub-agents:
    -   `intake_agent/`: Handles client information collection and internal KYC/AML checks.
        -   `agent.py`: Defines the `intake_agent`.
        -   `main.py`: Entry point to run the `intake_agent`'s ADK web server.
        -   `requirements.txt`: Dependencies for the `intake_agent`.
    -   `document_agent/`: Handles drafting initial legal documents.
        -   `agent.py`: Defines the `document_agent`.
        -   `main.py`: Entry point to run the `document_agent`'s ADK web server.
        -   `requirements.txt`: Dependencies for the `document_agent`.
    -   `conflict_check_agent/`: Handles conflict of interest checks.
        -   `agent.py`: Defines the `conflict_check_agent`.
        -   `main.py`: Entry point to run the `conflict_check_agent`'s ADK web server.
        -   `requirements.txt`: Dependencies for the `conflict_check_agent`.
    -   `billing_agent/`: Handles setting up client billing.
        -   `agent.py`: Defines the `billing_agent`.
        -   `main.py`: Entry point to run the `billing_agent`'s ADK web server.
        -   `requirements.txt`: Dependencies for the `billing_agent`.
    -   `case_agent/`: Handles creating new case entries.
        -   `agent.py`: Defines the `case_agent`.
        -   `main.py`: Entry point to run the `case_agent`'s ADK web server.
        -   `requirements.txt`: Dependencies for the `case_agent`.
-   `requirements.txt`: Lists the Python dependencies for the main orchestrator agent.
-   `README.md`: This file.
-   `main.py`, `pyproject.toml`, `uv.lock`: Other project files.

## Legal Automation Orchestrator

This project now features a specialized ADK agent designed to orchestrate legal client onboarding tasks through a private, local agent-to-agent (A2A) system. The `root_agent` acts as an orchestrator, delegating tasks to specialized internal legal sub-agents running as separate ADK web services.

### Core Client Onboarding Services (Actual Delegation)

The `app/agent.py` file has been updated to include a generic `call_sub_agent_tool` that now makes actual HTTP requests to the running sub-agent services. The orchestrator can delegate the following tasks:

1.  **Collect Initial Client Information:**
    -   **Agent:** `intake_agent` (running on `http://localhost:8002`)
    -   **Tool:** `call_sub_agent_tool(agent_name='intake_agent', tool_name='collect_client_info', tool_args={'client_name': '...', 'contact_info': '...', 'case_type': '...'})
    -   **Purpose:** Gathers basic client details like name, contact, and case type.

2.  **Draft Initial Client Agreement:**
    -   **Agent:** `document_agent` (running on `http://localhost:8003`)
    -   **Tool:** `call_sub_agent_tool(agent_name='document_agent', tool_name='draft_initial_agreement', tool_args={'client_id': '...', 'agreement_type': '...'})
    -   **Purpose:** Drafts an initial client agreement (e.g., retainer, engagement letter).

3.  **Perform Conflict of Interest Check:**
    -   **Agent:** `conflict_check_agent` (running on `http://localhost:8004`)
    -   **Tool:** `call_sub_agent_tool(agent_name='conflict_check_agent', tool_name='check_conflicts', tool_args={'client_name': '...'})
    -   **Purpose:** Checks for conflicts of interest against internal firm records.

4.  **Perform Internal KYC/AML Check:**
    -   **Agent:** `intake_agent` (running on `http://localhost:8002`)
    -   **Tool:** `call_sub_agent_tool(agent_name='intake_agent', tool_name='perform_internal_kyc_aml', tool_args={'client_id': '...', 'client_name': '...'})
    -   **Purpose:** Conducts an internal Know Your Client (KYC) and Anti-Money Laundering (AML) check.

5.  **Setup Client Billing:**
    -   **Agent:** `billing_agent` (running on `http://localhost:8005`)
    -   **Tool:** `call_sub_agent_tool(agent_name='billing_agent', tool_name='setup_client_billing', tool_args={'client_id': '...', 'fee_structure': '...'})
    -   **Purpose:** Sets up the client's billing account and defines the fee structure.

6.  **Create New Case Entry:**
    -   **Agent:** `case_agent` (running on `http://localhost:8006`)
    -   **Tool:** `call_sub_agent_tool(agent_name='case_agent', tool_name='create_new_case_entry', tool_args={'client_id': '...', 'case_title': '...'})
    -   **Purpose:** Creates a new case or matter within the firm's internal case management system.

### Interacting with the Legal Orchestrator Agent

Once all ADK Web Servers are running (the main orchestrator and all sub-agents), you can interact with the orchestrator agent through its web UI at `http://localhost:8001`. Prompt it to perform client onboarding tasks by specifying the `agent_name`, `tool_name`, and `tool_args` as described above. The orchestrator will delegate to the appropriate sub-agent and relay its actual response.

## ADK and A2A Documentation

For more information on the Google ADK and Agent-to-Agent communication patterns, refer to the official documentation:

*   **Google ADK Documentation:** [https://developers.google.com/adk/](https://developers.google.com/adk/)
*   **Agent-to-Agent (A2A) Communication:** [https://developers.google.com/adk/docs/guides/a2a](https://developers.google.com/adk/docs/guides/a2a)
