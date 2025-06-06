from google.adk.cli import AdkCli
from .agent import document_agent

if __name__ == "__main__":
    adk_cli = AdkCli(root_agent=document_agent)
    adk_cli.run(port=8003) 