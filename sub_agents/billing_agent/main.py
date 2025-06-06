from google.adk.cli import AdkCli
from .agent import billing_agent

if __name__ == "__main__":
    adk_cli = AdkCli(root_agent=billing_agent)
    adk_cli.run(port=8005) 