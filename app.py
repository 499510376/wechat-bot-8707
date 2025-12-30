from flask import Flask, request
import hashlib
import os

app = Flask(__name__)

# 从环境变量获取配置
COZE_API_TOKEN = os.getenv('COZE_API_TOKEN', '')
WECHAT_TOKEN = os.getenv('WECHAT_TOKEN', 'wechat123456')

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        # 微信验证
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        
        # 计算签名
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp_str = ''.join(tmp)
        hash_str = hashlib.sha1(tmp_str.encode()).hexdigest()
        
        if hash_str == signature:
            return echostr
        return '验证失败'
    
    return 'success'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
