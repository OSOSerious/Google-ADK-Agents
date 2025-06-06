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

## Usage

Once the ADK Web Server is running, you can interact with the agent through the web UI to get stock prices. Provide a ticker symbol when prompted.
