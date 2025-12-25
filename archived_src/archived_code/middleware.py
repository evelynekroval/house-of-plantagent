from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage



############################
# 1: Handling Tool Errors #
############################

@wrap_tool_call
def handle_tool_errors(user_query, handler):
    """Handle search tool execution errors with custom messages.
    Args:
        user_query: a user input to the model.
        handler: the AI model parsing the user_input in order to make a tool call.
    Returns:
        Ideally the user_query, if the user_query makes sense for a vegan search, return the model's willingness to search it.
        If the user_query is nonsensical in the context of a vegan recipe search, return the Exception."""
    try:
        return handler(user_query)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"""Tool Error: Please check your input 
            to ensure an appropriate vegan recipe, 
            and try again: ({str(e)})""",
            tool_call_id=user_query.tool_call["id"]
        )
