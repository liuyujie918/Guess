from django.test import TestCase

# Create your tests here.
import const.redisfunc as redisfunc
from singlerec.serializers import SingleRecSerializer


r = redisfunc.redisconn
print('yes')
