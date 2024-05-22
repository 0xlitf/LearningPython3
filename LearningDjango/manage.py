#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# 项目的管理、启动项目、创建app、数据管理
# 创建的项目中可以有多个app，支持拆分成不同的功能，例如用户管理、订单管理、后台管理等等
# 每个app有独立的数据库表结构、函数、html模板、css，由各自app管理，但都在一个大项目之下

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from app_main.gui import run_gui_thread
    run_gui_thread()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    from django.core.management.commands.runserver import Command as Runserver

    Runserver.default_addr = '0.0.0.0'  # 修改默认地址
    Runserver.default_port = '8080'  # 修改默认端口
    
    main()
