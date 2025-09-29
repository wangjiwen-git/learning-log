import os
from .settings import *  # 导入所有原有设置

# 覆盖原有设置
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# 数据库配置：使用PythonAnywhere提供的MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$learning_log',  # 数据库名，后面在PA面板里创建
        'USER': 'yourusername',               # 你的PA用户名
        'PASSWORD': 'your_mysql_password',    # 你的PA数据库密码（稍后设置）
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# 静态文件根目录
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')