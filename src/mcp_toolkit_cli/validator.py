#!/usr/bin/env python3
"""
MCP Toolkit CLI - MCP Validator
"""

import os
import json
from pathlib import Path


class MCPValidator:
    """Validate MCP server compliance"""
    
    def validate(self, target_dir):
        """Validate an MCP server directory"""
        results = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'issues': []
        }
        
        checks = [
            self._check_manifest_exists,
            self._check_manifest_structure,
            self._check_server_file,
            self._check_tools_definition,
            self._check_jsonrpc_support,
            self._check_stdio_transport,
            self._check_error_handling
        ]
        
        for check in checks:
            results['total'] += 1
            try:
                issue = check(target_dir)
                if issue:
                    results['issues'].append(issue)
                    if issue['severity'] == 'error':
                        results['failed'] += 1
                    else:
                        results['warnings'] += 1
                else:
                    results['passed'] += 1
            except Exception as e:
                results['issues'].append({
                    'severity': 'error',
                    'code': 'VALIDATION_ERROR',
                    'message': str(e),
                    'fix': None
                })
                results['failed'] += 1
        
        return results
    
    def _check_manifest_exists(self, target_dir):
        """Check if mcp_manifest.json exists"""
        manifest_path = os.path.join(target_dir, 'mcp_manifest.json')
        if not os.path.exists(manifest_path):
            return {
                'severity': 'error',
                'code': 'MISSING_MANIFEST',
                'message': 'mcp_manifest.json not found',
                'fix': 'Create mcp_manifest.json with server metadata'
            }
        return None
    
    def _check_manifest_structure(self, target_dir):
        """Check manifest structure"""
        manifest_path = os.path.join(target_dir, 'mcp_manifest.json')
        try:
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            
            required_fields = ['name', 'version', 'tools']
            missing = [f for f in required_fields if f not in manifest]
            
            if missing:
                return {
                    'severity': 'error',
                    'code': 'INVALID_MANIFEST',
                    'message': f"Missing required fields: {', '.join(missing)}",
                    'fix': f"Add {', '.join(missing)} to mcp_manifest.json"
                }
            
            if not isinstance(manifest['tools'], list):
                return {
                    'severity': 'error',
                    'code': 'INVALID_TOOLS',
                    'message': 'tools must be an array',
                    'fix': 'Change tools to an array in mcp_manifest.json'
                }
            
            return None
            
        except json.JSONDecodeError:
            return {
                'severity': 'error',
                'code': 'INVALID_JSON',
                'message': 'mcp_manifest.json is not valid JSON',
                'fix': 'Fix JSON syntax in mcp_manifest.json'
            }
    
    def _check_server_file(self, target_dir):
        """Check if server file exists"""
        server_files = ['server.py', 'server.js', 'src/server.ts']
        found = any(os.path.exists(os.path.join(target_dir, f)) for f in server_files)
        
        if not found:
            return {
                'severity': 'error',
                'code': 'MISSING_SERVER',
                'message': 'No server file found (server.py, server.js, or src/server.ts)',
                'fix': 'Create a server implementation file'
            }
        return None
    
    def _check_tools_definition(self, target_dir):
        """Check tools are properly defined"""
        manifest_path = os.path.join(target_dir, 'mcp_manifest.json')
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        tools = manifest.get('tools', [])
        
        if len(tools) == 0:
            return {
                'severity': 'warning',
                'code': 'NO_TOOLS',
                'message': 'No tools defined in manifest',
                'fix': 'Add at least one tool to the tools array'
            }
        
        for tool in tools:
            if 'name' not in tool:
                return {
                    'severity': 'error',
                    'code': 'TOOL_MISSING_NAME',
                    'message': 'Tool missing required "name" field',
                    'fix': 'Add name field to all tools'
                }
            if 'description' not in tool:
                return {
                    'severity': 'warning',
                    'code': 'TOOL_MISSING_DESC',
                    'message': f"Tool '{tool.get('name', 'unknown')}' missing description",
                    'fix': 'Add description field to all tools'
                }
        
        return None
    
    def _check_jsonrpc_support(self, target_dir):
        """Check JSON-RPC 2.0 support"""
        server_files = ['server.py', 'server.js', 'src/server.ts']
        server_content = ''
        
        for f in server_files:
            path = os.path.join(target_dir, f)
            if os.path.exists(path):
                with open(path, 'r') as file:
                    server_content = file.read()
                break
        
        if 'jsonrpc' not in server_content and 'JSON-RPC' not in server_content:
            return {
                'severity': 'error',
                'code': 'NO_JSONRPC',
                'message': 'Server does not appear to support JSON-RPC 2.0',
                'fix': 'Implement JSON-RPC 2.0 protocol in server'
            }
        return None
    
    def _check_stdio_transport(self, target_dir):
        """Check stdio transport support"""
        server_files = ['server.py', 'server.js', 'src/server.ts']
        server_content = ''
        
        for f in server_files:
            path = os.path.join(target_dir, f)
            if os.path.exists(path):
                with open(path, 'r') as file:
                    server_content = file.read()
                break
        
        if 'stdin' not in server_content and 'process.stdin' not in server_content:
            return {
                'severity': 'warning',
                'code': 'NO_STDIO',
                'message': 'Server may not support stdio transport',
                'fix': 'Add stdio transport support for MCP compatibility'
            }
        return None
    
    def _check_error_handling(self, target_dir):
        """Check error handling"""
        server_files = ['server.py', 'server.js', 'src/server.ts']
        server_content = ''
        
        for f in server_files:
            path = os.path.join(target_dir, f)
            if os.path.exists(path):
                with open(path, 'r') as file:
                    server_content = file.read()
                break
        
        has_try_catch = 'try' in server_content and ('except' in server_content or 'catch' in server_content)
        
        if not has_try_catch:
            return {
                'severity': 'warning',
                'code': 'NO_ERROR_HANDLING',
                'message': 'Server may lack error handling',
                'fix': 'Add try/catch or try/except blocks for robustness'
            }
        return None
