# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
import random
from click import confirm
from flask import Flask, request, abort
import pymysql
import random
import datetime
from datetime import date

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#from flask_sqlalchemy import SQLAlchemy
import re
#db = SQLAlchemy()
app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@IP:3306/eat"
#db.init_app(app)
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('DkawnchexvPm43aM8Wo6NE5k+EOYzE/d0uWKo6r6z3jeZpEfYOgrZGWzpVhawu5nzHapBJB0M9XRUq1QvmoAdNczkSx17mVvlQHV5PNL7BGWispl3ztqHlOwJ2s7B0RoakzQugMa+jXnDiKKc4GEBgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('108061922b6a62f37ac31d048d5569b9')

line_bot_api.push_message('U00e58cb0503ab1e4f9caf17e97f31f33', TextSendMessage(text='選擇您需要的功能',quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label="我想知道簡介!",text="簡介")),
            QuickReplyButton(action=MessageAction(label="我想知道進度!",text="進度如何")),
            QuickReplyButton(action=MessageAction(label="我想知道學校地圖!",text="學校地圖")),
            QuickReplyButton(action=MessageAction(label="我想知道學校的特約商店!",text="特約商店")),
            QuickReplyButton(action=MessageAction(label="我想知道行事曆!",text="行事曆")),
            QuickReplyButton(action=MessageAction(label="我想知道新生相關事項!",text="新生事項")),
            QuickReplyButton(action=MessageAction(label="我想知道宿舍規格或相關規定!",text="宿舍")),
            QuickReplyButton(action=MessageAction(label="我想知道位置!",text="位置")),
            QuickReplyButton(action=MessageAction(label="我想評價!",text="評價")),
            QuickReplyButton(action=MessageAction(label="我想看學校常用網站!",text="學校網站")),
            QuickReplyButton(action=MessageAction(label="我想看學生常用討論區!",text="學生討論區")),
            ])))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 
#訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #取得使用者傳送文字
    message = text = event.message.text
    if re.match('簡介',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('由於校園資訊廣泛分布於網站、臉書、學生信箱、論壇......等等討論區，然而各平台資訊卻不流通，時常花許多時間查找資訊，因此期望建置一個統整各項資訊的平台，以最方便且迅速的方式取得資訊並即時討論，亦提供未來學弟妹一個有效認識學校生活的管道。'))
    elif re.match('進度如何',message):
        sticker_message = StickerMessage(
            package_id='446',
            sticker_id='2021'
        )
        line_bot_api.reply_message(event.reply_token,sticker_message)
    elif re.match('學校地圖',message):
        image_message = ImageSendMessage(
            original_content_url='https://www.ntue.edu.tw/File/Userfiles/0000000090/images/160X120%E9%98%B2%E7%81%BD%E9%81%BF%E9%9B%A3%E5%9C%96final-20181116.JPG',
            preview_image_url='https://www.ntue.edu.tw/File/Userfiles/0000000090/images/160X120%E9%98%B2%E7%81%BD%E9%81%BF%E9%9B%A3%E5%9C%96final-20181116.JPG'
        )
        line_bot_api.reply_message(event.reply_token,image_message)
    elif re.match('特約商店',message):
        i=[]
        image_message1 = ImageSendMessage(
            original_content_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/270285192_4538109599576289_6917746024527125209_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=1Jzk6KvZA0AAX8lH81V&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8kj2ErLHGNm8sdC2LhgCG4FmqwDt3GStHbE7ZmaUoJMw&oe=62C217DE',
            preview_image_url='https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/270285192_4538109599576289_6917746024527125209_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=1Jzk6KvZA0AAX8lH81V&_nc_ht=scontent-tpe1-1.xx&oh=00_AT8kj2ErLHGNm8sdC2LhgCG4FmqwDt3GStHbE7ZmaUoJMw&oe=62C217DE'
        )
        image_message2 = ImageSendMessage(
            original_content_url='https://scontent.frmq2-1.fna.fbcdn.net/v/t39.30808-6/270468293_4538124009574848_8513163669988571719_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=pLk3ccQ4CGQAX_fGe7G&_nc_ht=scontent.frmq2-1.fna&oh=00_AT-uz0mx0aT9yqZsw-pDhPGP2XLrQ5wa2GZaNRDqucRPjg&oe=62C35388',
            preview_image_url='https://scontent.frmq2-1.fna.fbcdn.net/v/t39.30808-6/270468293_4538124009574848_8513163669988571719_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=pLk3ccQ4CGQAX_fGe7G&_nc_ht=scontent.frmq2-1.fna&oh=00_AT-uz0mx0aT9yqZsw-pDhPGP2XLrQ5wa2GZaNRDqucRPjg&oe=62C35388'
        )
        i.append(image_message1)
        i.append(image_message2)
        line_bot_api.reply_message(event.reply_token,i)
    elif re.match('今天吃什麼',message):
        randomeat()
        #location1=LocationSendMessage(
            #title='3隻貓頭鷹文創',
            #address='現代美式餐廳',
            #latitude=25.023302519115656, 
            #longitude=121.5426517140537
        #)
        #image1 = ImageSendMessage(
        #    original_content_url='https://julie1798.com/wp-content/uploads/flickr/36674516742_1e5760bd15_c.jpg',
        #    preview_image_url='https://julie1798.com/wp-content/uploads/flickr/36674516742_1e5760bd15_c.jpg'
        #)
        #location_message1 = [location1, image1]
        #ary=[location_message1,location_message2,location_message3,location_message4,location_message5]
        #eat = random.choice(ary)
        #隨機、判斷時間
        def randomeat():
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="password", db="mysql")
            cur = conn.cursor()
            sql_1="SELECT * FROM eat ORDER BY RAND()"
            cur.execute(sql_1)
            a=cur.fetchone()
            #print(a)
            nowtime=date.today()
            week=date(nowtime.year,nowtime.month,nowtime.day).isoweekday()

            if(week == 7):
                start1=a[30]
                start2=a[32]
                close1=a[31]
                close2=a[33]
            elif(week == 6):
                start1=a[26]
                start2=a[28]
                close1=a[27]
                close2=a[29]
            elif(week == 5):
                start1=a[22]
                start2=a[24]
                close1=a[23]
                close2=a[25]
            elif(week == 4):
                start1=a[18]
                start2=a[20]
                close1=a[19]
                close2=a[21]
            elif(week == 3):
                start1=a[14]
                start2=a[16]
                close1=a[15]
                close2=a[17]
            elif(week == 2):
                start1=a[10]
                start2=a[12]
                close1=a[11]
                close2=a[13]
            else:
                start1=a[6]
                start2=a[8]
                close1=a[7]
                close2=a[9]
                
            time(a,start1,close1,start2,close2)

        def time(aa,starttime1,closetime1,starttime2,closetime2):
            now=datetime.datetime.now()
            nowtime=now.strftime('%H:%M:%S')
            time_now = datetime.datetime.strptime(nowtime,"%H:%M:%S")
            if(starttime1 == None):
                #print("沒開ㄏㄏ")
                randomeat()
                #不能推薦
            elif(starttime2 == None):
                time_starttime1 = datetime.datetime.strptime(str(starttime1),"%H:%M:%S")
                time_closetime1 = datetime.datetime.strptime(str(closetime1),"%H:%M:%S")
                if (time_closetime1 >= time_now >= time_starttime1):
                    #print('開了ㄏㄏ')
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('我要哭了'))
                    lineeat(aa,starttime1,closetime1,starttime2,closetime2)
                    #可以推薦
                else:
                    #print('休息ㄏㄏ')
                    randomeat()
            else:
                time_starttime1 = datetime.datetime.strptime(str(starttime1),"%H:%M:%S")
                time_closetime1 = datetime.datetime.strptime(str(closetime1),"%H:%M:%S")
                time_starttime2 = datetime.datetime.strptime(str(starttime2),"%H:%M:%S")
                time_closetime2 = datetime.datetime.strptime(str(closetime2),"%H:%M:%S")
                if (time_closetime1 >= time_now >= time_starttime1):
                    #print('開了ㄏㄏ')
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('我要哭了'))
                    lineeat(aa,starttime1,closetime1,starttime2,closetime2)
                elif(time_closetime2 >= time_now >= time_starttime2):
                    #print('開了ㄏㄏ')
                    line_bot_api.reply_message(event.reply_token,TextSendMessage('我要哭了'))
                    lineeat(aa,starttime1,closetime1,starttime2,closetime2)
                else:
                    #print('休息ㄏㄏ')
                    randomeat()    

        def lineeat(aaa,start1,close1,start2,close2):
            location=LocationSendMessage(
                    title=aaa[1],
                    address=aaa[2],
                    latitude=aaa[3], 
                    longitude=aaa[4]
                )
            if(start2 == None):
                text=TextSendMessage('營業時間:'+str(start1)+'~'+str(close1))
            else:
                text=TextSendMessage('營業時間:'+str(start1)+'~'+str(close1)+';'+str(start2)+'~'+str(close2))
            image = ImageSendMessage(
                original_content_url=aaa[5],
                preview_image_url=aaa[5]
            )
            eat = [location, text, image]
            #line_bot_api.reply_message(eee.reply_token,eat)
            line_bot_api.reply_message(event.reply_token,TextSendMessage('有呼叫到'))
        
        
    elif re.match('今天喝什麼',message):
        location_message1 = LocationSendMessage(
            title='春山茶水舖',
            address='真情推薦，冰品飲料店',
            latitude=25.02498420466018,  
            longitude=121.54339817809928
        )
        location_message2 = LocationSendMessage(
            title='可不可熟成紅茶 科技大樓店',
            address='冰品飲料店',
            latitude=25.025761934146725,  
            longitude=121.54485729973584
        )
        location_message3 = LocationSendMessage(
            title='烏弄原生茶飲 科技大樓店',
            address='冰品飲料店',
            latitude=25.02611191080775,  
            longitude=121.5439989928908
        )
        location_message4 = LocationSendMessage(
            title='囍庄茶舖',
            address='冰品飲料店',
            latitude=25.026345228027317,  
            longitude=121.54502896110485 
        )
        location_message5 = LocationSendMessage(
            title='MTB米堤銀行｜鮮乳．茶（大安總行）創始店',
            address='冰品飲料店',
            latitude=25.0247897715185,    
            longitude=121.54331234741473
        )
        ary=[location_message1,location_message2,location_message3,location_message4,location_message5]
        drink = random.choice(ary)
        line_bot_api.reply_message(event.reply_token,drink)
    elif re.match('團購',message):
        buttons_template_message = TemplateSendMessage(
            alt_text='團購',
            template=ButtonsTemplate(
                thumbnail_image_url='https://cdn.store-assets.com/s/395287/f/5967693.jpeg',
                title='國北揪團購',
                text='~一起團購一起省錢~',
                actions=[
                    MessageAction(
                        label='國北揪團購介紹',
                        text='還沒想好簡介'
                    ),
                    URIAction(
                        label='國北揪團購小助手',
                        uri='https://tj42wwaiafmwrlbzjiri2w.on.drv.tw/%E6%9C%9F%E6%9C%AB%E8%A1%A8%E5%96%AE/mian.html'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,buttons_template_message)
    elif re.match('功能介紹',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='NTUE一點通功能',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://cdn.store-assets.com/s/395287/f/5967693.jpeg',
                        title='國北揪團購',
                        text='~一起團購一起省錢~',
                        actions=[
                            #PostbackAction(
                            #    label='',#表單上的字
                            #    display_text='',#回傳的字
                            #    data=''#後臺拿到的資料
                            #),
                            MessageAction(#回傳的資料和後臺拿到的是一樣的資料
                                label='國北揪團購介紹',
                                text='還沒想好簡介'
                            ),
                            URIAction(
                                label='國北揪團購小助手',
                                uri='https://tj42wwaiafmwrlbzjiri2w.on.drv.tw/%E6%9C%9F%E6%9C%AB%E8%A1%A8%E5%96%AE/mian.html'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn.store-assets.com/s/395287/f/5967693.jpeg',
                        title='國北揪團購',
                        text='~一起團購一起省錢~',
                        actions=[
                            MessageAction(#回傳的資料和後臺拿到的是一樣的資料
                                label='國北揪團購介紹',
                                text='還沒想好簡介'
                            ),
                            URIAction(
                                label='國北揪團購小助手',
                                url='https://tj42wwaiafmwrlbzjiri2w.on.drv.tw/%E6%9C%9F%E6%9C%AB%E8%A1%A8%E5%96%AE/mian.html'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn.store-assets.com/s/395287/f/5967693.jpeg',
                        title='國北揪團購',
                        text='~一起團購一起省錢~',
                        actions=[
                            MessageAction(#回傳的資料和後臺拿到的是一樣的資料
                                label='國北揪團購介紹',
                                text='還沒想好簡介'
                            ),
                            URIAction(
                                label='國北揪團購小助手',
                                url='https://tj42wwaiafmwrlbzjiri2w.on.drv.tw/%E6%9C%9F%E6%9C%AB%E8%A1%A8%E5%96%AE/mian.html'
                            )
                        ]
                    )        
                ]
            )
            
        )
        line_bot_api.reply_message(event.reply_token,carousel_template_message)
    elif re.match('評價',message):
        confirm_template_message = TemplateSendMessage(
            alt_text='詢問使用者評價',
            template=ConfirmTemplate(
                text='您還喜歡NTUE一點通linebot服務嗎?',
                actions=[
                    MessageAction(#回傳的資料和後臺拿到的是一樣的資料
                                label='喜歡',
                                text='喜歡'
                            ),
                    MessageAction(#回傳的資料和後臺拿到的是一樣的資料
                                label='有改進空間',
                                text='有改進空間'
                            )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,confirm_template_message)
    elif re.match('喜歡',message):
        flex_message = FlexSendMessage(
            alt_text='喜歡',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "謝謝您喜歡NTUE一點通😊",
                                "wrap": True,
                                "color": "#666666",
                                "size": "md",
                                "flex": 5
                            },
                            {
                                "type": "text",
                                "text": "若是有希望NTUE一點通增加的功能，都可以填表單告訴我們呦💖",
                                "wrap": True,
                                "color": "#666666",
                                "size": "md",
                                "flex": 5
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "前往填寫意見表單",
                        "uri": "https://docs.google.com/forms/d/e/1FAIpQLSflZz2_OnNKjpsDwck2LFQHSAtS417xIBHfFZDXKGtmM91Xag/viewform?usp=sf_link"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                })
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('有改進空間',message):
        flex_message = FlexSendMessage(
            alt_text='改進',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "謝謝您使用NTUE一點通😌",
                                "wrap": True,
                                "color": "#666666",
                                "size": "md",
                                "flex": 5
                            },
                            {
                                "type": "text",
                                "text": "若是有希望NTUE一點通改善的地方，或是希望增加更方便的功能，都歡迎填表單告訴我們呦❣",
                                "wrap": True,
                                "color": "#666666",
                                "size": "md",
                                "flex": 5
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "前往填寫意見表單",
                        "uri": "https://docs.google.com/forms/d/e/1FAIpQLSflZz2_OnNKjpsDwck2LFQHSAtS417xIBHfFZDXKGtmM91Xag/viewform?usp=sf_link"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                })
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('行事曆',message):
        flex_message = FlexSendMessage(
            alt_text='行事曆',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://www.overseas.edu.tw/wp-content/uploads/2020/10/%E5%9C%8B%E7%AB%8B%E8%87%BA%E5%8C%97%E6%95%99%E8%82%B2%E5%A4%A7%E5%AD%B81-1024x683.jpg",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "1:1",
                        "gravity": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "position": "absolute",
                        "background": {
                        "type": "linearGradient",
                        "angle": "0deg",
                        "endColor": "#00000000",
                        "startColor": "#00000099"
                        },
                        "width": "100%",
                        "height": "40%",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "台北教育大學教務處",
                                    "size": "xl",
                                    "color": "#ffffff"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "行事曆(pdf檔)",
                                        "color": "#ffffff",
                                        "size": "md",
                                        "flex": 0,
                                        "align": "end"
                                    }
                                    ],
                                    "flex": 0,
                                    "spacing": "lg"
                                }
                                ]
                            }
                            ],
                            "spacing": "xs"
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "paddingAll": "20px"
                    }
                    ],
                    "paddingAll": "0px",
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://academicntue.ntue.edu.tw/p/403-1002-97.php?Lang=zh-tw"
                    }
                }
                }
        )
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('新生事項',message):
        flex_message = FlexSendMessage(
            alt_text='新生事項',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.pexels.com/photos/1454360/pexels-photo-1454360.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://linecorp.com"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                    "type": "uri",
                    "uri": "https://linecorp.com"
                    },
                    "contents": [
                    {
                        "type": "text",
                        "text": "新生相關事項",
                        "size": "xl",
                        "weight": "bold"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/023/267/original/building_11-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "新生始業輔導專區",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/021/920/original/money_bag_34-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "學雜費",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/023/290/original/house_6-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "新生住宿申請",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/023/102/original/doctor_3-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "入學體檢",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/019/622/original/4_soldier-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "兵役",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_png_watermarkeds/000/021/919/original/money_43-premium.png"
                            },
                            {
                                "type": "text",
                                "text": "優秀新生全額獎學金",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_pngs/000/006/822/original/file12.png"
                            },
                            {
                                "type": "text",
                                "text": "學分抵免資訊",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_pngs/000/017/829/original/teacher_6454413.png"
                            },
                            {
                                "type": "text",
                                "text": "教務、學務、師培系統",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://d338t8kmirgyke.cloudfront.net/icons/icon_pngs/000/001/828/original/school.png"
                            },
                            {
                                "type": "text",
                                "text": "教育學程",
                                "weight": "bold",
                                "margin": "sm",
                                "flex": 0
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "color": "#905c44",
                        "margin": "xxl",
                        "action": {
                        "type": "uri",
                        "label": "前往",
                        "uri": "https://academicntue.ntue.edu.tw/p/403-1002-53.php?Lang=zh-tw"
                        }
                    }
                    ]
                }
                })
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('宿舍',message):
        reply_arr=[]
        flex_message1 = FlexSendMessage(
            alt_text='上',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                    "type": "uri",
                    "uri": "https://linecorp.com"
                    },
                    "contents": [
                    {
                        "type": "text",
                        "text": "第一次住宿要注意什麼？",
                        "size": "lg",
                        "weight": "regular"
                    },
                    {
                        "type": "text",
                        "text": "該帶哪些東西最精簡呢！",
                        "size": "lg"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "超完整住宿準備清單攻略(上)",
                        "uri": "https://medium.com/@evanhsu__0910/dormitory-supplies-ctbcbs-ca9205fac079"
                        },
                        "style": "primary",
                        "color": "#3269a8"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "uri": "https://medium.com/business-school-student-life/dormitory-supplies-ctbcbs-c534d6e2b2e7#8a59",
                        "label": "超完整住宿準備清單攻略(下)"
                        },
                        "color": "#3269a8",
                        "style": "primary"
                    }
                    ]
                }
                }
        )
        flex_message2 = FlexSendMessage(
            alt_text='下',
            contents={
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/zbjFrCD.jpeg",
                            "size": "5xl",
                            "aspectMode": "cover",
                            "aspectRatio": "150:196",
                            "gravity": "center",
                            "flex": 1
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://orad.ntue.edu.tw/uploads/asset/data/5ec620a7378e3d6d2e000242/%E6%9B%B8%E6%A1%8C.jpg",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "150:98",
                                "gravity": "center"
                            },
                            {
                                "type": "image",
                                "url": "https://orad.ntue.edu.tw/uploads/asset/data/5ec62443378e3d6d36000207/%E6%B4%97%E8%A1%A3%E9%96%93-1.jpg",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "150:98",
                                "gravity": "center"
                            }
                            ],
                            "flex": 1
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "台北教育大學新生宿舍",
                                "weight": "bold"
                            },
                            {
                                "type": "text",
                                "text": "宿舍規格、床位大小、"
                            },
                            {
                                "type": "text",
                                "text": "學長姐告訴你的宿舍注意事項"
                            }
                            ]
                        }
                        ],
                        "spacing": "none",
                        "paddingAll": "20px"
                    }
                    ],
                    "paddingAll": "0px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "Dcard給新生的宿舍介紹(討論區)",
                        "uri": "https://www.dcard.tw/f/ntue/p/234000894"
                        },
                        "style": "primary",
                        "color": "#a83250",
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "FB宿舍自治委員會",
                        "uri": "https://www.facebook.com/ntuedc2015/posts/657407294634633/"
                        },
                        "style": "primary",
                        "color": "#8a337a",
                        "height": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "國立臺北教育大學宿舍服務專區",
                        "uri": "https://dorm.ntue.edu.tw/"
                        },
                        "color": "#66338a",
                        "style": "primary",
                        "height": "sm"
                    }
                    ],
                    "margin": "none",
                    "spacing": "sm"
                }
                }
        )
        reply_arr.append(flex_message1)
        reply_arr.append(flex_message2)
        line_bot_api.reply_message(event.reply_token,reply_arr)
    elif re.match('學校網站',message):
        flex_message = FlexSendMessage(
            alt_text='網站',
            contents={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://www.ecfloor.com.tw/upload/news/201909171717420.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "台北教育大學官網",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": "學校主要網站，最新訊息會在此公布",
                                    "color": "#ffffffcc",
                                    "size": "sm"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm"
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://www.ntue.edu.tw/"
                                }
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#662222cc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://cdnec.sanmin.com.tw/product_images/986/986053743.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "教學魔法師",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": "老師放教材、學生主要繳交作業處",
                                    "color": "#ffffffcc",
                                    "size": "sm"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://imagic.ntue.edu.tw/magic/index.php"
                                    }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px"
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#226066cc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    },{
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://img.sur.ly/thumbnails/620x343/w/wm.ntue.edu.tw.png",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "新教學平台",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": "老師放教材、學生次要繳交作業處",
                                    "color": "#ffffffcc",
                                    "size": "sm"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://wm.ntue.edu.tw/"
                                    }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px"
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#412559cc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://upload.wikimedia.org/wikipedia/zh/thumb/6/62/National_Taipei_University_of_Education_logo.svg/1200px-National_Taipei_University_of_Education_logo.svg.png",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "iNTUE",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": "學生選課、請假、查詢成績等校務整合資訊系統",
                                    "color": "#ffffffcc",
                                    "size": "sm"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm",
                                    "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://nsa.ntue.edu.tw/"
                                    }
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px"
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    }                    
                ]
                }
        )
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('學生討論區',message):
        flex_message = FlexSendMessage(
            alt_text='學生討論區',
            contents={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://9.share.photo.xuite.net/paulkkh/19cc461/7500718/284226995_m.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "國北選課沒地雷",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "國北學生詢問老師、課程內容",
                                    "color": "#ebebeb",
                                    "size": "sm",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "雷課不要踩，專門討論選課的社團！",
                                    "size": "sm",
                                    "color": "#ebebeb"
                                }
                                ],
                                "spacing": "none"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm"
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://www.facebook.com/groups/194514594077227/"
                                }
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://images.pexels.com/photos/590493/pexels-photo-590493.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "國北教二手書籍 贈送/交換/出售",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "國北學生交換／拍賣二手書的社團！",
                                    "color": "#ebebeb",
                                    "size": "sm",
                                    "flex": 0
                                }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm"
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://www.facebook.com/groups/1810867679152822"
                                }
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#9C8E7Ecc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    },
                    {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://images.pexels.com/photos/3182768/pexels-photo-3182768.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Dcard台北教育大學版",
                                    "size": "xl",
                                    "color": "#ffffff",
                                    "weight": "bold"
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "國北學生在此討論各式各樣的內容",
                                    "color": "#ebebeb",
                                    "size": "sm",
                                    "flex": 0
                                }
                                ],
                                "spacing": "none"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "text",
                                        "text": "前往",
                                        "color": "#ffffff",
                                        "flex": 0,
                                        "offsetTop": "-2px"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                    ],
                                    "spacing": "sm"
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "https://www.dcard.tw/f/ntue/rule"
                                }
                            }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#2d394dcc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        }
                        ],
                        "paddingAll": "0px"
                    }
                    }
                ]
                })
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif re.match('選擇功能',message):
        flex_message = TextSendMessage(text='選擇您需要的功能',quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(label="我想知道簡介!",text="簡介")),
            QuickReplyButton(action=MessageAction(label="我想知道進度!",text="進度如何")),
            QuickReplyButton(action=MessageAction(label="我想知道位置!",text="位置")),
            QuickReplyButton(action=MessageAction(label="我想看影片!",text="影片")),
            QuickReplyButton(action=MessageAction(label="我想看照片!",text="照片")),
            QuickReplyButton(action=MessageAction(label="我想看功能介紹!",text="功能介紹")),
            QuickReplyButton(action=MessageAction(label="我想評價!",text="評價")),
            QuickReplyButton(action=MessageAction(label="我想看網站!",text="網站"))]))
        line_bot_api.reply_message(event.reply_token,flex_message)
    else:
        line_bot_api.reply_message(event.reply_token,TextMessage(message))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)