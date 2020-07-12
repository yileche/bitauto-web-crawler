# -*- coding: utf-8 -*-
# coding=gbk
import scrapy
import re
from bitauto.items import BitautoCarItem


# json_str = '''
# JsonpCallBack({char:{A:1,B:1,C:1,D:1,E:0,F:1,G:1,H:1,I:0,J:1,K:1,L:1,M:1,N:1,O:1,P:1,Q:1,R:1,S:1,T:1,U:0,V:0,W:1,X:1,Y:1,Z:1},brand:{A:[{type:"mb",activity:{"bsId":9,"tagName":"免税季"},id:9,name:"奥迪",url:"/mb9/",cur:0,num:48957},{type:"mb",activity:null,id:92,name:"阿尔法·罗密欧",url:"/mb92/",cur:0,num:232},{type:"mb",activity:null,id:97,name:"阿斯顿·马丁",url:"/mb97/",cur:0,num:122},{type:"mb",activity:null,id:268,name:"ALPINA",url:"/mb268/",cur:0,num:0},{type:"mb",activity:null,id:289,name:"ARCFOX",url:"/mb289/",cur:0,num:106}],B:[{type:"mb",activity:{"bsId":157,"tagName":"免税季"},id:157,name:"宝骏",url:"/mb157/",cur:0,num:36448},{type:"mb",activity:{"bsId":3,"tagName":"免税季"},id:3,name:"宝马",url:"/mb3/",cur:0,num:73855},{type:"mb",id:2,name:"奔驰",url:"/mb2/",cur:1,num:84588,child:[{type:"cb",name:"北京奔驰",url:"/b10075/",cur:0,num:28161,child:[{type:"cs",name:"C级",url:"/nb2364/",num:7330,cur:0},{type:"cs",name:"E级",url:"/nb1987/",num:11228,cur:0},{type:"cs",name:"GLA级",url:"/nb4477/",num:4653,cur:0},{type:"cs",name:"GLC级",url:"/nb4597/",num:4950,cur:0},{type:"cs",name:"A级三厢",url:"/nb5381/",num:0,cur:0}]},{type:"cb",name:"福建奔驰",url:"/b20163/",cur:0,num:3494,child:[{type:"cs",name:"V级",url:"/nb4138/",num:866,cur:0},{type:"cs",name:"威霆",url:"/nb3038/",num:455,cur:0},{type:"cs",name:"凌特",url:"/nb3542/",num:2173,cur:0}]},{type:"cb",name:"进口奔驰",url:"/b20007/",cur:0,num:44338,child:[{type:"cs",name:"A级",url:"/nb2564/",num:3058,cur:0},{type:"cs",name:"B级",url:"/nb2616/",num:3106,cur:0},{type:"cs",name:"C级",url:"/nb2257/",num:3161,cur:0},{type:"cs",name:"E级",url:"/nb2765/",num:3662,cur:0},{type:"cs",name:"S级",url:"/nb2259/",num:5011,cur:0},{type:"cs",name:"CLA级",url:"/nb3673/",num:4914,cur:0},{type:"cs",name:"CLS级",url:"/nb2261/",num:2853,cur:0},{type:"cs",name:"GLC级",url:"/nb4496/",num:2739,cur:0},{type:"cs",name:"GLE级",url:"/nb4401/",num:6695,cur:0},{type:"cs",name:"GLS级",url:"/nb4662/",num:4477,cur:0},{type:"cs",name:"G级",url:"/nb2356/",num:1198,cur:0},{type:"cs",name:"R级",url:"/nb1877/",num:1111,cur:0},{type:"cs",name:"SLC级",url:"/nb4770/",num:1777,cur:0},{type:"cs",name:"SL级",url:"/nb2262/",num:576,cur:0},{type:"cs",name:"X级",url:"/nb5162/",num:0,cur:0}]},{type:"cb",name:"进口奔驰新能源",url:"/b20339/",cur:0,num:36,child:[{type:"cs",name:"GLE级 插电混动",url:"/nb5291/",num:17,cur:0},{type:"cs",name:"S级 插电混动",url:"/nb5148/",num:19,cur:0}]},{type:"cb",name:"进口梅赛德斯-迈巴赫",url:"/b20256/",cur:0,num:422,child:[{type:"cs",name:"迈巴赫S级",url:"/nb4373/",num:422,cur:0}]},{type:"cb",name:"进口梅赛德斯-AMG",url:"/b20217/",cur:0,num:8137,child:[{type:"cs",name:"AMG A级",url:"/nb3984/",num:219,cur:0},{type:"cs",name:"AMG C级",url:"/nb3975/",num:987,cur:0},{type:"cs",name:"AMG E级",url:"/nb3983/",num:389,cur:0},{type:"cs",name:"AMG S级",url:"/nb3981/",num:797,cur:0},{type:"cs",name:"AMG CLA级",url:"/nb3985/",num:222,cur:0},{type:"cs",name:"AMG CLS级",url:"/nb3974/",num:373,cur:0},{type:"cs",name:"AMG GLA级",url:"/nb4104/",num:221,cur:0},{type:"cs",name:"AMG GLC级",url:"/nb4755/",num:1521,cur:0},{type:"cs",name:"AMG GLE级",url:"/nb4426/",num:1240,cur:0},{type:"cs",name:"AMG GLS级",url:"/nb4663/",num:208,cur:0},{type:"cs",name:"AMG G级",url:"/nb3976/",num:972,cur:0},{type:"cs",name:"AMG GT",url:"/nb4319/",num:988,cur:0}]}]},{type:"mb",activity:{"bsId":26,"tagName":"免税季"},id:26,name:"本田",url:"/mb26/",cur:0,num:62689},{type:"mb",activity:null,id:127,name:"别克",url:"/mb127/",cur:0,num:56769},{type:"mb",activity:null,id:5,name:"标致",url:"/mb5/",cur:0,num:16125},{type:"mb",activity:{"bsId":15,"tagName":"免税季"},id:15,name:"比亚迪",url:"/mb15/",cur:0,num:42789},{type:"mb",activity:{"bsId":82,"tagName":"免税季"},id:82,name:"保时捷",url:"/mb82/",cur:0,num:7121},{type:"mb",activity:null,id:236,name:"宝沃",url:"/mb236/",cur:0,num:5091},{type:"mb",activity:{"bsId":59,"tagName":"免税季"},id:59,name:"奔腾",url:"/mb59/",cur:0,num:17236},{type:"mb",activity:null,id:263,name:"比速",url:"/mb263/",cur:0,num:2924},{type:"mb",activity:null,id:195,name:"北汽绅宝",url:"/mb195/",cur:0,num:8457},{type:"mb",activity:null,id:211,name:"北汽幻速",url:"/mb211/",cur:0,num:13225},{type:"mb",activity:null,id:168,name:"北汽威旺",url:"/mb168/",cur:0,num:7119},{type:"mb",activity:null,id:129,name:"北汽昌河",url:"/mb129/",cur:0,num:7696},{type:"mb",activity:null,id:14,name:"北汽制造",url:"/mb14/",cur:0,num:722},{type:"mb",activity:null,id:282,name:"北汽道达",url:"/mb282/",cur:0,num:0},{type:"mb",activity:{"bsId":216,"tagName":"免税季"},id:216,name:"北汽新能源",url:"/mb216/",cur:0,num:1600},{type:"mb",activity:null,id:163,name:"北京",url:"/mb163/",cur:0,num:6721},{type:"mb",activity:{"bsId":85,"tagName":"免税季"},id:85,name:"宾利",url:"/mb85/",cur:0,num:424}],C:[{type:"mb",activity:null,id:136,name:"长安汽车",url:"/mb136/",cur:0,num:75915},{type:"mb",activity:null,id:159,name:"长安欧尚",url:"/mb159/",cur:0,num:25763},{type:"mb",activity:null,id:281,name:"长安轻型车",url:"/mb281/",cur:0,num:1871},{type:"mb",activity:null,id:283,name:"长安跨越",url:"/mb283/",cur:0,num:6481},{type:"mb",activity:null,id:21,name:"长城",url:"/mb21/",cur:0,num:16364}],D:[{type:"mb",activity:{"bsId":8,"tagName":"免税季"},id:8,name:"大众",url:"/mb8/",cur:0,num:224616},{type:"mb",activity:{"bsId":197,"tagName":"免税季"},id:197,name:"东风风度",url:"/mb197/",cur:0,num:1291},{type:"mb",activity:null,id:253,name:"东风风光",url:"/mb253/",cur:0,num:9742},{type:"mb",activity:null,id:141,name:"东风风神",url:"/mb141/",cur:0,num:9570},{type:"mb",activity:null,id:115,name:"东风风行",url:"/mb115/",cur:0,num:32759},{type:"mb",activity:null,id:205,name:"东风小康",url:"/mb205/",cur:0,num:7895},{type:"mb",activity:null,id:27,name:"东风",url:"/mb27/",cur:0,num:5606},{type:"mb",activity:{"bsId":29,"tagName":"免税季"},id:29,name:"东南",url:"/mb29/",cur:0,num:9365},{type:"mb",activity:null,id:113,name:"道奇",url:"/mb113/",cur:0,num:556},{type:"mb",activity:{"bsId":179,"tagName":"免税季"},id:179,name:"DS",url:"/mb179/",cur:0,num:1464},{type:"mb",activity:null,id:294,name:"电咖",url:"/mb294/",cur:0,num:0}],F:[{type:"mb",activity:{"bsId":7,"tagName":"免税季"},id:7,name:"丰田",url:"/mb7/",cur:0,num:77864},{type:"mb",activity:{"bsId":17,"tagName":"免税季"},id:17,name:"福特",url:"/mb17/",cur:0,num:64624},{type:"mb",activity:null,id:40,name:"菲亚特",url:"/mb40/",cur:0,num:1129},{type:"mb",activity:null,id:91,name:"法拉利",url:"/mb91/",cur:0,num:58},{type:"mb",activity:null,id:67,name:"福迪",url:"/mb67/",cur:0,num:1158},{type:"mb",activity:null,id:208,name:"福汽启腾",url:"/mb208/",cur:0,num:140},{type:"mb",activity:null,id:128,name:"福田",url:"/mb128/",cur:0,num:24591},{type:"mb",activity:null,id:257,name:"Faraday Future",url:"/mb257/",cur:0,num:0}],G:[{type:"mb",activity:{"bsId":147,"tagName":"免税季"},id:147,name:"广汽传祺",url:"/mb147/",cur:0,num:43465},{type:"mb",activity:{"bsId":295,"tagName":"免税季"},id:295,name:"广汽新能源",url:"/mb295/",cur:0,num:413},{type:"mb",activity:{"bsId":182,"tagName":"免税季"},id:182,name:"观致",url:"/mb182/",cur:0,num:1581},{type:"mb",activity:null,id:290,name:"国金",url:"/mb290/",cur:0,num:0},{type:"mb",activity:null,id:109,name:"GMC",url:"/mb109/",cur:0,num:370}],H:[{type:"mb",activity:null,id:196,name:"哈弗",url:"/mb196/",cur:0,num:58194},{type:"mb",activity:null,id:32,name:"海马",url:"/mb32/",cur:0,num:8368},{type:"mb",activity:null,id:259,name:"汉腾",url:"/mb259/",cur:0,num:5788},{type:"mb",activity:{"bsId":58,"tagName":"免税季"},id:58,name:"红旗",url:"/mb58/",cur:0,num:1245},{type:"mb",activity:null,id:112,name:"华泰",url:"/mb112/",cur:0,num:306},{type:"mb",activity:null,id:302,name:"红星汽车",url:"/mb302/",cur:0,num:0},{type:"mb",activity:null,id:52,name:"黄海",url:"/mb52/",cur:0,num:800},{type:"mb",activity:null,id:292,name:"华骐",url:"/mb292/",cur:0,num:1},{type:"mb",activity:null,id:225,name:"华颂",url:"/mb225/",cur:0,num:321}],J:[{type:"mb",activity:{"bsId":34,"tagName":"免税季"},id:34,name:"吉利",url:"/mb34/",cur:0,num:62653},{type:"mb",activity:null,id:35,name:"江淮",url:"/mb35/",cur:0,num:42289},{type:"mb",activity:null,id:98,name:"捷豹",url:"/mb98/",cur:0,num:11523},{type:"mb",activity:null,id:4,name:"Jeep",url:"/mb4/",cur:0,num:20845},{type:"mb",activity:null,id:296,name:"捷途",url:"/mb296/",cur:0,num:1584},{type:"mb",activity:null,id:37,name:"江铃",url:"/mb37/",cur:0,num:24086},{type:"mb",activity:null,id:287,name:"奇点汽车",url:"/mb287/",cur:0,num:0},{type:"mb",activity:null,id:39,name:"金杯",url:"/mb39/",cur:0,num:16140},{type:"mb",activity:null,id:57,name:"金龙",url:"/mb57/",cur:0,num:372},{type:"mb",activity:null,id:152,name:"九龙",url:"/mb152/",cur:0,num:16},{type:"mb",activity:{"bsId":279,"tagName":"免税季"},id:279,name:"君马",url:"/mb279/",cur:0,num:2031}],K:[{type:"mb",activity:null,id:107,name:"凯迪拉克",url:"/mb107/",cur:0,num:9602},{type:"mb",activity:null,id:220,name:"凯翼",url:"/mb220/",cur:0,num:4330},{type:"mb",activity:null,id:51,name:"克莱斯勒",url:"/mb51/",cur:0,num:410},{type:"mb",activity:null,id:150,name:"开瑞",url:"/mb150/",cur:0,num:3520},{type:"mb",activity:null,id:214,name:"卡升",url:"/mb214/",cur:0,num:17},{type:"mb",activity:null,id:213,name:"卡威",url:"/mb213/",cur:0,num:0},{type:"mb",activity:null,id:241,name:"康迪全球鹰",url:"/mb241/",cur:0,num:0}],L:[{type:"mb",activity:null,id:94,name:"雷克萨斯",url:"/mb94/",cur:0,num:12528},{type:"mb",activity:null,id:99,name:"雷诺",url:"/mb99/",cur:0,num:4344},{type:"mb",activity:null,id:267,name:"领克",url:"/mb267/",cur:0,num:2702},{type:"mb",activity:null,id:95,name:"林肯",url:"/mb95/",cur:0,num:4512},{type:"mb",activity:{"bsId":36,"tagName":"免税季"},id:36,name:"陆风",url:"/mb36/",cur:0,num:8875},{type:"mb",activity:{"bsId":96,"tagName":"免税季"},id:96,name:"路虎",url:"/mb96/",cur:0,num:14338},{type:"mb",activity:null,id:76,name:"力帆",url:"/mb76/",cur:0,num:4559},{type:"mb",activity:null,id:16,name:"铃木",url:"/mb16/",cur:0,num:7748},{type:"mb",activity:null,id:80,name:"劳斯莱斯",url:"/mb80/",cur:0,num:77},{type:"mb",activity:null,id:86,name:"兰博基尼",url:"/mb86/",cur:0,num:31},{type:"mb",activity:null,id:153,name:"猎豹",url:"/mb153/",cur:0,num:16311},{type:"mb",activity:null,id:301,name:"零跑汽车",url:"/mb301/",cur:0,num:0}],M:[{type:"mb",activity:{"bsId":18,"tagName":"免税季"},id:18,name:"马自达",url:"/mb18/",cur:0,num:10409},{type:"mb",activity:{"bsId":79,"tagName":"免税季"},id:79,name:"名爵",url:"/mb79/",cur:0,num:17076},{type:"mb",activity:null,id:81,name:"MINI",url:"/mb81/",cur:0,num:4558},{type:"mb",activity:null,id:183,name:"迈凯伦",url:"/mb183/",cur:0,num:23},{type:"mb",activity:null,id:93,name:"玛莎拉蒂",url:"/mb93/",cur:0,num:1772}],N:[{type:"mb",activity:null,id:155,name:"纳智捷",url:"/mb155/",cur:0,num:2843}],O:[{type:"mb",activity:null,id:300,name:"欧尚汽车",url:"/mb300/",cur:0,num:0},{type:"mb",activity:null,id:84,name:"讴歌",url:"/mb84/",cur:0,num:1268},{type:"mb",activity:null,id:305,name:"欧拉",url:"/mb305/",cur:0,num:3}],P:[{type:"mb",activity:null,id:293,name:"Polestar",url:"/mb293/",cur:0,num:0}],Q:[{type:"mb",activity:{"bsId":42,"tagName":"免税季"},id:42,name:"奇瑞",url:"/mb42/",cur:0,num:31750},{type:"mb",activity:{"bsId":156,"tagName":"免税季"},id:156,name:"启辰",url:"/mb156/",cur:0,num:9916},{type:"mb",activity:null,id:28,name:"起亚",url:"/mb28/",cur:0,num:38111},{type:"mb",activity:null,id:43,name:"庆铃",url:"/mb43/",cur:0,num:38},{type:"mb",activity:null,id:231,name:"前途",url:"/mb231/",cur:0,num:0}],R:[{type:"mb",activity:{"bsId":30,"tagName":"免税季"},id:30,name:"日产",url:"/mb30/",cur:0,num:78839},{type:"mb",activity:{"bsId":78,"tagName":"免税季"},id:78,name:"荣威",url:"/mb78/",cur:0,num:35242}],S:[{type:"mb",activity:null,id:10,name:"斯柯达",url:"/mb10/",cur:0,num:27290},{type:"mb",activity:{"bsId":111,"tagName":"免税季"},id:111,name:"斯巴鲁",url:"/mb111/",cur:0,num:4009},{type:"mb",activity:null,id:89,name:"smart",url:"/mb89/",cur:0,num:3231},{type:"mb",activity:null,id:260,name:"SWM斯威",url:"/mb260/",cur:0,num:3623},{type:"mb",activity:null,id:299,name:"思皓",url:"/mb299/",cur:0,num:0},{type:"mb",activity:{"bsId":25,"tagName":"免税季"},id:25,name:"三菱",url:"/mb25/",cur:0,num:9335},{type:"mb",activity:null,id:165,name:"上汽大通",url:"/mb165/",cur:0,num:24858},{type:"mb",activity:null,id:102,name:"双龙",url:"/mb102/",cur:0,num:3}],T:[{type:"mb",activity:null,id:189,name:"特斯拉",url:"/mb189/",cur:0,num:52},{type:"mb",activity:null,id:175,name:"腾势",url:"/mb175/",cur:0,num:56}],W:[{type:"mb",activity:{"bsId":48,"tagName":"免税季"},id:48,name:"五菱",url:"/mb48/",cur:0,num:16996},{type:"mb",activity:{"bsId":19,"tagName":"免税季"},id:19,name:"沃尔沃",url:"/mb19/",cur:0,num:11537},{type:"mb",activity:null,id:270,name:"WEY",url:"/mb270/",cur:0,num:2710},{type:"mb",activity:null,id:132,name:"五十铃",url:"/mb132/",cur:0,num:3774},{type:"mb",activity:null,id:207,name:"潍柴英致",url:"/mb207/",cur:0,num:728},{type:"mb",activity:null,id:266,name:"蔚来",url:"/mb266/",cur:0,num:0},{type:"mb",activity:null,id:298,name:"威马汽车",url:"/mb298/",cur:0,num:0}],X:[{type:"mb",activity:null,id:49,name:"雪佛兰",url:"/mb49/",cur:0,num:32712},{type:"mb",activity:{"bsId":6,"tagName":"免税季"},id:6,name:"雪铁龙",url:"/mb6/",cur:0,num:11056},{type:"mb",activity:null,id:13,name:"现代",url:"/mb13/",cur:0,num:58540},{type:"mb",activity:null,id:286,name:"星驰",url:"/mb286/",cur:0,num:28},{type:"mb",activity:null,id:297,name:"小鹏汽车",url:"/mb297/",cur:0,num:0},{type:"mb",activity:null,id:304,name:"新特汽车",url:"/mb304/",cur:0,num:0}],Y:[{type:"mb",activity:null,id:100,name:"英菲尼迪",url:"/mb100/",cur:0,num:4114},{type:"mb",activity:null,id:258,name:"驭胜",url:"/mb258/",cur:0,num:13012},{type:"mb",activity:null,id:138,name:"野马",url:"/mb138/",cur:0,num:1574},{type:"mb",activity:{"bsId":53,"tagName":"免税季"},id:53,name:"一汽",url:"/mb53/",cur:0,num:11726},{type:"mb",activity:null,id:41,name:"依维柯",url:"/mb41/",cur:0,num:3128},{type:"mb",activity:null,id:285,name:"云度",url:"/mb285/",cur:0,num:121},{type:"mb",activity:null,id:291,name:"裕路",url:"/mb291/",cur:0,num:0}],Z:[{type:"mb",activity:null,id:77,name:"众泰",url:"/mb77/",cur:0,num:59256},{type:"mb",activity:null,id:60,name:"中华",url:"/mb60/",cur:0,num:7871},{type:"mb",activity:null,id:233,name:"知豆",url:"/mb233/",cur:0,num:82},{type:"mb",activity:null,id:203,name:"之诺",url:"/mb203/",cur:0,num:2},{type:"mb",activity:null,id:33,name:"中兴",url:"/mb33/",cur:0,num:2067}]},setcityurl:[{tagname:"jingxiaoshang",tagurl:"http://dealer.bitauto.com/@citycode@@objspell@/",otherpara:"?showtype=@showtype@&carids=@carids@",allspell:"mercedesbenz"},{tagname:"yanghu",tagurl:"http://car.bitauto.com/tree_baoyang/mb_@objid@/",otherpara:"?citycode=@cityid@",allspell:"mercedesbenz"}]})
# '''
# results = re.findall(r'\/mb\d+\/', json_str)

# json_str = '''
# JsonpCallBack({char:{A:1,B:1,C:1,D:1,E:0,F:1,G:1,H:1,I:0,J:1,K:1,L:1,M:1,N:1,O:1,P:1,Q:1,R:1,S:1,T:1,U:0,V:0,W:1,X:1,Y:1,Z:1},brand:{A:[{type:"mb",activity:null,id:9,name:"奥迪",url:"/tree_chexing/mb_9/",cur:0,num:40},{type:"mb",activity:null,id:92,name:"阿尔法·罗密欧",url:"/tree_chexing/mb_92/",cur:0,num:5},{type:"mb",activity:null,id:97,name:"阿斯顿·马丁",url:"/tree_chexing/mb_97/",cur:0,num:12},{type:"mb",activity:null,id:268,name:"ALPINA",url:"/tree_chexing/mb_268/",cur:0,num:1},{type:"mb",activity:null,id:289,name:"ARCFOX",url:"/tree_chexing/mb_289/",cur:0,num:1}],B:[{type:"mb",activity:null,id:157,name:"宝骏",url:"/tree_chexing/mb_157/",cur:0,num:13},{type:"mb",activity:null,id:3,name:"宝马",url:"/tree_chexing/mb_3/",cur:0,num:42},{type:"mb",activity:null,id:2,name:"奔驰",url:"/tree_chexing/mb_2/",cur:0,num:57},{type:"mb",activity:null,id:26,name:"本田",url:"/tree_chexing/mb_26/",cur:0,num:29},{type:"mb",activity:null,id:127,name:"别克",url:"/tree_chexing/mb_127/",cur:0,num:15},{type:"mb",activity:null,id:5,name:"标致",url:"/tree_chexing/mb_5/",cur:0,num:23},{type:"mb",activity:null,id:15,name:"比亚迪",url:"/tree_chexing/mb_15/",cur:0,num:30},{type:"mb",activity:null,id:82,name:"保时捷",url:"/tree_chexing/mb_82/",cur:0,num:11},{type:"mb",activity:null,id:236,name:"宝沃",url:"/tree_chexing/mb_236/",cur:0,num:4},{type:"mb",activity:null,id:59,name:"奔腾",url:"/tree_chexing/mb_59/",cur:0,num:9},{type:"mb",activity:null,id:263,name:"比速",url:"/tree_chexing/mb_263/",cur:0,num:4},{type:"mb",activity:null,id:195,name:"北汽绅宝",url:"/tree_chexing/mb_195/",cur:0,num:10},{type:"mb",activity:null,id:211,name:"北汽幻速",url:"/tree_chexing/mb_211/",cur:0,num:9},{type:"mb",activity:null,id:168,name:"北汽威旺",url:"/tree_chexing/mb_168/",cur:0,num:9},{type:"mb",activity:null,id:129,name:"北汽昌河",url:"/tree_chexing/mb_129/",cur:0,num:11},{type:"mb",activity:null,id:14,name:"北汽制造",url:"/tree_chexing/mb_14/",cur:0,num:15},{type:"mb",activity:null,id:282,name:"北汽道达",url:"/tree_chexing/mb_282/",cur:0,num:1},{type:"mb",activity:null,id:216,name:"北汽新能源",url:"/tree_chexing/mb_216/",cur:0,num:8},{type:"mb",activity:null,id:163,name:"北京",url:"/tree_chexing/mb_163/",cur:0,num:4},{type:"mb",activity:null,id:85,name:"宾利",url:"/tree_chexing/mb_85/",cur:0,num:6},{type:"mb",activity:null,id:135,name:"布加迪",url:"/tree_chexing/mb_135/",cur:0,num:1},{type:"mb",activity:null,id:172,name:"巴博斯",url:"/tree_chexing/mb_172/",cur:0,num:6}],C:[{type:"mb",activity:null,id:136,name:"长安汽车",url:"/tree_chexing/mb_136/",cur:0,num:28},{type:"mb",activity:null,id:159,name:"长安欧尚",url:"/tree_chexing/mb_159/",cur:0,num:15},{type:"mb",activity:null,id:281,name:"长安轻型车",url:"/tree_chexing/mb_281/",cur:0,num:10},{type:"mb",activity:null,id:283,name:"长安跨越",url:"/tree_chexing/mb_283/",cur:0,num:10},{type:"mb",activity:null,id:21,name:"长城",url:"/tree_chexing/mb_21/",cur:0,num:17}],D:[{type:"mb",activity:null,id:8,name:"大众",url:"/tree_chexing/mb_8/",cur:0,num:44},{type:"mb",activity:null,id:197,name:"东风风度",url:"/tree_chexing/mb_197/",cur:0,num:3},{type:"mb",activity:null,id:253,name:"东风风光",url:"/tree_chexing/mb_253/",cur:0,num:6},{type:"mb",activity:null,id:141,name:"东风风神",url:"/tree_chexing/mb_141/",cur:0,num:12},{type:"mb",activity:null,id:115,name:"东风风行",url:"/tree_chexing/mb_115/",cur:0,num:15},{type:"mb",activity:null,id:205,name:"东风小康",url:"/tree_chexing/mb_205/",cur:0,num:18},{type:"mb",activity:null,id:27,name:"东风",url:"/tree_chexing/mb_27/",cur:0,num:17},{type:"mb",activity:null,id:29,name:"东南",url:"/tree_chexing/mb_29/",cur:0,num:12},{type:"mb",activity:null,id:113,name:"道奇",url:"/tree_chexing/mb_113/",cur:0,num:6},{type:"mb",activity:null,id:179,name:"DS",url:"/tree_chexing/mb_179/",cur:0,num:8},{type:"mb",activity:null,id:294,name:"电咖",url:"/tree_chexing/mb_294/",cur:0,num:1}],F:[{type:"mb",activity:null,id:7,name:"丰田",url:"/tree_chexing/mb_7/",cur:0,num:42},{type:"mb",activity:null,id:17,name:"福特",url:"/tree_chexing/mb_17/",cur:0,num:29},{type:"mb",activity:null,id:40,name:"菲亚特",url:"/tree_chexing/mb_40/",cur:0,num:12},{type:"mb",activity:null,id:91,name:"法拉利",url:"/tree_chexing/mb_91/",cur:0,num:16},{type:"mb",activity:null,id:67,name:"福迪",url:"/tree_chexing/mb_67/",cur:0,num:12},{type:"mb",activity:null,id:208,name:"福汽启腾",url:"/tree_chexing/mb_208/",cur:0,num:4},{type:"mb",activity:null,id:128,name:"福田",url:"/tree_chexing/mb_128/",cur:0,num:36},{type:"mb",activity:null,id:257,name:"Faraday Future",url:"/tree_chexing/mb_257/",cur:0,num:1}],G:[{type:"mb",activity:null,id:147,name:"广汽传祺",url:"/tree_chexing/mb_147/",cur:0,num:14},{type:"mb",activity:null,id:295,name:"广汽新能源",url:"/tree_chexing/mb_295/",cur:0,num:3},{type:"mb",activity:null,id:63,name:"广汽吉奥",url:"/tree_chexing/mb_63/",cur:0,num:20},{type:"mb",activity:null,id:133,name:"广汽日野",url:"/tree_chexing/mb_133/",cur:0,num:3},{type:"mb",activity:null,id:182,name:"观致",url:"/tree_chexing/mb_182/",cur:0,num:3},{type:"mb",activity:null,id:290,name:"国金",url:"/tree_chexing/mb_290/",cur:0,num:1},{type:"mb",activity:null,id:109,name:"GMC",url:"/tree_chexing/mb_109/",cur:0,num:3},{type:"mb",activity:null,id:110,name:"光冈",url:"/tree_chexing/mb_110/",cur:0,num:3}],H:[{type:"mb",activity:null,id:196,name:"哈弗",url:"/tree_chexing/mb_196/",cur:0,num:14},{type:"mb",activity:null,id:32,name:"海马",url:"/tree_chexing/mb_32/",cur:0,num:25},{type:"mb",activity:null,id:259,name:"汉腾",url:"/tree_chexing/mb_259/",cur:0,num:4},{type:"mb",activity:null,id:58,name:"红旗",url:"/tree_chexing/mb_58/",cur:0,num:8},{type:"mb",activity:null,id:112,name:"华泰",url:"/tree_chexing/mb_112/",cur:0,num:14},{type:"mb",activity:null,id:31,name:"哈飞",url:"/tree_chexing/mb_31/",cur:0,num:14},{type:"mb",activity:null,id:108,name:"悍马",url:"/tree_chexing/mb_108/",cur:0,num:2},{type:"mb",activity:null,id:181,name:"恒天",url:"/tree_chexing/mb_181/",cur:0,num:3},{type:"mb",activity:null,id:302,name:"红星汽车",url:"/tree_chexing/mb_302/",cur:0,num:1},{type:"mb",activity:null,id:262,name:"华凯",url:"/tree_chexing/mb_262/",cur:0,num:1},{type:"mb",activity:null,id:52,name:"黄海",url:"/tree_chexing/mb_52/",cur:0,num:20},{type:"mb",activity:null,id:44,name:"华普",url:"/tree_chexing/mb_44/",cur:0,num:11},{type:"mb",activity:null,id:292,name:"华骐",url:"/tree_chexing/mb_292/",cur:0,num:1},{type:"mb",activity:null,id:225,name:"华颂",url:"/tree_chexing/mb_225/",cur:0,num:1},{type:"mb",activity:null,id:45,name:"汇众",url:"/tree_chexing/mb_45/",cur:0,num:2}],J:[{type:"mb",activity:null,id:34,name:"吉利",url:"/tree_chexing/mb_34/",cur:0,num:36},{type:"mb",activity:null,id:35,name:"江淮",url:"/tree_chexing/mb_35/",cur:0,num:32},{type:"mb",activity:null,id:98,name:"捷豹",url:"/tree_chexing/mb_98/",cur:0,num:11},{type:"mb",activity:null,id:4,name:"Jeep",url:"/tree_chexing/mb_4/",cur:0,num:14},{type:"mb",activity:null,id:296,name:"捷途",url:"/tree_chexing/mb_296/",cur:0,num:2},{type:"mb",activity:null,id:37,name:"江铃",url:"/tree_chexing/mb_37/",cur:0,num:28},{type:"mb",activity:null,id:287,name:"奇点汽车",url:"/tree_chexing/mb_287/",cur:0,num:1},{type:"mb",activity:null,id:39,name:"金杯",url:"/tree_chexing/mb_39/",cur:0,num:27},{type:"mb",activity:null,id:57,name:"金龙",url:"/tree_chexing/mb_57/",cur:0,num:5},{type:"mb",activity:null,id:161,name:"金旅",url:"/tree_chexing/mb_161/",cur:0,num:3},{type:"mb",activity:null,id:152,name:"九龙",url:"/tree_chexing/mb_152/",cur:0,num:4},{type:"mb",activity:null,id:279,name:"君马",url:"/tree_chexing/mb_279/",cur:0,num:4}],K:[{type:"mb",activity:null,id:107,name:"凯迪拉克",url:"/tree_chexing/mb_107/",cur:0,num:12},{type:"mb",activity:null,id:220,name:"凯翼",url:"/tree_chexing/mb_220/",cur:0,num:6},{type:"mb",activity:null,id:51,name:"克莱斯勒",url:"/tree_chexing/mb_51/",cur:0,num:10},{type:"mb",activity:null,id:150,name:"开瑞",url:"/tree_chexing/mb_150/",cur:0,num:15},{type:"mb",activity:null,id:214,name:"卡升",url:"/tree_chexing/mb_214/",cur:0,num:6},{type:"mb",activity:null,id:213,name:"卡威",url:"/tree_chexing/mb_213/",cur:0,num:4},{type:"mb",activity:null,id:145,name:"科尼赛克",url:"/tree_chexing/mb_145/",cur:0,num:2},{type:"mb",activity:null,id:212,name:"KTM",url:"/tree_chexing/mb_212/",cur:0,num:1},{type:"mb",activity:null,id:188,name:"卡尔森",url:"/tree_chexing/mb_188/",cur:0,num:3},{type:"mb",activity:null,id:241,name:"康迪全球鹰",url:"/tree_chexing/mb_241/",cur:0,num:1}],L:[{type:"mb",activity:null,id:94,name:"雷克萨斯",url:"/tree_chexing/mb_94/",cur:0,num:15},{type:"mb",activity:null,id:99,name:"雷诺",url:"/tree_chexing/mb_99/",cur:0,num:12},{type:"mb",activity:null,id:267,name:"领克",url:"/tree_chexing/mb_267/",cur:0,num:4},{type:"mb",activity:null,id:95,name:"林肯",url:"/tree_chexing/mb_95/",cur:0,num:9},{type:"mb",activity:null,id:36,name:"陆风",url:"/tree_chexing/mb_36/",cur:0,num:10},{type:"mb",activity:null,id:96,name:"路虎",url:"/tree_chexing/mb_96/",cur:0,num:12},{type:"mb",activity:null,id:76,name:"力帆",url:"/tree_chexing/mb_76/",cur:0,num:21},{type:"mb",activity:null,id:16,name:"铃木",url:"/tree_chexing/mb_16/",cur:0,num:20},{type:"mb",activity:null,id:80,name:"劳斯莱斯",url:"/tree_chexing/mb_80/",cur:0,num:7},{type:"mb",activity:null,id:86,name:"兰博基尼",url:"/tree_chexing/mb_86/",cur:0,num:5},{type:"mb",activity:null,id:146,name:"莲花",url:"/tree_chexing/mb_146/",cur:0,num:3},{type:"mb",activity:null,id:153,name:"猎豹",url:"/tree_chexing/mb_153/",cur:0,num:22},{type:"mb",activity:null,id:301,name:"零跑汽车",url:"/tree_chexing/mb_301/",cur:0,num:1},{type:"mb",activity:null,id:166,name:"理念",url:"/tree_chexing/mb_166/",cur:0,num:1},{type:"mb",activity:null,id:83,name:"路特斯",url:"/tree_chexing/mb_83/",cur:0,num:4}],M:[{type:"mb",activity:null,id:18,name:"马自达",url:"/tree_chexing/mb_18/",cur:0,num:21},{type:"mb",activity:null,id:79,name:"名爵",url:"/tree_chexing/mb_79/",cur:0,num:11},{type:"mb",activity:null,id:81,name:"MINI",url:"/tree_chexing/mb_81/",cur:0,num:12},{type:"mb",activity:null,id:88,name:"迈巴赫",url:"/tree_chexing/mb_88/",cur:0,num:4},{type:"mb",activity:null,id:183,name:"迈凯伦",url:"/tree_chexing/mb_183/",cur:0,num:10},{type:"mb",activity:null,id:93,name:"玛莎拉蒂",url:"/tree_chexing/mb_93/",cur:0,num:8},{type:"mb",activity:null,id:201,name:"摩根",url:"/tree_chexing/mb_201/",cur:0,num:7}],N:[{type:"mb",activity:null,id:155,name:"纳智捷",url:"/tree_chexing/mb_155/",cur:0,num:8}],O:[{type:"mb",activity:null,id:300,name:"欧尚汽车",url:"/tree_chexing/mb_300/",cur:0,num:1},{type:"mb",activity:null,id:84,name:"讴歌",url:"/tree_chexing/mb_84/",cur:0,num:11},{type:"mb",activity:null,id:305,name:"欧拉",url:"/tree_chexing/mb_305/",cur:0,num:2},{type:"mb",activity:null,id:104,name:"欧宝",url:"/tree_chexing/mb_104/",cur:0,num:7},{type:"mb",activity:null,id:171,name:"欧朗",url:"/tree_chexing/mb_171/",cur:0,num:1}],P:[{type:"mb",activity:null,id:185,name:"帕加尼",url:"/tree_chexing/mb_185/",cur:0,num:1},{type:"mb",activity:null,id:293,name:"Polestar",url:"/tree_chexing/mb_293/",cur:0,num:1}],Q:[{type:"mb",activity:null,id:42,name:"奇瑞",url:"/tree_chexing/mb_42/",cur:0,num:37},{type:"mb",activity:null,id:156,name:"启辰",url:"/tree_chexing/mb_156/",cur:0,num:11},{type:"mb",activity:null,id:28,name:"起亚",url:"/tree_chexing/mb_28/",cur:0,num:36},{type:"mb",activity:null,id:231,name:"前途",url:"/tree_chexing/mb_231/",cur:0,num:1},{type:"mb",activity:null,id:43,name:"庆铃",url:"/tree_chexing/mb_43/",cur:0,num:2}],R:[{type:"mb",activity:null,id:30,name:"日产",url:"/tree_chexing/mb_30/",cur:0,num:36},{type:"mb",activity:null,id:78,name:"荣威",url:"/tree_chexing/mb_78/",cur:0,num:18},{type:"mb",activity:null,id:142,name:"瑞麒",url:"/tree_chexing/mb_142/",cur:0,num:5}],S:[{type:"mb",activity:null,id:10,name:"斯柯达",url:"/tree_chexing/mb_10/",cur:0,num:16},{type:"mb",activity:null,id:111,name:"斯巴鲁",url:"/tree_chexing/mb_111/",cur:0,num:8},{type:"mb",activity:null,id:89,name:"smart",url:"/tree_chexing/mb_89/",cur:0,num:3},{type:"mb",activity:null,id:260,name:"SWM斯威",url:"/tree_chexing/mb_260/",cur:0,num:3},{type:"mb",activity:null,id:299,name:"思皓",url:"/tree_chexing/mb_299/",cur:0,num:1},{type:"mb",activity:null,id:103,name:"萨博",url:"/tree_chexing/mb_103/",cur:0,num:2},{type:"mb",activity:null,id:239,name:"赛麟",url:"/tree_chexing/mb_239/",cur:0,num:5},{type:"mb",activity:null,id:25,name:"三菱",url:"/tree_chexing/mb_25/",cur:0,num:22},{type:"mb",activity:null,id:165,name:"上汽大通",url:"/tree_chexing/mb_165/",cur:0,num:8},{type:"mb",activity:null,id:137,name:"世爵",url:"/tree_chexing/mb_137/",cur:0,num:1},{type:"mb",activity:null,id:50,name:"双环",url:"/tree_chexing/mb_50/",cur:0,num:4},{type:"mb",activity:null,id:102,name:"双龙",url:"/tree_chexing/mb_102/",cur:0,num:9}],T:[{type:"mb",activity:null,id:189,name:"特斯拉",url:"/tree_chexing/mb_189/",cur:0,num:3},{type:"mb",activity:null,id:175,name:"腾势",url:"/tree_chexing/mb_175/",cur:0,num:1}],W:[{type:"mb",activity:null,id:48,name:"五菱",url:"/tree_chexing/mb_48/",cur:0,num:15},{type:"mb",activity:null,id:19,name:"沃尔沃",url:"/tree_chexing/mb_19/",cur:0,num:26},{type:"mb",activity:null,id:270,name:"WEY",url:"/tree_chexing/mb_270/",cur:0,num:4},{type:"mb",activity:null,id:266,name:"蔚来",url:"/tree_chexing/mb_266/",cur:0,num:2},{type:"mb",activity:null,id:132,name:"五十铃",url:"/tree_chexing/mb_132/",cur:0,num:4},{type:"mb",activity:null,id:247,name:"潍柴欧睿",url:"/tree_chexing/mb_247/",cur:0,num:1},{type:"mb",activity:null,id:207,name:"潍柴英致",url:"/tree_chexing/mb_207/",cur:0,num:5},{type:"mb",activity:null,id:140,name:"威麟",url:"/tree_chexing/mb_140/",cur:0,num:4},{type:"mb",activity:null,id:298,name:"威马汽车",url:"/tree_chexing/mb_298/",cur:0,num:1},{type:"mb",activity:null,id:186,name:"威兹曼",url:"/tree_chexing/mb_186/",cur:0,num:2}],X:[{type:"mb",activity:null,id:49,name:"雪佛兰",url:"/tree_chexing/mb_49/",cur:0,num:25},{type:"mb",activity:null,id:6,name:"雪铁龙",url:"/tree_chexing/mb_6/",cur:0,num:19},{type:"mb",activity:null,id:13,name:"现代",url:"/tree_chexing/mb_13/",cur:0,num:39},{type:"mb",activity:null,id:297,name:"小鹏汽车",url:"/tree_chexing/mb_297/",cur:0,num:1},{type:"mb",activity:null,id:286,name:"星驰",url:"/tree_chexing/mb_286/",cur:0,num:3},{type:"mb",activity:null,id:304,name:"新特汽车",url:"/tree_chexing/mb_304/",cur:0,num:1},{type:"mb",activity:null,id:87,name:"西雅特",url:"/tree_chexing/mb_87/",cur:0,num:3}],Y:[{type:"mb",activity:null,id:100,name:"英菲尼迪",url:"/tree_chexing/mb_100/",cur:0,num:18},{type:"mb",activity:null,id:258,name:"驭胜",url:"/tree_chexing/mb_258/",cur:0,num:2},{type:"mb",activity:null,id:138,name:"野马",url:"/tree_chexing/mb_138/",cur:0,num:10},{type:"mb",activity:null,id:53,name:"一汽",url:"/tree_chexing/mb_53/",cur:0,num:32},{type:"mb",activity:null,id:41,name:"依维柯",url:"/tree_chexing/mb_41/",cur:0,num:9},{type:"mb",activity:null,id:75,name:"永源",url:"/tree_chexing/mb_75/",cur:0,num:5},{type:"mb",activity:null,id:291,name:"裕路",url:"/tree_chexing/mb_291/",cur:0,num:1},{type:"mb",activity:null,id:285,name:"云度",url:"/tree_chexing/mb_285/",cur:0,num:3}],Z:[{type:"mb",activity:null,id:77,name:"众泰",url:"/tree_chexing/mb_77/",cur:0,num:29},{type:"mb",activity:null,id:60,name:"中华",url:"/tree_chexing/mb_60/",cur:0,num:19},{type:"mb",activity:null,id:233,name:"知豆",url:"/tree_chexing/mb_233/",cur:0,num:4},{type:"mb",activity:null,id:203,name:"之诺",url:"/tree_chexing/mb_203/",cur:0,num:1},{type:"mb",activity:null,id:33,name:"中兴",url:"/tree_chexing/mb_33/",cur:0,num:18}]}})
# '''
# results = re.findall(r'\/tree_chexing\/mb_\d+\/', json_str)


class Bitautospider(scrapy.Spider):
    name = 'bitautospider'
    allowed_domains = ['car.bitauto.com']
    start_urls = ['http://api.car.bitauto.com/CarInfo/getlefttreejson.ashx?tagtype=chexing&pagetype=masterbrand&objid=0']

    def parse(self, response):  # 生成每个品牌链接
        page_root = 'car.bitauto.com'
        json_str = response.text
        mb_pages = re.findall(r'\/tree_chexing\/mb_\d+\/', json_str)
#       mb_pages = ['/tree_chexing/mb_95/', '/tree_chexing/mb_189/', '/tree_chexing/mb_147/', '/tree_chexing/mb_196/', '/tree_chexing/mb_9/']
        for info in mb_pages:
            page_href = info
            page_url = 'https://' + str(page_root) + str(page_href)
            yield scrapy.Request(url=page_url, callback=self.parse_model_page, dont_filter=True)

    def parse_model_page(self, response):  # 生成每个车型链接
        base_url = 'car.bitauto.com'
        model = '.col-xs-9 div:nth-child(2) #divCsLevel_0 div .col-xs-3'
        # brand = response.css('.col-xs-9 div:nth-child(2) #divCsLevel_0 h5 a::text').extract_first()
        for info in response.css(model):
            car_page_url_href = info.css('div div a::attr(href)').extract_first()
            car_page_url = 'https://' + str(base_url) + str(car_page_url_href)
            tingchan = info.css('div ul .price a::text').extract_first()
            yield scrapy.Request(url=car_page_url, meta={'tingchan': tingchan},
                                 callback=self.parse_car_page, dont_filter=True)

    def not_on_sale(self, response):   # 年款页面
        base_url = 'car.bitauto.com'
        notsale = '.middle-nav-box div div ul'
        brand = response.meta['brand']
        tingchan = response.meta['tingchan']
        for info in response.css(notsale):
            notsale_href = info.css('a[href*="2017"]::attr(href)').extract_first()
            if notsale_href:
                notsale_url = 'https://' + str(base_url) + str(notsale_href)
                yield scrapy.Request(url=notsale_url, meta={'brand': brand, 'tingchan': tingchan},
                                     callback=self.parse_car_page, dont_filter=True)

    def parse_car_page(self, response):  # 生成配置链接
        base_url = 'car.bitauto.com'
        peizhi_url_href = response.css('#car_tag nav div div ul li:nth-child(2) a::attr(href)').extract_first()
        peizhi_url = 'https://' + str(base_url) + str(peizhi_url_href)
        brand = response.css('.crumbs-txt a:nth-last-child(2)::text').extract_first()
        tingchan = response.meta['tingchan']
        yield scrapy.Request(url=peizhi_url, meta={'brand': brand, 'tingchan': tingchan}, callback=self.parse_detail_page, dont_filter=True)

    def parse_detail_page(self, response):
        ff = re.search('\[\[\[(.*?)\]\]\]', response.body.decode('utf-8')).group()  # str
        infos = eval(ff)

        for s_second in infos:
            item = BitautoCarItem()

            item['brand'] = response.meta['brand']  # 华晨宝马
            item['brandmodel'] = s_second[0][5]
            item['url'] = str(response.url)[8:]
            item['version'] = s_second[0][1]
            item['price'] = s_second[1][0]
            item['year'] = s_second[0][7]
            item['marketyear'] = s_second[1][12]
            item['marketmonth'] = s_second[1][11]
            item['marketday'] = s_second[1][10]
            item['zaichan'] = s_second[0][8]
            item['zaixiao'] = s_second[0][9]
            item['bodytype'] = s_second[1][13]  # "SUV"
            item['modellevel'] = s_second[0][12]  # 中型suv
            item['powertype'] = s_second[1][14]  # 汽油
            item['fuelconsumption'] = s_second[3][18]  # 混合工况油耗 7.9
            item['jiasushijian'] = s_second[3][17]  # 百公里加速时间
            item['maximumspeed'] = s_second[3][16]  # 最高车速
            item['huanbao'] = s_second[3][19]  # 环保标准
            item['baoxiuzhengce'] = s_second[1][3]  # 保修政策
            item['color'] = s_second[0][13]   # 颜色
            item['fadongjipailie'] = s_second[3][7]  # 直列
            item['gangshu'] = s_second[3][8]  # 四缸
            item['zuidaxuhanglicheng'] = s_second[3][-9]  # 最大续航里程 或[3][30] 电
            item['dianchichongdianman'] = '慢充' + s_second[3][27]  # 电池慢充时间  电
            item['dianchichongdiankuai'] = '快充' + s_second[3][28]  # 电池快充时间  电
            item['dianchibaoxiu'] = s_second[3][-8]   # 电池保修 或[3][31] 电
            item['butie'] = s_second[2][-3]   # 补贴 或[2][21] 电  基本信息完
            item['clength'] = s_second[2][0]  # 长宽高，为了清楚表示，加了前缀c 4717
            item['cwidth'] = s_second[2][1]  # 长宽高，为了清楚表示，加了前缀c 1891
            item['cheight'] = s_second[2][2]  # 长宽高，为了清楚表示，加了前缀c 1689
            item['wheelbase'] = s_second[2][3]  # 轴距 2864
            item['quaility'] = s_second[2][4]  # 整备质量
            item['seats'] = s_second[2][5]  # 5
            item['xinglixiangrongjimin'] = s_second[2][6]  # 行李厢容积（最小）
            item['xinglixiangrongjimax'] = s_second[2][-5]  # 行李厢容积（最大）
            item['youxiang'] = s_second[2][7]  # 油箱容积
            item['qianluntai'] = s_second[2][8]  # 前轮胎规格
            item['houluntai'] = s_second[2][9]  # 后轮胎规格
            item['beitai'] = s_second[2][10]  # 备胎
            item['zuixiaozhuanwanzhijing'] = s_second[2][-2]  # 最小转弯直径
            item['xitongzonghekw'] = s_second[3][-6]  # 系统综合功率
            item['xitongzonghenm'] = s_second[3][-5]  # 系统综合扭矩
            item['lidijianxi'] = s_second[2][-1]  # 最小离地间隙  车身尺寸完
            item['aspiration'] = s_second[1][5]  # 涡轮增压
            item['displacement'] = s_second[3][0]  # 1998 下一项是2.0
            item['maximumpower'] = s_second[3][2]  # 135
            item['zuidamali'] = s_second[3][3]  # 最大马力
            item['zuidagonglvrpm'] = s_second[3][4]  # 最大功率转速
            item['maximumtorque'] = s_second[3][5]  # 最大扭矩 290
            item['zuidaniujurpm'] = s_second[3][6]  # 最大扭矩转速
            item['gongyou'] = s_second[3][10]  # 供油方式
            item['ranyou'] = s_second[3][12]  # 燃油标号
            item['fadongjiqiting'] = s_second[3][13]  # 发动机启停
            item['gearboxtype'] = s_second[3][14]  # 变速箱类型 手自一体
            item['gears'] = s_second[3][15]  # 档位个数 8
            item['diandongjikw'] = s_second[3][20]  # 电动机总功率
            item['diandongjiniuju'] = s_second[3][21]  # 电动机总扭矩
            item['houdiandongjikw'] = s_second[3][24]  # 后电动机最大功率
            item['houdiandongjinm'] = s_second[3][25]  # 后电动机最大扭矩
            item['dianchirongliang'] = s_second[3][26]  # 电池容量
            item['haodianliang'] = s_second[3][29]  # 耗电量  # 动力系统完
            item['drivemode'] = s_second[4][0]  # 全时四驱
            item['frontsuspensiontype'] = s_second[4][1]  # 前悬架类型
            item['rearsuspensiontype'] = s_second[4][2]  # 后悬架类型
            item['ketiaoxuanjia'] = s_second[4][3]  # 可调悬架
            item['qianlunzhidong'] = s_second[4][4]  # 前轮制动器类型
            item['houlunzhidong'] = s_second[4][5]  # 后轮制动器类型
            item['zhuchezhidong'] = s_second[4][6]  # 驻车制动类型
            item['carbodystructure'] = s_second[4][7]  # 车体结构 承载式
            item['chasusuo'] = s_second[4][8]  # 限滑差速器/差速锁
            item['jiejinjiao'] = s_second[4][-4]  # 接近角
            item['liqujiao'] = s_second[4][-3]  # 离去角
            item['zuidasheshuishendu'] = s_second[4][-1]  # 最大涉水深度
            item['tongguojiao'] = s_second[4][-2]  # 通过角 底盘制动结束
            item['abs'] = s_second[5][0]  # 安全配置开始
            item['ebd'] = s_second[5][1]
            item['eba'] = s_second[5][2]
            item['ars'] = s_second[5][3]
            item['esp'] = s_second[5][4]
            item['zhuqinang'] = s_second[5][5]
            item['fuqinang'] = s_second[5][6]
            item['qianqinang'] = s_second[5][8]  # 怀疑这个与[7]相反 需验证
            item['houqinang'] = s_second[5][7]
            item['ceqilian'] = s_second[5][9]
            item['xiqinang'] = s_second[5][10]
            item['anquandai'] = s_second[5][11]
            item['houpaiqinang'] = s_second[5][12]
            item['taiya'] = s_second[5][13]
            item['lingtaiya'] = s_second[5][14]
            item['ertongzuo'] = s_second[5][15]  # 安全配置结束
            item['dingsu'] = s_second[6][0]  # 驾驶辅助开始
            item['chedao'] = s_second[6][1]
            item['pengzhuang'] = s_second[6][2]
            item['pilao'] = s_second[6][3]
            item['automaticparking'] = s_second[6][4]  # 自动泊车 有
            item['yaokong'] = s_second[6][5]
            item['automaticdrivingassitance'] = s_second[6][6]  # 自动驾驶辅助 无
            item['zhuche'] = s_second[6][7]
            item['shangpo'] = s_second[6][8]
            item['doupo'] = s_second[6][9]
            item['yeshi'] = s_second[6][10]
            item['kebianchibi'] = s_second[6][11]
            item['qianleida'] = s_second[6][12]
            item['houleida'] = s_second[6][13]
            item['daocheyingxiang'] = s_second[6][14]
            item['jiashimoshi'] = s_second[6][15]
            item['bingxianfuzhu'] = s_second[6][16]  # 驾驶辅助结束
            item['qiandadeng'] = s_second[7][0]  # 外部配置开始
            item['led'] = s_second[7][1]
            item['zidongdadeng'] = s_second[7][2]
            item['qianwudeng'] = s_second[7][3]
            item['dadeng'] = s_second[7][4]
            item['tianchuang'] = s_second[7][5]
            item['qianchechuang'] = s_second[7][6]
            item['houchechuang'] = s_second[7][7]
            item['waihoushijing'] = s_second[7][8]
            item['neihoushijing'] = s_second[7][10]
            item['waihoushijingxuanmu'] = s_second[7][11]
            item['yinsi'] = s_second[7][12]
            item['houpai'] = s_second[7][13]
            item['houzheyang'] = s_second[7][14]
            item['qianyushua'] = s_second[7][15]
            item['houyushua'] = s_second[7][16]
            item['dianximen'] = s_second[7][17]
            item['diandongcehua'] = s_second[7][18]
            item['diandongxingli'] = s_second[7][19]
            item['chedingxinglijia'] = s_second[7][20]
            item['zhongkongsuo'] = s_second[7][21]
            item['zhinengyaoshi'] = s_second[7][22]
            item['yuanchengyaokong'] = s_second[7][23]
            item['weiyi'] = s_second[7][24]
            item['yundongwaiguan'] = s_second[7][25]
            item['liumeiti'] = s_second[7][26]  # 外部配置结束  流媒体怀疑放在了最后一行
            item['neishi'] = s_second[8][0]  # 内部配置开始
            item['fenweideng'] = s_second[8][1]
            item['zheyangban'] = s_second[8][2]
            item['fangxiangpan'] = s_second[8][3]
            item['duogongnengfxp'] = s_second[8][4]
            item['fxptiaojie'] = s_second[8][5]
            item['fxpjiare'] = s_second[8][6]
            item['fxphuandang'] = s_second[8][7]
            item['qianpaikongtiao'] = s_second[8][8]
            item['houpaikongtiao'] = s_second[8][9]
            item['xiangfen'] = s_second[8][10]
            item['kongqijinghua'] = s_second[8][11]
            item['chezaibingxiang'] = s_second[8][12]
            item['zhudongjiangzao'] = s_second[8][13]  # 内部配置结束
            item['zuoyicaizhi'] = s_second[9][0]  # 座椅配置开始
            item['yundongfenggezuoyi'] = s_second[9][1]
            item['zhuzuoyi'] = s_second[9][2]
            item['fuzuoyi'] = s_second[9][3]
            item['zhutiaojie'] = s_second[9][4]
            item['futiaojie'] = s_second[9][5]
            item['dierpai1'] = s_second[9][6]
            item['dierpai2'] = s_second[9][7]
            item['qianpaizuoyi'] = s_second[9][8]
            item['houpaizuoyi'] = s_second[9][9]
            item['qianpaizhongyang'] = s_second[9][10]
            item['houpaizhongyang'] = s_second[9][11]
            item['disanpai'] = s_second[9][12]
            item['zuoyifangdao'] = s_second[9][13]
            item['houpaibeijia'] = s_second[9][14]
            item['houpaizhedie'] = s_second[9][15]  # 座椅配置结束
            item['zhongkongcaise'] = s_second[10][0]  # 信息娱乐开始
            item['quanyejing'] = s_second[10][1]
            item['xingchediannao'] = s_second[10][2]
            item['hud'] = s_second[10][3]
            item['gps'] = s_second[10][4]
            item['zhinenghulian'] = s_second[10][5]
            item['viocecontrol'] = s_second[10][6]  # 语音控制 o
            item['mobileinternet'] = s_second[10][7]  # CarPlay
            item['shoujiwuxian'] = s_second[10][8]
            item['shoushikongzhi'] = s_second[10][9]
            item['cd'] = s_second[10][10]
            item['bluetoothwifi'] = s_second[10][11]  # 蓝牙
            item['waijie'] = s_second[10][12]
            item['chezaidianshi'] = s_second[10][13]
            item['audiobrand'] = s_second[10][14]  # 音响品牌
            item['yangshengqi'] = s_second[10][-5]
            item['houpaiyejingping'] = s_second[10][16]
            item['chezai220'] = s_second[10][17]
            item['yejingping'] = s_second[10][18]
            item['chezaixingche'] = s_second[10][19]  # 信息娱乐结束
            yield item
