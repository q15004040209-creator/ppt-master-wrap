# -*- coding: utf-8 -*-
"""
PPT Master Wrapper - Core Generator
===================================
核心生成器模块
"""

import os
import time
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List


@dataclass
class GenerationConfig:
    """生成配置类"""

    # 模型配置
    model: str = "claude"  # claude / gpt / gemini / kimi
    api_key: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 8000

    # 输出配置
    output_dir: str = "outputs"
    output_format: str = "pptx"  # pptx / pdf
    aspect_ratio: str = "16:9"  # 16:9 / 4:3 / 9:16

    # 图片配置
    image_backend: str = "gpt-image-2"
    image_quality: str = "high"  # low / medium / high

    # 内容配置
    max_pages: int = 20
    min_pages: int = 5
    template: str = "modern"  # corporate / modern / minimal / free

    # 调试
    debug: bool = False
    verbose: bool = False


class PPTGenerator:
    """
    PPT 生成器类

    基于 PPT Master 工作流，通过自然语言提示词生成可编辑的 PowerPoint 文件。

    Args:
        api_key: AI API 密钥
        model: 使用的模型 (claude/gpt/gemini/kimi)
        config: GenerationConfig 配置对象（可选）

    Example:
        >>> generator = PPTGenerator(api_key="sk-xxx", model="claude")
        >>> result = generator.generate_from_text(
        ...     prompt="创建一份AI发展史PPT",
        ...     output_path="ai.pptx"
        ... )
    """

    SUPPORTED_MODELS = ["claude", "gpt", "gemini", "kimi"]
    SUPPORTED_FORMATS = ["pptx", "pdf"]
    SUPPORTED_TEMPLATES = ["corporate", "modern", "minimal", "free"]

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude",
        config: Optional[GenerationConfig] = None,
    ):
        self.api_key = api_key or self._get_api_key(model)
        self.model = model.lower()

        if config:
            self.config = config
            if self.config.model:
                self.model = self.config.model.lower()
        else:
            self.config = GenerationConfig(model=self.model, api_key=self.api_key)

        self._validate()

    def _get_api_key(self, model: str) -> str:
        """从环境变量获取 API Key"""
        key_map = {
            "claude": "ANTHROPIC_API_KEY",
            "gpt": "OPENAI_API_KEY",
            "gemini": "GEMINI_API_KEY",
            "kimi": "MOONSHOT_API_KEY",
        }
        env_key = key_map.get(model, "OPENAI_API_KEY")
        return os.getenv(env_key, "")

    def _validate(self):
        """验证配置"""
        if self.model not in self.SUPPORTED_MODELS:
            raise ValueError(
                f"不支持的模型: {self.model}。"
                f"支持的模型: {self.SUPPORTED_MODELS}"
            )

        if self.config.output_format not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"不支持的格式: {self.config.output_format}。"
                f"支持的格式: {self.SUPPORTED_FORMATS}"
            )

        if self.config.template not in self.SUPPORTED_TEMPLATES:
            raise ValueError(
                f"不支持的模板: {self.config.template}。"
                f"支持的模板: {self.SUPPORTED_TEMPLATES}"
            )

        if not self.api_key:
            raise ValueError(
                f"未提供 API Key。请通过参数或环境变量设置 "
                f"{self.model.upper()}_API_KEY"
            )

    def generate_from_text(
        self,
        prompt: str,
        output_path: str,
        language: str = "auto",
        **kwargs
    ) -> Dict[str, Any]:
        """
        从文本提示词生成 PPT

        Args:
            prompt: 描述 PPT内容的提示词
            output_path: 输出文件路径
            language: 语言设置 ("auto" / "zh-CN" / "en-US")
            **kwargs: 其他参数传递给底层 PPT Master

        Returns:
            包含生成结果的字典

        Example:
            >>> result = generator.generate_from_text(
            ...     prompt="创建10页AI发展史PPT",
            ...     output_path="ai.pptx"
            ... )
        """
        self._log(f"开始从文本生成 PPT...")
        self._log(f"提示词: {prompt[:100]}...")

        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        # 这里调用底层 PPT Master 工作流
        # 实际实现需要调用原始的 ppt-master 脚本
        result = self._call_ppt_master(
            source="text",
            content=prompt,
            output_path=output_path,
            language=language,
            **kwargs
        )

        return result

    def generate_from_file(
        self,
        file_path: str,
        output_path: str,
        template: str = "free",
        aspect_ratio: str = "16:9",
        max_pages: int = 20,
        **kwargs
    ) -> Dict[str, Any]:
        """
        从文件生成 PPT

        Args:
            file_path: 源文件路径 (PDF/DOCX/HTML/EPUB/TXT/MD)
            output_path: 输出文件路径
            template: 模板风格 (corporate/modern/minimal/free)
            aspect_ratio: 画面比例 (16:9/4:3/9:16)
            max_pages: 最大页数

        Returns:
            包含生成结果的字典

        Example:
            >>> result = generator.generate_from_file(
            ...     file_path="report.pdf",
            ...     output_path="report.pptx"
            ... )
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"源文件不存在: {file_path}")

        self._log(f"开始从文件生成 PPT: {file_path}")

        result = self._call_ppt_master(
            source="file",
            content=file_path,
            output_path=output_path,
            template=template,
            aspect_ratio=aspect_ratio,
            max_pages=max_pages,
            **kwargs
        )

        return result

    def fill_template(
        self,
        template_path: str,
        content: str,
        output_path: str,
        pages: Optional[List[int]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        使用模板填充内容

        Args:
            template_path: 模板 PPTX 文件路径
            content: 要填充的内容
            output_path: 输出文件路径
            pages: 指定要填充的页面列表 (None=全部)

        Returns:
            包含生成结果的字典

        Example:
            >>> result = generator.fill_template(
            ...     template_path="template.pptx",
            ...     content="产品介绍内容...",
            ...     output_path="filled.pptx"
            ... )
        """
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"模板文件不存在: {template_path}")

        self._log(f"使用模板填充内容: {template_path}")

        result = self._call_ppt_master(
            source="template",
            content=content,
            template_path=template_path,
            output_path=output_path,
            pages=pages or "all",
            **kwargs
        )

        return result

    def _call_ppt_master(
        self,
        source: str,
        content: str,
        output_path: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        调用底层 PPT Master 工作流

        这是一个封装方法，实际调用原始 ppt-master 的脚本。
        """
        # 模拟生成结果（实际实现需要调用 ppt-master 脚本）
        timestamp = time.strftime("%Y%m%d_%H%M%S")

        result = {
            "success": True,
            "output_path": output_path,
            "source": source,
            "model": self.model,
            "timestamp": timestamp,
            "page_count": kwargs.get("max_pages", 10),
            "message": f"PPT 生成成功 (模拟模式)"
        }

        # 实际实现中，这里应该调用：
        # subprocess.run([
        #     "python", "scripts/ppt-master/generate.py",
        #     "--source", source,
        #     "--content", content,
        #     "--output", output_path,
        #     ...
        # ])

        self._log(f"✅ 生成完成: {output_path}")
        return result

    def _log(self, message: str):
        """日志输出"""
        if self.config.verbose or self.config.debug:
            print(f"[PPTGenerator] {message}")

    def __repr__(self):
        return (
            f"<PPTGenerator(model={self.model}, "
            f"template={self.config.template}, "
            f"aspect_ratio={self.config.aspect_ratio})>"
        )


# ============================================================
# 便捷函数
# ============================================================

def quick_generate(
    prompt: str,
    output_path: str = "output.pptx",
    api_key: Optional[str] = None,
    model: str = "claude"
) -> Dict[str, Any]:
    """
    快速生成 PPT（便捷函数）

    Args:
        prompt: 提示词
        output_path: 输出路径
        api_key: API 密钥
        model: 模型

    Returns:
        生成结果字典
    """
    generator = PPTGenerator(api_key=api_key, model=model)
    return generator.generate_from_text(prompt=prompt, output_path=output_path)


# ============================================================
# 导出
# ============================================================

__all__ = [
    "PPTGenerator",
    "GenerationConfig",
    "quick_generate",
]