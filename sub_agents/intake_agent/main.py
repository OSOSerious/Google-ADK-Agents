from google.adk.cli import AdkCli
from .agent import intake_agent

if __name__ == "__main__":
    adk_cli = AdkCli(root_agent=intake_agent)
    adk_cli.run() 