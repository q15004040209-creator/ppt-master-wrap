#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PPT Master Wrapper - CLI Interface
==================================
命令行接口模块
"""

import argparse
import sys
import os
from .generator import PPTGenerator, GenerationConfig


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        prog="ppt_master_wrapper",
        description="🤖 PPT Master Wrapper - AI PPT 生成工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  #文本生成
  python -m ppt_master_wrapper generate --prompt "创建AI报告" --output ai.pptx

  # 文件生成
  python -m ppt_master_wrapper generate --file report.pdf --output report.pptx

  # 指定模型
  python -m ppt_master_wrapper generate --prompt "创建PPT" --model gpt --api-key YOUR_KEY

更多信息: https://github.com/q15004040209-creator/ppt-master-wrap
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # =============================================
    # generate 子命令
    # =============================================
    gen_parser = subparsers.add_parser(
        "generate",
        help="生成 PPT",
        description="从文本或文件生成 PowerPoint"
    )

    gen_parser.add_argument(
        "--prompt", "-p",
        type=str,
        help="PPT 内容描述提示词"
    )

    gen_parser.add_argument(
        "--file", "-f",
        type=str,
        help="源文件路径 (PDF/DOCX/HTML等)"
    )

    gen_parser.add_argument(
        "--output", "-o",
        type=str,
        required=True,
        help="输出文件路径"
    )

    gen_parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("ANTHROPIC_API_KEY"),
        help="AI API 密钥"
    )

    gen_parser.add_argument(
        "--model", "-m",
        type=str,
        choices=["claude", "gpt", "gemini", "kimi"],
        default="claude",
        help="使用的 AI 模型 (默认: claude)"
    )

    gen_parser.add_argument(
        "--template",
        type=str,
        choices=["corporate", "modern", "minimal", "free"],
        default="free",
        help="模板风格"
    )

    gen_parser.add_argument(
        "--format",
        type=str,
        choices=["16:9", "4:3", "9:16"],
        default="16:9",
        dest="aspect_ratio",
        help="画面比例"
    )

    gen_parser.add_argument(
        "--max-pages",
        type=int,
        default=20,
        help="最大页数"
    )

    gen_parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细输出"
    )

    # =============================================
    # version 子命令
    # =============================================
    subparsers.add_parser(
        "version",
        help="显示版本信息",
        description="显示版本和作者信息"
    )

    # =============================================
    # help 子命令
    # =============================================
    subparsers.add_parser(
        "help",
        help="显示帮助",
        description="显示详细帮助信息"
    )

    # 解析参数
    args = parser.parse_args()

    # 执行命令
    if args.command == "version":
        from . import __version__, __author__
        print(f"PPT Master Wrapper v{__version__}")
        print(f"Author: {__author__}")
        print(f"Based on: PPT Master (https://github.com/hugohe3/ppt-master)")

    elif args.command == "generate":
        if not args.prompt and not args.file:
            gen_parser.print_help()
            sys.exit(1)

        if not args.api_key:
            print("❌ 错误: 未提供 API 密钥")
            print("   请通过 --api-key 参数或环境变量设置 API_KEY")
            print("   环境变量:")
            print("     - Claude: ANTHROPIC_API_KEY")
            print("     - GPT: OPENAI_API_KEY")
            print("     - Gemini: GEMINI_API_KEY")
            sys.exit(1)

        try:
            generator = PPTGenerator(
                api_key=args.api_key,
                model=args.model,
                config=GenerationConfig(
                    model=args.model,
                    api_key=args.api_key,
                    output_dir=os.path.dirname(args.output) or ".",
                    aspect_ratio=args.aspect_ratio,
                    max_pages=args.max_pages,
                    template=args.template,
                    verbose=args.verbose
                )
            )

            if args.prompt:
                result = generator.generate_from_text(
                    prompt=args.prompt,
                    output_path=args.output
                )
            else:
                result = generator.generate_from_file(
                    file_path=args.file,
                    output_path=args.output
                )

            if result["success"]:
                print(f"✅ PPT 生成成功: {result['output_path']}")
                print(f"   模型: {result['model']}")
                print(f"   页数: {result.get('page_count', 'N/A')}")
            else:
                print(f"❌ 生成失败: {result.get('message', '未知错误')}")
                sys.exit(1)

        except Exception as e:
            print(f"❌ 错误: {e}")
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()