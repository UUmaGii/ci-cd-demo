# 测试代码
import app

def test_add():
    assert app.add(1,2) == 3

def test_index_html():
    with open('public/index.html','r') as f:
        html = f.read()
        assert '<h1>Hello CI-CD WORKFLOW</h1>' in html
