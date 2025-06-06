from google.adk.cli import AdkCli
from .agent import case_agent

if __name__ == "__main__":
    adk_cli = AdkCli(root_agent=case_agent)
    adk_cli.run(port=8006) 