#coding:utf-8
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SingleRecSerializer
import random
import json
import const.const as const
import const.redisfunc as redisfunc

class SingleRecView(APIView):
    def post(self, request, format=None):
        serializer = SingleRecSerializer(data=request.data)
        if serializer.is_valid():
            r = redisfunc.redisconn
            uid = serializer.data["uid"]
            lid = serializer.data["lid"]
            # 画单推荐radis
            genSingleKey = const.key_Rec_Single_General  # 通用推荐表
            uidSingleKey = const.key_Rec_Single_UI + str(uid)  # 基于用户推荐表
            lidSingleKey = const.key_Rec_Single_LI + str(lid)  # 基于画单推荐表
            # 返回字符串
            genSingleStr = r.get(genSingleKey)
            uidSingleStr = r.get(uidSingleKey)
            lidSingleStr = r.get(lidSingleKey)
            resultSingle = []

            if uidSingleStr or lidSingleStr:  # 基于用户和画单推荐表存在
                resultSingle1 = redisfunc.strToSample(uidSingleStr, const.SingleRecUidNum)  # 基于用户
                resultSingle.extend(resultSingle1)
                resultSingle2 = redisfunc.strToSample(lidSingleStr, const.SingleRecLidNum)  # 基于画单
                resultSingle.extend(resultSingle2)

                if len(resultSingle) == const.SingleRecTotalNum:  # 推荐数量够
                    return Response(resultSingle, status=status.HTTP_200_OK)
                else:  # 推荐数量不够
                    lack = const.SingleRecTotalNum - len(resultSingle)
                    if len(redisfunc.strToSingle(uidSingleStr)) < const.SingleRecUidNum:
                        resultSingle3 = redisfunc.strToSample(lidSingleStr, lack)
                        resultSingle.extend(resultSingle3)
                    elif len(redisfunc.strToSingle(lidSingleStr)) < const.SingleRecUidNum:
                        resultSingle3 = redisfunc.strToSample(uidSingleStr, lack)
                        resultSingle.extend(resultSingle3)

                    if len(resultSingle) == const.SingleRecTotalNum:  # 推荐数量够
                        return Response(resultSingle, status=status.HTTP_200_OK)
                    else:
                        randSingle = redisfunc.strToSample(genSingleStr, const.SingleRecTotalNum)
                        resultSingle.extend(randSingle)
                        return Response(resultSingle, status=status.HTTP_200_OK)
            else:  # 基于用户和画单推荐表不存在
                resultSingle = redisfunc.strToSample(genSingleStr, const.SingleRecTotalNum)
                return Response(resultSingle, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
