from django.conf import settings

from linebot import LineBotApi
from linebot.models import *
import datetime
import json

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def sendText(event):
    try:
        message = TextSendMessage(
            text='嚕喵毛，換毛季是打掃季！',
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendImage(event):
    try:
        message = ImageSendMessage(
            original_content_url="https://imgur.com/TcSD7FL.png",
            preview_image_url="https://imgur.com/TcSD7FL.png"
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendStick(event):
    try:
        message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114124'
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendMulti(event):
    try:
        message = [
            TextSendMessage(
                text='嚕喵毛，換毛季是打掃季！',
            ),
            ImageSendMessage(
                original_content_url="https://imgur.com/TcSD7FL.png",
                preview_image_url="https://imgur.com/TcSD7FL.png"
            ),
            StickerSendMessage(
                package_id='11539',
                sticker_id='52114124'
            )

        ]

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendPosition(event):
    try:
        message = LocationSendMessage(
            title='台北教育大學',
            address='台北市大安區和平東路二段134號',
            latitude=25.024163,  # 緯度
            longitude=121.544888  # 經度

        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendQuickreply(event):
    try:
        message = TextSendMessage(
            text='嚕喵毛，今天要打掃哪裡呢？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="客廳", text="客廳")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="房間", text="房間")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="廚房", text="廚房")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="廁所", text="廁所")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="不想打掃", text="不想打掃")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def sendButton(event):
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/pRdaAmS.jpg',
                title='按鈕樣板範例',
                text='請選擇：',
                actions=[
                    MessageTemplateAction(
                        label='文字訊息',
                        text='@購買披薩'
                    ),
                    URITemplateAction(
                        label='連結網頁',
                        uri='https://www.grazie.com.tw/menu#food=1&meal=1'
                    ),
                    PostbackTemplateAction(
                        label='回傳訊息',
                        data='action=buy'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendPizza(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，我們盡快為您製作',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendBack_buy(event, backdata):
    try:
        text1 = '感謝您的購買，我們盡快為您製作。(action 的值為' + backdata.get('action') + ')'

        message = TextSendMessage(
            text=text1
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendConfirm(event):
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ConfirmTemplate(
                text='確認是否購買這項產品？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，\n我們會盡快寄出商品',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendNo(event):
    try:
        message = TextSendMessage(
            text='期待下次為您服務~',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendCarousel(event):
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/pRdaAmS.jpg',
                        title='PIZZA 樣板',
                        text='PIZZA 轉盤樣板',
                        actions=[
                            URITemplateAction(
                                label='連結披薩菜單網頁',
                                uri='https://www.grazie.com.tw/'
                            ),
                            PostbackTemplateAction(
                                label='選擇披薩',
                                data='action=sell&item=披薩'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/MyLoA5d.jpg',
                        title='DRINK 樣板',
                        text='DRINK 轉盤樣板二',
                        actions=[
                            URITemplateAction(
                                label='連結飲料菜單網頁',
                                uri='https://www.facebook.com/'
                            ),
                            PostbackTemplateAction(
                                label='選擇飲料',
                                data='action=sell&item=飲料'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendImgCarousel(event):
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/pRdaAmS.jpg',
                        action=PostbackTemplateAction(
                            label='選擇披薩',
                            text='選擇披薩',
                            data='action=sell&item=披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MyLoA5d.jpg',
                        action=PostbackTemplateAction(
                            label='選擇飲料',
                            text='選擇飲料',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )

        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendBack_sell(event, backdata):
    try:
        message = TextSendMessage(
            text='你選擇的是'+backdata.get('item')
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendImgmap(event):
    try:
        image_url = 'https://i.imgur.com/Yz2yzve.jpg'
        imgwidth = 1040
        imgheight = 300

        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),
            actions=[
                MessageImagemapAction(
                    text='選擇紅色',
                    area=ImagemapArea(  # 設定圖片範圍左方1/4
                        x=0,
                        y=0,
                        width=imgwidth * 0.25,
                        height=imgheight
                    )
                ),
                MessageImagemapAction(
                    text='選擇藍色',
                    area=ImagemapArea(  # 設定圖片範圍右方1/4
                        x=imgwidth * 0.75,
                        y=0,
                        width=imgwidth * 0.25,
                        height=imgheight
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendDatetime(event):
    try:
        message = TemplateSendMessage(
            alt_text="日期時間範例",
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/pRdaAmS.jpg',
                title='日期時間練習',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label="選取日期",
                        data="action=sell_time&mode=date",
                        mode="date",
                        initial="2022-09-24",
                        min="2022-03-24",
                        max="2022-12-25"
                    ),
                    DatetimePickerTemplateAction(
                        label="選取時間",
                        data="action=sell_time&mode=time",
                        mode="time",
                        initial="10:00",
                        min="00:00",
                        max="23:59"
                    ),
                    DatetimePickerTemplateAction(
                        label="選取日期時間",
                        data="action=sell_time&mode=datetime",
                        mode="datetime",
                        initial="2022-09-24T10:00",
                        min="2022-03-24T00:00",
                        max="2022-12-25T23:59"
                    )
                ]

            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendData_sell(event, backdata):
    try:
        if backdata.get('mode') == 'date':
            dt = '日期為：' + event.postback.params.get('date')
        elif backdata.get('mode') == 'time':
            dt = '時間為：' + event.postback.params.get('time')

        elif backdata.get('mode') == 'datetime':
            # 讀取日期時間
            dt = datetime.datetime.strptime(
                event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')

            # 轉為字串
            dt = dt.strftime(
                '{d}%Y-%m-%d, {t}%H:%M').format(d='日期為:', t='時間為:')

        message = TextSendMessage(
            text=dt
        )

        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))


def sendFlexMessage(event):
    try:
        flex_message = FlexSendMessage(
            alt_text="flex message",
            contents={
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Flex Message Corp",
                            "color": "#FFFFFF",
                            "weight": "bold"
                        }
                    ]
                },
                "hero": {
                    "type": "image",
                    "url": "https://apng.onevcat.com/assets/elephant.png",
                    "size": "xl",
                    "align": "center"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Cassie Huang",
                            "align": "center",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "Software Engineer",
                            "align": "center"
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "Visit my website",
                                "uri": "https://pinqih.github.io/MeetMe/"
                            }
                        }
                    ]
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#00B900"
                    }
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤!'))
