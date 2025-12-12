from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, wrap_tool_call
from langchain.messages import ToolMessage


################################
# Tool 1: Dynamic Model Change #
################################


COMMON_MODEL_KWARGS = {"temperature": 0.1, "timeout": 60}

basic_model = ChatOpenAI(
    model="gpt-4o-mini", 
    **COMMON_MODEL_KWARGS,
)
advanced_model = ChatOpenAI(
    model="gpt-4o", 
    **COMMON_MODEL_KWARGS,
)

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))


################################
# Tool 2: Handling Tool Errors #
################################

@wrap_tool_call
def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"]
        )
