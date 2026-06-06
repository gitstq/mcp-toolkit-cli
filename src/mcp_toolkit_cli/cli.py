#!/usr/bin/env python3
"""
MCP Toolkit CLI - Command Line Interface
"""

import argparse
import sys
import os
import json
import subprocess
import shutil
from pathlib import Path

from . import __version__
from .generator import ProjectGenerator
from .validator import MCPValidator
from .debugger import MCPDebugger
from .templates import TEMPLATES


def print_banner():
    """Print CLI banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║  🔧 MCP Toolkit CLI v{}                                      ║
║  Lightweight MCP Server Development Toolkit                   ║
║  Zero Dependencies · Multi-Language · One-Command Scaffold   ║
╚══════════════════════════════════════════════════════════════╝
""".format(__version__)
    print(banner)


def cmd_init(args):
    """Initialize a new MCP server project"""
    print(f"🚀 Initializing MCP server project: {args.name}")
    
    generator = ProjectGenerator()
    result = generator.generate(
        name=args.name,
        template=args.template,
        language=args.language,
        output_dir=args.output or os.getcwd(),
        features=args.features or []
    )
    
    if result['success']:
        print(f"✅ Project '{args.name}' created successfully!")
        print(f"📁 Location: {result['path']}")
        print(f"📋 Template: {args.template}")
        print(f"🔤 Language: {args.language}")
        print("\n📝 Next steps:")
        print(f"   cd {args.name}")
        print("   mcp-toolkit dev        # Start development server")
        print("   mcp-toolkit validate   # Validate MCP compliance")
        print("   mcp-toolkit test       # Run test suite")
    else:
        print(f"❌ Error: {result['error']}")
        return 1
    return 0


def cmd_validate(args):
    """Validate MCP server compliance"""
    print("🔍 Validating MCP server compliance...")
    
    validator = MCPValidator()
    target = args.path or os.getcwd()
    
    result = validator.validate(target)
    
    print(f"\n📊 Validation Results:")
    print(f"   Total Checks: {result['total']}")
    print(f"   ✅ Passed: {result['passed']}")
    print(f"   ❌ Failed: {result['failed']}")
    print(f"   ⚠️  Warnings: {result['warnings']}")
    
    if result['issues']:
        print("\n📝 Issues Found:")
        for issue in result['issues']:
            icon = "❌" if issue['severity'] == 'error' else "⚠️"
            print(f"   {icon} [{issue['code']}] {issue['message']}")
            if issue.get('fix'):
                print(f"      💡 Fix: {issue['fix']}")
    
    if result['failed'] > 0:
        print(f"\n❌ Validation failed with {result['failed']} errors.")
        return 1
    else:
        print("\n✅ All checks passed! MCP compliant.")
    return 0


def cmd_debug(args):
    """Debug MCP server"""
    print("🐛 Starting MCP debugger...")
    
    debugger = MCPDebugger()
    target = args.path or os.getcwd()
    
    result = debugger.debug(target, port=args.port, verbose=args.verbose)
    
    if not result['success']:
        print(f"❌ Debug failed: {result['error']}")
        return 1
    return 0


def cmd_test(args):
    """Run MCP server tests"""
    print("🧪 Running MCP server tests...")
    
    target = args.path or os.getcwd()
    test_file = os.path.join(target, 'test_mcp_server.py')
    
    if not os.path.exists(test_file):
        print(f"⚠️  No test file found at {test_file}")
        print("   Creating default test suite...")
        _create_default_tests(target)
    
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pytest', test_file, '-v'],
            cwd=target,
            capture_output=False
        )
        return result.returncode
    except FileNotFoundError:
        print("⚠️  pytest not found. Running with unittest...")
        result = subprocess.run(
            [sys.executable, '-m', 'unittest', 'discover', '-v'],
            cwd=target,
            capture_output=False
        )
        return result.returncode


def cmd_list_templates(args):
    """List available templates"""
    print("📋 Available MCP Server Templates:\n")
    
    for name, template in TEMPLATES.items():
        print(f"🔹 {name}")
        print(f"   Description: {template['description']}")
        print(f"   Languages: {', '.join(template['languages'])}")
        print(f"   Features: {', '.join(template['features'])}")
        print()


def cmd_info(args):
    """Show MCP Toolkit info"""
    print_banner()
    print(f"Version: {__version__}")
    print(f"Python: {sys.version}")
    print(f"Platform: {sys.platform}")
    print("\n📚 Documentation: https://github.com/gitstq/mcp-toolkit-cli")
    print("🐛 Issues: https://github.com/gitstq/mcp-toolkit-cli/issues")
    print("⭐ Star: https://github.com/gitstq/mcp-toolkit-cli")


def _create_default_tests(target_dir):
    """Create default test suite"""
    test_content = '''"""
Default MCP Server Test Suite
"""

import unittest
import json
import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))


class TestMCPServer(unittest.TestCase):
    """Test MCP server basic functionality"""
    
    def test_server_import(self):
        """Test server module can be imported"""
        try:
            import server
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import server: {e}")
    
    def test_manifest_exists(self):
        """Test MCP manifest exists"""
        manifest_path = os.path.join(os.path.dirname(__file__), 'mcp_manifest.json')
        self.assertTrue(os.path.exists(manifest_path), "mcp_manifest.json not found")
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        self.assertIn('name', manifest)
        self.assertIn('version', manifest)
        self.assertIn('tools', manifest)
    
    def test_tools_defined(self):
        """Test at least one tool is defined"""
        manifest_path = os.path.join(os.path.dirname(__file__), 'mcp_manifest.json')
        
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        self.assertGreater(len(manifest.get('tools', [])), 0, "No tools defined")


if __name__ == '__main__':
    unittest.main()
'''
    test_path = os.path.join(target_dir, 'test_mcp_server.py')
    with open(test_path, 'w') as f:
        f.write(test_content)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        prog='mcp-toolkit',
        description='MCP Toolkit CLI - Lightweight MCP Server Development Toolkit',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  mcp-toolkit init my-server --template basic --language python
  mcp-toolkit validate ./my-server
  mcp-toolkit debug ./my-server --port 8080
  mcp-toolkit test ./my-server
  mcp-toolkit list-templates
        """
    )
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # init command
    init_parser = subparsers.add_parser('init', help='Initialize a new MCP server project')
    init_parser.add_argument('name', help='Project name')
    init_parser.add_argument('--template', '-t', default='basic',
                            choices=list(TEMPLATES.keys()),
                            help='Project template (default: basic)')
    init_parser.add_argument('--language', '-l', default='python',
                            choices=['python', 'typescript', 'javascript'],
                            help='Programming language (default: python)')
    init_parser.add_argument('--output', '-o', help='Output directory')
    init_parser.add_argument('--features', '-f', nargs='+',
                            choices=['auth', 'logging', 'metrics', 'sandbox'],
                            help='Additional features')
    init_parser.set_defaults(func=cmd_init)
    
    # validate command
    validate_parser = subparsers.add_parser('validate', help='Validate MCP server compliance')
    validate_parser.add_argument('path', nargs='?', help='Path to MCP server directory')
    validate_parser.set_defaults(func=cmd_validate)
    
    # debug command
    debug_parser = subparsers.add_parser('debug', help='Debug MCP server')
    debug_parser.add_argument('path', nargs='?', help='Path to MCP server directory')
    debug_parser.add_argument('--port', '-p', type=int, default=8080, help='Debug port')
    debug_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    debug_parser.set_defaults(func=cmd_debug)
    
    # test command
    test_parser = subparsers.add_parser('test', help='Run MCP server tests')
    test_parser.add_argument('path', nargs='?', help='Path to MCP server directory')
    test_parser.set_defaults(func=cmd_test)
    
    # list-templates command
    list_parser = subparsers.add_parser('list-templates', help='List available templates')
    list_parser.set_defaults(func=cmd_list_templates)
    
    # info command
    info_parser = subparsers.add_parser('info', help='Show toolkit information')
    info_parser.set_defaults(func=cmd_info)
    
    args = parser.parse_args()
    
    if not args.command:
        print_banner()
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
