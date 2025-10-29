# MCP pyATS Network Automation Tool

> **Note:** This documentation was generated with the assistance of Generative AI.

A Model Context Protocol (MCP) server that integrates pyATS for network device automation, designed as a learning primer for network engineers preparing for CCNP-level certifications and exploring AI capabilities in network automation.

## 🎯 Overview

This project demonstrates how to create an MCP (Model Context Protocol) server that leverages Cisco's pyATS framework to interact with network devices. The tool provides AI agents with the ability to execute show commands on network devices and receive structured, parsed output - making it perfect for network analysis, troubleshooting, and automation workflows.

## 🏗️ Architecture

The project consists of:

- **`mcp_pyats_01.py`** - Main MCP server with pyATS integration
- **`requirements.txt`** - Python dependencies including pyATS/Genie libraries
- **MCP Tool Function** - `send_show_command()` that connects to devices and executes commands

## 🚀 Quick Start

### Prerequisites

1. **Python 3.12+** installed on your system
2. **Network devices** accessible via SSH (Cisco IOS, IOS-XE, NX-OS, etc.)
3. **MCP-compatible client** such as [LM Studio](https://lmstudio.ai/). See [this blog](https://blogs.cisco.com/learning/creating-a-netai-playground-for-agentic-ai-experimentation) for an overview of using LM Studio and MCP servers.

### Installation

1. Clone or download this project to your local machine

2. Navigate to the MCP pyATS directory:
   ```bash
   cd mcp-pyats
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the MCP Server

You can run the MCP server in two ways:

#### Option 1: Direct Python execution
```bash
python mcp_pyats_01.py
```

#### Option 2: Using FastMCP (recommended for MCP clients)
```bash
fastmcp run --transport http --port 8002 mcp_pyats_01.py
```

The server will start and listen for MCP client connections, providing the `send_show_command` tool to AI agents.

### MCP Client Configuration

To connect your MCP client to this server, add the following configuration:

```json
{
  "mcpServers": {
    "pyats": {
      "url": "http://localhost:8002/mcp"
    }
  }
}
```

This configuration tells the MCP client to connect to the pyATS server running on localhost port 8002.

## 🔧 Tool Usage

### `send_show_command` Function

Executes show commands on network devices and returns structured data.

**Parameters:**
- `command` (str): The show command to execute (e.g., "show version", "show ip interface brief")
- `device_name` (str): Logical name for the device
- `username` (str): SSH username for authentication
- `password` (str): SSH password for authentication  
- `ip_address` (str): IP address or hostname of the target device
- `ssh_port` (int, optional): SSH port number (default: 22)
- `network_os` (str, optional): Network OS type ("ios", "iosxe", "nxos", etc. - default: "ios")

**Returns:**
- Structured dictionary with parsed command output, or error message if command fails

## 💻 Example Usage

When connected to an MCP client, you can use the tool like this:

```python
# Example of what the AI agent would receive
result = send_show_command(
    command="show version",
    device_name="router1",
    username="admin", 
    password="cisco123",
    ip_address="192.168.1.1",
    network_os="iosxe"
)

# The result contains structured data like:
{
    "version": {
        "version": "17.03.04a",
        "version_short": "17.3",
        "platform": "Catalyst 8000V",
        "image_id": "CAT8KV_IOSXE",
        "uptime": "2 days, 4 hours, 15 minutes"
    }
}
```

## 📚 External Libraries

This project uses several key Python libraries:

### Core Network Automation Libraries
- **[pyATS/Genie](https://developer.cisco.com/docs/pyats/)** - Cisco's Python automation framework
  - `genie` - Core testing and automation framework
  - `genie.libs.parser` - Device command parsers for structured output
  - `genie.libs.ops` - Operational state libraries
  - `genie.libs.sdk` - Software development kit with device APIs

### MCP Framework
- **[FastMCP](https://gofastmcp.com/getting-started/welcome)** - Fast Model Context Protocol server implementation
  - Provides decorators for creating MCP tools
  - Handles HTTP transport and client communication
  - Enables AI agents to discover and use network automation functions

### Supporting Libraries
- **cryptography** - SSH connection security
- **paramiko** (via pyATS) - SSH client implementation
- **click** - Command-line interface utilities

## 🌐 Supported Network Operating Systems

The tool supports various Cisco and other vendor network operating systems through pyATS:

- **Cisco IOS** - Traditional Cisco router/switch OS
- **Cisco IOS-XE** - Modern Cisco enterprise OS
- **Cisco NX-OS** - Cisco Nexus data center switches
- **Cisco IOS-XR** - Cisco service provider routers
- **ASA** - Cisco Adaptive Security Appliances
- **And many more** - Check pyATS documentation for full support matrix

## 🔧 Configuration

### Device Connection

The tool dynamically creates pyATS testbed configurations for each device connection:

```python
device_dict = {
    "devices": {
        device_name: {
            "os": network_os,
            "credentials": {
                "default": {"username": username, "password": password}
            },
            "connections": {
                "ssh": {"protocol": "ssh", "ip": ip_address, "port": ssh_port}
            },
        }
    }
}
```

### MCP Server Configuration

The server runs on HTTP transport by default:
- **Host**: localhost
- **Port**: 8002 (configurable)
- **Transport**: HTTP
- **Log Level**: DEBUG

## 🎓 Learning Opportunities for CCNP Engineers

This project demonstrates several key concepts relevant to CCNP-level network automation:

### 1. **Programmatic Device Access**
- SSH-based device connectivity
- Authentication and connection management
- Multi-vendor device support

### 2. **Structured Data Parsing**
- Converting CLI output to structured JSON/dictionaries
- Consistent data formats across different devices
- Error handling and connection management

### 3. **API Integration Patterns**
- How network tools can be exposed as APIs
- RESTful service patterns for network automation
- Integration with AI and automation platforms

### 4. **Modern Automation Frameworks**
- pyATS/Genie ecosystem and capabilities
- Model Context Protocol for AI integration
- Microservice architecture for network tools

## 🚀 Advanced Use Cases

Consider extending this MCP server with additional tools for:

### Configuration Management
```python
@mcp.tool()
def apply_configuration(device_name: str, config_lines: list):
    """Apply configuration changes to a network device"""
    # Implementation here
```

### Network Validation
```python
@mcp.tool() 
def validate_network_state(device_name: str, expected_state: dict):
    """Validate that device state matches expected configuration"""
    # Implementation here
```

### Bulk Operations
```python
@mcp.tool()
def execute_on_multiple_devices(command: str, device_list: list):
    """Execute command across multiple devices simultaneously"""
    # Implementation here
```

## 🛡️ Security Considerations

### Credential Management
- Store credentials securely (environment variables, key management systems)
- Implement credential rotation policies
- Use SSH keys instead of passwords when possible

### Network Access
- Limit SSH access to management networks
- Implement proper firewall rules
- Use jump hosts/bastion hosts for production access

### Logging and Auditing  
- Log all device interactions
- Implement proper audit trails
- Monitor for unauthorized access attempts

## 🐛 Troubleshooting

### Common Issues

**Connection Timeouts:**
```python
# Increase timeout values in device configuration
"connections": {
    "ssh": {
        "protocol": "ssh", 
        "ip": ip_address, 
        "port": ssh_port,
        "timeout": 30
    }
}
```

**Authentication Failures:**
- Verify username/password combination
- Check SSH access is enabled on target device
- Ensure user has proper privilege levels

**Parser Issues:**
- Not all commands have parsers for all OS versions
- Check pyATS parser documentation for supported commands
- Consider using `device.execute()` instead of `device.parse()` for unparsed output

## 📈 Next Steps

Extend this foundation to build comprehensive network automation solutions:

1. **Integration with Network Monitoring** - Connect to monitoring systems for proactive issue detection
2. **Configuration Compliance** - Automated compliance checking and remediation
3. **Network Discovery** - Automatic topology discovery and documentation
4. **Change Management** - Automated change approval and rollback workflows
5. **AI-Driven Analysis** - Use AI to analyze network data and provide insights

## 🎯 CCNP Exam Relevance

This tool directly supports several CCNP exam topics:

- **Network Automation** - Programmatic device interaction
- **APIs and Protocols** - RESTful services and data formats
- **Troubleshooting** - Structured data collection and analysis
- **Configuration Management** - Automated configuration deployment
- **Network Monitoring** - Operational state verification

## 📝 License

This project is provided as educational material for learning AI and automation concepts in network engineering contexts.

---

Ready to automate your network with AI? 🤖🌐✨