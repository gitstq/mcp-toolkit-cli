#!/usr/bin/env python3
"""
MCP Toolkit CLI - Project Generator
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

from .templates import TEMPLATES, get_template_files


class ProjectGenerator:
    """Generate MCP server project scaffolding"""
    
    def generate(self, name, template='basic', language='python', 
                 output_dir='.', features=None):
        """Generate a new MCP server project"""
        try:
            features = features or []
            project_path = os.path.join(output_dir, name)
            
            # Check if directory exists
            if os.path.exists(project_path):
                return {
                    'success': False,
                    'error': f"Directory '{name}' already exists"
                }
            
            # Create project directory
            os.makedirs(project_path, exist_ok=True)
            
            # Get template configuration
            template_config = TEMPLATES.get(template, TEMPLATES['basic'])
            
            # Generate files based on template and language
            files = get_template_files(template, language, name, features)
            
            for file_path, content in files.items():
                full_path = os.path.join(project_path, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # Make server.py executable
            server_path = os.path.join(project_path, 'server.py')
            if os.path.exists(server_path):
                os.chmod(server_path, 0o755)
            
            return {
                'success': True,
                'path': os.path.abspath(project_path),
                'name': name,
                'template': template,
                'language': language
            }
            
        except Exception as e:
            # Clean up on failure
            if 'project_path' in locals() and os.path.exists(project_path):
                shutil.rmtree(project_path)
            return {
                'success': False,
                'error': str(e)
            }
