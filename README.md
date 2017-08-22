# 命令行英汉字典

**使用click模板创建的命令行程序**

新增加web应用版本，在`http://127.0.0.1/?q=`传入q参数即可以在浏览器看到翻译结果

## 使用方法

进入目录，使用命令`pip install --editable .`，把程序注册为命令行程序。

然后使用：

```shell
$ trans apple
查询: apple
结果: 苹果
解释: n. 苹果，苹果树，苹果似的东西；[美俚]炸弹，手榴弹，（棒球的）球；[美俚]人，家伙。
```

