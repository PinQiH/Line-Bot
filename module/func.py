from django.conf import settings

from linebot import LineBotApi
from linebot.models import *
import datetime
import json
from linebot.models import FlexSendMessage
from linebot.models.flex_message import (
    BubbleContainer, ImageComponent, BoxComponent
)
from linebot.models.actions import URIAction
from order.models import Order

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

menu = {"M啪噠紅茶": "30", "L啪噠紅茶": "40",

        "M四季烏龍": "35", "L四季烏龍": "45",

        "M啪噠普洱茶": "40", "L啪噠普洱茶": "50",

        "M啪噠焙茶": "40", "L啪噠焙茶": "50",

        "M精靈珍珠黑糖鮮奶茶": "65", "L精靈珍珠黑糖鮮奶茶": "75",

        "M深焙鮮奶茶": "60", "L深焙鮮奶茶": "70",

        "M四季烏龍鮮奶茶": "55", "L四季烏龍鮮奶茶": "65",

        "M香芋鮮奶茶": "65", "L香芋鮮奶茶": "75",

        "M啪噠奶茶": "45", "L啪噠奶茶": "55",

        "M茉香奶綠": "45", "L茉香奶綠": "55",

        "M鐵觀音奶茶": "50", "L鐵觀音奶茶": "60",

        "M香芋奶綠": "55", "L香芋奶綠": "65",
        }
menu_e = {"M啪噠紅茶": "40", "L啪噠紅茶": "50",

          "M四季烏龍": "45", "L四季烏龍": "55",

          "M啪噠普洱茶": "50", "L啪噠普洱茶": "60",

          "M啪噠焙茶": "50", "L啪噠焙茶": "60",

          "M精靈珍珠黑糖鮮奶茶": "75", "L精靈珍珠黑糖鮮奶茶": "85",

          "M深焙鮮奶茶": "70", "L深焙鮮奶茶": "80",

          "M四季烏龍鮮奶茶": "65", "L四季烏龍鮮奶茶": "75",

          "M香芋鮮奶茶": "75", "L香芋鮮奶茶": "85",

          "M啪噠奶茶": "55", "L啪噠奶茶": "65",

          "M茉香奶綠": "55", "L茉香奶綠": "65",

          "M鐵觀音奶茶": "60", "L鐵觀音奶茶": "70",

          "M香芋奶綠": "65", "L香芋奶綠": "75",
          }
iceMenu = ['正常', '少冰', '微冰', '去冰', '常溫']
sugerMenu = ['全糖', '少糖', '半糖', '微糖', '無糖']
amountMenu = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
addMenu = ['黑糖珍珠', '蜂蜜白玉', '仙草', '小芋園', '椰果', '布丁', '不用加料']


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


def sendIntro(event):
    try:
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url="https://images.pexels.com/photos/160755/kittens-cats-foster-playing-160755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                title='成員介紹',
                text='請選擇',
                actions=[
                    PostbackTemplateAction(
                        label='第一隻喵',
                        text='第一隻喵',
                        data='action=第一隻喵'
                    ),
                    PostbackTemplateAction(
                        label='第二隻喵',
                        text='第二隻喵',
                        data='action=第二隻喵'
                    ),
                    PostbackTemplateAction(
                        label='第三隻喵',
                        text='第三隻喵',
                        data='action=第三隻喵'
                    )
                ]
            )

        )
        line_bot_api.reply_message(event.reply_token, message)

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='失敗'))


def sendBack_cat01(event, backdata):
    try:
        message_A = []
        message_A.append(TextSendMessage(text="我是喵仔"))
        message_A.append(ImageSendMessage(
            original_content_url="https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.png",
            preview_image_url="https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.png"
        ))
        line_bot_api.reply_message(event.reply_token, message_A)

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='失敗'))


def sendBack_cat02(event, backdata):
    try:
        message_A = []
        message_A.append(TextSendMessage(text="我是毛毛"))
        message_A.append(ImageSendMessage(
            original_content_url="https://images.pexels.com/photos/257532/pexels-photo-257532.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            preview_image_url="https://images.pexels.com/photos/257532/pexels-photo-257532.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        ))
        line_bot_api.reply_message(event.reply_token, message_A)

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='失敗'))


def sendBack_cat03(event, backdata):
    try:
        message_A = []
        message_A.append(TextSendMessage(text="我是嚕嚕"))
        message_A.append(ImageSendMessage(
            original_content_url="https://images.pexels.com/photos/1404819/pexels-photo-1404819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            preview_image_url="https://images.pexels.com/photos/1404819/pexels-photo-1404819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        ))
        line_bot_api.reply_message(event.reply_token, message_A)

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='失敗'))


def sendMenu(event):
    try:
        message = ImageSendMessage(
            original_content_url="https://raw.githubusercontent.com/shakuneko/pic0412/main/menu%20(1).jpg",
            preview_image_url="https://raw.githubusercontent.com/shakuneko/pic0412/main/menu%20(1).jpg"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendButton(event):
    try:
        # deleteData = order.objects.all()
        # deleteData.delete()

        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E6%88%91%E8%A6%81%E8%8F%9C%E5%96%AE.JPG",
                title='Menu',
                text='請問要哪個種類的飲料',
                actions=[
                    PostbackTemplateAction(
                        label='啪噠原茶',
                        text='啪噠原茶',
                        data='action=啪噠原茶'
                    ),
                    PostbackTemplateAction(
                        label='精靈純鮮奶茶',
                        text='精靈純鮮奶茶',
                        data='action=精靈純鮮奶茶'
                    ),
                    PostbackTemplateAction(
                        label='啪噠奶茶',
                        text='啪噠奶茶',
                        data='action=啪噠奶茶'
                    )

                ]
            )

        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_original(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='啪噠原茶',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠紅茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠紅茶',
                                        'text': '想喝 M 啪噠紅茶',
                                        'data': 'A&M啪噠紅茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠紅茶',
                                        'text': '想喝 L 啪噠紅茶',
                                        'data': 'A&L啪噠紅茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "四季烏龍",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 四季烏龍',
                                        'text': '想喝 M 四季烏龍',
                                        'data': 'A&M四季烏龍'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 四季烏龍',
                                        'text': '想喝 L 四季烏龍',
                                        'data': 'A&L四季烏龍'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠普洱茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠普洱茶',
                                        'text': '想喝 M 啪噠普洱茶',
                                        'data': 'A&M啪噠普洱茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠普洱茶',
                                        'text': '想喝 L 啪噠普洱茶',
                                        'data': 'A&L啪噠普洱茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠焙茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠焙茶',
                                        'text': '想喝 M 啪噠焙茶',
                                        'data': 'A&M啪噠焙茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠焙茶',
                                        'text': '想喝 L 啪噠焙茶',
                                        'data': 'A&L啪噠焙茶'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_pure(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='精靈純鮮奶茶',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "精靈珍珠黑糖鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 精靈珍珠黑糖鮮奶茶',
                                        'text': '想喝 M 精靈珍珠黑糖鮮奶茶',
                                        'data': 'A&M精靈珍珠黑糖鮮奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 精靈珍珠黑糖鮮奶茶',
                                        'text': '想喝 L 精靈珍珠黑糖鮮奶茶',
                                        'data': 'A&L精靈珍珠黑糖鮮奶茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "深焙鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 深焙鮮奶茶',
                                        'text': '想喝 M 深焙鮮奶茶',
                                        'data': 'A&M深焙鮮奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 深焙鮮奶茶',
                                        'text': '想喝 L 深焙鮮奶茶',
                                        'data': 'A&L深焙鮮奶茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "四季烏龍鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 四季烏龍鮮奶茶',
                                        'text': '想喝 M 四季烏龍鮮奶茶',
                                        'data': 'A&M四季烏龍鮮奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 四季烏龍鮮奶茶',
                                        'text': '想喝 L 四季烏龍鮮奶茶',
                                        'data': 'A&L四季烏龍鮮奶茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "香芋鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 香芋鮮奶茶',
                                        'text': '想喝 M 香芋鮮奶茶',
                                        'data': 'A&M香芋鮮奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 香芋鮮奶茶',
                                        'text': '想喝 L 香芋鮮奶茶',
                                        'data': 'A&L香芋鮮奶茶'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_milktea(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='啪噠奶茶',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠奶茶',
                                        'text': '想喝 M 啪噠奶茶',
                                        'data': 'A&M啪噠奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠奶茶',
                                        'text': '想喝 L 啪噠奶茶',
                                        'data': 'A&L啪噠奶茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "茉香奶綠",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 茉香奶綠',
                                        'text': '想喝 M 茉香奶綠',
                                        'data': 'A&M茉香奶綠'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 茉香奶綠',
                                        'text': '想喝 L 茉香奶綠',
                                        'data': 'A&L茉香奶綠'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "鐵觀音奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 鐵觀音奶茶',
                                        'text': '想喝 M 鐵觀音奶茶',
                                        'data': 'A&M鐵觀音奶茶'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 鐵觀音奶茶',
                                        'text': '想喝 L 鐵觀音奶茶',
                                        'data': 'A&L鐵觀音奶茶'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "香芋奶綠",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 香芋奶綠',
                                        'text': '想喝 M 香芋奶綠',
                                        'data': 'A&M香芋奶綠'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 香芋奶綠',
                                        'text': '想喝 L 香芋奶綠',
                                        'data': 'A&L香芋奶綠'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_ice(event, backdata, ice):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B8%B8%E6%BA%AB-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='常溫',
                            text='想要 常溫',
                            data='B&' + ice + '&常溫'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%8E%BB%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='去冰',
                            text='想要 去冰',
                            data='B&' + ice + '&去冰'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%BE%AE%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='微冰',
                            text='想要 微冰',
                            data='B&' + ice + '&微冰'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B0%91%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='少冰',
                            text='想要 少冰',
                            data='B&' + ice + '&少冰'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E6%AD%A3%E5%B8%B8-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='正常',
                            text='想要 正常',
                            data='B&' + ice + '&正常'
                        )
                    ),
                ]
            )
        )

        message = FlexSendMessage(alt_text="冰塊", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='ice no'))


def sendback_suger(event, backdata, suger):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E7%84%A1%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='無糖',
                            text='想要 無糖',
                            data='C&' + suger + '&無糖'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%BE%AE%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='微糖',
                            text='想要 微糖',
                            data='C&' + suger + '&微糖'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%8D%8A%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='半糖',
                            text='想要 半糖',
                            data='C&' + suger + '&半糖'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B0%91%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='少糖',
                            text='想要 少糖',
                            data='C&' + suger + '&少糖'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%85%A8%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='全糖',
                            text='想要 全糖',
                            data='C&' + suger + '&全糖'
                        )
                    ),
                ]
            )
        )

        message = FlexSendMessage(alt_text="糖度", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='suger no'))


def sendback_add(event, backdata, add):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                background_color='#DBD3D8',
                contents=[
                    TextComponent(
                        text="加料 +10，只能選一種!",
                        size="md",
                        weight="bold",
                        margin="sm"
                    )
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                margin="sm",
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E9%BB%91%E7%B3%96%E7%8F%8D%E7%8F%A0.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='黑糖珍珠',
                                    text='想要 黑糖珍珠',
                                    data='D&' + add + '&黑糖珍珠'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E6%A4%B0%E6%9E%9C.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='椰果',
                                    text='想要 椰果',
                                    data='D&' + add + '&椰果'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E5%B0%8F%E8%8A%8B%E5%9C%93.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='小芋圓',
                                    text='想要 小芋圓',
                                    data='D&' + add + '&小芋圓'
                                )
                            ),
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E8%9C%82%E8%9C%9C%E7%99%BD%E7%8E%89.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='蜂蜜白玉',
                                    text='想要 蜂蜜白玉',
                                    data='D&' + add + '&蜂蜜白玉'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E4%BB%99%E8%8D%89.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='仙草',
                                    text='想要 仙草',
                                    data='D&' + add + '&仙草'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E5%B8%83%E4%B8%81.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='布丁',
                                    text='想要 布丁',
                                    data='D&' + add + '&布丁'
                                )
                            ),
                        ]
                    ),
                ]
            ),
            footer=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ButtonComponent(
                        style='secondary',
                        color="#C4DABB",
                        action=PostbackTemplateAction(
                            label='不用加料',
                            text='想要 不用加料',
                            data='D&' + add + '&不用加料'
                        )
                    )
                ]
            )

        )

        message = FlexSendMessage(alt_text="加料嗎", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不add'))


def sendback_num(event, backdata, num):
    try:
        message = TextSendMessage(
            text='請問要幾份',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(
                    label="1", text="1份", data='E&' + num + '&1')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="2", text="2份", data='E&' + num + '&2')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="3", text="3份", data='E&' + num + '&3')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="4", text="4份", data='E&' + num + '&4')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="5", text="5份", data='E&' + num + '&5')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="6", text="6份", data='E&' + num + '&6')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="7", text="7份", data='E&' + num + '&7')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="8", text="8份", data='E&' + num + '&8')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="9", text="9份", data='E&' + num + '&9')),

            ]))

        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不買'))


def sendback_confirm(event, backdata, result, nn):  # 點完加料
    try:
        drink = result[0]
        ice = result[1]
        suger = result[2]
        add = result[3]
        amount = result[4]
        uid = nn

        if add == "不用加料":
            price = menu[drink]
        else:
            price = menu_e[drink]

        # 將資料新增到資料庫
        unit = Order.objects.create(
            drink=drink, ice=ice, suger=suger, add=add, price=price, amount=amount, uid=uid)
        unit.save()

        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                # background_color='#DBD3D8',
                contents=[
                    TextComponent(
                        text="已加入： " + amount + " 杯 " + drink,
                        size="md",
                        weight="bold",
                    ),
                    SeparatorComponent(
                        color="#C8BCC3",
                        margin="xxl"
                    ),
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(
                        text="\n冰塊：" + ice
                    ),
                    TextComponent(
                        text="\n糖度：" + suger
                    ),
                    TextComponent(
                        text="\n加料：" + add
                    ),
                    TextComponent(
                        text=" 加料 + 10 元喔!",
                        color="#C8BCC3",
                        size="xs",
                        margin='xs'
                    ),
                    TextComponent(
                        text="\n一杯單價：" + price
                    ),
                    TextComponent(
                        text="\n"
                    ),
                    TextComponent(
                        text="\n請問要結束購買嗎",
                        weight="bold",
                    ),
                ]
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ButtonComponent(
                                style='secondary',
                                color="#E8F1E4",
                                action=PostbackTemplateAction(
                                    label='修改此筆訂單',
                                    text='修改此筆訂單',
                                    data='H'
                                )
                            ),
                            ButtonComponent(
                                style='secondary',
                                color="#C4DABB",
                                action=PostbackTemplateAction(
                                    label='繼續購物',
                                    text='繼續購物',
                                    data='G'
                                )
                            )
                        ]
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#F6DCCB",
                        action=PostbackTemplateAction(
                            label='結帳',
                            text='結帳',
                            data='F'
                        )
                    )
                ]
            )
        )

        message = FlexSendMessage(alt_text="確認訂單", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendButton_Again(event):
    try:
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E6%88%91%E8%A6%81%E8%8F%9C%E5%96%AE.JPG",
                title='Menu',
                text='請問要哪個種類的飲料',
                actions=[
                    PostbackTemplateAction(
                        label='啪噠原茶',
                        text='啪噠原茶',
                        data='action=啪噠原茶'
                    ),
                    PostbackTemplateAction(
                        label='精靈純鮮奶茶',
                        text='精靈純鮮奶茶',
                        data='action=精靈純鮮奶茶'
                    ),
                    PostbackTemplateAction(
                        label='啪噠奶茶',
                        text='啪噠奶茶',
                        data='action=啪噠奶茶'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendRECEIPT(event, nn):
    try:
        messageA = []
        uid = nn
        orders = Order.objects.filter(
            uid=uid, is_checkout=False).order_by('id')

        if not orders.exists():
            messageA.append(TextSendMessage(text="目前沒有尚未結帳的訂單。"))
            line_bot_api.reply_message(event.reply_token, messageA)
            return

        total = 0
        text1 = ""
        drinkA = ""
        iceA = ""
        sugerA = ""
        addA = ""
        priceA = ""
        amountA = ""
        tt = ""

        for order in orders:
            drink = order.drink
            ice = order.ice
            suger = order.suger
            add = order.add
            amount = order.amount
            price = int(order.price)

            m = int(amount)

            # 將同項目資料做整理
            text1 += "\n"
            drinkA += "\n" + drink
            iceA += "\n" + ice
            sugerA += "\n" + suger
            addA += "\n" + add
            amountA += "\n" + str(amount)
            priceA += "\n$" + str(price)

            tt += f"\n{drink}：{ice}，{suger}，{add}"
            total += int(price) * int(amount)

        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(
                        text="結帳 RECEIPT",
                        color="#CCAE8F",
                        size="md",
                        weight="bold",
                    ),
                    TextComponent(
                        text="啪噠啪噠河馬",
                        size="35px",
                        weight="bold",
                        wrap=True,
                        margin="md"
                    ),
                    TextComponent(
                        text="河馬調製的茶飲能讓您開心一整天!",
                        size="xs",
                        weight="bold",
                        color="#C8BCC3",
                    ),
                    SeparatorComponent(
                        color="#C8BCC3",
                        margin="xxl"
                    ),
                    BoxComponent(
                        layout="vertical",
                        margin="xxl",
                        spacing="sm",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(
                                        text='飲料',
                                        color="#4B8F8C",
                                        flex=4,
                                        size="sm",
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text='杯',
                                        color="#4B8F8C",
                                        align="end",
                                        size="sm",
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text='單價',
                                        color="#4B8F8C",
                                        align="end",
                                        size="sm",
                                        wrap=True
                                    ),
                                ]
                            ),
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(
                                        text=drinkA,
                                        color="#555555",
                                        flex=4,
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text=amountA,
                                        color="#111111",
                                        align="end",
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text=priceA,
                                        color="#C171BD",
                                        align="end",
                                        wrap=True
                                    ),
                                ]
                            )
                        ]
                    ),
                    SeparatorComponent(
                        color="#C8BCC3",
                        margin="xxl"
                    ),
                    BoxComponent(
                        layout="vertical",
                        margin="xxl",
                        spacing="sm",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(
                                        text='詳細飲料清單',
                                        color="#4B8F8C",
                                        size="sm",
                                        wrap=True
                                    ),
                                ]
                            ),
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(
                                        text=tt,
                                        color="#555555",
                                        flex=0,
                                        wrap=True
                                    ),
                                ]
                            )
                        ]
                    ),
                    SeparatorComponent(
                        color="#C8BCC3",
                        margin="xxl"
                    ),
                    BoxComponent(
                        layout="vertical",
                        margin="xxl",
                        spacing="sm",
                        contents=[
                            BoxComponent(
                                layout="horizontal",
                                contents=[
                                    TextComponent(
                                        text="飲料總杯數",
                                        color="#555555",
                                        flex=0,
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text=str(m),
                                        color="#111111",
                                        align="end",
                                        wrap=True
                                    ),
                                ]
                            ),
                            BoxComponent(
                                layout="horizontal",
                                margin="xl",
                                contents=[
                                    TextComponent(
                                        text="總價",
                                        color="#C171BD",
                                        flex=0,
                                        size="xl",
                                        wrap=True
                                    ),
                                    TextComponent(
                                        text="$" + str(total),
                                        color="#C171BD",
                                        align="end",
                                        size="xl",
                                        wrap=True
                                    ),
                                ]
                            )
                        ]
                    ),
                ]
            ),
        )

        messageA.append(FlexSendMessage(alt_text="結帳", contents=bubble))
        messageA.append(TextSendMessage(text="我們會盡快幫您準備飲料，請您稍等片刻~"))
        Order.objects.filter(
            uid=uid, is_checkout=False).update(is_checkout=True)
        line_bot_api.reply_message(event.reply_token, messageA)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='結帳錯誤'))


def sendback_which(event, backdata):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                background_color='#DBD3D8',
                contents=[
                    TextComponent(
                        text="請問要修改此訂單的哪個項",
                        size="md",
                        weight="bold",
                    ),
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[

                    ButtonComponent(
                        style='secondary',
                        color="#E8F1E4",
                        action=PostbackTemplateAction(
                            label='飲料品項',
                            text='要修改飲料品項',
                            data='M1&'
                        )
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#E8F1E4",
                        action=PostbackTemplateAction(
                            label='數量',
                            text='要修改數量',
                            data='M2&'
                        )
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#E8F1E4",
                        action=PostbackTemplateAction(
                            label='糖度',
                            text='要修改糖度',
                            data='M3&'
                        )
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#E8F1E4",
                        action=PostbackTemplateAction(
                            label='冰塊',
                            text='要修改冰塊',
                            data='M4&'
                        )
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#E8F1E4",
                        action=PostbackTemplateAction(
                            label='加料',
                            text='要修改加料',
                            data='M5&'
                        )
                    ),
                ]
            ),
        )

        message = FlexSendMessage(alt_text="修改哪項訂單", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendModifyButton(event, backdata):
    try:
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E6%88%91%E8%A6%81%E8%8F%9C%E5%96%AE.JPG",
                title='Menu',
                text='請問要哪個種類的飲料',
                actions=[
                    PostbackTemplateAction(
                        label='啪噠原茶',
                        text='啪噠原茶',
                        data='action=M啪噠原茶'
                    ),
                    PostbackTemplateAction(
                        label='精靈純鮮奶茶',
                        text='精靈純鮮奶茶',
                        data='action=M精靈純鮮奶茶'
                    ),
                    PostbackTemplateAction(
                        label='啪噠奶茶',
                        text='啪噠奶茶',
                        data='action=M啪噠奶茶'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_Modifyoriginal(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='啪噠原茶',
            contents={
                "type": "carousel",

                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#DBD3D8",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠紅茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠紅茶',
                                        'text': '改成 M啪噠紅茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠紅茶',
                                        'text': '改成 L啪噠紅茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "backgroundColor": "#DBD3D8",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "四季烏龍",
                                    # "color":"#9A8492",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 四季烏龍',
                                        'text': '改成 M四季烏龍',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 四季烏龍',
                                        'text': '改成 L四季烏龍',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "backgroundColor": "#DBD3D8",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠普洱茶",
                                    # "color":"#9A8492",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠普洱茶',
                                        'text': '改成 M啪噠普洱茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠普洱茶',
                                        'text': '改成 L啪噠普洱茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "backgroundColor": "#DBD3D8",
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠焙茶",
                                    # "color":"#9A8492",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠焙茶',
                                        'text': '改成 M啪噠焙茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠焙茶',
                                        'text': '改成 L啪噠焙茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='修改啪噠原茶失敗'))


def sendback_Modifypure(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='精靈純鮮奶茶',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "精靈珍珠黑糖鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 精靈珍珠黑糖鮮奶茶',
                                        'text': '改成 M 精靈珍珠黑糖鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 精靈珍珠黑糖鮮奶茶',
                                        'text': '改成 L 精靈珍珠黑糖鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "深焙鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 深焙鮮奶茶',
                                        'text': '改成 M 深焙鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 深焙鮮奶茶',
                                        'text': '改成 L 深焙鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "四季烏龍鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 四季烏龍鮮奶茶',
                                        'text': '改成 M 四季烏龍鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 四季烏龍鮮奶茶',
                                        'text': '改成 L 四季烏龍鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "香芋鮮奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 香芋鮮奶茶',
                                        'text': '改成 M 香芋鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 香芋鮮奶茶',
                                        'text': '改成 L 香芋鮮奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_Modifymilktea(event, backdata):
    try:
        flex_message = FlexSendMessage(
            alt_text='啪噠奶茶',
            contents={
                "type": "carousel",
                "contents": [
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "啪噠奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%B4%85%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',

                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 啪噠奶茶',
                                        'text': '改成 M 啪噠奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 啪噠奶茶',
                                        'text': '改成 L 啪噠奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "茉香奶綠",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%9B%9B%E5%AD%A3%E7%83%8F%E9%BE%8D.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 茉香奶綠',
                                        'text': '改成 M 茉香奶綠',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 茉香奶綠',
                                        'text': '改成 L 茉香奶綠',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "鐵觀音奶茶",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E6%99%AE%E6%B4%B1%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 鐵觀音奶茶',
                                        'text': '改成 M 鐵觀音奶茶',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 鐵觀音奶茶',
                                        'text': '改成 L 鐵觀音奶茶',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                    {
                        'type': 'bubble',
                        'direction': 'ltr',
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "香芋奶綠",
                                    "weight": "bold",
                                    "margin": "sm",
                                    "size": "md",
                                    "wrap": True
                                }
                            ]
                        },
                        'hero': {
                            'type': 'image',
                            'url': 'https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%A3%B2%E6%96%99/%E5%95%AA%E5%99%A0%E7%84%99%E8%8C%B6.JPG',
                            'size': 'full',
                            'aspectRatio': '1:1',
                            'aspectMode': 'cover',
                        },
                        'body': {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#F6DCCB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'M 香芋奶綠',
                                        'text': '改成 M 香芋奶綠',
                                        'data': 'do'
                                    }
                                },
                                {
                                    "type": "button",
                                    "style": "secondary",
                                    "color": "#C4DABB",
                                    "action": {
                                        'type': 'postback',
                                        'label': 'L 香芋奶綠',
                                        'text': '改成 L 香芋奶綠',
                                        'data': 'do'
                                    }
                                },
                            ]
                        }
                    },
                ]
            }
        )

        line_bot_api.reply_message(event.reply_token, flex_message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不'))


def sendback_modifyConfirm(event, stuff, nn):  # 點完加料
    try:
        uid = nn
        p = Order.objects.filter(
            uid=uid, is_checkout=False).order_by('id').last()
        stuff = stuff.replace(" ", "")

        if stuff in menu:
            p.drink = stuff
            p.price = menu[stuff]
            p.save()
            whichOne = "飲料品項"
        elif stuff in iceMenu:
            p.ice = stuff
            p.save()
            whichOne = "冰塊"
        elif stuff in sugerMenu:
            p.suger = stuff
            p.save()
            whichOne = "糖度"
        elif stuff[:1] in amountMenu:
            stuff = stuff[:1]
            p.amount = stuff
            p.save()
            whichOne = "數量"
        elif stuff in addMenu:
            p.add = stuff
            p.save()
            whichOne = "加料"

        drink = p.drink
        ice = p.ice
        suger = p.suger
        add = p.add
        amount = p.amount

        if add == "不用加料":  # 判斷價格
            p.price = menu[drink]
            p.save()
        else:
            p.price = menu_e[drink]
            p.save()
        price = p.price

        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                background_color='#DBD3D8',
                contents=[
                    TextComponent(
                        text="確認修改訂單",
                        size="md",
                        weight="bold",
                    ),
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(
                        text="\n修改 " + whichOne + " 為： " + stuff,
                        weight="bold",
                        wrap=True
                    ),
                    TextComponent(
                        text="\n"
                    ),
                    TextComponent(
                        text="\n修改後訂單全貌："
                    ),
                    TextComponent(
                        text="\n飲料品項：" + drink
                    ),
                    TextComponent(
                        text="\n數量：" + str(amount)
                    ),
                    TextComponent(
                        text="\n冰塊：" + ice
                    ),
                    TextComponent(
                        text="\n糖度：" + suger
                    ),
                    TextComponent(
                        text="\n加料：" + add
                    ),
                    TextComponent(
                        text=" 加料 + 10 元喔!",
                        color="#C8BCC3",
                        size="xs",
                        margin='xs'
                    ),
                    TextComponent(
                        text="\n一杯單價：" + str(price)
                    ),
                    TextComponent(
                        text="\n"
                    ),
                    TextComponent(
                        text="\n請問要結束購買嗎",
                        weight="bold",
                    ),
                ]
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ButtonComponent(
                                style='secondary',
                                color="#E8F1E4",
                                action=PostbackTemplateAction(
                                    label='修改此筆訂單',
                                    text='修改此筆訂單',
                                    data='H'
                                )
                            ),
                            ButtonComponent(
                                style='secondary',
                                color="#C4DABB",
                                action=PostbackTemplateAction(
                                    label='繼續購物',
                                    text='繼續購物',
                                    data='G'
                                )
                            )
                        ]
                    ),
                    ButtonComponent(
                        style='secondary',
                        color="#F6DCCB",
                        action=PostbackTemplateAction(
                            label='結帳',
                            text='結帳',
                            data='F'
                        )
                    )
                ]
            )
        )

        message = FlexSendMessage(alt_text="修改後訂單", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='修改失敗'))


def sendback_Modifyadd(event, backdata):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                background_color='#DBD3D8',
                contents=[
                    TextComponent(
                        text="加料 +10，只能選一種!",
                        size="md",
                        weight="bold",
                        margin="sm"
                    )
                ]
            ),
            body=BoxComponent(
                layout='vertical',
                margin="sm",
                contents=[
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E9%BB%91%E7%B3%96%E7%8F%8D%E7%8F%A0.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='黑糖珍珠',
                                    text='改成 黑糖珍珠',
                                    data='aa'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E6%A4%B0%E6%9E%9C.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='椰果',
                                    text='改成 椰果',
                                    data='aa'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E5%B0%8F%E8%8A%8B%E5%9C%93.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='小芋圓',
                                    text='改成 小芋圓',
                                    data='aa'
                                )
                            ),
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        spacing='xs',
                        contents=[
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E8%9C%82%E8%9C%9C%E7%99%BD%E7%8E%89.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='蜂蜜白玉',
                                    text='改成 蜂蜜白玉',
                                    data='aa'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E4%BB%99%E8%8D%89.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='仙草',
                                    text='改成 仙草',
                                    data='aa'
                                )
                            ),
                            ImageComponent(
                                url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E9%85%8D%E6%96%99/%E5%B8%83%E4%B8%81.JPG",
                                size="lg",
                                aspect_mode="cover",
                                action=PostbackTemplateAction(
                                    label='布丁',
                                    text='改成 布丁',
                                    data='aa'
                                )
                            ),
                        ]
                    ),
                ]
            ),
            footer=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ButtonComponent(
                        style='secondary',
                        color="#C4DABB",
                        action=PostbackTemplateAction(
                            label='不用加料',
                            text='改成 不用加料',
                            data='aa'
                        )
                    )
                ]
            )
        )

        message = FlexSendMessage(alt_text="修改加料", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='無法修改加料'))


def sendback_Modifynum(event, backdata):
    try:
        message = TextSendMessage(
            text='請問要改成幾份',
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackTemplateAction(
                    label="1", text="改成 1份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="2", text="改成 2份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="3", text="改成 3份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="4", text="改成 4份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="5", text="改成 5份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="6", text="改成 6份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="7", text="改成 7份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="8", text="改成 8份", data='bb')),
                QuickReplyButton(action=PostbackTemplateAction(
                    label="9", text="改成 9份", data='bb')),
            ]))

        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='不買'))


def sendback_Modifysuger(event, backdata):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E7%84%A1%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='無糖',
                            text='改成 無糖',
                            data='cc'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%BE%AE%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='微糖',
                            text='改成 微糖',
                            data='cc'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%8D%8A%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='半糖',
                            text='改成 半糖',
                            data='cc'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B0%91%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='少糖',
                            text='改成 少糖',
                            data='cc'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%85%A8%E7%B3%96-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='全糖',
                            text='改成 全糖',
                            data='cc'
                        )
                    ),
                ]
            )
        )

        message = FlexSendMessage(alt_text="修改糖度", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='無法修改糖度'))


def sendback_Modifyice(event, backdata):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
                layout='horizontal',
                spacing='xs',
                contents=[
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B8%B8%E6%BA%AB-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='常溫',
                            text='改成 常溫',
                            data='dd'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%8E%BB%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='去冰',
                            text='改成 去冰',
                            data='dd'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%BE%AE%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='微冰',
                            text='改成 微冰',
                            data='dd'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E5%B0%91%E5%86%B0-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='少冰',
                            text='改成 少冰',
                            data='dd'
                        )
                    ),
                    ImageComponent(
                        url="https://raw.githubusercontent.com/shakuneko/pic0412/main/%E5%86%B0%E5%A1%8A%E7%94%9C%E5%BA%A6/%E6%AD%A3%E5%B8%B8-03.jpg",
                        size="lg",
                        aspect_mode="cover",
                        action=PostbackTemplateAction(
                            label='正常',
                            text='改成 正常',
                            data='dd'
                        )
                    ),
                ]
            )
        )

        message = FlexSendMessage(alt_text="修改冰塊", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        print(e)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='無法修改冰塊'))
