
搜索历史命令的快捷键:ctrl + r
它是通过关键字去匹配历史记录,执行后会提示:(reverse-i-search)
输入你记得的关键字去匹配,如果出现你需要的命令,按Enter就可以选择命令;如果不是请输入更精确的关键字去匹配


移动操作快捷键

Ctrl + f-- 向右移动一个字符，当然多数人用→
Ctrl + b-- 向左移动一个字符， 多数人用←
ESC + f-- 向右移动一个单词，MAC下建议用ALT + →
ESC + b-- 向左移动一个单词，MAC下建议用ALT + ←
Ctrl + a-- 跳到行首
Ctrl + e-- 跳到行尾

删除操作快捷键

Ctrl + d-- 向右删除一个字符
Ctrl + h-- 向左删除一个字符
Ctrl + u-- 删除当前位置字符至行首（输入密码错误的时候多用下这个）
Ctrl + k-- 删除当前位置字符至行尾
Ctrl + w-- 删除从光标到当前单词开头

命令切换操作快捷键

Ctrl + p-- 上一个命令，也可以用↑
Ctrl + n-- 下一个命令，也可以用↓

其他操作快捷键

Ctrl + y-- 插入最近删除的单词
Ctrl + c-- 终止操作
Ctrl + d-- 当前操作转到后台
Ctrl + l-- 清屏


先总结几个个人觉得最有用的

ctrl + ? 撤消前一次输入

ctrl + c 另起一行

ctrl + r 输入单词搜索历史命令

ctrl + u 删除光标前面所有字符相当于VIM里d shift+^

ctrl + k 删除光标后面所有字符相当于VIM里d shift+$

删除
ctrl + d 删除光标所在位置上的字符相当于VIM里x或者dl
ctrl + h 删除光标所在位置前的字符相当于VIM里hx或者dh
ctrl + k 删除光标后面所有字符相当于VIM里d shift+$
ctrl + u 删除光标前面所有字符相当于VIM里d shift+^
ctrl + w 删除光标前一个单词相当于VIM里db
ctrl + y 恢复ctrl+u上次执行时删除的字符
ctrl + ? 撤消前一次输入
alt + r 撤消前一次动作
alt + d 删除光标所在位置的后单词

移动
ctrl + a 将光标移动到命令行开头相当于VIM里shift+^
ctrl + e 将光标移动到命令行结尾处相当于VIM里shift+$
ctrl + f 光标向后移动一个字符相当于VIM里l
ctrl + b 光标向前移动一个字符相当于VIM里h
ctrl + 方向键左键 光标移动到前一个单词开头
ctrl + 方向键右键 光标移动到后一个单词结尾
ctrl + x 在上次光标所在字符和当前光标所在字符之间跳转
alt + f 跳到光标所在位置单词尾部

替换
ctrl + t 将光标当前字符与前面一个字符替换
alt + t 交换两个光标当前所处位置单词和光标前一个单词
alt + u 把光标当前位置单词变为大写
alt + l 把光标当前位置单词变为小写
alt + c 把光标当前位置单词头一个字母变为大写
^oldstr^newstr 替换前一次命令中字符串

历史命令编辑
ctrl + p 返回上一次输入命令字符
ctrl + r 输入单词搜索历史命令
alt + p 输入字符查找与字符相接近的历史命令
alt + > 返回上一次执行命令

其它
ctrl + s 锁住终端
ctrl + q 解锁终端
ctrl + l 清屏相当于命令clear
ctrl + c 另起一行
ctrl + i 类似TAB健补全功能
ctrl + o 重复执行命令
alt + 数字键 操作的次数候为了好看）