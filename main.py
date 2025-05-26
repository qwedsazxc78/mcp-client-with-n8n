import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=openai_api_key)

# MCP Server configuration
MCP_SERVER_URL = os.getenv("MCP_SERVER", "https://n8n-alex.zeabur.app/mcp/calculator/sse")


def call_with_mcp(user_message: str) -> str:
    """
    Call OpenAI Responses API with MCP tool enabled
    """
    try:
        response = client.responses.create(
            model="gpt-4.1-nano",
            tools=[
                {
                    "type": "mcp",
                    "server_label": "n8n-mcp-server",
                    "server_url": MCP_SERVER_URL,
                    "require_approval": "never",
                    # If your n8n server requires authentication, add:
                    # "headers": {
                    #     "Authorization": f"Bearer {os.getenv('MCP_SERVER_TOKEN')}"
                    # }
                }
            ],
            input=user_message,
        )

        return response.output_text

    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    print("MCP with n8n Integration - Using OpenAI Responses API")
    print("=" * 60)

    # Example 1: Calculator
    print("\nExample 1: Calculator")
    print("-" * 40)
    content1 = "使用 mcp tools n8n-mcp-server，請計算 123 + 456 ="
    response1 = call_with_mcp(content1)
    print(f"Response: {response1}")

    # Example 2: CRM Query
    print("\nExample 2: CRM Query")
    print("-" * 40)
    content2 = "使用 mcp tools n8n-mcp-server，請給我 CRM 客戶名單，其中狀態是 '潛在機會' "
    response2 = call_with_mcp(content2)
    print(f"Response: {response2}")
