from flask import Flask, render_template
# micro framework - Flask vs Django
app = Flask(__name__)

# decorator : @
# 라우팅 - 복잡한 URL를 쉽게 처리하는 기능
# <name> : 일종의 변수

@app.route('/')
def index():
    return render_template('index.html')

# str 타입은 파라미터의 기본값(생략가능)
@app.route('/page/<name>')
def show_page(name):
    return '지금 보고있는 페이지는 %s 입니다' % name

# int 타입은 파라미터
@app.route('/post/<int:postNum>')
def show_post(postNum):
    return '지금 보여지는 포스트 넘버는 %d 입니다' % postNum

# float 타입의 파라미터
@app.route('/calc/<float:num>')
def show_calc(num):
    return '요청하신 값은 %f 입니다' % num

if __name__ == '__main__':
    app.run()