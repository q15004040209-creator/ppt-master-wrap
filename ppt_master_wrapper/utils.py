# -*- coding: utf-8 -*-
"""
PPT Master Wrapper - Utility Functions
========================================
工具函数模块
"""

import os
import re
from typing import Optional, List, Dict, Any


# ============================================================
# 文件类型检测
# ============================================================

SUPPORTED_FILE_EXTENSIONS = {
    ".pdf": "PDF 文档",
    ".docx": "Word 文档",
    ".doc": "Word 文档 (旧版)",
    ".html": "HTML 网页",
    ".htm": "HTML 网页",
    ".epub": "EPUB 电子书",
    ".ipynb": "Jupyter Notebook",
    ".txt": "纯文本",
    ".md": "Markdown",
    ".rtf": "RTF 富文本",
    ".odt": "OpenDocument 文档",
    ".tex": "LaTeX 文档",
}


def detect_file_type(file_path: str) -> Optional[str]:
    """
    检测文件类型

    Args:
        file_path: 文件路径

    Returns:
        文件类型描述，未知则返回 None
    """
    ext = os.path.splitext(file_path)[1].lower()
    return SUPPORTED_FILE_EXTENSIONS.get(ext)


def is_supported_file(file_path: str) -> bool:
    """
    检查文件是否支持

    Args:
        file_path: 文件路径

    Returns:
        bool
    """
    ext = os.path.splitext(file_path)[1].lower()
    return ext in SUPPORTED_FILE_EXTENSIONS


# ============================================================
# 路径处理
# ============================================================

def ensure_output_dir(file_path: str) -> str:
    """
    确保输出目录存在

    Args:
        file_path: 文件路径

    Returns:
        规范化后的文件路径
    """
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return file_path


def get_default_output_path(input_path: str, suffix: str = "pptx") -> str:
    """
    根据输入文件生成默认输出路径

    Args:
        input_path: 输入文件路径
        suffix: 输出文件后缀

    Returns:
        默认输出路径
    """
    base = os.path.splitext(input_path)[0]
    return f"{base}.{suffix}"


# ============================================================
# 提示词处理
# ============================================================

def clean_prompt(prompt: str) -> str:
    """
    清理提示词（移除多余空白）

    Args:
        prompt: 原始提示词

    Returns:
        清理后的提示词
    """
    # 移除多余空白
    prompt = re.sub(r"\s+", " ", prompt)
    prompt = prompt.strip()
    return prompt


def extract_page_count_from_prompt(prompt: str) -> Optional[int]:
    """
    从提示词中提取页数信息

    Args:
        prompt: 提示词

    Returns:
        页数，未找到则返回 None
    """
    patterns = [
        r"(\d+)\s*页",
        r"(\d+)\s*page",
        r"(\d+)\s*slides",
        r"(\d+)\s*张",
    ]

    for pattern in patterns:
        match = re.search(pattern, prompt, re.IGNORECASE)
        if match:
            return int(match.group(1))

    return None


# ============================================================
# 配置验证
# ============================================================

def validate_api_key(api_key: str, model: str) -> bool:
    """
    验证 API Key 格式

    Args:
        api_key: API 密钥
        model: 模型名称

    Returns:
        是否有效
    """
    if not api_key:
        return False

    # 简单的格式检查
    key_patterns = {
        "claude": r"^sk-ant-",
        "gpt": r"^sk-",
        "gemini": r"^[A-Za-z0-9_-]{20,}",
        "kimi": r"^pk-",
    }

    pattern = key_patterns.get(model, r".+")
    return bool(re.match(pattern, api_key))


def get_env_key(model: str) -> str:
    """
    获取模型对应的环境变量名

    Args:
        model: 模型名称

    Returns:
        环境变量名
    """
    key_map = {
        "claude": "ANTHROPIC_API_KEY",
        "gpt": "OPENAI_API_KEY",
        "gemini": "GEMINI_API_KEY",
        "kimi": "MOONSHOT_API_KEY",
    }
    return key_map.get(model, "OPENAI_API_KEY")


# ============================================================
# 输出格式化
# ============================================================

def format_size(size_bytes: int) -> str:
    """
    格式化文件大小

    Args:
        size_bytes: 字节数

    Returns:
        格式化字符串 (e.g., "1.5 MB")
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def format_result(result: Dict[str, Any]) -> str:
    """
    格式化生成结果

    Args:
        result: 生成结果字典

    Returns:
        格式化的字符串
    """
    lines = [
        "=" * 40,
        "📊 PPT 生成结果",
        "=" * 40,
        f"✅ 状态: {'成功' if result.get('success') else '失败'}",
        f"📁 输出: {result.get('output_path', 'N/A')}",
        f"🤖 模型: {result.get('model', 'N/A')}",
        f"📄 页数: {result.get('page_count', 'N/A')}",
       f"⏱️  时间: {result.get('timestamp', 'N/A')}",
        "=" * 40,
    ]
    return "\n".join(lines)


# ============================================================
# 导出
# ============================================================

__all__ = [
    "SUPPORTED_FILE_EXTENSIONS",
    "detect_file_type",
    "is_supported_file",
    "ensure_output_dir",
    "get_default_output_path",
    "clean_prompt",
    "extract_page_count_from_prompt",
    "validate_api_key",
    "get_env_key",
    "format_size",
    "format_result",
]