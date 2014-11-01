# -*- coding: utf8 -*-
"""
Модуль передаёт для анализа информацию о проекте.
"""
class ClsInfo(object):
    """
    Содержит информацию о проекте для анализа.проекта.
    """
    def __init__(self):
        self.author_info = 'Valerij Shipkov'
        self.project_info = ''
        self.about_info = ''
        self.build_info = ''


def author(self):
    """
    Возвращает информацию об авторе.
    :param self:
    :return:
    """
    return self.author_info


def project(self):
    """
    Возвращает информацию о проекте.
    :param self:
    :return:
    """
    return self.project_info


def about(self):
    """
    Возвращает информацию о программе.
    :param self:
    :return:
    """
    return self.about_info


def version(self):
    """
    Возвращает версию програмы.
    :param self:
    :return:
    """
    return self.project_info


def build(self):
    """
    Возвращает номер сборки програмы.
    :param self:
    :return:
    """
    return self.build_info
