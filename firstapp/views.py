from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, PostbackEvent, TextSendMessage
from module import func
from urllib.parse import parse_qsl

from firstapp.models import student
from django.shortcuts import render


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
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '#傳送文字':
                        func.sendText(event)

                    elif mtext == '#傳送圖片':
                        func.sendImage(event)

                    elif mtext == '#傳送貼圖':
                        func.sendStick(event)

                    elif mtext == '#多項傳送':
                        func.sendMulti(event)

                    elif mtext == '#傳送位置':
                        func.sendPosition(event)

                    elif mtext == '#快速選單':
                        func.sendQuickreply(event)

                    elif mtext == '@按鈕樣板':
                        func.sendButton(event)

                    elif mtext == '@購買披薩':
                        func.sendPizza(event)

                    elif mtext == '@確認樣板':
                        func.sendConfirm(event)

                    elif mtext == '@yes':
                        func.sendYes(event)

                    elif mtext == '@no':
                        func.sendNo(event)

                    elif mtext == '@轉盤樣板':
                        func.sendCarousel(event)

                    elif mtext == '@圖片樣板':
                        func.sendImgCarousel(event)

                    elif mtext == '@圖片地圖':
                        func.sendImgmap(event)

                    elif mtext == '@日期時間':
                        func.sendDatetime(event)

                    elif mtext == '@線上測試':
                        func.sendFlexMessage(event)
            elif isinstance(event, PostbackEvent):
                backdata = dict(parse_qsl(event.postback.data))
                if backdata.get('action') == 'buy':
                    message = TextSendMessage(
                        text='感謝您的購買，我們盡快為您製作',
                    )
                    line_bot_api.reply_message(event.reply_token, message)
                if backdata.get('action') == 'sell':
                    func.sendBack_sell(event, backdata)
                if backdata.get('action') == 'sell_time':
                    func.sendData_sell(event, backdata)
            return HttpResponse()

    else:
        return HttpResponseBadRequest()


def listone(request):
    try:
        unit = student.objects.get(cName="黃品綺")  # 讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())


def listall(request):
    students = student.objects.all().order_by('id')
    return render(request, "listall.html", locals())


def insert(request):  # 新增資料
    cName = '林三和'
    cSex = 'M'
    cBirthday = '1987-12-26'
    cEmail = 'miwamail@gmail.com'
    cPhone = '0963245612'
    cAddr = '新北市蘆洲區中正路243巷19號'
    unit = student.objects.create(
        cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr)
    unit.save()  # 寫入資料庫
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())


def modify(request):  # 修改資料
    unit = student.objects.get(cName='aa')
    unit.cName = '林和'
    unit.cBirthday = '1987-12-11'
    unit.cAddr = '新北市蘆洲區中正路185巷63號'
    unit.save()  # 寫入資料庫
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())


def delete(request, id=None):  # 刪除資料
    unit = student.objects.get(id=4)
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())
