def fToB64(iF,oF,fpath='.',open_m='b',encoding='utf-8',method=None,rtmd=None,m_index=0):
    """fToB64(iF,oF,path='.',open_m='b',encoding='utf-8',method=None,rtmd=None,m_index=0)\n
iF是要转换的图片的文件名，
oF是要输出的txt文件的文件名，
path是文件路径（不包含文件名），默认为当前目录（“.”）
open_m是读取文件的方式，b为二进制（默认），t为文本
encoding是读取文件的编码，默认为UTF-8，
method是要输出到txt文件字符串类型，\n如果输入b64uri则输出“data:”开头的uri，\n否则输出纯base64字符串，
rtmd是函数返回值类型，\n如果输入b64则返回和输出文件相同的内容\n（除非你要赋值给变量，或者做其它函数的参数，否则请不要使用！），\n否则返回输出文件和类型，
m_index是MIME的id，仅在文件扩展名为sub或wmz时有意义。"""
    from base64 import b64encode
    from os import getcwd,chdir
    ffpath=getcwd()
    chdir(fpath)
    try:
        if open_m=='b':
            with open(iF,"rb") as f:
                fv=f.read()
        elif open_m=='t':
            with open(iF,encoding=encoding) as f:
                fv=f.read()
        else:
            return 'File_Open_Method_Err'
    except:
        return 'File_Open_Err'
    if str(type(fv)) == "<class 'bytes'>":
        fB64=b64encode(fv)
    else:
        fB64=b64encode(fv.encode())
    fB64=str(fB64)
    fB64=fB64[2:len(fB64)-1]
    if method=="b64uri":
        from os import path
        from json import load
        exname=path.splitext(iF)[1][1:]
        try:
            chdir(ffpath)
            with open('MIME.json',encoding='utf-8') as f:
                mimelist=load(f)
            chdir(fpath)
        except:
            return 'MIME_List_Err'
        if exname == 'sub':
            if not m_index in (0,1):
                try:
                    m_index=int(input('请选择Data URI的MIME类型id，\n\r\t0.%s\n\r\t1.%s'%(mimelist['sub'][0],mimelist['sub'][1])))
                except:
                    return 'Id_Err'
                if not m_index in (0,1):
                    return 'Id_Err'
            mime = mimelist[exname][m_index]
        elif exname == 'wmz':
            if not m_index in (0,1):
                try:
                    m_index=int(input('请选择Data URI的MIME类型id，\n\r\t0.%s\n\r\t1.%s'%(mimelist['wmz'][0],mimelist['wmz'][1])))
                except:
                    return 'Id_Err'
                if not m_index in (0,1):
                    return 'Id_Err'
            mime = mimelist[exname][m_index]
        elif exname in ('',' ','  '):
            mime = 'application/octet-stream'
        else:
            try:
                mime = mimelist[exname]
            except:
                mime = 'application/octet-stream'
        fB64="data:%s;base64,%s"%(mime,fB64)
        rt="b64uri"
    else:
        rt="b64str"
    try:
        with open(oF,"w",encoding="utf-8") as f:
            size=f.write(fB64)
    except:
        return 'File_Save_Err'
    if(rtmd=="b64"):
        return fB64
    oF=getcwd()+"\\"+oF
    if size>=1048576:
        size=size/1048576
    elif size>=1024:
        size=size/1024
    return oF+"  (%s)(size: %sBytes)"%(rt,size)

if __name__ == '__main__':
    print(help(fToB64))
