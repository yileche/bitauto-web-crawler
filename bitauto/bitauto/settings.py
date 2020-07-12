# -*- coding: utf-8 -*-

# Scrapy settings for bitauto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bitauto'

SPIDER_MODULES = ['bitauto.spiders']
NEWSPIDER_MODULE = 'bitauto.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bitauto (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   # 'Accept-Language': 'en',
   # 'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bitauto.middlewares.BitautoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'bitauto.middlewares.BitautoDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#      'bitauto.pipelines.CsvPipeline': 300,
#  } 有bug：导出不了列名

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MONGODB 主机环回地址127.0.0.1
# MONGODB_HOST = 'localhost'
# 端口号，默认是27017
# MONGODB_PORT = 27017
# 设置数据库名称
# MONGODB_DBNAME = 'data3'
# 存放本次数据的表名称
# MONGODB_DOCNAME = 'version7'

FEED_EXPORTERS = {
    'csv': 'bitauto.spiders.csv_item_exporter.MyProjectCsvItemExporter',
}

FIELDS_TO_EXPORT = [
    'brand',
    'brandmodel',
    'url',
    'version',
    'price',
    'year',
    'marketyear',
    'marketmonth',
    'marketday',
    'zaichan',
    'zaixiao',
    'bodytype',
    'modellevel',
    'powertype',
    'fuelconsumption',
    'jiasushijian',
    'maximumspeed',
    'huanbao',
    'baoxiuzhengce',
    'color',
    'fadongjipailie',
    'gangshu',
    'zuidaxuhanglicheng',
    'dianchichongdianman',
    'dianchichongdiankuai',
    'dianchibaoxiu',
    'butie',
    'clength',
    'cwidth',
    'cheight',
    'wheelbase',
    'quaility',
    'seats',
    'xinglixiangrongjimin',
    'xinglixiangrongjimax',
    'youxiang',
    'qianluntai',
    'houluntai',
    'beitai',
    'zuixiaozhuanwanzhijing',
    'lidijianxi',
    'aspiration',
    'displacement',
    'maximumpower',
    'zuidamali',
    'zuidagonglvrpm',
    'maximumtorque',
    'zuidaniujurpm',
    'gongyou',
    'ranyou',
    'fadongjiqiting',
    'gearboxtype',
    'gears',
    'diandongjikw',
    'diandongjiniuju',
    'houdiandongjikw',
    'houdiandongjinm',
    'dianchirongliang',
    'haodianliang',
    'xitongzonghekw',
    'xitongzonghenm',
    'drivemode',
    'frontsuspensiontype',
    'rearsuspensiontype',
    'ketiaoxuanjia',
    'qianlunzhidong',
    'houlunzhidong',
    'zhuchezhidong',
    'carbodystructure',
    'chasusuo',
    'jiejinjiao',
    'liqujiao',
    'zuidasheshuishendu',
    'tongguojiao',
    'abs',
    'ebd',
    'eba',
    'ars',
    'esp',
    'zhuqinang',
    'fuqinang',
    'qianqinang',
    'houqinang',
    'ceqilian',
    'xiqinang',
    'anquandai',
    'houpaiqinang',
    'taiya',
    'lingtaiya',
    'ertongzuo',
    'dingsu',
    'chedao',
    'pengzhuang',
    'pilao',
    'automaticparking',
    'yaokong',
    'automaticdrivingassitance',
    'zhuche',
    'shangpo',
    'doupo',
    'yeshi',
    'kebianchibi',
    'qianleida',
    'houleida',
    'daocheyingxiang',
    'jiashimoshi',
    'bingxianfuzhu',
    'qiandadeng',
    'led',
    'zidongdadeng',
    'qianwudeng',
    'dadeng',
    'tianchuang',
    'qianchechuang',
    'houchechuang',
    'waihoushijing',
    'neihoushijing',
    'liumeiti',
    'waihoushijingxuanmu',
    'yinsi',
    'houpai',
    'houzheyang',
    'qianyushua',
    'houyushua',
    'dianximen',
    'diandongcehua',
    'diandongxingli',
    'chedingxinglijia',
    'zhongkongsuo',
    'zhinengyaoshi',
    'yuanchengyaokong',
    'weiyi',
    'yundongwaiguan',
    'neishi',
    'fenweideng',
    'zheyangban',
    'fangxiangpan',
    'duogongnengfxp',
    'fxptiaojie',
    'fxpjiare',
    'fxphuandang',
    'qianpaikongtiao',
    'houpaikongtiao',
    'xiangfen',
    'kongqijinghua',
    'chezaibingxiang',
    'zhudongjiangzao',
    'zuoyicaizhi',
    'yundongfenggezuoyi',
    'zhuzuoyi',
    'fuzuoyi',
    'zhutiaojie',
    'futiaojie',
    'dierpai1',
    'dierpai2',
    'qianpaizuoyi',
    'houpaizuoyi',
    'qianpaizhongyang',
    'houpaizhongyang',
    'disanpai',
    'zuoyifangdao',
    'houpaibeijia',
    'houpaizhedie',
    'zhongkongcaise',
    'yejingping',
    'quanyejing',
    'xingchediannao',
    'hud',
    'gps',
    'zhinenghulian',
    'viocecontrol',
    'mobileinternet',
    'shoujiwuxian',
    'shoushikongzhi',
    'cd',
    'bluetoothwifi',
    'waijie',
    'chezaixingche',
    'chezaidianshi',
    'audiobrand',
    'yangshengqi',
    'houpaiyejingping',
    'chezai220'
]

# LOG_FILE = "log1.txt"  # log信息输出到log.txt文件
