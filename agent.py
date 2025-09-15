import asyncio
import os
from pathlib import Path
from typing import Any, Dict

import nest_asyncio
from dotenv import load_dotenv
from dp.agent.adapter.adk import CalculationMCPToolset
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams
from google.genai import types

load_dotenv()
nest_asyncio.apply()


# Global Configuration

LOCAL_EXECUTOR = {
    "type": "local"
}

server_url = ""

# Initialize MCP tools and agent
#mcp_tools = CalculationMCPToolset(
#    connection_params=SseServerParams(url=server_url),
#    storage=BOHRIUM_STORAGE,
#    executor=BOHRIUM_EXECUTOR
#)
mcp_tools = CalculationMCPToolset(
    connection_params=SseServerParams(url=server_url),
)


root_agent = LlmAgent(
    model=LiteLlm(model="deepseek/deepseek-chat"),
    name="dpa_calculations_agent",
    description="An agent specialized in computational research using VASP, DeepMD and LAMMPS",
    instruction=(
        "You are an expert in materials science and computational chemistry. "
        "Help users perform Deep Potential calculations including structure optimization, molecular dynamics and property calculations. "
        "Use default parameters if the users do not mention, but let users confirm them before submission. "
        "Use VASP as mainly calculation program"
        "Always verify the input parameters to users and provide clear explanations of results."
    ),
    tools=[mcp_tools],
)
