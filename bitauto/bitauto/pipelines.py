from scrapy.conf import settings
import pymongo
from imp import reload
import os
import sys


# class MongoPipeline(object):
#     def __init__(self):
#         # 获取setting主机名、端口号和数据库名
#         host = settings['MONGODB_HOST']
#         port = settings['MONGODB_PORT']
#         dbname = settings['MONGODB_DBNAME']

        # pymongo.MongoClient(host, port) 创建MongoDB链接
#         client = pymongo.MongoClient(host=host, port=port)

#         # 指向指定的数据库
#         mdb = client[dbname]
#         # 获取数据库里存放数据的表名
#         self.post = mdb[settings['MONGODB_DOCNAME']]

#     def process_item(self, item, spider):
#         data = dict(item)
#         # 向指定的表里添加数据
#         self.post.insert(data)
#         return item
class CsvPipeline(object):
    '''保存到csv'''
    def process_item(self, item, spider):
        reload(sys)
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = '/Users/cheyile/PycharmProjects/SScrapy/bitauto/bitauto20171.csv'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item["brand"] + ",")
            f.write(item["brandmodel"] + ",")
            f.write(item["url"] + ",")
            f.write(item["version"] + ",")
            f.write(item["tingchan"] + ",")
            f.write(item["price"] + ",")
            f.write(item["year"] + ",")
            f.write(item["marketyear"] + ",")
            f.write(item["marketmonth"] + ",")
            f.write(item["marketday"] + ",")
            f.write(item["zaichan"] + ",")
            f.write(item["zaixiao"] + ",")
            f.write(item["bodytype"] + ",")
            f.write(item["modellevel"] + ",")
            f.write(item["powertype"] + ",")
            f.write(item["fuelconsumption"] + ",")
            f.write(item["jiasushijian"] + ",")
            f.write(item["maximumspeed"] + ",")
            f.write(item["huanbao"] + ",")
            f.write(item["baoxiuzhengce"] + ",")
            f.write(item["color"] + ",")
            f.write(item["fadongjipailie"] + ",")
            f.write(item["gangshu"] + ",")
            f.write(item["zuidaxuhanglicheng"] + ",")
            f.write(item["dianchichongdianman"] + ",")
            f.write(item["dianchichongdiankuai"] + ",")
            f.write(item["dianchibaoxiu"] + ",")
            f.write(item["butie"] + ",")
            f.write(item["clength"] + ",")
            f.write(item["cwidth"] + ",")
            f.write(item["cheight"] + ",")
            f.write(item["wheelbase"] + ",")
            f.write(item["quaility"] + ",")
            f.write(item["seats"] + ",")
            f.write(item["xinglixiangrongjimin"] + ",")
            f.write(item["xinglixiangrongjimax"] + ",")
            f.write(item["youxiang"] + ",")
            f.write(item["qianluntai"] + ",")
            f.write(item["houluntai"] + ",")
            f.write(item["beitai"] + ",")
            f.write(item["zuixiaozhuanwanzhijing"] + ",")
            f.write(item["lidijianxi"] + ",")
            f.write(item["aspiration"] + ",")
            f.write(item["displacement"] + ",")
            f.write(item["maximumpower"] + ",")
            f.write(item["zuidamali"] + ",")
            f.write(item["zuidagonglvrpm"] + ",")
            f.write(item["maximumtorque"] + ",")
            f.write(item["zuidaniujurpm"] + ",")
            f.write(item["gongyou"] + ",")
            f.write(item["ranyou"] + ",")
            f.write(item["fadongjiqiting"] + ",")
            f.write(item["gearboxtype"] + ",")
            f.write(item["gears"] + ",")
            f.write(item["diandongjikw"] + ",")
            f.write(item["diandongjiniuju"] + ",")
            f.write(item["houdiandongjikw"] + ",")
            f.write(item["houdiandongjinm"] + ",")
            f.write(item["dianchirongliang"] + ",")
            f.write(item["haodianliang"] + ",")
            f.write(item["xitongzonghekw"] + ",")
            f.write(item["xitongzonghenm"] + ",")
            f.write(item["drivemode"] + ",")
            f.write(item["frontsuspensiontype"] + ",")
            f.write(item["rearsuspensiontype"] + ",")
            f.write(item["ketiaoxuanjia"] + ",")
            f.write(item["qianlunzhidong"] + ",")
            f.write(item["houlunzhidong"] + ",")
            f.write(item["zhuchezhidong"] + ",")
            f.write(item["carbodystructure"] + ",")
            f.write(item["chasusuo"] + ",")
            f.write(item["jiejinjiao"] + ",")
            f.write(item["liqujiao"] + ",")
            f.write(item["zuidasheshuishendu"] + ",")
            f.write(item["tongguojiao"] + ",")
            f.write(item["abs"] + ",")
            f.write(item["ebd"] + ",")
            f.write(item["eba"] + ",")
            f.write(item["ars"] + ",")
            f.write(item["esp"] + ",")
            f.write(item["zhuqinang"] + ",")
            f.write(item["fuqinang"] + ",")
            f.write(item["qianqinang"] + ",")
            f.write(item["houqinang"] + ",")
            f.write(item["ceqilian"] + ",")
            f.write(item["xiqinang"] + ",")
            f.write(item["anquandai"] + ",")
            f.write(item["houpaiqinang"] + ",")
            f.write(item["taiya"] + ",")
            f.write(item["lingtaiya"] + ",")
            f.write(item["ertongzuo"] + ",")
            f.write(item["dingsu"] + ",")
            f.write(item["chedao"] + ",")
            f.write(item["pengzhuang"] + ",")
            f.write(item["pilao"] + ",")
            f.write(item["automaticparking"] + ",")
            f.write(item["yaokong"] + ",")
            f.write(item["automaticdrivingassitance"] + ",")
            f.write(item["zhuche"] + ",")
            f.write(item["shangpo"] + ",")
            f.write(item["doupo"] + ",")
            f.write(item["yeshi"] + ",")
            f.write(item["kebianchibi"] + ",")
            f.write(item["qianleida"] + ",")
            f.write(item["houleida"] + ",")
            f.write(item["daocheyingxiang"] + ",")
            f.write(item["jiashimoshi"] + ",")
            f.write(item["bingxianfuzhu"] + ",")
            f.write(item["qiandadeng"] + ",")
            f.write(item["led"] + ",")
            f.write(item["zidongdadeng"] + ",")
            f.write(item["qianwudeng"] + ",")
            f.write(item["dadeng"] + ",")
            f.write(item["tianchuang"] + ",")
            f.write(item["qianchechuang"] + ",")
            f.write(item["houchechuang"] + ",")
            f.write(item["waihoushijing"] + ",")
            f.write(item["neihoushijing"] + ",")
            f.write(item["liumeiti"] + ",")
            f.write(item["waihoushijingxuanmu"] + ",")
            f.write(item["yinsi"] + ",")
            f.write(item["houpai"] + ",")
            f.write(item["houzheyang"] + ",")
            f.write(item["qianyushua"] + ",")
            f.write(item["houyushua"] + ",")
            f.write(item["dianximen"] + ",")
            f.write(item["diandongcehua"] + ",")
            f.write(item["diandongxingli"] + ",")
            f.write(item["chedingxinglijia"] + ",")
            f.write(item["zhongkongsuo"] + ",")
            f.write(item["zhinengyaoshi"] + ",")
            f.write(item["yuanchengyaokong"] + ",")
            f.write(item["weiyi"] + ",")
            f.write(item["yundongwaiguan"] + ",")
            f.write(item["neishi"] + ",")
            f.write(item["fenweideng"] + ",")
            f.write(item["zheyangban"] + ",")
            f.write(item["fangxiangpan"] + ",")
            f.write(item["duogongnengfxp"] + ",")
            f.write(item["fxptiaojie"] + ",")
            f.write(item["fxpjiare"] + ",")
            f.write(item["fxphuandang"] + ",")
            f.write(item["qianpaikongtiao"] + ",")
            f.write(item["houpaikongtiao"] + ",")
            f.write(item["xiangfen"] + ",")
            f.write(item["kongqijinghua"] + ",")
            f.write(item["chezaibingxiang"] + ",")
            f.write(item["zhudongjiangzao"] + ",")
            f.write(item["zuoyicaizhi"] + ",")
            f.write(item["yundongfenggezuoyi"] + ",")
            f.write(item["zhuzuoyi"] + ",")
            f.write(item["fuzuoyi"] + ",")
            f.write(item["zhutiaojie"] + ",")
            f.write(item["futiaojie"] + ",")
            f.write(item["dierpai1"] + ",")
            f.write(item["dierpai2"] + ",")
            f.write(item["qianpaizuoyi"] + ",")
            f.write(item["houpaizuoyi"] + ",")
            f.write(item["qianpaizhongyang"] + ",")
            f.write(item["houpaizhongyang"] + ",")
            f.write(item["disanpai"] + ",")
            f.write(item["zuoyifangdao"] + ",")
            f.write(item["houpaibeijia"] + ",")
            f.write(item["houpaizhedie"] + ",")
            f.write(item["zhongkongcaise"] + ",")
            f.write(item["yejingping"] + ",")
            f.write(item["quanyejing"] + ",")
            f.write(item["xingchediannao"] + ",")
            f.write(item["hud"] + ",")
            f.write(item["gps"] + ",")
            f.write(item["zhinenghulian"] + ",")
            f.write(item["viocecontrol"] + ",")
            f.write(item["mobileinternet"] + ",")
            f.write(item["shoujiwuxian"] + ",")
            f.write(item["shoushikongzhi"] + ",")
            f.write(item["cd"] + ",")
            f.write(item["bluetoothwifi"] + ",")
            f.write(item["waijie"] + ",")
            f.write(item["chezaixingche"] + ",")
            f.write(item["chezaidianshi"] + ",")
            f.write(item["audiobrand"] + ",")
            f.write(item["yangshengqi"] + ",")
            f.write(item["houpaiyejingping"] + ",")
            f.write(item["chezai220"] + "\n")
        return item
