run app:
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

swagger url:
[127.0.0.1.8000/docs](http://127.0.0.1:8000)

prompt for building scaffolding:
帮我搭一下阶段1 的脚手架，写上必要的中文注释 然后手把手教我一步一步该干嘛，但是代码我自己写。创建一个独立的文件夹可以被app 引用的，符合fastapi和 python的最佳实践