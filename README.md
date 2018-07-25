# Dots-and-Boxes
[![PyPI version](https://img.shields.io/pypi/v/DotsAndBoxes.svg)](https://pypi.python.org/pypi/DotsAndBoxes)


### Dots-and-Boxes项目介绍

Dots-and-Boxes项目旨在使用Python语言编写一个简单易用扩展性强的点格棋对弈软件。本项目由[@EverybodyLies](https://github.com/Everyb0dyLies)开发维护。

本软件的一个分支是应中国大学生计算机博弈大赛组委会邀请，定制开发的官方打谱软件，本软件支持官方标准棋谱，并欢迎开发者接入自有AI或二次定制开发。参加中国大学生计算机博弈大赛可以在符合本软件开源许可协议及大赛规则的情况下使用本软件全部或部分代码，也可以不使用本软件。


### DotsAndBoxes点格棋对弈软件

DotsAndBoxes是一个点格棋博弈软件，可用于人人对战，人机对战和机机对战功能。

用户运行软件后，要先通过“工具-设置红方/蓝方玩家”，来添加红方和蓝方玩家（目前尚无法在图形界面选择AI，请通过代码指定AI，后期将更新选择功能），之后从“文件-新游戏”创建游戏，左侧是棋盘，右侧分别显示当前玩家、当前步数、得分和历史信息，通过双击历史信息，可以跳转到特定步。在跳转到某一步后，如果不更改落子，则历史信息不会变化，如果用户更改落子位置，则历史信息被删除并添加新的落子位置。用户可以随时保存游戏，在游戏没有开始或者结束后可以加载之前保存的游戏。

软件具有载入和导出大学生计算机博弈大赛点格棋标准棋谱文件

程序使用py3实现点格棋对弈基础功能，并使用pyqt5构建了人机交互界面。

##### 安装方法
pip3 install DotsAndBoxes

##### 运行环境要求：
Python3

##### UI界面适配
Windows 10；Ubuntu Desktop 1604


### 感谢

非常感谢以下两位学长的帮助与指导

[@yimmon](https://github.com/yimmon)，他开发了一个非常厉害的点格棋AI（[dots-and-boxes](https://github.com/yimmon/dots-and-boxes)）

[@zhangyp]()


### License

[Dots-and-Boxes is licensed under the MIT License](https://github.com/Everyb0dyLies/Dots-and-Boxes/blob/master/LICENSE)

重申本代码仅用于实验和学习，使用者的一切商业行为及非法行为皆由其本人承担责任。
