from langchain.agents import initialize_agent, AgentType
from .Llm import llm
import warnings
from .Template import TEMPLATE
from History import get_chat_history
from Preferences import get_preference
from Real_Time_Info import get_real_time_data
from .Tool_Initilization import tools

# Ignore deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Initialize the agent with the specified parameters
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    prompt=TEMPLATE,
    handle_parsing_errors=True,
)

# Run Agent
def Run_Agent(Query: str) -> str:
    try:
        Format_Prompt = TEMPLATE.format(
            real_time_info = get_real_time_data(),
            preferences = get_preference(),
            chat_history = get_chat_history(),
            query = Query
        )

        response = agent({
            "input": Format_Prompt,
            })
        
        return response.get("output", "").replace("*", "").replace("`","").replace("\n","")
    
    except Exception as e:
        return f"Error processing request: {str(e)}"
