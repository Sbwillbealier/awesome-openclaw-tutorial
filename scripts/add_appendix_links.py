#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob

# 网站基础URL
BASE_URL = "https://awesome.tryopenclaw.asia"

# 获取所有附录文件
appendix_files = glob.glob("appendix/*.md")

# 排除某些文件
exclude_files = ["appendix/H-config-templates.md"]

# 在线阅读链接模板
web_link_template = """

---

## 🌐 在线阅读

📖 **想在线阅读此附录？**

[🔗 在线阅读此附录]({url})

访问网站获取更好的阅读体验：
- 📱 响应式设计，支持手机、平板、电脑
- 🌙 支持黑暗模式，保护眼睛
- 🔍 内置搜索功能，快速定位内容
- 📋 目录导航，轻松跳转章节

[🏠 访问完整教程网站]({base_url})
"""

def add_web_links_appendix():
    """为每个附录添加在线阅读链接"""

    for file_path in appendix_files:
        if file_path in exclude_files:
            continue

        if not os.path.exists(file_path):
            print(f"✗ 文件不存在: {file_path}")
            continue

        # 生成URL（将.md替换为/）
        url = f"{BASE_URL}/{file_path.replace('.md', '/')}"

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经添加了在线阅读链接
        if "## 🌐 在线阅读" in content:
            print(f"✓ {file_path} 已经包含在线阅读链接，跳过")
            continue

        # 添加在线阅读链接
        web_links = web_link_template.format(url=url, base_url=BASE_URL)
        content += web_links

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ 已添加链接: {file_path}")

    print("\n✅ 完成！所有附录已添加在线阅读链接")

if __name__ == "__main__":
    add_web_links_appendix()
