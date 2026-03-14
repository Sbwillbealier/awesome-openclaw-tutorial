#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# 网站基础URL
BASE_URL = "https://awesome.tryopenclaw.asia"

# 章节文件和对应的URL
chapter_files = {
    "docs/01-basics/01-introduction.md": f"{BASE_URL}/docs/01-basics/01-introduction/",
    "docs/01-basics/02-installation.md": f"{BASE_URL}/docs/01-basics/02-installation/",
    "docs/01-basics/03-quick-start.md": f"{BASE_URL}/docs/01-basics/03-quick-start/",
    "docs/02-core-features/04-file-management.md": f"{BASE_URL}/docs/02-core-features/04-file-management/",
    "docs/02-core-features/05-knowledge-management.md": f"{BASE_URL}/docs/02-core-features/05-knowledge-management/",
    "docs/02-core-features/06-schedule-management.md": f"{BASE_URL}/docs/02-core-features/06-schedule-management/",
    "docs/02-core-features/07-automation-workflow.md": f"{BASE_URL}/docs/02-core-features/07-automation-workflow/",
    "docs/03-advanced/08-skills-extension.md": f"{BASE_URL}/docs/03-advanced/08-skills-extension/",
    "docs/03-advanced/09-multi-platform-integration.md": f"{BASE_URL}/docs/03-advanced/09-multi-platform-integration/",
    "docs/03-advanced/10-api-integration.md": f"{BASE_URL}/docs/03-advanced/10-api-integration/",
    "docs/03-advanced/11-advanced-configuration.md": f"{BASE_URL}/docs/03-advanced/11-advanced-configuration/",
    "docs/03-advanced/99-security-guide.md": f"{BASE_URL}/docs/03-advanced/99-security-guide/",
    "docs/04-practical-cases/12-personal-productivity.md": f"{BASE_URL}/docs/04-practical-cases/12-personal-productivity/",
    "docs/04-practical-cases/13-advanced-automation.md": f"{BASE_URL}/docs/04-practical-cases/13-advanced-automation/",
    "docs/04-practical-cases/14-creative-applications.md": f"{BASE_URL}/docs/04-practical-cases/14-creative-applications/",
    "docs/04-practical-cases/15-solo-entrepreneur-cases.md": f"{BASE_URL}/docs/04-practical-cases/15-solo-entrepreneur-cases/",
}

# 在线阅读链接模板
web_link_template = """

---

## 🌐 在线阅读

📖 **想在线阅读此章节？**

[🔗 在线阅读此章节]({url})

访问网站获取更好的阅读体验：
- 📱 响应式设计，支持手机、平板、电脑
- ���� 支持黑暗模式，保护眼睛
- 🔍 内置搜索功能，快速定位内容
- 📋 目录导航，轻松跳转章节

[🏠 访问完整教���网站]({base_url})
"""

def add_web_links():
    """为每个章节添加在线阅读链接"""

    for file_path, url in chapter_files.items():
        if not os.path.exists(file_path):
            print(f"✗ 文件不存在: {file_path}")
            continue

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

    print("\n✅ 完成！所有章节已添加在线阅读链接")

if __name__ == "__main__":
    add_web_links()
