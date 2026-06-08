# -*- coding: utf-8 -*-
"""
PPT Master Wrapper
==================
Python 封装库 - 用自然语言提示词生成可编辑 PowerPoint

基于 PPT Master (https://github.com/hugohe3/ppt-master) 封装

Usage:
    from ppt_master_wrapper import PPTGenerator

    generator = PPTGenerator(api_key="your-key", model="claude")
    result = generator.generate_from_text(
        prompt="创建一份关于AI的报告",
        output_path="output.pptx"
    )
"""

__version__ = "1.0.0"
__author__ = "Wrapper Contributors"
__license__ = "MIT"

from .generator import PPTGenerator, GenerationConfig

__all__ = [
    "PPTGenerator",
    "GenerationConfig",
    "__version__",
]