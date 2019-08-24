from flask import Flask, render_template, jsonify, request
from KakaoTalk_Stripper import file_writer, kakao_stripper
app = Flask(__name__)


## 설명서를 주는 부분 = HTML

@app.route('/')
def main_page():
   return render_template('index.html')

## 데이터를 주고받는 부분 = API

## making dictionary from received id and password
## checking input data, matching with registered data
## API
@app.route('/submit', methods=['POST'])
def submit():
    text_receive = request.form['text']
    print(text_receive)
    kakao_stripper(text_receive)
    print("방금 클라가 입력했어!")
    return jsonify({'result': 'success'})

#run localhost

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
