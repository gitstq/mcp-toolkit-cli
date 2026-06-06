#!/usr/bin/env python3
"""
MCP Toolkit CLI - Setup Script
"""

from setuptools import setup, find_packages
import os

# Read README
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = ''
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='mcp-toolkit-cli',
    version='1.0.0',
    description='🔧 MCP Toolkit CLI - Lightweight MCP Server Development Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='gitstq',
    author_email='',
    url='https://github.com/gitstq/mcp-toolkit-cli',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'mcp-toolkit=mcp_toolkit_cli.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators',
    ],
    python_requires='>=3.8',
    keywords='mcp model-context-protocol cli toolkit server generator',
    project_urls={
        'Bug Reports': 'https://github.com/gitstq/mcp-toolkit-cli/issues',
        'Source': 'https://github.com/gitstq/mcp-toolkit-cli',
    },
    include_package_data=True,
    zip_safe=False,
)
