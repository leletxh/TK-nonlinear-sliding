# TK非线性滑动

[进入GitHub仓库](https://github.com/leletxh/TK-nonlinear-sliding)

## 1 调用方法

你可以调用以下命令使用

```python
#引入包
import tkns
#调用
move(currently_x,currently_y,to_x,to_y,n,win,debug = False,sleep = 0.01,wait_on_startup = True)
```
## 2 参数介绍

```python

move(
    currently_x,  #组件X坐标
    currently_y,  #组件y坐标
    to_x,  #要前往的X坐标
    to_y,  #要前往的Y坐标
    n,  #要前往的组将
    win,  #窗口需要刷新刷新
    debug=False,  #调试模式，显示移动坐标数据
    sleep=0.01,  #等待时间，与动画速度有关
    wait_on_startup=True,  #启动时等待0.5秒，以免在程序开启时出现错误
)
#暂无返回值
```

[有个彩蛋](https://autopatchcn.yuanshen.com/client_app/download/launcher/20240513153024_R4Y2Siji8AadjI0Q/mihoyo/yuanshen_setup_202405121226.exe)

