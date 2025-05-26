# MCP with n8n Integration

This project demonstrates how to use OpenAI's Responses API with MCP (Model Context Protocol) support to connect to an n8n MCP server.

## Overview

OpenAI now provides native MCP support through their Responses API, making it incredibly simple to connect to remote MCP servers. This project shows how to:

* Use OpenAI's Responses API with MCP tools
* Connect to an n8n MCP server
* Execute calculator and CRM operations through natural language

## Features

* ✅ Simple, clean implementation using OpenAI's native MCP support
* ✅ Environment variable configuration with `python-dotenv`
* ✅ Error handling
* ✅ Multiple example use cases
* ✅ Secure API key management

## Prerequisites

* Python 3.13+
* OpenAI API key
* Access to n8n MCP server (https://n8n-alex.zeabur.app/mcp/calculator/sse)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd mcp-with-n8n
```

2. Install dependencies:

```bash
pip install openai python-dotenv
```

Or using the project's dependencies:

```bash
pip install -e .
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key-here
MCP_SERVER=https://n8n-alex.zeabur.app/mcp/calculator/sse
MCP_SERVER_TOKEN=optional-auth-token-if-needed
```

## Usage

### Basic Usage

Run the main script:

```bash
python main.py
```

This will execute three examples:
1. Calculator operation (123 + 456)
2. CRM query (listing customers with "潛在機會" status)
3. Multiplication calculation (789 × 321)

### Code Example

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Call with MCP
response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "n8n-mcp-server",
            "server_url": "https://n8n-alex.zeabur.app/mcp/calculator/sse",
            "require_approval": "never"
        }
    ],
    input="Calculate 123 + 456"
)

print(response.output_text)
```

## Available MCP Tools

Based on the n8n server configuration, the following tools are available:

1. **calculator**: Mathematical calculations
   - Example: "Calculate 123 + 456"

2. **CRM_Create**: Create CRM records
   - Requires specific field values

3. **CRM_ListAll**: List all CRM records
   - Can filter by status or other fields

4. **CRM_GET**: Get specific CRM record
   - Requires Record_ID

## How It Works

```mermaid
graph LR
    A[User Input] --> B[OpenAI Responses API]
    B --> C[MCP Tool Detection]
    C --> D[n8n MCP Server]
    D --> E[Tool Execution]
    E --> F[Response to OpenAI]
    F --> G[Natural Language Output]
```

## Security Notes

1. **Never commit `.env` files** - The `.gitignore` is configured to exclude them
2. Store API keys securely
3. Use environment variables for all sensitive data
4. Review data being sent to MCP servers
5. Use `require_approval` parameter to control tool execution

## MCP Server Authentication

If your MCP server requires authentication, add headers:

```python
response = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "n8n-mcp-server",
            "server_url": MCP_SERVER_URL,
            "require_approval": "never",
            "headers": {
                "Authorization": f"Bearer {os.getenv('MCP_SERVER_TOKEN')}"
            }
        }
    ],
    input=user_message
)
```

## Project Structure

```
mcp-with-n8n/
├── main.py              # Simple implementation using Responses API
├── main_alternative.py  # Alternative implementation with function calling
├── .env                 # Environment variables (not in git)
├── .env.example        # Example environment file
├── .gitignore          # Git ignore rules
├── pyproject.toml      # Project dependencies
├── README.md           # This file
└── uv.lock            # Dependency lock file
```

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**: Ensure `.env` file exists and contains valid API key
2. **MCP Server connection errors**: Check server URL and network connectivity
3. **Model not found**: Ensure you're using a supported model (gpt-4.1, gpt-4o, etc.)

### Debug Tips

* Check the response object for detailed error messages
* Verify MCP server is accessible
* Ensure proper authentication headers if required

## Alternative Implementation

The `main_alternative.py` file contains a more complex implementation using:
* OpenAI function calling
* Async/await for better performance
* Manual MCP server communication

Use this if you need more control over the MCP interaction process.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Resources

* [OpenAI Responses API Documentation](https://platform.openai.com/docs/api-reference/responses)
* [OpenAI MCP Guide](https://platform.openai.com/docs/guides/tools-remote-mcp)
* [Model Context Protocol Specification](https://modelcontextprotocol.io/)
* [n8n Documentation](https://docs.n8n.io/)

## License

[Specify your license here]

## Contact

[Your contact information]
