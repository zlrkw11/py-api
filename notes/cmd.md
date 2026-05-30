# `py-api` 常用命令

## 1. 环境准备

### 检查 Python 版本
```bash
python3.11 --version
```

### 创建虚拟环境
```bash
python3.11 -m venv .venv
```

### 激活虚拟环境
每次打开新 terminal 都需要执行：

```bash
source .venv/bin/activate
```

### 安装依赖
先升级 `pip`，再安装项目依赖：

```bash
python -m pip install --upgrade pip
pip install "fastapi>=0.111,<1" "uvicorn[standard]>=0.30,<1"
pip install sqlmodel
```

## 2. 启动服务

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Swagger 文档：
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 3. 代码质量（Ruff）

### Lint 检查
```bash
ruff check .
```

### 自动修复
```bash
ruff check --fix .
```

### 格式化代码
```bash
ruff format .
```

## 4. 清理命令

### 清理 `.gitignore` 中的垃圾文件
```bash
git clean -fdX
```

## 5. 脚手架 Prompt

```text
帮我搭一下阶段1 的脚手架，写上必要的中文注释 然后手把手教我一步一步该干嘛，但是代码我自己写。创建一个独立的文件夹可以被app 引用的，符合fastapi和 python的最佳实践
```
