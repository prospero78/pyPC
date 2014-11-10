# -*- coding: utf8 -*-
"""
    Главный запускающий файл для всего класса видеокарты.
"""
from pak_cpu.mod_cpu import ClsCPU

def main():
    """
    Запуск подсистемы видеокарты.
    """
    app_cpu = ClsCPU()
    app_cpu.run()
    
if __name__ == '__main__':
    main()
