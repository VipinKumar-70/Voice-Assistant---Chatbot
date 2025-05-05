# Tool Initialization Module
from langchain.tools import Tool

from Tools.Google_Search import G_search, Google_Search_Description

tools = [
    Tool(
        name="Google Search",
        func=G_search.run,
        description=Google_Search_Description,
        input_variables=["query"],
    ),
]
