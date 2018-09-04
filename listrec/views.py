import json
import random

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ListRecSerializer
import const.const as const
import const.redisfunc as redisfunc


class ListRecView(APIView):
    def post(self, request, format=None):
        serializer = ListRecSerializer(data=request.data)
        if serializer.is_valid():
            r = redisfunc.redisconn
            uid = serializer.data["uid"]
            lid = serializer.data["lid"]
            # 画单推荐radis
            genListKey = const.key_Rec_List_General  # 通用推荐表
            uidListKey = const.key_Rec_List_UI + str(uid)  # 基于用户推荐表
            lidListKey = const.key_Rec_List_LI + str(lid)  # 基于画单推荐表
            # 返回字符串
            genListStr = r.get(genListKey)
            uidListStr = r.get(uidListKey)
            lidListStr = r.get(lidListKey)
            resultList = []

            if uidListStr or lidListStr:  # 基于用户和画单推荐表存在
                resultList1 = redisfunc.strToSample(uidListStr, const.listRecUidNum)  # 基于用户
                resultList.extend(resultList1)
                resultList2 = redisfunc.strToSample(lidListStr, const.listRecLidNum)  # 基于画单
                resultList.extend(resultList2)

                if len(resultList) == const.listRecTotalNum:  # 推荐数量够
                    return Response(resultList, status=status.HTTP_200_OK)
                else:  # 推荐数量不够
                    lack = const.listRecTotalNum - len(resultList)
                    if len(redisfunc.strToList(uidListStr)) < const.listRecUidNum:
                        resultList3 = redisfunc.strToSample(lidListStr, lack)
                        resultList.extend(resultList3)
                    elif len(redisfunc.strToList(lidListStr)) < const.listRecUidNum:
                        resultList3 = redisfunc.strToSample(uidListStr, lack)
                        resultList.extend(resultList3)

                    if len(resultList) == const.listRecTotalNum:  # 推荐数量够
                        return Response(resultList, status=status.HTTP_200_OK)
                    else:
                        randList = redisfunc.strToSample(genListStr, const.listRecTotalNum)
                        resultList.extend(randList)
                        return Response(resultList, status=status.HTTP_200_OK)
            else:  # 基于用户和画单推荐表不存在
                resultList = redisfunc.strToSample(genListStr, const.listRecTotalNum)
                return Response(resultList, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
