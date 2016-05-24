外网一键改ip QQ群：490342664

软件仅适用于已经开外网成功的小伙伴便捷修改两个目录下的外网ip使用

测试阶段，欢迎大家试试效果。

建议大家先备份一下自己的cfg文件

该软件不能直接开外网！！！
该软件不能直接开外网！！！
该软件不能直接开外网！！！

所有命令都不用敲引号！！！

1.将 onekey.py 用winscp传到虚拟机 到哪里都行
	比如说我放到 /root 目录下，那我就敲命令 “cd /root” 切换到当前目录

2.执行  "chmod 777 onekey.py"

3.onekey.py 里面的两个路径 修改为 你虚拟机存着公网ip的cfg的两个目录(都开外网了，不会不知道路径是啥吧？)
	可以用winscp改，在第7/8行，标识的很明显
	万万不能填错，填错了的话程序会出错
	vbox的单库端是/home/neople/channel/cfg 和 /home/neople/game/cfg

	填好之后，长这样

	# 修改下方文件路径！！！ 仅仅修改双引号之间的内容！！！
	path1 = r"/home/neople/channel/cfg"
	path2 = r"/home/neople/game/cfg"
	# 修改上方文件路径！！！ 仅仅修改双引号之间的内容！！！

4.然后将 这两个目录下 所有的有公网ip的cfg文件 要填写公网ip的地方改为 "0.0.0.0"（没有引号）
	比如说我的 /home/neople/channel/cfg 目录下的 channle.cfg

	[server]
	max_client = 1000
	this_ip = 110.111.111.192
	this_tcp_port = 7001
	this_udp_port = 7001
	bridge_ip = 192.168.56.10
	bridge_port = 7000
	id = 3

	只要是公网ip的地方 就改成 0.0.0.0
	改成了下面的样子
	[server]
	max_client = 1000
	this_ip = 0.0.0.0
	this_tcp_port = 7001
	this_udp_port = 7001
	bridge_ip = 192.168.56.10
	bridge_port = 7000
	id = 3

	有外网ip的所有文件都需要修改，没有外网ip的文件就不用改

5.使用“./onekey.py bak” 初始化程序

6.以后仅需使用
cd /root
./onekey.py
就可以替换公网ip了
