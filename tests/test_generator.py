#!/usr/bin/env python3
"""
MCP Toolkit CLI - Generator Tests
"""

import unittest
import os
import sys
import shutil
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mcp_toolkit_cli.generator import ProjectGenerator


class TestProjectGenerator(unittest.TestCase):
    """Test project generator"""
    
    def setUp(self):
        """Set up test environment"""
        self.generator = ProjectGenerator()
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_generate_basic_python(self):
        """Test generating basic Python project"""
        result = self.generator.generate(
            name='test-server',
            template='basic',
            language='python',
            output_dir=self.test_dir
        )
        
        self.assertTrue(result['success'])
        self.assertEqual(result['name'], 'test-server')
        
        project_path = result['path']
        self.assertTrue(os.path.exists(project_path))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'server.py')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'mcp_manifest.json')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'README.md')))
    
    def test_generate_duplicate_name(self):
        """Test generating project with duplicate name"""
        # First generation
        self.generator.generate(
            name='test-server',
            template='basic',
            language='python',
            output_dir=self.test_dir
        )
        
        # Second generation should fail
        result = self.generator.generate(
            name='test-server',
            template='basic',
            language='python',
            output_dir=self.test_dir
        )
        
        self.assertFalse(result['success'])
        self.assertIn('already exists', result['error'])
    
    def test_generate_with_features(self):
        """Test generating project with features"""
        result = self.generator.generate(
            name='test-server',
            template='basic',
            language='python',
            output_dir=self.test_dir,
            features=['auth', 'logging']
        )
        
        self.assertTrue(result['success'])
        
        # Check config has features
        config_path = os.path.join(result['path'], 'config.json')
        import json
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        self.assertIn('auth', config['features'])
        self.assertIn('logging', config['features'])


class TestValidator(unittest.TestCase):
    """Test MCP validator"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_validate_empty_dir(self):
        """Test validating empty directory"""
        from mcp_toolkit_cli.validator import MCPValidator
        
        validator = MCPValidator()
        result = validator.validate(self.test_dir)
        
        self.assertGreater(result['failed'], 0)
        self.assertTrue(any(i['code'] == 'MISSING_MANIFEST' for i in result['issues']))


if __name__ == '__main__':
    unittest.main()
