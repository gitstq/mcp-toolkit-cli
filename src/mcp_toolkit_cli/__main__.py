#!/usr/bin/env python3
"""
MCP Toolkit CLI - Main Entry Point
"""

import sys
import os

# Add src to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mcp_toolkit_cli.cli import main

if __name__ == '__main__':
    sys.exit(main())
