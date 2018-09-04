# coding:utf-8
import json
import logging
import random

from rediscluster import StrictRedisCluster, RedisCluster
from rest_framework.views import APIView

from const import const

logger = logging.getLogger('django')

redis_nodes = const.redis_cluster
pd = const.redis_password

try:
    redisconn = RedisCluster(startup_nodes=redis_nodes, decode_responses=True, password=pd, max_connections=150)
except Exception:
    logger.error("Connect Redis Error")


def strToList(str):  # 字符串转化为列表
    if str:
        js = json.loads(str)
        li = list(js)
    else:
        li = []
    return li


def strToSample(str, num):  # 从查询数据集中选取固定画单
    ll = strToList(str)
    if len(ll) >= num:
        result = random.sample(ll, num)
    else:
        result = ll
    return result


def listToResult(resultList, varStr, alg):  # 筛选画单重新定义ID号
    result = []
    for l in resultList:
        dic = {varStr: l, "alg": alg}
        result.append(dic)
    return result

class RecView(APIView):
    def post(self, request, format=None):
        serializer = RecSerializer(data=request.data)
