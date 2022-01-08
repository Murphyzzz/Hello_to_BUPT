import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
        "address":"北京市海淀区西三旗街道君安家园(西区)君安家园西区",
        "area":"北京市  海淀区",
        "bztcyy":"",
        "city":"北京市",
        "csmjry":"0",
        "fjqszgjdq":"",
        "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_462438_\",\"position\":{\"Q\":40.04175,\"R\":116.34296,\"lng\":116.34296,\"lat\":40.04175},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"西三旗\",\"id\":\"110108\",\"location\":{\"Q\":40.05349,\"R\":116.35109599999998,\"lng\":116.351096,\"lat\":40.05349}},{\"name\":\"清河\",\"id\":\"110108\",\"location\":{\"Q\":40.040177,\"R\":116.34281499999997,\"lng\":116.342815,\"lat\":40.040177}},{\"name\":\"永泰\",\"id\":\"110108\",\"location\":{\"Q\":40.03475,\"R\":116.35658000000001,\"lng\":116.35658,\"lat\":40.03475}}],\"neighborhoodType\":\"商务住宅;住宅区;住宅小区\",\"neighborhood\":\"君安家园(西区)\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"营福路\",\"streetNumber\":\"9号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"towncode\":\"110108019000\",\"township\":\"西三旗街道\"},\"formattedAddress\":\"北京市海淀区西三旗街道君安家园(西区)君安家园西区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
        "glksrq":"",
        "gllx":"",
        "gtjzzchdfh":"",
        "gtjzzfjsj":"",
        "ismoved":"0",
        "jcbhlx":"",
        "jcbhrq":"",
        "jchbryfs":"",
        "jcjgqr":"0",
        "jcwhryfs":"",
        "jhfjhbcc":"",
        "jhfjjtgj":"",
        "jhfjrq":"",
        "mjry":"0",
        "province":"北京市",
        "qksm":"",
        "remark":"",
        "sfcxtz":"0",
        "sfcxzysx":"0",
        "sfcyglq":"0",
        "sfjcbh":"0",
        "sfjchbry":"0",
        "sfjcwhry":"0",
        "sfjzdezxgym":"1",
        "sfjzxgym":"1",
        "sfsfbh":"0",
        "sftjhb":"0",
        "sftjwh":"0",
        "sfxk":"0",
        "sfygtjzzfj":"",
        "sfyyjc":"0",
        "sfzx":1,
        "szcs":"",
        "szgj":"",
        "szsqsfybl":"0",
        "tw":"2",
        "xjzd":"",
        "xkqq":"",
        "xwxgymjzqk":"3",
        "ymjzxgqk":"已接种",
        "zgfxdq":"0"
        }"""

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

