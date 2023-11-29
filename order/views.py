from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import parse_qsl
from module import func

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    PostbackEvent,
    PostbackAction
)

from order.models import Order

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
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                mtext = event.message.text
                nn = event.source.user_id  # 儲存使用者 ID
                if mtext == "我要菜單":
                    func.sendMenu(event)
                elif mtext == "我要點餐":
                    func.sendButton(event)
                elif mtext[:2] == "改成":
                    stuff = mtext[3:]  # 拿取修改哪項項目的名稱，EX：飲料
                    func.sendback_modifyConfirm(event, stuff, nn)
            if isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                result = event.postback.data[2:].split('&')
                nn = event.source.user_id  # 儲存使用者 ID

                if backdata.get('action') == '啪噠原茶':
                    func.sendback_original(event, backdata)

                elif backdata.get('action') == '精靈純鮮奶茶':
                    func.sendback_pure(event, backdata)

                elif backdata.get('action') == '啪噠奶茶':
                    func.sendback_milktea(event, backdata)

                elif event.postback.data[0:1] == "A":
                    ice = event.postback.data[2:]
                    func.sendback_ice(event, backdata, ice)

                elif event.postback.data[0:1] == "B":
                    suger = event.postback.data[2:]
                    func.sendback_suger(event, backdata, suger)

                elif event.postback.data[0:1] == "C":
                    add = event.postback.data[2:]
                    func.sendback_add(event, backdata, add)

                elif event.postback.data[0:1] == "D":
                    num = event.postback.data[2:]
                    func.sendback_num(event, backdata, num)

                # 確認當前輸入的訂單
                elif event.postback.data[0:1] == "E":
                    func.sendback_confirm(event, backdata, result, nn)

                elif event.postback.data[0:1] == "G":  # 繼續購物
                    func.sendButton_Again(event)

                elif event.postback.data[0:1] == "F":  # 結帳
                    func.sendRECEIPT(event, nn)

                elif event.postback.data[0:1] == "H":  # 修改哪一項訂單
                    func.sendback_which(event, backdata)

                elif event.postback.data[0:2] == "M1":  # 修改飲料
                    func.sendModifyButton(event, backdata)

                elif backdata.get('action') == 'M啪噠原茶':
                    func.sendback_Modifyoriginal(event, backdata)

                elif backdata.get('action') == 'M精靈純鮮奶茶':
                    func.sendback_Modifypure(event, backdata)

                elif backdata.get('action') == 'M啪噠奶茶':
                    func.sendback_Modifymilktea(event, backdata)

                elif event.postback.data[0:2] == "M2":  # 修改數量
                    func.sendback_Modifynum(event, backdata)

                elif event.postback.data[0:2] == "M3":  # 修改糖度
                    func.sendback_Modifysuger(event, backdata)

                elif event.postback.data[0:2] == "M4":  # 修改冰塊
                    func.sendback_Modifyice(event, backdata)

                elif event.postback.data[0:2] == "M5":  # 修改加料
                    func.sendback_Modifyadd(event, backdata)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
