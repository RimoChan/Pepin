# 同事批评器！

你是否有1些同事，明明已经到了下班时间，却还在写代码？

这种行为非常不好，带坏了公司风气以后大家都没有好果汁吃！

所以聪明的莉沫酱发明了同事批评器，可以找到哪些同事在下班以后偷偷上班，这样1来就可以把他们抓出来在周会狠狠地批评啦！


## 使用方法

首先你需要1个Python，然后把这个仓库clone回去。

先安装依赖:

```sh
pip install -r requirements.txt
```

然后就可以运行`pepin.py`，看看你的同事有没有在偷偷上班了，比如我们看看[云游君](https://github.com/YunYouJun)——

```text
yunyoujun 坏: 33/50
 0点|
 1点|
 2点|▇
 3点|
 4点|
 5点|
 6点|
 7点|▇▇▇▇▇▇▇▇▇▇
 8点|▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
 9点|
10点|
11点|
12点|
13点|▇▇▇▇▇▇▇▇▇▇
14点|
15点|
16点|▇
17点|▇▇▇▇▇▇▇▇▇▇▇▇
18点|▇▇▇▇▇▇▇▇▇▇▇▇
19点|
20点|
21点|
22点|▇
23点|▇
```

可以看出云游君经常在早上8点偷偷上班，太坏了，要抓起来好好地惩❤️罚！


## 原理

其实是用了GitHub的RSS feed功能！

这个feed流里是人的操作数据，比如我push代码之后，feed流里面就会多出1条「RimoChan pushed to 分支的名字 in 仓库的名字」，因此只要读这个feed就知道他每个操作的时间啦。

不过star的操作也会混在里面，如果不想看的话可以用手把它们过滤掉。

哦，还有就是，如果那个人是在private仓库里push的，feed里面就看不到了。


## 结束

就这样，我要去惩❤️罚小云了，大家88！
