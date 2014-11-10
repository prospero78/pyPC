# -*- coding: utf8 -*-
"""
    Главный запускающий файл для всего класса видеокарты.
"""
from pak_video.mod_video import ClsVideo

def main():
    """
    Запуск подсистемы видеокарты.
    """
    app_video = ClsVideo()
    app_video.run()
    
if __name__ == '__main__':
    main()
