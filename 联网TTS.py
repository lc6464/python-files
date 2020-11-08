from datetime import datetime
from urllib.request import urlopen
from urllib.parse import quote

def tts(msg,lang='zh'):
    "tts(msg,lang)\nmsg：要生成的内容，必填！\nlang：语言，默认值\"zh\"，zh,en二选一。"
    if lang=="zh":
	    mes="http://tts.baidu.com/text2audio?lan=zh&pid=101&vol=9&ie=UTF-8&text="
    elif lang=="en":
	    mes="http://tts.baidu.com/text2audio?lan=en&pid=101&vol=9&ie=UTF-8&text="
    else:
        return "语言错误！仅支持zh和en！"
    return urlopen(mes+quote(msg)).read()

def save_binFile(Bytes):
    'save_binFile(Bytes)\nBytes：要保存的二进制文件的字节流。'
    if not isinstance(Bytes,bytes):
        return 'Bytes参数必须为bytes类型！'
    fname='TTS_%s.mp3'%datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    f=open(fname,"wb")
    f.write(Bytes)
    f.close()
    return fname

def writeTTS(msg,lang='zh'):
    'writeTTS(msg,lang)\n生成语音并输出到二进制文件，\ntts()和save_binFile()的组合，\n详情请见help(tts)和help(save_binFile)。'
    tts_return=tts(msg,lang)
    ttsb=True if lang in ('zh','en') else False
    if ttsb:
        return save_binFile(tts_return)
    else:
        return '语言错误！仅支持zh和en！'

if __name__=='__main__':
    print(help(tts),'\n',help(save_binFile),'\n',help(writeTTS))
