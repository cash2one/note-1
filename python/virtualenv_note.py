# -*- coding: utf-8 -*-

"""virtualenv 使用"""


# 创建虚拟环境

virtualenv [venv]

virtualenv [venv] --no-site-packages

# 进入虚拟环境

source venv/bin/activate

# 退出虚拟环境

deactivate

# 删除虚拟环境

rm -r venv

