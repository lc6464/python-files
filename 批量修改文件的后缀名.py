# 批量修改某个文件夹下的所有文件后缀名
# 比如把jpg 修改成JNG
# 把rar修改成7z

import easygui as g
import os



class Revise:
    def __init__(self):
        # 确定要修改的文件的目录位置
        self.msg_file =g.diropenbox(msg='请选择目标文件位置',title='选择文件夹')
        os.chdir(self.msg_file)
        return self.job()

    # 让用户输入需要修改的后缀名及要改成的目标后缀名
    def job(self):
        self.initial_name = g.enterbox(msg='你想要修改的后缀名是什么！')
        self.goal_name = g.enterbox(msg='你想要修改成什么后缀名!')
        self.filename_list = os.listdir(path='.')
        # 给用户显示该文件夹下所有的文件，让他确定一下
        g.choicebox(msg='这是文件夹下所有的文件，不能有不想修改文件！！！\
其实无所谓，只是我太懒了，不想在完善了！',choices=self.filename_list)
        for i in self.filename_list:
            name = i.split('.')
            if name[1] == self.initial_name:
                os.rename(i,name[0]+'.'+self.goal_name)
    
message = '注意事项:\n\
    1、这个修改后缀名支持任何形式的修改；\
\t2、需要你把要修改的问题放在一个文件夹之中。'
g.msgbox(msg=message,title='批量修改后缀名',ok_button='我同意，开始使用！')
a = Revise()
 
g.msgbox(msg='修改成功！！！')
