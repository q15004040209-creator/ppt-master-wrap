# -*- coding: utf-8 -*-
"""
PPT Master Wrapper - Setup
==========================
Python 封装库安装配置
"""

from setuptools import setup, find_packages
import os

# 读取 README
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ppt-master-wrapper",
    version="1.0.0",
    author="Wrapper Contributors",
    author_email="q15004040209@example.com",
    description="Python wrapper for PPT Master - AI generates editable PowerPoint from natural language prompts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/q15004040209-creator/ppt-master-wrap",
    project_urls={
        "Bug Tracker": "https://github.com/q15004040209-creator/ppt-master-wrap/issues",
        "Source": "https://github.com/q15004040209-creator/ppt-master-wrap",
        "Documentation": "https://github.com/hugohe3/ppt-master",
        "Original Project": "https://github.com/hugohe3/ppt-master",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Presentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=[
        # 核心依赖
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
        "all": [
            "openai>=1.0",
            "anthropic>=0.20",
            "google-generativeai>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "ppt-master-wrap=ppt_master_wrapper.cli:main",
        ],
    },
    package_data={
        "ppt_master_wrapper": [
            "py.typed",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)