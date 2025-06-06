# ADK Stock Price Agent

This project contains a simple ADK agent that fetches the current price of a given stock ticker symbol using the `yfinance` library.

## Setup Instructions

To get this project up and running on your local machine, follow the instructions for your operating system.

### Prerequisites

Ensure you have Python 3.9+ installed. This project uses `uv` for dependency management. If you don't have `uv` installed, you can install it using pip:

```bash
pip install uv
```

### General Steps (All Operating Systems)

1.  **Clone the repository:**

    ```bash
    git clone <YOUR_REPOSITORY_URL>
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

## Project Structure

-   `app/agent.py`: Contains the ADK agent definition and the `get_stock_price` tool.
-   `requirements.txt`: Lists the Python dependencies.
-   `README.md`: This file.
-   `main.py`, `pyproject.toml`, `uv.lock`: Other project files.

## Usage

Once the ADK Web Server is running, you can interact with the agent through the web UI to get stock prices. Provide a ticker symbol when prompted.
