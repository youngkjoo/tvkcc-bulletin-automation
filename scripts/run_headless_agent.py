#!/usr/bin/env python3
import asyncio
import sys
import os
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

async def main():
    # Force working directory to repository root
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(workspace_dir)
    print(f"Running Google Antigravity SDK in workspace: {workspace_dir}")

    # Set up configuration enabling write capabilities for file edits and running commands
    config = LocalAgentConfig(
        system_instructions="You are an automated agent executing the weekly TVKCC bulletin workflow.",
        capabilities=CapabilitiesConfig()
    )

    # Spawn the agent
    async with Agent(config) as agent:
        print("Agent spawned. Triggering the weekly bulletin workflow...")
        
        # Initiate the from-scratch workflow instructively
        response = await agent.chat("@tvkcc_bulletin.md Execute the weekly bulletin translation from scratch")

        # Stream the output tokens in real-time
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\nWorkflow execution finished.")

if __name__ == "__main__":
    asyncio.run(main())
