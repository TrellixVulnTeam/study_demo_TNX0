# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题


**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~

>这是引用的内容

***

![图片alt](图片地址 ''图片title'')

图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加

[简书](http://jianshu.com)
[百度](http://baidu.com)

- 列表内容
+ 列表内容
* 列表内容

1.列表内容
2.列表内容
3.列表内容

注意：序号跟内容之间要有空格


表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

```python 
import os
print("this is a python code ")
```
|one|two|three|
|----|----|----|
|liyuan|haizeiwang|wocao|
|3123|fsdafsa|fsadf|


| 一个普通标题 | 一个普通标题 | 一个普通标题 |
| ----    | ----    | ----     |
| 短文本      | 中等文本     | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本    | 中等文本      |



-----
*****
----
#这是**一个**python代码
1. liyuan
2. dsafsa
3. dsafsadf


1. liyuan 
   - 111
   - 1212
   - dsafsad
2. 发生大幅度
   - 1212

|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |




表头|表头|表头
---|:--:|---:
![内容](BP.jpeg)|![内容](BP.jpeg)|![内容](BP.jpeg)
表头|表头|表头
![内容](BP.jpeg)|![内容](BP.jpeg)|![内容](BP.jpeg)
zheshiw afasdf asdf adsf sadf asdf |![内容](BP.jpeg)|![内容](BP.jpeg)

```echarts
{
    "title": {
        "text": "某站点用户访问来源", 
        "subtext": "纯属虚构", 
        "x": "center"
    }, 
    "tooltip": {
        "trigger": "item", 
        "formatter": "{a} <br/>{b} : {c} ({d}%)"
    }, 
    "legend": {
        "orient": "vertical", 
        "x": "left", 
        "data": [
            "直接访问", 
            "邮件营销", 
            "联盟广告", 
            "视频广告", 
            "搜索引擎"
        ]
    }, 
    "toolbox": {
        "show": true, 
        "feature": {
            "mark": {
                "show": true
            }, 
            "dataView": {
                "show": true, 
                "readOnly": false
            }, 
            "magicType": {
                "show": true, 
                "type": [
                    "pie", 
                    "funnel"
                ], 
                "option": {
                    "funnel": {
                        "x": "25%", 
                        "width": "50%", 
                        "funnelAlign": "left", 
                        "max": 1548
                    }
                }
            }, 
            "restore": {
                "show": true
            }, 
            "saveAsImage": {
                "show": true
            }
        }
    }, 
    "calculable": true, 
    "series": [
        {
            "name": "访问来源", 
            "type": "pie", 
            "radius": "55%", 
            "center": [
                "50%", 
                "60%"
            ], 
            "data": [
                {
                    "value": 335, 
                    "name": "直接访问"
                }, 
                {
                    "value": 310, 
                    "name": "邮件营销"
                }, 
                {
                    "value": 234, 
                    "name": "联盟广告"
                }, 
                {
                    "value": 135, 
                    "name": "视频广告"
                }, 
                {
                    "value": 1548, 
                    "name": "搜索引擎"
                }
            ]
        }
    ]
}


```