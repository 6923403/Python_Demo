from src.Wy_Finance import WangYi
#from src.Ths_Finance import TongHuaShun
#from src.Jrj_Finance import JinRongJie
from src.Platform import Files


def Wy(filename):
    Wy = WangYi(filename)
    Wy.main(filename)

def THS(filename):
    Ths = TongHuaShun(filename)
    Ths.main(filename)

def JRJ(filename):
    Jrj = JinRongJie(filename)
    Jrj.main(filename)


def get_News(platform, filename):
        Wy(filename)
#        THS(filename)
#        JRJ(filename)

def get_filename(platform):
    if m_platform == True:
        win_file = pt.win_filename()
        return win_file
    else:
        linux_file = pt.linux_filename()
        return linux_file

if __name__ == '__main__':
    pt = Files()

    m_platform = pt.get_platform() #判断系统
    filename = get_filename(m_platform)
    get_News(m_platform, filename) #获取信息

    #pt.file_move(m_platform) #文件移动 重命名操作

    print("操作完成")

    if m_platform == True:
        pt.pause()
