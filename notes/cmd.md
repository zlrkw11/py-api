check version: 

python3.11 --version

go into venv: 

python3.11 -m venv .venv

activate venv:
每次运行新terminal都必须执行此操作

source .venv/bin/activate

install:
确保pip是最新版本

python -m pip install --upgrade pip

pip install "fastapi>=0.111,<1" "uvicorn[standard]>=0.30,<1"

run app:

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

swagger url:

[127.0.0.1.8000/docs](http://127.0.0.1:8000)

prompt for building scaffolding:

帮我搭一下阶段1 的脚手架，写上必要的中文注释 然后手把手教我一步一步该干嘛，但是代码我自己写。创建一个独立的文件夹可以被app 引用的，符合fastapi和 python的最佳实践

清理gitignore
git clean -fdX