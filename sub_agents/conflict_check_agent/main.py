from google.adk.cli import AdkCli
from .agent import conflict_check_agent

if __name__ == "__main__":
    adk_cli = AdkCli(root_agent=conflict_check_agent)
    adk_cli.run(port=8004) 