# learn-python

2014/2015年第2学期《Python语言与算法》课程的编程作业仓库，祝同学们学习愉快，愿2015是我们进步的一年^_^<br>

一段简单的hello world，走起!
```python
#没有比这个更简单的Hello World程序了~~~~
print 'hello world'
```

----------

###以后布置作业都会在这个页面更新，请同学们实时关注哟~

```python
#2015/03/20 周五5,6节 尔雅208 课堂PPT的62页:练习(2)

#提示用户输入相关信息
xuehao=raw_input('请输入学号:')
name=raw_input('请输入姓名:')
age=input('请输入年龄:')
gs=input('请输入高数成绩:')
yy=input('请输入英语成绩:')
zz=input('请输入政治成绩:')

#计算加权平均分(高数60%,英语30%,政治10%)
jq=gs*0.6 + yy*0.3 + zz*0.1

#打印所有的信息
print '学号:',xuehao, '姓名:', name, '年龄:', age
print '高数:',gs, '英语:',yy, '政治:',zz
print '加权平均分:', jq

'''
说明
(1)"#"号开头的一行表示注释,这一行代码不会执行,注释是为了便于我们理解代码要做什么,同学们忽略即可
(2)如果要输入字符串信息,请使用raw_input()函数,如果要输入与数相关的信息,请使用input()函数
(3)请同学们照着敲一遍代码吧~~~
'''

```

----------

首先要向各位同学宣布几个不幸的消息：
 > 1. 这门课程是第一次开设；
 > 2. 这门课程会布置一定量的编程作业；
 > 3. 这门课程要求同学们编写代码；
 > 4. 这门课程要求同学们用[Github][19]交作业；
 > 5. 这门课程不会在课堂上讲授如何使用[Github][19]；
 > 6. 这门课程的综合训练项目要求同学们合作完成；
 > 7. 综合训练项目要求用[Markdown][20]语法编写文档；
 > 8. 抛弃***Word***、抛弃***QQ***、抛弃***邮箱***，使用[Github][19]交流!
 
注1：某位老师喜欢追逐时髦技术，所以通风14级的2个班不幸成为了首块试验田`(*∩_∩*)′<br>
注2：使用Github的Fork+Pull-Request模式可以看出同学们是否自己写代码，相当给力Y(^o^)Y~<br>
注3：有些同学不加思考的抄袭是老师们心中的痛啊→_→ <br>
注4：努力学习吧，抱怨是解决不了问题滴~<br>

----------

下面列出了一些Git/Github/Markdown的参考教程，同学们努力学习哦，现在只能靠自己啦~<br>
1、不用全部看完，只要大致掌握下面的几个知识点就能开工干活啦<br>
> * 注册Github账号，生成SSH公钥和密钥
> * Github创建仓库/Fork仓库
> * Clone仓库到本地(git clone)
> * 新建/删除/切换分支(git branch / git checkout)
> * 修改/提交(git add / git commit / git gui)
> * 推送(git push)和更新(git pull)
> * Fork + Pull-Request的使用方法

2、学习技术不要像学数学语文那样一字一字的读，要学会快速阅读，多动手实践，写的次数多了自然就会了<br>
3、信息大爆炸时代学会用搜索引擎查资料是必备的技能啊<br>
|| [百度][21]  ||  [必应][22]  ||  [Google][23] ||

4：***Google***已死，请学会[科学上网][24]


----------
##基本电脑常识
- [win7电脑怎样修改环境变量][26]
- [win7系统中如何使文件显示出扩展名][27]

##使用Github的缘由
- [有效提升大學生競爭力 -- 用 Git Pull Request 收作業][17]
- [国内有哪些大学使用GitHub Education？][18]

##Windows版本的Git安装程序
- [msysgit][31]

## 一、Github入门教程
- [手把手教你最简单的开源项目托管GitHub入门教程][1]
- [github简单使用教程][14]
- [windows下使用git及github仓库管理项目 入门][30]
- [git使用简易指南][28]
- [写给Git初学者的7个建议][29]
- 
##二、Git进阶教程
 - [《廖雪峰git教程》][2]
 - [《Pro Git》中文版][3]

##三、Github的Fork与Pull-Request教程
- [【视频】github 上 fork 和 pull request 的工作流][5]
- [如何在github上fork一个项目来贡献代码以及同步原作者的修改][4]
- [在Github和Git上fork之简单指南][6]
- [GitHub将Fork来的Project合并到原Project - Folk和Pull Request模式][7]
- [使用GitHub][8]
- [如何在GitHub上协作开发开源项目？][13]
- [GotGitHub][15]
- [如何向开源社区提问题][16]

##四、Markdown在线编辑器
- [Cmd Makrdown编辑器][12]

##五、Markdown入门教程
- [Markdown快速入门][9]
- [Markdown教程][10]
- [Markdown入门][11]
- [一个叫阳志平写的Github与Markdown博客文章][25]
----------
[1]:http://jingyan.baidu.com/article/f7ff0bfc7181492e27bb1360.html
[2]:http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000
[3]:http://git.oschina.net/progit/index.html
[4]:http://www.360doc.com/content/13/0410/18/2569758_277424931.shtml
[5]:http://happycasts.net/episodes/37
[6]:http://linux.cn/article-4292-1-rss.html
[7]:http://www.tuicool.com/articles/ZnERVn
[8]:http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137628548491051ccfaef0ccb470894c858999603fedf000
[9]:http://www.oschina.net/question/100267_75314
[10]:http://www.markdown.cn
[11]:http://www.360doc.com/content/13/1119/13/3300331_330476656.shtml
[12]:https://www.zybuluo.com/mdeditor
[13]:http://www.tuicool.com/articles/eE7bE3
[14]:http://wuyuans.com/2012/05/github-simple-tutorial/
[15]:http://www.worldhello.net/gotgithub/index.html
[16]:https://github.com/seajs/seajs/issues/545
[17]:http://blog.xdite.net/posts/2014/06/18/git-pull-request-homework/
[18]:http://www.zhihu.com/question/25849130
[19]:https://github.com/
[20]:https://www.zybuluo.com/mdeditor
[21]:http://www.baidu.com/
[22]:http://http://cn.bing.com/
[23]:http://www.google.com.hk/
[24]:https://www.baidu.com/s?wd=%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91&rsv_spt=1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=2&rsv_sug1=2&rsv_sug2=0&inputT=2661&rsv_sug4=2661
[25]:http://site.douban.com/196781/widget/notes/12161495/note/264946576/
[26]:http://jingyan.baidu.com/article/b24f6c82cba6dc86bfe5da9f.html
[27]:http://jingyan.baidu.com/article/9080802281e294fd91c80fe4.html
[28]:http://www.bootcss.com/p/git-guide/
[29]:http://blog.jobbole.com/50603/
[30]:http://blog.sina.com.cn/s/blog_700aa8830101kdp3.html
[31]:http://msysgit.github.io/

----------

##附录：msysgit中文乱码问题解决方法<br>
###[git初始设置]<br>
安装完git之后的**第一件事**就是设置user和email<br>
打开git bash<br>
git config --global user.name xxx<br>
git config --global user.email xxx@xxx.com<br>

###[msysgit中文乱码问题]<br>
假设git安装目录：$Git_Root=C:\develop\Tool\Git<br>
则git的所有配置文件都在$Git_Root\etc路径下<br>
**1、修改inputrc**<br>
set meta-flag on<br>
set input-meta on<br>
set output-meta on<br>
set convert-meta off<br>
**2、修改gitconfig**<br>
添加<br>
[core]<br>
autoctrlf = true<br>
删除<br>
[i18n]<br>
**3、修改git-completion.bash**<br>
末尾添加<br>
alias ls='ls --show-control-chars --color=auto'<br>
**4、修改profile**<br>
按Ctrl+f搜索utf-8<br>
export LESSCHARSET=utf-8<br>
**5、Git Gui中查看UTF-8编码的文本文件时乱码**
在Bash提示符下输入：git config --global gui.encoding utf-8<br>

注：通过上述设置，UTF-8编码的文本文件可以正常查看，但是GBK编码的文件将会乱码，所以还是没有从根本上解决问题。可行的方法之一为：将所有文本文件的编码统一为UTF-8
