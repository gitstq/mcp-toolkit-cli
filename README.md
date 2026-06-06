# 🔧 MCP Toolkit CLI

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)](#)
[![MCP](https://img.shields.io/badge/MCP-Protocol-orange)](#)

**🚀 Lightweight MCP Server Development Toolkit | 轻量级 MCP 服务器开发工具包 | 輕量級 MCP 伺服器開發工具包**

[简体中文](#简体中文) | [繁體中文](#繁體中文) | [English](#english)

</div>

---

## 简体中文

### 🎉 项目介绍

**MCP Toolkit CLI** 是一款专为 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 设计的轻量级服务器开发工具包。它让开发者能够通过一条命令快速搭建符合 MCP 标准的 AI 工具服务器，无需繁琐的配置和重复劳动。

**灵感来源**：随着 Claude、Cursor、Copilot 等 AI 编码助手生态的爆发，MCP 协议成为连接 AI 与外部工具的标准桥梁。然而，开发一个合规的 MCP 服务器需要处理 JSON-RPC 通信、工具注册、参数校验等复杂逻辑。MCP Toolkit CLI 正是为了解决这一痛点而生——**让 MCP 服务器开发像搭积木一样简单**。

**自研差异化亮点**：
- 🎯 **零依赖核心**：纯 Python 标准库实现，无需安装任何第三方包
- 🌐 **多语言支持**：一键生成 Python / TypeScript / JavaScript 项目
- 📦 **丰富模板**：内置基础、API、数据处理、AI 集成四大模板
- 🔍 **合规校验器**：自动检测 MCP 协议兼容性，提前发现问题
- 🐛 **交互式调试器**：内置 stdio 通信测试，一键验证服务器功能

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| ⚡ **一键脚手架** | `mcp-toolkit init my-server` 秒级生成完整项目 |
| 🈳 **零依赖运行** | 核心功能仅依赖 Python 标准库，部署零负担 |
| 🔤 **多语言生成** | 支持 Python、TypeScript、JavaScript 三种语言 |
| 📋 **4 大模板** | Basic / API / Data / AI 覆盖常见场景 |
| 🛡️ **合规校验** | 7 项自动化检查确保 MCP 协议兼容 |
| 🐛 **内置调试** | 模拟 MCP 客户端通信，快速定位问题 |
| 🔧 **可选功能** | 认证、日志、指标、沙箱等插件化扩展 |
| 🧪 **测试套件** | 自动生成单元测试，保障代码质量 |

### 🚀 快速开始

#### 环境要求

- **Python** >= 3.8
- 支持平台：Linux / macOS / Windows

#### 安装

```bash
# 方式一：pip 安装
pip install mcp-toolkit-cli

# 方式二：源码安装
git clone https://github.com/gitstq/mcp-toolkit-cli.git
cd mcp-toolkit-cli
pip install -e .
```

#### 创建你的第一个 MCP 服务器

```bash
# 创建一个基础 Python MCP 服务器
mcp-toolkit init my-first-server --template basic --language python

# 进入项目目录
cd my-first-server

# 查看生成的文件
ls
# server.py  mcp_manifest.json  README.md  config.json

# 运行服务器
python server.py
```

#### 验证合规性

```bash
# 检查服务器是否符合 MCP 协议
mcp-toolkit validate .

# 输出示例：
# ✅ All checks passed! MCP compliant.
```

#### 调试服务器

```bash
# 启动交互式调试，测试 stdio 通信
mcp-toolkit debug . --verbose

# 输出示例：
# ✅ Server initialized successfully!
# 🔧 Available tools (3):
#    - hello_world: Say hello to the world
#    - echo: Echo back the input message
#    - calculator: Perform basic calculations
```

### 📖 详细使用指南

#### 命令一览

```bash
mcp-toolkit info              # 显示工具包信息
mcp-toolkit list-templates    # 列出所有可用模板
mcp-toolkit init <name>       # 初始化新项目
  --template, -t    选择模板 (basic/api/data/ai)
  --language, -l    选择语言 (python/typescript/javascript)
  --features, -f    附加功能 (auth/logging/metrics/sandbox)
mcp-toolkit validate [path]   # 验证 MCP 合规性
mcp-toolkit debug [path]      # 调试服务器
mcp-toolkit test [path]       # 运行测试套件
```

#### 高级用法：带认证的 API 服务器

```bash
mcp-toolkit init my-api-server \
  --template api \
  --language python \
  --features auth logging

# 生成的服务器将包含：
# - HTTP 客户端工具
# - Token 认证接口
# - 日志查询接口
```

#### 模板说明

| 模板 | 适用场景 | 内置工具 |
|------|---------|---------|
| `basic` | 通用工具服务器 | hello_world, echo, calculator |
| `api` | 外部 API 封装 | http_client, auth, rate_limiting |
| `data` | 数据处理管道 | csv_parser, json_transform, validator |
| `ai` | AI/LLM 集成 | prompt_template, chain_builder, model_router |

### 💡 设计思路与迭代规划

**技术选型原因**：
- 选择 Python 作为核心语言，因其标准库丰富、跨平台兼容性好
- 零依赖设计确保在任何环境中都能即装即用
- 模板引擎采用纯代码生成，避免引入 Jinja2 等模板依赖

**后续迭代计划**：
- [ ] 支持更多语言模板（Go、Rust、Java）
- [ ] 集成 MCP Inspector 可视化调试
- [ ] 添加 Docker 打包支持
- [ ] 支持远程模板仓库（自定义模板）
- [ ] 集成 CI/CD 工作流生成

**社区贡献方向**：
- 提交新的服务器模板
- 完善多语言文档翻译
- 报告 MCP 协议兼容性 issue

### 📦 打包与部署

```bash
# 本地打包
python setup.py sdist bdist_wheel

# 安装到本地
pip install dist/mcp_toolkit_cli-1.0.0-py3-none-any.whl

# 发布到 PyPI（维护者）
python -m twine upload dist/*
```

### 🤝 贡献指南

欢迎提交 PR！请遵循以下规范：

1. **代码风格**：遵循 PEP 8，使用 4 空格缩进
2. **提交信息**：使用 Angular 规范（`feat:` / `fix:` / `docs:` / `refactor:`）
3. **测试覆盖**：新功能需附带单元测试
4. **文档同步**：更新对应语言版本的 README

### 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 繁體中文

### 🎉 專案介紹

**MCP Toolkit CLI** 是一款專為 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 設計的輕量級伺服器開發工具包。開發者只需一條指令，即可快速建立符合 MCP 標準的 AI 工具伺服器，省去繁瑣的設定與重複工作。

**自研差異化亮點**：
- 🎯 **零依賴核心**：純 Python 標準函式庫實作，無需安裝任何第三方套件
- 🌐 **多語言支援**：一鍵生成 Python / TypeScript / JavaScript 專案
- 📦 **豐富模板**：內建基礎、API、資料處理、AI 整合四大模板
- 🔍 **合規校驗器**：自動檢測 MCP 協定相容性，提前發現問題
- 🐛 **互動式除錯器**：內建 stdio 通訊測試，一鍵驗證伺服器功能

### ✨ 核心特性

| 特性 | 說明 |
|------|------|
| ⚡ **一鍵腳手架** | `mcp-toolkit init my-server` 秒級生成完整專案 |
| 🈳 **零依賴執行** | 核心功能僅依賴 Python 標準函式庫，部署零負擔 |
| 🔤 **多語言生成** | 支援 Python、TypeScript、JavaScript 三種語言 |
| 📋 **4 大模板** | Basic / API / Data / AI 覆蓋常見場景 |
| 🛡️ **合規校驗** | 7 項自動化檢查確保 MCP 協定相容 |
| 🐛 **內建除錯** | 模擬 MCP 客戶端通訊，快速定位問題 |
| 🔧 **可選功能** | 認證、日誌、指標、沙箱等外掛化擴充 |
| 🧪 **測試套件** | 自動生成單元測試，保障程式碼品質 |

### 🚀 快速開始

#### 環境要求

- **Python** >= 3.8
- 支援平台：Linux / macOS / Windows

#### 安裝

```bash
# pip 安裝
pip install mcp-toolkit-cli
```

#### 建立你的第一個 MCP 伺服器

```bash
mcp-toolkit init my-first-server --template basic --language python
cd my-first-server
python server.py
```

#### 驗證合規性

```bash
mcp-toolkit validate .
# ✅ All checks passed! MCP compliant.
```

### 📖 詳細使用指南

#### 指令一覽

```bash
mcp-toolkit info              # 顯示工具包資訊
mcp-toolkit list-templates    # 列出所有可用模板
mcp-toolkit init <name>       # 初始化新專案
  --template, -t    選擇模板 (basic/api/data/ai)
  --language, -l    選擇語言 (python/typescript/javascript)
  --features, -f    附加功能 (auth/logging/metrics/sandbox)
mcp-toolkit validate [path]   # 驗證 MCP 合規性
mcp-toolkit debug [path]      # 除錯伺服器
mcp-toolkit test [path]       # 執行測試套件
```

### 💡 設計思路與迭代規劃

**技術選型原因**：選擇 Python 作為核心語言，因其標準函式庫豐富、跨平台相容性佳。零依賴設計確保在任何環境中都能即裝即用。

**後續迭代計畫**：
- [ ] 支援更多語言模板（Go、Rust、Java）
- [ ] 整合 MCP Inspector 視覺化除錯
- [ ] 新增 Docker 打包支援
- [ ] 支援遠端模板倉庫

### 🤝 貢獻指南

歡迎提交 PR！請遵循 Angular 提交規範（`feat:` / `fix:` / `docs:` / `refactor:`）。

### 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## English

### 🎉 Project Introduction

**MCP Toolkit CLI** is a lightweight development toolkit for [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers. It enables developers to scaffold MCP-compliant AI tool servers with a single command—no tedious configuration or repetitive work required.

**Inspiration**: As AI coding assistants like Claude, Cursor, and Copilot explode in popularity, MCP has become the standard bridge connecting AI to external tools. However, building a compliant MCP server involves complex JSON-RPC communication, tool registration, parameter validation, and more. MCP Toolkit CLI was born to solve this pain point—**making MCP server development as easy as building with blocks**.

**Key Differentiators**:
- 🎯 **Zero-dependency core**: Pure Python standard library, no third-party packages needed
- 🌐 **Multi-language support**: Generate Python / TypeScript / JavaScript projects in one click
- 📦 **Rich templates**: Built-in Basic, API, Data, and AI integration templates
- 🔍 **Compliance validator**: Auto-detect MCP protocol compatibility issues
- 🐛 **Interactive debugger**: Built-in stdio communication testing

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| ⚡ **One-command scaffold** | `mcp-toolkit init my-server` generates a complete project in seconds |
| 🈳 **Zero dependencies** | Core functionality relies solely on Python standard library |
| 🔤 **Multi-language** | Supports Python, TypeScript, and JavaScript |
| 📋 **4 Templates** | Basic / API / Data / AI covering common scenarios |
| 🛡️ **Compliance check** | 7 automated checks ensure MCP protocol compatibility |
| 🐛 **Built-in debugger** | Simulates MCP client communication for quick debugging |
| 🔧 **Optional features** | Auth, logging, metrics, sandbox plugin extensions |
| 🧪 **Test suite** | Auto-generated unit tests for code quality assurance |

### 🚀 Quick Start

#### Requirements

- **Python** >= 3.8
- Platforms: Linux / macOS / Windows

#### Installation

```bash
# Via pip
pip install mcp-toolkit-cli

# Or from source
git clone https://github.com/gitstq/mcp-toolkit-cli.git
cd mcp-toolkit-cli
pip install -e .
```

#### Create Your First MCP Server

```bash
# Create a basic Python MCP server
mcp-toolkit init my-first-server --template basic --language python

# Enter project directory
cd my-first-server

# Run the server
python server.py
```

#### Validate Compliance

```bash
mcp-toolkit validate .
# ✅ All checks passed! MCP compliant.
```

#### Debug Server

```bash
mcp-toolkit debug . --verbose
# ✅ Server initialized successfully!
# 🔧 Available tools (3):
#    - hello_world: Say hello to the world
#    - echo: Echo back the input message
#    - calculator: Perform basic calculations
```

### 📖 Detailed Usage Guide

#### Command Reference

```bash
mcp-toolkit info              # Show toolkit information
mcp-toolkit list-templates    # List available templates
mcp-toolkit init <name>       # Initialize new project
  --template, -t    Choose template (basic/api/data/ai)
  --language, -l    Choose language (python/typescript/javascript)
  --features, -f    Additional features (auth/logging/metrics/sandbox)
mcp-toolkit validate [path]   # Validate MCP compliance
mcp-toolkit debug [path]      # Debug server
mcp-toolkit test [path]       # Run test suite
```

#### Advanced: API Server with Auth

```bash
mcp-toolkit init my-api-server \
  --template api \
  --language python \
  --features auth logging
```

#### Template Overview

| Template | Use Case | Built-in Tools |
|----------|----------|----------------|
| `basic` | General-purpose tool server | hello_world, echo, calculator |
| `api` | External API wrapper | http_client, auth, rate_limiting |
| `data` | Data processing pipeline | csv_parser, json_transform, validator |
| `ai` | AI/LLM integration | prompt_template, chain_builder, model_router |

### 💡 Design Philosophy & Roadmap

**Tech Stack Rationale**:
- Python chosen for its rich standard library and cross-platform compatibility
- Zero-dependency design ensures it works out-of-the-box in any environment
- Template engine uses pure code generation to avoid Jinja2 dependencies

**Roadmap**:
- [ ] More language templates (Go, Rust, Java)
- [ ] MCP Inspector visual debugging integration
- [ ] Docker packaging support
- [ ] Remote template repository support
- [ ] CI/CD workflow generation

**Community Contributions**:
- Submit new server templates
- Improve multi-language documentation
- Report MCP protocol compatibility issues

### 📦 Packaging & Deployment

```bash
# Local build
python setup.py sdist bdist_wheel

# Install locally
pip install dist/mcp_toolkit_cli-1.0.0-py3-none-any.whl

# Publish to PyPI (maintainers)
python -m twine upload dist/*
```

### 🤝 Contributing

PRs are welcome! Please follow these guidelines:

1. **Code style**: Follow PEP 8, 4-space indentation
2. **Commit messages**: Use Angular convention (`feat:` / `fix:` / `docs:` / `refactor:`)
3. **Test coverage**: New features require unit tests
4. **Documentation**: Update corresponding README language versions

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
