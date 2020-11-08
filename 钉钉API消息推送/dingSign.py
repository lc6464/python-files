def sign(sec):
    from time import time
    from hmac import new
    from hashlib import sha256
    from base64 import b64encode
    from urllib.parse import quote_plus
    timestamp = int(round(time() * 1000))
    sec_enc = sec.encode()
    string_to_sign = '{}\n{}'.format(timestamp, sec)
    string_to_sign_enc = string_to_sign.encode()
    hmac_code = new(sec_enc, string_to_sign_enc, digestmod=sha256).digest()
    sign = quote_plus(b64encode(hmac_code))
    return {"timestamp":timestamp,"sign":sign}
if __name__=='__main__':
    print(sign(input('请输入SEC Key：')))
