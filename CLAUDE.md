# CLAUDE.md

## 环境约定（用户要求）

- 安装 Python 包一律装进 conda 环境 `claude_en`（`D:\anaconda_envs\envs\claude_en`），不要装进 base 或其他环境
- 安装命令：`conda run -n claude_en python -m pip install <包名>`
- 运行依赖这些包的 Python 脚本也用 claude_en：`conda run -n claude_en python <脚本>`
