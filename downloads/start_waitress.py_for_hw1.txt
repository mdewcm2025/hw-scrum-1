#pip install waitress
from waitress import serve
from cmsimde.flaskapp import app

if __name__ == "__main__":
    # 僅綁定在 IPv6 localhost (::1)，port 8080
    serve(app, host='::1', port=8080)