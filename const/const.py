#coding:utf-8

# sit redis cluster
redis_cluster = [
    {"host": "10.252.96.13", "port": 9001},
    {'host': '10.252.96.13', 'port': 9002},
    {'host': '10.252.96.13', 'port': 9003},
    {'host': '10.252.96.13', 'port': 9004},
    {'host': '10.252.96.13', 'port': 9005},
    {'host': '10.252.96.13', 'port': 9006}
]
redis_password = "Redis@2017"

# 画单List推荐表
key_Rec_List_General = "Rec_List_General:"  # 通用推荐表 Key: "Rec_General"
key_Rec_List_UI = "Rec_List_User:"  # 基于用户的推荐表 Key: "Rec_User:uid"
key_Rec_List_LI = "Rec_List_Item:"  # 基于画作的推荐表 Key: "Rec_Item:lid"

# 画作Pic推荐表
key_Rec_Single_General = "Rec_Pic_General:"  # 通用推荐表 Key: "Rec_General"
key_Rec_Single_UI = "Rec_Pic_User:"  # 基于用户的推荐表 Key: "Rec_User:uid"
key_Rec_Single_PI = "Rec_Pic_Item:"  # 基于画作的推荐表 Key: "Rec_Item:pid"

#详情页画单推荐数量
listRecUidNum = 5
listRecLidNum = 5
listRecTotalNum = 10

#详情页画作推荐数量
SingleRecUidNum = 5
SingleRecLidNum = 5
SingleRecTotalNum = 10

pidStr="pid" #返回值中的 画作ID
lidStr="lid" #返回值中的画单ID
