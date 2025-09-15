# chem-cal-agent
This is the attachment of the AI Agent mentioned in Article "AI-Agent Guided Design of Dual-scale Modulated Nickel-based Catalyst with Built-in Electric Field for Enhanced Biomass Electrooxidation."

Run "server.py" in your remote sever and run "agent.py" in your local computer 

In the remote sever, type: python server.py to run the activate

In the local server:
1. Create a forder named "agent" and put "agent.py" and "1.env" in it
2. Rename the file "1.env" to ".env"
3. Edit the deepseek api in the .env
4. Install google-adk with "pip install google-adk"
5. Run "adk web" in the folder contaning "agent" forder.

This project mainly references: 

“https://deepmodeling.github.io/AI4S-agent-tools/”

and

"https://arxiv.org/abs/2508.07035"
