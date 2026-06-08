# PPT Master Wrapper - AI PPT 生成工具封装

[English](#english) | [中文](#中文)

---

## 中文

<p align="center">
  <h1>🤖 PPT Master Wrapper</h1>
  <p>基于<strong>PPT Master</strong> 的 Python 封装库 — 用自然语言提示词直接生成可编辑的 PowerPoint演示文稿</p>
  <a href="https://github.com/hugohe3/ppt-master">原始仓库</a> ·<a href="https://github.com/hugohe3/ppt-master/stargazers">⭐ 25,236 Stars</a> · <a href="https://github.com/hugohe3/ppt-master/releases">📦 下载</a>
</p>

---

###✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎯 **自然语言驱动** | 用提示词描述需求，AI 自动生成完整 PPT |
| ✏️ **完全可编辑** | 输出的 `.pptx` 每个元素均可点击编辑，非图片导出 |
| 📊 **原生 PowerPoint** | 生成标准 PPTX 文件，兼容 Office 2016+ |
| 🖼️ **AI 图片生成** | 支持 GPT Image / Gemini 等模型自动配图 |
| 🔒 **数据本地化** | 文件仅在本地处理，不上传第三方服务器 |
| 🤖 **多 AI 模型支持** | Claude / GPT / Gemini / Kimi 等主流模型 |
| 📐 **多格式支持** | PPT 16:9、小红书、微信图文等10+ 格式 |

---

### 📦 安装

```bash
pip install git+https://github.com/q15004040209-creator/ppt-master-wrap.git
```

或克隆后本地安装：

```bash
git clone https://github.com/q15004040209-creator/ppt-master-wrap.git
cd ppt-master-wrap
pip install -e .
```

---

### 🚀 快速开始

#### 方式一：Python API（推荐）

```python
from ppt_master_wrapper import PPTGenerator

# 初始化生成器
generator = PPTGenerator(
    api_key="your-api-key",          # 你的 AI API Key
    model="claude" # 模型：claude / gpt / gemini / kimi
)

# 方法1：从文本生成
result = generator.generate_from_text(
    prompt="创建一份关于人工智能发展历史的演示文稿，包含5张幻灯片",
    output_path="ai_history.pptx"
)

# 方法2：从 PDF 文件生成
result = generator.generate_from_file(
    file_path="path/to/your/document.pdf",
    output_path="document.pptx"
)

# 方法3：使用模板填充
result = generator.fill_template(
    template_path="template.pptx",
    content="将以下内容填充到模板中：...",
    output_path="filled.pptx"
)

print(f"✅ PPT 已生成：{result['output_path']}")
```

#### 方式二：命令行

```bash
# 文本生成
python -m ppt_master_wrapper generate --prompt "创建产品介绍PPT，包含5页" --output product.pptx --api-key YOUR_KEY

# 文件生成
python -m ppt_master_wrapper generate --file document.pdf --output output.pptx --api-key YOUR_KEY

# 查看帮助
python -m ppt_master_wrapper --help
```

---

### 🏗️ 项目结构

```
ppt-master-wrap/
├── README.md
├── README_CN.md
├── demo.py              # Python 使用示例
├── setup.py
└── ppt_master_wrapper/
    ├── __init__.py
    ├── generator.py    # 核心生成器
    ├── cli.py          # 命令行接口
    └── utils.py        # 工具函数
```

---

###🔧 配置说明

#### 环境变量（可选）

```bash
# .env 文件
OPENAI_API_KEY=sk-xxxxx          # OpenAI API Key
ANTHROPIC_API_KEY=sk-ant-xxxxx    # Anthropic (Claude) API Key
GEMINI_API_KEY=xxxxx              # Google Gemini API Key
IMAGE_BACKEND=gpt-image-2 # 图片生成后端
```

#### 支持的 AI 模型

| 模型 | 提供商 | 特点 |
|------|--------|------|
| `claude` | Anthropic | 最佳效果，推荐 Claude Opus |
| `gpt` | OpenAI | 稳定快速 |
| `gemini` | Google | 性价比高 |
| `kimi` | 月之暗面 | 中文支持好 |

---

### 📖 详细文档

- [PPT Master 官方文档](https://github.com/hugohe3/ppt-master)
- [Getting Started](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md)
- [常见问题 FAQ](https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md)

---

###🐛 问题反馈

如遇问题，请前往 [GitHub Issues](https://github.com/q15004040209-creator/ppt-master-wrap/issues)

---

### 📜 许可证

本项目基于 [MIT License](https://github.com/hugohe3/ppt-master/blob/main/LICENSE)
原始项目由 [Hugo He](https://www.hehugo.com/) 开发维护

---

## English

<p align="center">
  <h1>🤖 PPT Master Wrapper</h1>
  <p>Python wrapper for<strong>PPT Master</strong> — Generate editable PowerPoint presentations from natural language prompts</p>
  <a href="https://github.com/hugohe3/ppt-master">Original Repo</a> · <a href="https://github.com/hugohe3/ppt-master/stargazers">⭐ 25,236 Stars</a> · <a href="https://github.com/hugohe3/ppt-master/releases">📦 Releases</a>
</p>

---

###✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Natural Language Driven** | Describe what you want, AI generates the complete PPT |
| ✏️ **Fully Editable** | Every element in output `.pptx` is clickable and editable |
| 📊 **Native PowerPoint** | Standard PPTX format, compatible with Office 2016+ |
| 🖼️ **AI Image Generation** | Auto-generate illustrations with GPT Image / Gemini |
| 🔒 **Local Data Processing** | Files processed locally, no third-party server upload |
| 🤖 **Multi-Model Support** | Claude / GPT / Gemini / Kimi and more |
| 📐 **Multi-Format Support** | PPT 16:9, Xiaohongshu, WeChat articles, 10+ formats |

---

### 📦 Installation

```bash
pip install git+https://github.com/q15004040209-creator/ppt-master-wrap.git
```

Or clone and install locally:

```bash
git clone https://github.com/q15004040209-creator/ppt-master-wrap.git
cd ppt-master-wrap
pip install -e .
```

---

### 🚀 Quick Start

#### Method 1: Python API (Recommended)

```python
from ppt_master_wrapper import PPTGenerator

# Initialize generator
generator = PPTGenerator(
    api_key="your-api-key",          # Your AI API Key
    model="claude"                    # Model: claude / gpt / gemini / kimi
)

# Method 1: Generate from text
result = generator.generate_from_text(
    prompt="Create a presentation about the history of AI development with 5 slides",
    output_path="ai_history.pptx"
)

# Method 2: Generate from file
result = generator.generate_from_file(
    file_path="path/to/your/document.pdf",
    output_path="document.pptx"
)

# Method 3: Fill template
result = generator.fill_template(
    template_path="template.pptx",
    content="Fill the template with the following content: ...",
    output_path="filled.pptx"
)

print(f"✅ PPT generated: {result['output_path']}")
```

#### Method 2: Command Line

```bash
# Text generation
python -m ppt_master_wrapper generate --prompt "Create a product intro PPT with 5 pages" --output product.pptx --api-key YOUR_KEY

# File generation
python -m ppt_master_wrapper generate --file document.pdf --output output.pptx --api-key YOUR_KEY

# Help
python -m ppt_master_wrapper --help
```

---

### 🏗️ Project Structure

```
ppt-master-wrap/
├── README.md
├── README_CN.md
├── demo.py              # Python usage example
├── setup.py
└── ppt_master_wrapper/
    ├── __init__.py
    ├── generator.py    # Core generator
    ├── cli.py          # CLI interface
    └── utils.py        # Utility functions
```

---

### 🔧 Configuration

#### Environment Variables (Optional)

```bash
# .env file
OPENAI_API_KEY=sk-xxxxx          # OpenAI API Key
ANTHROPIC_API_KEY=sk-ant-xxxxx    # Anthropic (Claude) API Key
GEMINI_API_KEY=xxxxx              # Google Gemini API Key
IMAGE_BACKEND=gpt-image-2         # Image generation backend
```

#### Supported AI Models

| Model | Provider | Notes |
|-------|----------|-------|
| `claude` | Anthropic | Best quality, recommend Claude Opus |
| `gpt` | OpenAI | Stable and fast |
| `gemini` | Google | Best value for money |
| `kimi` | Moonshot | Excellent Chinese support |

---

### 📖 Full Documentation

- [PPT Master Official Docs](https://github.com/hugohe3/ppt-master)
- [Getting Started](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md)
- [FAQ](https://github.com/hugohe3/ppt-master/blob/main/docs/faq.md)

---

### 🐛 Issue Reporting

For issues, please open at [GitHub Issues](https://github.com/q15004040209-creator/ppt-master-wrap/issues)

---

### 📜 License

This project is under [MIT License](https://github.com/hugohe3/ppt-master/blob/main/LICENSE)  
Original project developed and maintained by [Hugo He](https://www.hehugo.com/)

---

*Made with ❤️ — If this project helps you, please give it a ⭐*