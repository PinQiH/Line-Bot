from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import parse_qsl
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from module import func

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext = event.message.text
                if mtext == '成員介紹':
                    func.sendIntro(event)
            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == '第一隻喵':
                    func.sendBack_cat01(event, backdata)
                elif backdata.get('action') == '第二隻喵':
                    func.sendBack_cat02(event, backdata)
                elif backdata.get('action') == '第三隻喵':
                    func.sendBack_cat03(event, backdata)
            return HttpResponse()
    else:
        return HttpResponseBadRequest()
