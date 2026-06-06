#!/usr/bin/env python3
"""
MCP Toolkit CLI - MCP Debugger
"""

import os
import sys
import json
import subprocess
import socket
import threading
import time


class MCPDebugger:
    """Debug MCP server"""
    
    def debug(self, target_dir, port=8080, verbose=False):
        """Start debugging an MCP server"""
        try:
            print(f"🔍 Starting MCP debugger on port {port}...")
            
            # Find server file
            server_file = self._find_server_file(target_dir)
            if not server_file:
                return {
                    'success': False,
                    'error': 'No server file found'
                }
            
            print(f"📁 Server file: {server_file}")
            
            # Start server process
            process = self._start_server(server_file, target_dir)
            
            print(f"🚀 Server started (PID: {process.pid})")
            print(f"📝 Testing stdio communication...")
            
            # Test initialize
            init_request = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {}
            }
            
            if verbose:
                print(f"📤 Sending: {json.dumps(init_request)}")
            
            process.stdin.write(json.dumps(init_request) + '\n')
            process.stdin.flush()
            
            # Read response
            response = process.stdout.readline().strip()
            
            if verbose:
                print(f"📥 Received: {response}")
            
            try:
                result = json.loads(response)
                if 'result' in result:
                    server_info = result['result'].get('serverInfo', {})
                    print(f"✅ Server initialized successfully!")
                    print(f"   Name: {server_info.get('name', 'unknown')}")
                    print(f"   Version: {server_info.get('version', 'unknown')}")
                else:
                    print(f"⚠️  Initialize returned error: {result.get('error', {})}")
            except json.JSONDecodeError:
                print(f"⚠️  Invalid JSON response: {response}")
            
            # Test tools/list
            tools_request = {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {}
            }
            
            process.stdin.write(json.dumps(tools_request) + '\n')
            process.stdin.flush()
            
            response = process.stdout.readline().strip()
            
            try:
                result = json.loads(response)
                if 'result' in result:
                    tools = result['result'].get('tools', [])
                    print(f"🔧 Available tools ({len(tools)}):")
                    for tool in tools:
                        print(f"   - {tool.get('name', 'unnamed')}: {tool.get('description', 'No description')}")
                else:
                    print(f"⚠️  tools/list returned error")
            except json.JSONDecodeError:
                print(f"⚠️  Invalid JSON response")
            
            # Test tool call
            if tools:
                test_tool = tools[0]
                tool_name = test_tool.get('name')
                
                call_request = {
                    "jsonrpc": "2.0",
                    "id": 3,
                    "method": "tools/call",
                    "params": {
                        "name": tool_name,
                        "arguments": {}
                    }
                }
                
                process.stdin.write(json.dumps(call_request) + '\n')
                process.stdin.flush()
                
                response = process.stdout.readline().strip()
                
                try:
                    result = json.loads(response)
                    if 'result' in result:
                        print(f"✅ Tool '{tool_name}' executed successfully")
                        if verbose:
                            print(f"   Result: {json.dumps(result['result'], indent=2)}")
                    else:
                        print(f"⚠️  Tool call returned error: {result.get('error', {})}")
                except json.JSONDecodeError:
                    print(f"⚠️  Invalid JSON response")
            
            # Clean up
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            
            print(f"\n✅ Debug session completed")
            return {'success': True}
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _find_server_file(self, target_dir):
        """Find server file in directory"""
        candidates = ['server.py', 'server.js', 'src/server.ts']
        for candidate in candidates:
            path = os.path.join(target_dir, candidate)
            if os.path.exists(path):
                return path
        return None
    
    def _start_server(self, server_file, target_dir):
        """Start server process"""
        if server_file.endswith('.py'):
            cmd = [sys.executable, server_file]
        elif server_file.endswith('.js'):
            cmd = ['node', server_file]
        elif server_file.endswith('.ts'):
            cmd = ['npx', 'ts-node', server_file]
        else:
            cmd = [sys.executable, server_file]
        
        return subprocess.Popen(
            cmd,
            cwd=target_dir,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
