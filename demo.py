#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PPT Master Wrapper - Demo & Usage Examples
==========================================
Python 封装库演示 - 用自然语言提示词生成可编辑 PowerPoint

依赖安装:
    pip install -e .

环境变量 (.env):
    OPENAI_API_KEY=sk-xxxxx
    ANTHROPIC_API_KEY=sk-ant-xxxxx
    GEMINI_API_KEY=xxxxx
    IMAGE_BACKEND=gpt-image-2
"""

import os
import sys

# ============================================================
# 示例 1: 基础文本生成 (Basic Text Generation)
# ============================================================
def example_basic_text_generation():
    """最基础的用法：从文本描述直接生成 PPT"""
    try:
        from ppt_master_wrapper import PPTGenerator

        generator = PPTGenerator(
            api_key=os.getenv("ANTHROPIC_API_KEY", "your-api-key"),
            model="claude"  # 可选: claude / gpt / gemini / kimi
        )

        result = generator.generate_from_text(
            prompt="""
            创建一份关于"人工智能发展史"的演示文稿：
            - 10页幻灯片
            - 包含：AI起源、机器学习崛起、深度学习突破、大模型时代、未来展望
            - 使用专业商务风格
            """,
            output_path="outputs/ai_history.pptx"
        )

        print(f"✅ 生成成功: {result['output_path']}")
        print(f"   页数: {result.get('page_count', 'N/A')}")
        return result

    except ImportError:
        print("⚠️  请先安装: pip install -e .")
        return None
    except Exception as e:
       print(f"❌ 生成失败: {e}")
        return None


# ============================================================
# 示例 2: 从文件生成 (File-based Generation)
# ============================================================
def example_file_generation():
    """从 PDF、DOCX 等文件自动提取内容生成 PPT"""
    try:
        from ppt_master_wrapper import PPTGenerator

        generator = PPTGenerator(
            api_key=os.getenv("OPENAI_API_KEY", "your-api-key"),
            model="gpt"
        )

        # 支持格式: .pdf, .docx, .html, .epub, .ipynb, .txt, .md
        result = generator.generate_from_file(
            file_path="projects/annual_report_2024.pdf",
            output_path="outputs/annual_report.pptx",
            # 可选参数
            template="corporate",  # 模板风格: corporate / modern / minimal / free
            aspect_ratio="16:9",  # 画面比例: 16:9 / 4:3 / 9:16
            max_pages=15          # 最大页数限制
        )

        print(f"✅ 文件生成成功: {result['output_path']}")
        return result

    except FileNotFoundError:
        print("⚠️  演示文件不存在，请替换为您的实际文件路径")
        return None
    except Exception as e:
       print(f"❌ 生成失败: {e}")
        return None


# ============================================================
# 示例 3: 模板填充 (Template Fill)
# ============================================================
def example_template_fill():
    """复用您的自定义 PPT 模板，只填充新内容"""
    try:
        from ppt_master_wrapper import PPTGenerator

        generator = PPTGenerator(
            api_key=os.getenv("GEMINI_API_KEY", "your-api-key"),
            model="gemini"
        )

        result = generator.fill_template(
            template_path="templates/product_intro.pptx",
            content="""
            产品名称：智能助手 Pro
            核心功能：语音交互 / 智能推荐 / 自动化流程
            发布日期：2024年12月
            目标用户：企业级客户
            """,
            output_path="outputs/product_intro_filled.pptx",
            # 指定要填充的页面（留空则填充全部）
            pages=[1, 2, 3]  # 只填充前3页
        )

        print(f"✅ 模板填充成功: {result['output_path']}")
        print(f"  保留原模板设计，仅更新内容")
        return result

    except FileNotFoundError:
        print("⚠️  模板文件不存在，请准备您的 PPTX 模板文件")
        return None
    except Exception as e:
       print(f"❌ 填充失败: {e}")
        return None


# ============================================================
# 示例 4: 多语言支持 (Multi-language Support)
# ============================================================
def example_multilingual():
    """演示多语言内容生成能力"""
    try:
        from ppt_master_wrapper import PPTGenerator

        generator = PPTGenerator(
            api_key=os.getenv("ANTHROPIC_API_KEY", "your-api-key"),
            model="claude"
        )

        # 中文内容
        result_cn = generator.generate_from_text(
            prompt="创建一份关于新能源车市场的中文报告，包含市场现状、竞争格局、未来趋势三部分",
            output_path="outputs/ev_market_cn.pptx",
            language="zh-CN"
        )

        # 英文内容
        result_en = generator.generate_from_text(
            prompt="Create a report on global EV market trends, covering current state, competition landscape, and future outlook",
            output_path="outputs/ev_market_en.pptx",
            language="en-US"
        )

        print(f"✅ 中文 PPT: {result_cn['output_path']}")
        print(f"✅ English PPT: {result_en['output_path']}")
        return result_cn, result_en

    except Exception as e:
        print(f"❌ 生成失败: {e}")
        return None, None


# ============================================================
# 示例 5: 批量生成 (Batch Generation)
# ============================================================
def example_batch_generation():
    """批量从多个文件生成 PPT"""
    try:
        from ppt_master_wrapper import PPTGenerator

        generator = PPTGenerator(
            api_key=os.getenv("OPENAI_API_KEY", "your-api-key"),
            model="gpt"
        )

        # 定义批量任务
        tasks = [
            {
                "source": "projects/q1_report.pdf",
                "output": "outputs/q1_report.pptx",
                "title": "Q1 季度报告"
            },
            {
                "source": "projects/q2_report.pdf",
                "output": "outputs/q2_report.pptx",
                "title": "Q2 季度报告"
            },
            {
                "source": "projects/q3_report.pdf",
                "output": "outputs/q3_report.pptx",
                "title": "Q3 季度报告"
            },
        ]

        results = []
        for task in tasks:
            try:
                result = generator.generate_from_file(
                    file_path=task["source"],
                    output_path=task["output"]
                )
                results.append(result)
                print(f"✅ {task['title']} 已生成")
            except FileNotFoundError:
                print(f"⚠️  文件不存在，跳过: {task['source']}")
                continue

        print(f"\n📊 批量完成: {len(results)}/{len(tasks)} 个 PPT 生成成功")
        return results

    except Exception as e:
       print(f"❌ 批量生成失败: {e}")
        return []


# ============================================================
# 示例 6: 高级配置 (Advanced Configuration)
# ============================================================
def example_advanced():
    """展示高级配置选项"""
    try:
        from ppt_master_wrapper import PPTGenerator, GenerationConfig

        # 自定义生成配置
        config = GenerationConfig(
            # 模型配置
            model="claude",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.7,
            max_tokens=8000,

            # 输出配置
            output_dir="outputs",
            output_format="pptx", # pptx / pdf
            aspect_ratio="16:9",

            # 图片配置
            image_backend="gpt-image-2",
            image_quality="high",  # low / medium / high

            # 内容配置
            max_pages=20,
            min_pages=5,
            template="modern",  # corporate / modern / minimal / free

            # 调试
            debug=True,
            verbose=True
        )

        generator = PPTGenerator(config=config)

        result = generator.generate_from_text(
            prompt="创建一份科技公司年度技术峰会的主持人稿PPT",
            output_path="outputs/tech_summit.pptx"
        )

        print(f"✅ 高级配置生成成功: {result['output_path']}")
        return result

    except Exception as e:
       print(f"❌ 生成失败: {e}")
        return None


# ============================================================
# 示例 7: 命令行模拟 (CLI Simulation)
# ============================================================
def example_cli_simulation():
    """演示如何通过代码模拟命令行调用"""
    try:
        from ppt_master_wrapper.cli import main

        # 模拟命令行参数
        sys.argv = [
            "ppt_master_wrapper",
            "generate",
            "--prompt", "创建一份关于健康饮食的科普PPT",
            "--output", "outputs/healthy_diet.pptx",
            "--api-key", os.getenv("OPENAI_API_KEY", "demo-key"),
            "--model", "gpt",
            "--format", "16:9"
        ]

        print("🔧 执行命令:", " ".join(sys.argv[1:]))
        # main()  # 取消注释即可执行真实命令行
        print("⚠️  命令行功能已模拟，实际执行请在终端运行")

    except Exception as e:
       print(f"❌ CLI 模拟失败: {e}")


# ============================================================
# 主函数
# ============================================================
def main():
    """运行所有示例"""
    print("=" * 60)
    print("🤖 PPT Master Wrapper - Python Demo")
    print("=" * 60)

    examples = [
        ("1. 基础文本生成", example_basic_text_generation),
        ("2. 文件生成", example_file_generation),
        ("3. 模板填充", example_template_fill),
        ("4. 多语言支持", example_multilingual),
        ("5. 批量生成", example_batch_generation),
        ("6. 高级配置", example_advanced),
        ("7. 命令行模拟", example_cli_simulation),
    ]

    print("\n可用示例:")
    for name, _ in examples:
        print(f"  {name}")

    print("\n" + "-" * 60)

    # 运行所有示例（根据实际情况取消注释需要运行的示例）
    print("\n[运行示例 1: 基础文本生成]")
    example_basic_text_generation()

    print("\n[运行示例 7: 命令行模拟]")
    example_cli_simulation()

    print("\n" + "=" * 60)
    print("📌 提示: 安装依赖后运行 python demo.py 体验完整功能")
    print("📌 更多示例请查看: https://github.com/hugohe3/ppt-master")
    print("=" * 60)


if __name__ == "__main__":
    main()