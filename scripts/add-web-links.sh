#!/bin/bash

# 为每个章节添加网页链接
# 网站地址：https://awesome.tryopenclaw.asia

# 定义网站基础URL
BASE_URL="https://awesome.tryopenclaw.asia"

# 章节文件列表
declare -A CHAPTER_FILES=(
    ["docs/01-basics/01-introduction.md"]="$BASE_URL/docs/01-basics/01-introduction/"
    ["docs/01-basics/02-installation.md"]="$BASE_URL/docs/01-basics/02-installation/"
    ["docs/01-basics/03-quick-start.md"]="$BASE_URL/docs/01-basics/03-quick-start/"
    ["docs/02-core-features/04-file-management.md"]="$BASE_URL/docs/02-core-features/04-file-management/"
    ["docs/02-core-features/05-knowledge-management.md"]="$BASE_URL/docs/02-core-features/05-knowledge-management/"
    ["docs/02-core-features/06-schedule-management.md"]="$BASE_URL/docs/02-core-features/06-schedule-management/"
    ["docs/02-core-features/07-automation-workflow.md"]="$BASE_URL/docs/02-core-features/07-automation-workflow/"
    ["docs/03-advanced/08-skills-extension.md"]="$BASE_URL/docs/03-advanced/08-skills-extension/"
    ["docs/03-advanced/09-multi-platform-integration.md"]="$BASE_URL/docs/03-advanced/09-multi-platform-integration/"
    ["docs/03-advanced/10-api-integration.md"]="$BASE_URL/docs/03-advanced/10-api-integration/"
    ["docs/03-advanced/11-advanced-configuration.md"]="$BASE_URL/docs/03-advanced/11-advanced-configuration/"
    ["docs/03-advanced/99-security-guide.md"]="$BASE_URL/docs/03-advanced/99-security-guide/"
    ["docs/04-practical-cases/12-personal-productivity.md"]="$BASE_URL/docs/04-practical-cases/12-personal-productivity/"
    ["docs/04-practical-cases/13-advanced-automation.md"]="$BASE_URL/docs/04-practical-cases/13-advanced-automation/"
    ["docs/04-practical-cases/14-creative-applications.md"]="$BASE_URL/docs/04-practical-cases/14-creative-applications/"
    ["docs/04-practical-cases/15-solo-entrepreneur-cases.md"]="$BASE_URL/docs/04-practical-cases/15-solo-entrepreneur-cases/"
)

# 遍历所有章节文件
for file in "${!CHAPTER_FILES[@]}"; do
    if [ -f "$file" ]; then
        url="${CHAPTER_FILES[$file]}"

        # 检查是否已经添加了在线阅读链接
        if grep -q "## 🌐 在线阅读" "$file"; then
            echo "✓ $file 已经包含在线阅读链接，跳过"
            continue
        fi

        # 在文件末尾添加在线阅读链接
        cat >> "$file" << 'EOF'

---

## 🌐 在线阅读

📖 **想在线阅读此章节？**

[🔗 在线阅读此章节](WEB_URL_PLACEHOLDER)

访问网站获取更好的阅读体验：
- 📱 响应式设计，支持手机、平板、电脑
- 🌙 支持黑暗模式，保护眼睛
- 🔍 内置搜索功能，快速定位内容
- 📋 目录导航，轻松跳转章节

[🏠 访问完整教程网站](https://awesome.tryopenclaw.asia)
EOF

        # 替换占位符为实际URL
        sed -i '' "s|WEB_URL_PLACEHOLDER|${url}|g" "$file"

        echo "✓ 已添加链接: $file"
    else
        echo "✗ 文件不存在: $file"
    fi
done

echo ""
echo "✅ 完成！所有章节已添加在线阅读链接"
