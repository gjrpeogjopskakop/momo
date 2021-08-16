# -*- coding: utf-8 -*-
from linepy import *
import asyncio
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup 
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length, Timer
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy
from threading import Thread
set = {
    "bots1" : []
}
####################################################
botStart = time.time() 
####################################################
ts = time.time()
#################################################### 
cl = LINE("rcv55731@cuoly.com","q224300978")
####################################################
cl.log(cl.authToken)
AuthToken = []
for i in range(1,151): AuthToken.append(LINE(cl.authToken))
AuthToken1 = []
for i in range(1,21): AuthToken1.append(LINE(cl.authToken))
X = ['u4f998dda4280d43f46d3c686d28d253a','u2db707c088044deb4757c666d1eea1a0']
####################################################
cl.sendMessage("u2db707c088044deb4757c666d1eea1a0","專武垢登入成功\n開啟時間: {} s\n開啟線程數 {}".format(time.time()-ts, len(AuthToken)))
####################################################
#profile = cl.getProfile()
#status = str(profile.statusMessage)
#lock = _name = "\n\nnŠhęñŸiń ßöᴛ 運行中(๑′ᴗ‵๑)\n長久運作中Ing.....\n作者:神隱\nMade in Taiwan\nLineID:greg6567550"
#if lock not in status:
#    profile.statusMessage = status + lock
#    cl.updateProfile(profile)
#else:
#    pass
####################################################
oepoll = OEPoll(cl)
####################################################
datadir = {"switch": False,"gid": ""}
####################################################
readOpen = codecs.open("read.json","r","utf-8")
read = json.load(readOpen)
cbg = codecs.open("bodyguard.json","r","utf-8")
####################################################
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)

####################################################
redOpen = codecs.open("red.json","r","utf-8")
red = json.load(redOpen)
####################################################
jgOpen = codecs.open("jg.json","r","utf-8")
jg = json.load(jgOpen)
####################################################
banOpen = codecs.open("ban.json","r","utf-8")
ban = json.load(banOpen)
####################################################
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
####################################################
####################################################
lineSettings = cl.getSettings()
clMID = cl.profile.mid
clProfile = cl.getProfile()
clSetting = cl.getSettings()
####################################################

####################################################
bl = [clMID]
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
####################################################

####################################################

King = clMID
#################################################### 
####################################################
msg_dict = {}
msg_dictt = {}
####################################################

####################################################
wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': False,
    'um': False,#收回高速
    'cvp': False,#更換頭貼
    'clp':False,#頭貼
    'clpp':False,
    'gbc':{},
    'resset': False,#偵測更新
    'warmode':False
    }
####################################################

####################################################
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
####################################################

####################################################
setTime = {}
setTime = wait2['setTime']
####################################################

####################################################
profile = cl.getProfile()
####################################################

####################################################
msg_dict = {}
msg_dictt = {}
####################################################

####################################################
mulai = time.time()
####################################################
def kick(n, to, mid):
    while 1: AuthToken[n].kickoutFromGroup(to, mid); break
def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天\n%02d 時\n%02d 鐘\n%02d 秒\n以上為半垢機体運行時間\n半垢 運行時間測試' % (days, hours, mins, secs)
def Rtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False
def cance(n, to, mid):
    while 1: AuthToken1[n].cancelGroupInvitation(to, mid); break
def kick(n, to, mid):
    while 1: AuthToken[n].kickoutFromGroup(to, mid); break
async def kkick():
    group = cl.getGroup(op.message.to)
    gMembMids = [contact.mid for contact in group.members]
    gMembMid = [contact.mid for contact in group.invitee]
    matched_lists = []
    matched_list = []
    for tag in ban["tlist"]:
        matched_lists+=filter(lambda str: str == tag, gMembMids)
    for tag in ban["klist"]:
        matched_list+=filter(lambda str: str == tag, gMembMid)
    else:
        n = 0
        for i in matched_lists:
            if n == len(AuthToken):
                n = 0
            if i not in settings["admin"]:
                threading.Thread(target=kick, args=(n, op.message.to, [i],)).start()
                n += 1
        n = 0
        for i in matched_list:
            threading.Thread(target=cance, args=(n, op.message.to, [i],)).start()
            n += 1
        return
def kkickrun():
    loop.run_until_complete(kkick())
loop = asyncio.get_event_loop()
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = jg
        f = codecs.open('jg.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = cbg
        f = codecs.open('bodyguard.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageTag(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  此人在群組(私聊)標住您'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessagegat(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Yi  '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendReplyMention(self,RynId, to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Jwwwwwwwww "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 15
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ""
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        return cl.sendReplyMention(msg_id, to,textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def ytdl(url):
    video = pafy.new(url)
    best = video.getbest() 
    best.download(filepath="test.mp4")
def gettoken(to):
    try:
        k1 = LINE() 
        cl.sendMessage(to,str(k1.authToken))
    except:
        pass
    return True
def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help = text.format(key=key.title())
    return help
def help1():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help1.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help1 = text.format(key=key.title())
    return help1
def help2():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help2.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help2 = text.format(key=key.title())
    return help2
def help3():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help3.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help3 = text.format(key=key.title())
    return help3
def help4():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help4.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help4 = text.format(key=key.title())
    return help4
def help5():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help5.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help5 = text.format(key=key.title())
    return help5
def help6():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help6.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help6 = text.format(key=key.title())
    return help6
def help7():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help7.txt','r',encoding="UTF-8") as f:
        text = f.read()
    help7 = text.format(key=key.title())
    return help7
def bodyguardinvite():
    if settings["bgi"] == True:
        try:
            for mi_d in cbg:
                try:
                    cl.inviteIntoGroup(to,mi_d)
                    time.sleep(0.1)
                except:
                    pass
        except:
            pass
    elif settings["bgi"] == False:
        group = cl.getGroup(to)
        group.preventedJoinByTicket = False
        Ticket = cl.reissueGroupTicket(to)
        link = "https://line.me/R/ti/g/{}".format(str(Ticket))
        cl.updateGroup(group)
        try:
            for mi_d in cbg:
                try:
                    cl.sendMessage(mi_d,link)
                except:
                    pass
            time.sleep(1)
            group.preventedJoinByTicket = True
            cl.updateGroup(group)
        except:
            pass
def unsend(msgid):
    sleep(1)
    cl.unsendMessage(msgid)
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 1:
            print ("更新配置文件")
            #profile = cl.getProfile()
            #status = str(profile.statusMessage)
            #lock = _name = "\n\nŠhęñŸiń ßöᴛ 運行中(๑′ᴗ‵๑)\n長久運作中Ing.....\n作者:神隱\nMade in Taiwan\nLineID:greg6567550"
            #if lock not in status:
                #profile.statusMessage = status + lock
                #cl.updateProfile(profile)
        if op.type in [17]:
            if op.param1 in settings["jm"]:
                cl.sendMessage(op.param1,settings["jm"][op.param1])
            if op.param2 in ban["blacklist"]:
                try:
                    threading.Thread(target=cl.kickoutFromGroup, args=(op.param1,[op.param2],)).start()
                    cl.sendMessage(op.param1,"此人位於黑名單\n取消黑單請找作者")
                except Exception as e:
                    if "request blocked" in e.reason:
                        cl.sendMessage(op.param1,"此人位於黑名單\n因機器規制所以無法踢出")
            
        if op.type == 2:
            contact = cl.getContact(op.param1)
            if wait["resset"] == True:
                if op.param2 == "2":
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d","通知好友更改名稱:\n" + contact.displayName)
                if op.param2 == "8":
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d","通知好友更改動態頭貼:\n" + contact.displayName)
                if op.param2 == "16":
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d","通知好友更改個簽:\n" + contact.displayName)
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
        if op.type == 5:#自動防封鎖
            print ("[ 5 ] INV PRO")
            if settings["invBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "•防邀機功能運行中•\n•[已啟動自動封鎖]•\nÇręätør:大米 我的作者網址:line.me/ti/p/~0970737883".format(str(cl.getContact(op.param1).displayName))) 
        if op.type == 26:
            msg = op.message
            text = msg.text
            sender = msg._from
            to = msg.to
            if msg.text in settings['mute']:
                cl.sendReplyMessage(msg.id,to,settings['mute'][text.lower()]) 
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 1:
                if msg._from in settings["admin"]:
                    if wait["clp"] == True:
                        path1 = cl.downloadObjectMsg(msg.id)
                        wait["clp"] = False
                        cl.updateProfilePicture(path1)
                        cl.sendMessage(to, "更換成功")  
            if msg.contentType == 1:
                if msg._from in settings["admin"]:
                    if wait["clpp"] == True:
                        path1 = cl.downloadObjectMsg(msg.id)
                        wait["clpp"] = False
                        cl.updateProfileCoverURL(path1)
                        cl.sendMessage(to, "更換成功")    
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                contact1 = cl.getContact(op.param2)
                contact2 = cl.getContact(op.param3)
                group = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:                    
                       cl.acceptGroupInvitation(op.param1)
            if op.param2 in settings["admin"]:
                            cl.sendMessage(op.param1,"偵測:您是權限者,感謝邀請")
                            cl.sendMessage('c1dca4d48eac80ad9d8d5dd2802e2662d',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
            if clMID in op.param3:
                if settings["autoPtt"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "自動進退運行中...")
                    cl.leaveGroup(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 7:
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                number = str(stk_id) + str(pkg_id)
                if sender in settings['limit']:
                    if number in settings['limit'][sender]['stick']:
                        if settings ['limit'][sender]['stick'][number] >= 3:
                            settings ['limit'][sender]['stick']['react'] = False
                        else:
                            settings ['limit'][sender]['stick'][number] += 1
                            settings ['limit'][sender]['stick']['react'] = True
                    else:
                        try:
                            del settings['limit'][sender]['stick']
                        except:
                            pass
                        settings['limit'][sender]['stick'] = {}
                        settings['limit'][sender]['stick'][number] = 1
                        settings['limit'][sender]['stick']['react'] = True
                else:
                    settings['limit'][sender] = {}
                    settings['limit'][sender]['stick'] = {}
                    settings['limit'][sender]['text'] = {}
                    settings['limit'][sender]['stick'][number] = 1
                    settings['limit'][sender]['stick']['react'] = True
                if settings['limit'][sender]['stick']['react'] == False:
                    return
                if to in settings['cc']:
                    command = "->貼圖回覆ID:" + format(stk_id) + ":" + format(pkg_id) + ":"
                    command1 = "->刪貼圖回覆ID:" + format(stk_id) + ":" + format(pkg_id)
                    cl.sendReplyMessage(msg.id, to, command)
                    cl.sendReplyMessage(msg.id, to, command1)
                elif number in settings['sr']:
                    react = settings['sr'][number]
                    cl.sendReplyMention(msg_id, to,"@!" + str(react),[sender])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if clMID in op.param3:
                if settings["autojoinkick"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('【自動入群】\n')
                        arr = []
                        mention = "@Grk "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "戰爭運作中"
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendContact(op.param1, "u77c34b6198166ffe142d671369fed4bd")
                        cl.sendMessage('c1dca4d48eac80ad9d8d5dd2802e2662d',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
                        cl.sendMessage(op.param1, "老子瘋狗啦,不服來辯")
                    except Exception as error:
                        print(error)
        if op.type == 15:
            if settings["seeLeave"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('[提示]\n')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} 群組 離我們而去了OAO！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 60:
            if op.param1 in jg["JoinGroup"]:
                if op.param2 not in settings["admin"]:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        
        if op.type == 17:
            if settings["seeJoin"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@Mili "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "您加入 {} 我們的小窩！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d","有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param3 in settings["admin"]:
                try:
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                    pass
            if settings["protect"] == True:
                if op.param2 in settings["admin"]:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@Mili "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@Mili "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@Mili "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25 and wait["um"]: cl.unsendMessage(op.message.id)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in settings["admin"] or sender not in settings["admin"]:
                if "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                            for ticket_id in n_links:
                                group = cl.findGroupByTicket(ticket_id)
                                cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "網址成功進入《%s》群組" % str(group.name))
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            G = cl.getGroup(op.param1)
            if clMID in op.param3:    
                if op.param2 in set["bots1"]:
                    pass            
                    if op.param1 not in settings["gm"]:
                        settings["gm"][op.param1] = []
                    try:
                        if G.creator.mid not in settings["gm"][op.param1]:
                            settings["gm"][op.param1].append(G.creator.mid)
                    except:
                        if op.param2 not in settings["gm"][op.param1]:
                            settings["gm"][op.param1].append(op.param2)
                elif op.param2 in settings["user"]:
                    if "gid" in settings["user"][op.param2] :
                        settings["user"][op.param2].remove("gid")
                        settings["user"][op.param2].append(op.param1)
                        text = "你還擁有{}張邀請證".format(str(settings["user"][op.param2].count("gid")))
                    elif op.param1 in ban["user"][op.param2]:
                       text = "🗳票卷入群 🗳\n入群通知 \n "    
   
                    else:
                        return
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,text)	
                    backupData()
                    if op.param1 not in settings["gm"]:
                        settings["gm"][op.param1] =[]
                    if op.param2 not in settings["gm"][op.param1]:
                        settings["gm"][op.param1].append(op.param2)
                    G = cl.getGroup(op.param1)
                    try:
                        if G.creator.mid not in settings["gm"][op.param1]:
                            settings["gm"][op.param1].append(G.creator.mid)
                    except:
                        pass
                    cl.sendMessage(op.param1,"✰ 已設置此群群長為邀請者與創群者 ✰")
                    backupData()
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in settings["admin"]:
                pass 
            else:
                if msg.to in wait["rapidFire"]:
                    if time.time() - wait["rapidFire"][msg.to] < 2:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()       
            if msg.contentType == 0:
                if text is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 1:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id )
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《圖片》\n" + wait['gbc'][sender]['text'] )
                            cl.sendImage(manusia,image)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
            if msg.contentType == 13:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'contact':
                    mid =msg.contentMetadata["mid"]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《友資》\n" + wait['gbc'][sender]['text'] )
                            cl.sendContact(manusia,mid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if msg.contentType == 16:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'post':
                    postid =str(msg.contentMetadata['postEndUrl']).split("&postId=")[1]
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《貼文》\n" + wait['gbc'][sender]['text'] )
                            cl.sendPostToTalk(manusia,postid)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    del wait['gbc'][sender]
            if sender in settings["user"] or sender in settings["admin"]:
                if text.lower().startswith("新增 "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in settings["gm"]:
                        settings["gm"][G.id] =[]
                        for x in key["MENTIONEES"]:
                            settings["gm"][G.id].append(x["M"])
                        cl.relatedMessage(to, "成功新增！",op.message.id)
                    else:
                        for x in key["MENTIONEES"]:
                            settings["gm"][G.id].append(x["M"])
                        cl.relatedMessage(to,"成功新增！",op.message.id)
                if text.lower() == 'reset':
                    G = cl.getGroup(to)
                    settings["gm"][G.id]=[]
                    cl.sendMessage(to, "成功清空群組使徒")
                if text.lower().startswith("刪除 "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in settings["gm"]:
                        cl.relatedMessage(to, "成功刪除！",op.message.id)
                    else:
                        for x in key["MENTIONEES"]:
                            try:
                                settings["gm"][G.id].remove(x["M"])
                            except:
                                cl.relatedMessage(to,"成功刪除！",op.message.id)
                        cl.relatedMessage(to,"成功刪除！",op.message.id)
                if text.lower() == 'ccc':
                    if sender in settings["user"]:
                        if settings["user"][sender].count("gid") == 0:
                            cl.sendMessage(to,"沒有票了")
                            cl.sendContact(to,"u2db707c088044deb4757c666d1eea1a0")
                        else:
                            cl.sendMessage(to,"您還擁有{}張邀請證".format(str(settings["user"][sender].count("gid"))))
                    else:
                        cl.sendMessage(to,"你沒票還不快去買")
                        cl.sendContact(to,"u2db707c088044deb4757c666d1eea1a0")
            if sender in settings["admin"]:
				#指令表txt版本
                if text.lower() == 'help':
                        cl.sendMessage(to, help())
                elif text.lower() == 'help1':
                        cl.sendMessage(to, help1())
                elif text.lower() == 'help2':
                        cl.sendMessage(to, help2())
                elif text.lower() == 'help3':
                        cl.sendMessage(to, help3())
                elif text.lower() == 'help4':
                        cl.sendMessage(to, help4())
                elif text.lower() == 'help5':
                        cl.sendMessage(to, help5())
                elif text.lower() == 'help6':
                        cl.sendMessage(to, help6())
                elif text.lower() == 'help7':
                        cl.sendMessage(to, help7())
                elif text.lower() in ['rg']:				
                    G = cl.getGroup(msg.to)
                    group = cl.getGroup(to)
                    contact = cl.getContact(sender)
                    gtime = group.createdTime
                    gtimee = int(round(gtime/1000))
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "創群者已砍帳"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                         gPending = str(len(group.invitee))				
                    ret_ ="☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n成員數量\n【"+(str(len(group.members)))+"】"
                    ret_ +="\n邀請數量\n【"+(gPending)+"】"
                    ret_ +="\n☲☲☲☲☲群組☲☲☲☲☲"
                    ret_ +="\n群組名稱\n【{}】".format(str(group.name))
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組建立時間\n【{}】".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                    ret_ +="\n☲☲☲☲☲說明☲☲☲☲☲"
                    ret_ +="\n群主創建者"
                    ret_ +="\n【"+(str(gCreator))+"】"
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    ret_ +="\n群組Gid"
                    ret_ +="\n【{}】".format(group.id)
                    ret_ +="\n☲☲☲☲☲☲☲☲☲☲☲☲"
                    cl.sendMessage(to, str(ret_))
                elif text.lower() == 'rlb':
                    a = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    b = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    c = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    d = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    e = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    f = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    g = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    h = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    i = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    j = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    k = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    l = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    m = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    n = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    o = random.choice(["０","９","８","７","６","５","４","３","２","２","１"])
                    slot = "拉霸機拉霸一次\n第一行==>{}  {}  {}<==\n第二行==>{}  {}  {}<==\n第三行==>{}  {}  {}<==\n第四行==>{}  {}  {}<==\n第五行==>{}  {}  {}<==\n以上是您的拉霸結果".format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                    cl.sendMessage(to,slot)
                    if a == e == i == j == o:
                        cl.sendMessage(to,"[自動回覆]\n恭喜拉霸機中獎~~")
                        return
                    cl.sendMessage(to,"[自動回覆]\n可惜啦ww再試一次吧w")	
                elif msg.text in ["本日運勢","rls"]:
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.sendMessage(to,slot)
                    cl.sendMessage(to,"[自動回覆]\n在測試一次吧！ヽ(✿ﾟ▽ﾟ)ノ")
                elif text.lower().startswith("ai"):
                    list_ = msg.text.split(":")
                    msgs = list_[1]
                    conn = cl.findContactsByUserid(msgs)
                    cl.findAndAddContactsByMid(msgs)
                    cl.inviteIntoGroup(to,[msgs])
                    cl.sendMessage(to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                elif msg.text.lower().startswith('id'):
                    try:
                        list_ = msg.text.split(":")
                        msgs = list_[1]		
                        conn = cl.findContactsByUserid(msgs)
                        cl.sendMessage(to, "http://line.me/ti/p/~" + msgs)
                        cl.sendMessage(to, None, contentMetadata={'mid': conn.mid}, contentType=13)	
                    except:
                        cl.sendMessage(to, '執行命令錯誤')
                elif text.lower().startswith("增加回覆 "):
                    x = text.split(' ')
                    settings['mute'][x[1].lower()] = x[2]
                    cl.sendReplyMessage(msg.id, to,'成功新增關鍵字回復\n關鍵字:' + str(x[1].lower())+'\n回覆:' + str(x[2]))   
                elif text.lower().startswith("刪除回覆"):
                    x = text.split(' ')
                    del settings['mute'][x[1].lower()]
                    cl.sendReplyMessage(msg.id, to,'成功刪除關鍵字回復\n\n關鍵字:' + str(x[1].lower())) 
                #回覆列表
                elif text.lower() == '回覆列表':
                    if settings['mute'] == {}:
                        cl.sendMessage(to, "沒有回復列表")
                    else:
                        mc = "[回覆列表]"
                        no = 1
                        for iii in settings['mute']:
                            #text = settings['mute']
                            ttxt = settings['mute']["{}".format(iii)]
                            mc += "\n"+str(no)+"."+iii+"\n"+str(ttxt)
                            no += 1
                        mc += "\n[總共 {} 個回覆]".format(str(no-1))
                        cl.sendReplyMessage(msg.id,to, str(mc))
                elif msg.text.lower().startswith("youtube:"):
                    number = text.replace("youtube:","")
                    url = "https://m.youtube.com/results?search_query={}".format(number)
                    request = requests.get(url)
                    content = request.content
                    soup = BeautifulSoup(content, "html.parser")
                    ret_ = "—YouTube搜尋結果—"
                    no = 0 + 1
                    for all_mv in soup.select(".yt-lockup-video"):
                         name = all_mv.select("a[rel='spf-prefetch']")
                         ret_ += "\n\n =====[ {} ]====={}\n\n https://www.youtube.com{}".format(str(no), str(name[0].get("title")), str(name[0].get("href")))
                         no += 1
                    cl.sendReplyMessage(msg.id, to, str(ret_))
                elif text.lower().startswith("票 "):
                    x = text.split(" ")
                    if not ismid(x[1]):
                        return
                    if x[1] not in settings["user"]:
                        settings["user"][x[1]] = []
                    if len(x) ==2:
                        t = 1
                    elif len(x) ==3:
                        try:
                            t = int(x[2])
                        except:
                            t = 0
                            cl.relatedMessage(to,"沒有這個識別碼",op.message.id)
                    settings["user"][x[1]] += ["gid"]*t
                    cl.relatedMessage(to,"成功發出" + str(t) + "張",op.message.id)
                    json.dump(settings, codecs.open('temp.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                elif msg.text.lower().startswith("name "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[Name]\n" + cl.getContact(inkey).displayName)
                elif msg.text.lower().startswith("mname"):
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[Name]\n" + me.displayName)
                elif msg.text.lower().startswith("mbio"):
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif msg.text.lower().startswith("nc "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[自訂名稱]\n" + cl.getContact(inkey).displayNameOverridden)
                elif msg.text.lower().startswith("bio "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + cl.getContact(inkey).statusMessage)
                elif msg.text.lower().startswith("cover "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to, cl.getProfileCoverURL(inkey))
                elif msg.text.lower().startswith("picture "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus)
                elif msg.text.lower().startswith("videoprofile "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus + "/vp")
                elif msg.text.lower().startswith("info "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName +"\n[ 個簽 ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                            cl.sendImageWithURL(msg.to, str("http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus)) 
                            cl.sendImageWithURL(msg.to, str(cl.getProfileCoverURL(ls)))
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    s = text.split(' ')
                    cl.findAndAddContactsByMid(inkey)
                    try:
                        for a in range(int(s[2])):
                            cl.createGroup("L.D.T System-邀機測試",[inkey])
                    except:
                        pass
                    c =cl.getGroupIdsByName("L.D.T System-邀機測試")
                    for gid in c:
                        cl.leaveGroup(gid)
                elif text.lower() == '剔除':
                    asyncio.run(kkickrun())
                #addop
                elif text.lower().startswith("opp "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in settings["admin"]:
                        settings["admin"].append(str(inkey))
                        cl.relatedMessage(to, "已獲得權限！",op.message.id)
                    else:
                        cl.relatedMessage(to,"此用戶已擁有權限",op.message.id)
                elif msg.text.lower().startswith("delop "):
                    try:
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        settings["admin"].remove(str(inkey))
                        cl.sendMessage(op.message.to, "已取消權限！")
                    except:
                        cl.relatedMessage(to,"此用戶沒有權限",op.message.id)
                elif msg.text.lower().startswith("主人"):
                    cl.sendMessage(op.message.to, "👇👇我的主人!!👇👇")
                    cl.sendContact(op.message.to, "u4f749287486340aff896823734edbea2")
                elif text.lower() == 'oplist':
                    if settings["admin"] == []:
                        cl.sendMessage(op.message.to,"無擁有權限者!")
                    else:
                        mc = "[ 權限者  ]"
                        for mi_d in settings["admin"]:
                            mc += "\n➽➤"+cl.getContact(mi_d).displayName
                        cl.sendMessage(op.message.to,mc + "\n[ 結束  ]")
                elif msg.text.lower().startswith("system "):
                    BanText = ["cd ..", "root", "passwd"]
                    txt = text[7:]
                    if sender != King:
                        for i in BanText:
                            if i in cmd:
                                return cl.sendMessage(to, "You are not a privilege")
                    cl.sendMessage(to, str(subprocess.Popen([txt], shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
                    return
                #專武
                elif op.message.text.lower() == ".set":
                    t1 = time.time()
                    threading.Thread(target=cl.sendMessage, args=(op.message.to, "",)).start()
                    t2 = time.time() - t1
                    time.sleep(0.1)
                    ret_ = "[資料]\n"
                    if datadir["switch"] == False: ret_ +="C4尚未設置\n"
                    else: ret_ += "C4已設置成功\n"
                    if settings["kick"] == False: ret_ +="專武未開啟\n"
                    else: ret_ += "專武已開啟✅\n"
                    ret_ += "已開啟之線程數:{}\n版本資訊: 專武 5.0".format(len(AuthToken))
                    cl.sendMessage(op.message.to, str(ret_))
                    return
                #專武開關
                elif text.lower() == '專武開':
                    settings["kick"] = True
                    with open('temp.json', 'w') as fp:
                        json.dump(settings, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to=op.message.to, text="專武已開啟✔")
                elif text.lower() == '專武關':
                    settings["kick"] = False
                    with open('temp.json', 'w') as fp:
                        json.dump(settings, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to=op.message.to, text="專武已關閉✖")    
                #單位
                elif text.lower() == 'sat':
                    ret_ = "［ 全部速度 ］"
                    ret_ += "\n回傳速度:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n群組邀請:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n好友讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n友資讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=1000))
                    ret_ += "\n群組讀取:\n"+str(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
                    ret_ += "\n［ 完 ］"
                    cl.sendReplyMessage(msg.id, to, str(ret_))  
                #定名踢
                elif msg.text.startswith("Nk:"): 
                    _name = msg.text.replace("Nk:","")
                    namelist = _name.split()
                    gs = cl.getGroup(to)
                    targets == [] 
                    for g in gs.member:
                        try: 
                            if _name in g.displayNameOverridden: 
                                targets.append(g.mid) 
                        except:
                            pass
                    if targets == []: 
                        cl.sendMessage(to, "沒有這個人") 
                    else:
                        try: 
                            cl.kickoutFromGroup(to, targets) 
                        except:
                            cl.sendMessage(to, "規制中")
                #Yn
                elif msg.text.startswith("Yn:"):
                    c = msg.text.replace("Yn:","")
                    cl.findAndAddContactsByMid(msg.to)
                    cl.renameContact(toc)
                    contact = cl.getContact(msg.to)
                    cl.sendMessage(to, "更改定名:"+contact.displayNameOverridden)
                #加入好友
                elif msg.text.lower().startswith("ad "):
                    MENTION = eval(msg.contentMetadata['MENTION']) 
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.findAndAddContactsByMid(inkey)
                    cl.sendMessage(to,"成功加入好友")
                #定名
                elif msg.text.startswith("Ni:"):
                    _name = msg.text.replace("Ni:","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        try:
                            cl.inviteIntoGroup(to, targets)
                        except:
                            cl.sendMessage(to, "規制中")
                elif msg.text.startswith("Sex "):
                    txt = msg.text.split(" ")
                    text = msg.text.replace("Sex "+txt[1]+" ","")
                    if text != "":
                        for x in range(int(txt[1])):
                            if "MENTION" in msg.contentMetadata.keys()!= None:
                                datalist = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                taglist = []
                                for data in datalist:
                                    tags = int(data["S"]) - 5 - len(txt[1])
                                    tage = int(data["E"]) - 5 - len(txt[1])
                                    tagm = data["M"]
                                    taglist.append({"S":str(tags), "E" :str(tage), "M":tagm})
                                cl.sendMessage(msg.to, text, contentMetadata={u"MENTION": json.dumps({"MENTIONEES":taglist})})
                            else:
                                cl.sendMessage(msg.to, text)
                elif msg.text.startswith("Ac:"):
                    _name = msg.text.replace("Ac:","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        for target in targets:
                            cl.sendContact(to, target)
                elif "Tn*" in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    ga = cl.getAllContactIds()
                    txt = msg.text.split("*")
                    text = msg.text.replace("Tn*"+txt[1]+"*","")
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        for key1 in targets:
                            if key1 not in ga:
                                cl.findAndAddContactsByMid(key1)
                            cl.renameContact(key1, text)
                            cl.sendMessage(to, "更改定名:"+cl.getContact(key1).displayNameOverridden)
                elif msg.text.startswith("Di:"):
                    _name = msg.text.replace("Di:","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            try:
                                if name in g.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        try:
                            cl.inviteIntoGroup(to,targets)
                        except:
                            cl.sendMessage(to, "規制中")
                elif msg.text.startswith("Adc:"):
                    _name = msg.text.replace("Adc:","")
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            try:
                                if name in g.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                    if targets == []:
                        cl.sendMessage(to, "沒這個人")
                    else:
                        for target in targets:
                            cl.sendContact(to, target)
            if sender in settings["admin"]:
                if text.lower().startswith("解封鎖 "):
                    if sender in X:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        a = 0
                        for target in targets:
                            cl.unblockContact(target)
                            a += 1
                        cl.sendMessage(msg.to,"已解封鎖共" + str(a) + "人")
                    else:
                        cl.relatedMessage(to,"你不是中路",op.message.id)
            if sender in settings["admin"]:
                if text.lower().startswith("封鎖 "):
                    if sender in X:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        a = 0
                        for target in targets:
                            cl.blockContact(target)
                            a += 1
                        cl.sendMessage(msg.to,"已封鎖共" + str(a) + "人")
                    else:
                        cl.relatedMessage(to,"你不是中路,無法執行",op.message.id)
                elif text.lower() == '邀取消機':
                    mid = "u96f3bb9b894f4ec6317788d5124f298a"
                    cl.findAndAddContactsByMid(mid)
                    cl.inviteIntoGroup(to,[mid])
                #少數重要功能
                elif text.lower() == '中路重啟':
                    cl.sendMessage(to, "重新啟動中....")	
                    cl.sendMessage(to, "重啟完成")
                    restartBot()
                elif op.message.text.lower().startswith("cad "):
                    input1 = op.message.text.replace("cad "," ")
                    num1 = int(input1)
                    cl.sendMessage(op.message.to, "線程準備登入中請稍後")
                    cl.sendMessage(op.message.to, "載入數量:" + str(num1))
                    cl.sendMessage(op.message.to, "登入中")
                    for i in range(0, num1):
                        AuthToken.append(LINE(cl.authToken))
                    cl.sendMessage(op.message.to, "載入成功")
                elif text.lower() == '.setk':
                    cl.sendMessage(to, " ☵☲核彈設定☱☴\n核彈已開啟✔\n進群踢已關閉\n線呈數{}\n取消線呈{}\n版本:半垢核彈".format(len(AuthToken),len(AuthToken1)))	
                elif text.lower() == '增線':
                    AuthToken.append(LINE(cl.authToken))
                    cl.sendMessage(to, "已增加線呈數")	
                elif text.lower() == '中路 滾':
                    if msg.toType == 2:
                        cl.sendMessage(op.message.to,"各位再見,有心邀回")
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)
                        except:
                            cl.leaveRoom(to) 
                elif text.lower() == '增加線呈':
                    for i in range(1,51):
                        try:
                            AuthToken.append(LINE(cl.authToken))
                        except:
                            pass
                    cl.sendMessage(to, "已增加線呈數50")
                elif text.lower() == '增加線呈數':
                    for i in range(1,11):
                        try:
                            AuthToken1.append(LINE(cl.authToken))
                        except:
                            pass
                    cl.sendMessage(to, "已增加線呈數" + str(i))	
                elif text.lower() == 'ren':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" +Runtime(eltime)
                    cl.sendMessage(msg.to,bot)	
                elif text.lower() == 'res':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
				#進群退群退副本
                elif text.lower() == 'raj on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟 ✔")	
                elif text.lower() == 'raj off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉 ✘")	
                elif text.lower() == 'ra on':
                    settings["autoJoinkick"] = True
                    cl.sendMessage(to, "進群翻已開啟 ✔")	
                elif text.lower() == 'ra off':
                    settings["autoJoinkick"] = False
                    cl.sendMessage(to, "進群翻已關閉 ✘")		
                elif text.lower() == 'ral on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟 ✔")	
                elif text.lower() == 'ral off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉 ✘")	
                elif text.lower() == 'rqj on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址自動入群已開啟 ✔")	
                elif text.lower() == 'rqj off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關閉 ✘")	
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    cl.sendMessage(to, "自動進退已開啟 ✔")	
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    cl.sendMessage(to, "自動進退已關閉 ✘")	
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "貼圖查詢已開啟 ✔")	
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "貼圖查詢已關閉 ✘")
                elif text.lower() == 'cc on':
                    settings['cc'][to] = True
                    cl.sendReplyMessage(msg.id, to, "生成貼圖指令開啟")
                elif text.lower() == '貼圖 off':
                    del settings['cc'][to]
                    cl.sendReplyMessage(msg.id, to, "生成貼圖指令關閉")
				#其餘加好友收回自動已讀
                elif text.lower() == 'rdd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟 ✔")	
                elif text.lower() == 'rdd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉 ✘")	
                elif text.lower() == 'red on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟 ✔")	
                elif text.lower() == 'red off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉 ✘")	
                elif text.lower() == 'rd on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟 ✔")	
                elif text.lower() == 'rd off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉 ✘")	
				#更改顯示
                elif text.lower() == 'rt on':
                    wait["resset"] = True
                    cl.sendMessage(to, "偵測更新帳號\n名子✘/圖片✘/個簽✘\n更新為開啟偵測狀態✔\n名子✔/圖片✔/個簽✔")	
                elif text.lower() == 'rt off':
                    wait["resset"] = False
                    cl.sendMessage(to, "偵測更新帳號\n名子✔/圖片✔/個簽✔\n更新為關閉偵測狀態✘\n名子✘/圖片✘/個簽✘")	
				#踢人顯示
                elif text.lower() == 'rc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "踢人標註已開啟 ✔═")	
                elif text.lower() == 'rc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "踢人標註已關閉 ✘═")	
				#進群退群
                elif text.lower() == 'rj on':
                    settings["seeJoin"] = True
                    cl.sendMessage(to, "入群通知已開啟 ✔═")	
                elif text.lower() == 'rj off':
                    settings["seeJoin"] = False
                    cl.sendMessage(to, "入群通知已關閉 ✘═")	
                elif text.lower() == 'rl on':
                    settings["seeLeave"] = True
                    cl.sendMessage(to, "退群通知已開啟 ✔═")	
                elif text.lower() == 'rl off':
                    settings["seeLeave"] = False
                    cl.sendMessage(to, "退群通知已關閉 ✘═")	
                elif text.lower() == 'rm on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已開啟 ✔")	
                elif text.lower() == 'rm off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已關閉 ✘")	
                elif text.lower() == 'ru on':
                    wait["um"] = True
                    cl.sendMessage(to, "收回已開啟 ✔")	
                elif text.lower() == 'ru off':
                    wait["um"] = False
                    cl.sendMessage(to, "收回已關閉 ✘")	
                elif text.lower() == 'cn on':
                    wait["contact"] = True
                    cl.sendMessage(to, "已開啟 ✔")	
                elif text.lower() == 'cn off':
                    wait["contact"] = False
                    cl.sendMessage(to, "已關閉 ✘")	
				#保護項目
                elif text.lower() == 'rop on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟 ✔")
                elif text.lower() == 'rop off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉 ✘")
                elif text.lower() == 'rip on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟 ✔")
                elif text.lower() == 'rip off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉 ✘")
                elif text.lower() == 'rqp on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟 ✔")
                elif text.lower() == 'rqp off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉 ✘")
                elif text.lower() in ['開啟']:
                    if msg.toType ==2:
                        jg["JoinGroup"][to] = True
                        cl.sendMessage(to, "開啟 ✔")
                elif text.lower() in ['關閉']:
                    if msg.toType ==2 :
                        try:
                            del jg["JoinGroup"][to]
                            cl.sendMessage(to, "關閉 ✘")
                        except:
                            cl.sendMessage(to, "關閉狀態中 ✘")
                elif text.lower() == 'bl on':
                    settings["autoAdd"] = False
                    settings["invBlock"] = True
                    cl.sendReplyMessage(msg.id, to, "自動封鎖開啟")
                elif text.lower() == 'bl off':
                    settings["autoAdd"] = True
                    settings["invBlock"] = False
                    cl.sendReplyMessage(msg.id, to, "自動封鎖關閉")  
                elif text.lower() == 'block on':
                    settings["kick"] = False
                    settings["Block"] = True
                    cl.sendReplyMessage(msg.id, to, "踢人封鎖開啟")
                elif text.lower() == 'block off':
                    settings["kick"] = True
                    settings["Block"] = False
                    cl.sendReplyMessage(msg.id, to, "踢人封鎖關閉")  
                elif text.lower() == 'war:on':
                    cl.sendMessage(to,"已開啟戰爭模式")
                    settings["warmode"][to] = True
                elif text.lower() == 'war:off':
                    cl.sendMessage(to,"已關閉戰爭模式")
                    del settings["warmode"][to]
                elif text.lower() == 'war':
                    if to in settings["warmode"]:
                        cl.sendMessage(to,"戰爭狀態:開啟")
                    else:
                        cl.sendMessage(to,"戰爭狀態:關閉")
                elif text.lower() == '模式 邀請':
                    settings["bgi"] = False
                    cl.sendMessage(to, "模式:1(邀請)✘維修中")
                    cl.sendMessage(to, "已幫您轉為網址入群")
                elif text.lower() == '模式 網址':
                    settings["bgi"] = False
                    cl.sendMessage(to, "模式:2(網址)")
                elif text.lower() == '模式':
                    bgin = None
                    if settings["bgi"] == False:
                        bgin = "網址"
                    elif settings["bgi"] == True:
                        bgin = "邀請"
                    cl.sendMessage(to,"模式:{}".format(len(bgin)))
                elif text.lower() == 'joing on':
                    settings["bodyguard"] = True
                    cl.sendMessage(to, "進群已開啟 ✔")	
                elif text.lower() == 'joing off':
                    settings["bodyguard"] = False
                    cl.sendMessage(to, "進群保鑣已關閉 ✘")	
				#機器開關查詢
                elif text.lower() == 'set':
                    try:
                        ret_ = "大米半垢 V4 設定"
                        ret_ += "\n進群類型 開關"
                        if settings["autoJoin"] == True: ret_ += "\n自動入群 ✅"
                        else: ret_ += "\n自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址入群 ✅"
                        else: ret_ += "\n網址入群 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n自離副本 ✅"
                        else: ret_ += "\n自離副本 ❌"
                        ret_ += "\n其餘功能 開關"
                        if settings["autoAdd"] == True: ret_ += "\n自動加友 ✅"
                        else: ret_ += "\n自動加友 ❌"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 ✅"
                        else: ret_ += "\n自動已讀 ❌"
                        if settings["invblock"] == True: ret_ += "\n防邀機開啟 ✅"
                        else: ret_ += "\n防邀機關閉 ❌"
                        if settings["checkSticker"] == True: ret_ += "\n貼圖查詢 ✅"
                        else: ret_ += "\n貼圖查詢 ❌"
                        if settings["reread"] == True: ret_ += "\n查詢收回 ✅"
                        else: ret_ += "\n查詢收回 ❌"
                        if wait["resset"] == True: ret_ += "\n偵測更改 ✅"
                        else: ret_ += "\n偵測更改 ❌"
                        ret_ += "\n保護類型 開關"
                        if settings["protect"] == True: ret_ += "\n群組保護 ✅"
                        else: ret_ += "\n群組保護 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n邀請保護 ✅"
                        else: ret_ += "\n邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n網址保護 ✅"
                        else: ret_ += "\n網址保護 ❌"
                        ret_ += "\n通知類型 開關"
                        if settings["seeJoin"] == True: ret_ += "\n入群通知開啟 ✅"
                        else: ret_ += "\n入群通知關閉 ❌"
                        if settings["seeLeave"] == True: ret_ += "\n退群通知開啟 ✅"
                        else: ret_ += "\n退群通知關閉 ❌"
                        if msg.toType==2:
                            ret_ += "\n大米半垢 V4 單群設定"
                            G = cl.getGroup(msg.to)
                            ret_ += "\n群組名稱\n<{}>".format(str(G.name))
                            ret_ += "\n進群保護 開關"
                            if G.id in jg["JoinGroup"] : ret_+="\n進群保護 ✅"
                            else: ret_ += "\n進群保護 ❌"
                        ret_ += "\n作者: 大米"
                        ret_ += "\n<查詢完畢>"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == '群管':
                    G = cl.getGroup(to)
                    if G.id not in settings["gm"] or settings["gm"][G.id]==[]:
                        cl.relatedMessage(to,"無此群助手「(°ヘ°)",op.message.id)
                    else:
                        try:
                            mc = "⇉⇉⇉⇉以下為此群助手⇇⇇⇇⇇\n"
                            no = 0 
                            for mi_d in settings["gm"][G.id]:
                                no += 1	                                
                                mc += "➢{}. ".format(str(no))+ cl.getContact(mi_d).displayName + "\n"
                            mc += "➢總共"+str(len(settings["gm"][to]))+"個人\n"
                            cl.relatedMessage(to, mc+"◎◎◎◎◎◎◎◎◎◎◎◎◎◎",op.message.id)
                        except:
                            pass
				#機器簡介
                elif text.lower() == 'about':
                    try:
                        cl.kickoutFromGroup(to,["fuck"])
                        cl.inviteIntoGroup(to, ["fuck"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                        arr = []
                        t1 = time.time()
                        cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "About檢查中......")
                        t2 = (time.time() - t1)/100
                        owner = "u2db707c088044deb4757c666d1eea1a0"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        eltime = time.time() - mulai
                        bot = Rtime(eltime)
                        ret_ = "《關於自己》"
                        ret_ += "\n➲群組數量: {}".format(str(len(grouplist)))
                        ret_ += "\n➲好友人數: {}".format(str(len(contactlist)))
                        ret_ += "\n➲封鎖人數: {}".format(str(len(blockedlist)))
                        ret_ += "\n➲個簽字數: {}".format(str(len(clProfile.statusMessage)))
                        ret_ += "\n➲最愛人數: {}".format(str(len(cl.getFavoriteMids())))
                        ret_ += "\n➲封鎖好友: {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n➲邀請群組: {}".format(str(len(cl.getGroupIdsInvited())))
                        ret_ += "\n➲Line帳號ID:\n➲{}".format(clProfile.userid)
                        ret_ += "\n➲個人名稱:\n➲{}".format(contact.displayName)
                        ret_ += "\n➲個人網址(一):\n➲http://line.me/ti/p/{}".format(str(clProfile.userid))
                        ret_ += "\n➲個人網址(二):\n➲http://line.me/ti/p/{}".format(str(clSetting.contactMyTicket))
                        ret_ += "\n➲識別碼:\n➲{}".format(str(clProfile.mid))
                        ret_ += "\n《狀態規制》"
                        ret_ += "\n➲踢人狀態: {}".format(aa)
                        ret_ += "\n➲邀請狀態: {}".format(aa)
                        ret_ += "\n➲取消狀態: 可以執行(無規制)"
                        ret_ += "\n《個人開關》"
                        if settings["autoJoin"] == True: ret_ += "\n➲自動入群 ✅"
                        else: ret_ += "\n➲自動入群 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n➲網址入群 ✅"
                        else: ret_ += "\n➲網址入群 ❌"
                        if settings["reread"] == True: ret_ += "\n➲防止收回 ✅"
                        else: ret_ += "\n➲防止收回 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➲自動已讀 ✅"
                        else: ret_ += "\n➲自動已讀 ❌"
                        ret_ += "\n《關於半垢》"
                        ret_ += "\n➲商業半垢 V4"
                        ret_ += "\n➲半垢作者:\n➲{}".format(creator.displayName)
                        ret_ += "\n➲半垢極限速度:\n➲{}".format(str(t2))
                        ret_ += "\n➲半垢運行時間:\n➲l───────●──────l\n➲{}\n➲⇆ ㅤ ㅤ◁  ㅤ❚ ❚  ㅤ▷  ㅤ↻".format(bot)
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                #網址開關
                elif text.lower() == 'ru':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組沒有開啟網址")
                elif msg.text.lower().startswith("add_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number not in settings['sr']:
                            try:
                                settings['sr'][number] = list_[3]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[新增貼圖回應]\n" + "回應: " + list_[3] + "\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n" + "新增貼圖關鍵字失敗")
                        else:
                            cl.sendMessage(to, "[ERROR]\n" + "貼圖關鍵字已存在")
                elif msg.text.lower().startswith("del_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number in settings['sr']:
                            try:
                                del settings['sr'][number]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[刪除貼圖關鍵字]\n成功刪除貼圖關鍵字!!!\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n刪除貼圖關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定刪除的貼圖關鍵字並不在列表中!!!")
                elif msg.text.lower().startswith("renew_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number in settings['sr']:
                            try:
                                del settings['sr'][number]
                                settings['sr'][number] = list_[3]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[更新貼圖回應]\n成功更新貼圖回應!!!\n回應: " + list_[3] + "\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n更新貼圖關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定更新貼圖關鍵字並不在列表中!!!")              
                elif text.lower() == 'ro':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "開啟成功")
                elif text.lower() == 'rc':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "關閉成功")
                elif text.lower() == '全票':
                    user1 = ""
                    for x in settings["user"]:
                        user1 += "【票卷持有者】\n├≽"+cl.getContact(x).displayName+"\n[票卷] {}\n[群組]\n".format(str(settings["user"][x].count("gid")))
                        for y in settings["user"][x]:
                            if y != "gid":
                                try:
                                    user1 += "├≽ "+cl.getGroupWithoutMembers(y).name+"\n"+str(y)+""
                                except:
                                    user1 += "├≽ #Can't not relate to that group#\n"
                        user1 += "\n─────────\n"
                    cl.sendMessage(to,user1+"[完成]") 
                #廣播
                elif text.lower().startswith("rt:"):
                    id = text[3:].split(':')
                    for x in range(int(id[1])):
                        cl.sendPostToTalk(to,id[0])
                    cl.sendMessage(to, "文章分享完畢")
                elif text.lower().startswith("rpc:"):
                    separate = text.split(":")
                    bctxt = text.replace(separate[0] + ":","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,bctxt[1])
                elif text.lower().startswith("rgb:"):
                    data = text[4:].lower().split(':')
                    if len(data) == 2:data.append("0")
                    elif len(data) >3 or len(data) <2:return
                    try:int(data[2])
                    except:return
                    if data[0] == 'text':
                        n = cl.getGroupIdsJoined()
                        g = 0
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(data[2]):
                                cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《文字》\n" + data[1])
                                g+=1
                            else:
                                pass
                        cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    elif data[0] in ['pic', 'contact', 'post']:
                        wait['gbc'][sender] = {'type':data[0],'text':data[1],'over':data[2]}
                        cl.sendMessage(to,'請發送你要廣播的東西~')
				#測速功能
                elif text.lower() == 'sp':
                    start = time.time()
                    contact = cl.getContact(sender)
                    elapsed_time = time.time()- start
                    cl.sendReplyMention(msg_id, to,"☰☱☲☳標註測速☴☵☶☷\n☰☱☲☳測速者為☴☵☶☷\n@!\n☰☱☲☳測速結果☴☵☶☷\n"+ format(str(elapsed_time)) + "秒\n☰☱☲☳☰☱☲☳☴☵☶☷☶",[contact.mid])
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組mid : ]\n" + gid.id)
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif msg.text in ["/sp","/speed"]:
                    t1 = time.time()
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "第1次速度")
                    t2 = time.time() - t1
                    time.sleep(0.01)
                    t3 = time.time()
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "第2次速度")
                    t4 = time.time() - t3
                    time.sleep(0.01)
                    t5 = time.time()
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "第3次速度")
                    t6 = time.time() - t5
                    time.sleep(0.01)
                    t7 = time.time()
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "第4次速度")
                    t8 = time.time() - t7
                    time.sleep(0.01)
                    t9 = time.time()
                    cl.sendMessage("c1dca4d48eac80ad9d8d5dd2802e2662d", "第5次速度")
                    t10 = time.time() - t9
                    time.sleep(0.01)
                    a1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b1 = str(a1)
                    a2 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b2 = str(a2)
                    a3 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b3 = str(a3)
                    a4 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b4 = str(a4)
                    a5 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b5 = str(a5)
                    ret_ = "     [反應速度]\n"
                    ret_ += "第一次:{}秒\n".format(str(t2))
                    ret_ += "第二次:{}秒\n".format(str(t4))
                    ret_ += "第三次:{}秒\n".format(str(t6))
                    ret_ += "第四次:{}秒\n".format(str(t8))
                    ret_ += "第五次:{}秒\n     [處理速度]\n".format(str(t10))
                    ret_ += "第一次:{}秒\n".format(str(b1))
                    ret_ += "第二次:{}秒\n".format(str(b2))
                    ret_ += "第三次:{}秒\n".format(str(b3))
                    ret_ += "第四次:{}秒\n".format(str(b4))
                    ret_ += "第五次:{}秒\n".format(str(b5))
                    ret_ += "     [速度測試]"
                    cl.sendMessage(to, str(ret_))
				#踢人指令
                elif text.lower().startswith("ri:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("ti:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("vk:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif msg.text.lower().startswith("tk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif msg.text.lower().startswith("fk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.leaveRoom(msg.to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif text.lower() == '更換頭貼':
                    wait["clp"] = True
                    cl.sendMessage(to,"丟出您想更換的頭貼")
                elif text.lower() == '更換封面':
                    wait["clpp"] = True
                    cl.sendMessage(to,"丟出您想更換的封面")
                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif text.lower() == 'cccdl':
                    for x in settings["user"]:
                        settings["user"] = {}
                    cl.sendMessage(to, "已收回全部票卷") 
                elif text.lower().startswith("ccd"):
                    num = int(text.lower().split(' ')[2])
                    user = str(text.lower().split(' ')[1])
                    if settings["user"][user].count('gid') >= num:
                        for a in range(num):
                            settings["user"][user].remove("gid")
                        cl.relatedMessage(to,"成功收回" + str(num) + "張票",op.message.id)
                    else:
                        cl.relatedMessage(to,"此人的證件不夠多能進行收回動作",op.message.id)
                elif text.lower() == 'join':
                    if to in settings['jm']:
                        cl.sendMessage(to, settings['jm'][to])
                    else:
                        cl.sendMessage(to, "未設置")
                elif msg.text.startswith("join:"):
                    _name = msg.text.replace("join:","")
                    if _name == '':
                        cl.sendMessage(to,"已關閉")
                        settings["jm"][to] = ""
                    else:
                        settings["jm"][to] = _name
                        cl.sendMessage(to,"已更改至{}".format(str(_name)))
                elif msg.text.startswith("joinleave:"):
                    _name = msg.text.replace("joinleave:","")
                    if _name == '':
                        cl.sendMessage(to,"已關閉")
                        settings["seeLeave"][to] = ""
                    else:
                        settings["seeLeave"][to] = _name
                        cl.sendMessage(to,"已更改至{}".format(str(_name)))
                elif msg.text.lower().startswith("ti "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif msg.text.lower().startswith("vk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif text.lower() == 'mine':
                     try:
                         cl.kickoutFromGroup(msg.to, ["fuck you"])
                         cl.sendMessage(msg.to, "正常")
                     except Exception as e:
                         if e.reason == "request blocked":
                            me = cl.getContact(sender)
                            cl.sendMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: request blocked\n邀請狀態: request blocked\n取消狀態: 可以執行\n[完]")
                         else:
                            me = cl.getContact(sender)
                            cl.sendMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: 可以執行\n邀請狀態: 可以執行\n取消狀態: 可以執行\n[完]")
                elif text.lower() == 'check':
                     try:
                         cl.kickoutFromGroup(msg.to, ["fuck you"])
                         cl.sendMessage(msg.to, "正常")
                     except Exception as e:
                         if e.reason == "request blocked":
                            me = cl.getContact(sender)
                            cl.sendMessage(op.message.to, "💥查詢中💥")
                            cl.sendMessage(op.message.to,"🔥規制中🔥")
                         else:
                            me = cl.getContact(sender)
                            cl.sendMessage(op.message.to, "💥查詢中💥")
                            cl.sendMessage(op.message.to,"🔥無規制🔥")
                elif "/邀請我:" in msg.text:
                    gid = msg.text.replace("/邀請我:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                        except:
                            cl.sendMessage(to, "我不在群組內")
                elif msg.text.lower().startswith('邀請我'):
                    x = text.split(' ')
                    groups = cl.groups
                    targets = []
                    for gid in groups:
                        group = cl.getGroup(gid)
                        targets.append(group.id)
                    c = int(x[1])
                    c = c-1
                    gid = targets[c]
                    group = cl.getGroup(gid)
                    if gid == "":
                        cl.sendMessage(to, "請輸入數字")
                    else:
                        try:
                            cl.sendMessage(gid, "權限者遠端邀請.....")
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                            cl.sendReplyMessage(msg.id,to, "成功邀請至:\n" + str(group.name))
                        except:
                            cl.sendMessage(to, "我不在群組內\n或是正在群內\n導致無法邀請")
                elif msg.text.lower().startswith('網址'):
                    x = text.split(' ')
                    groups = cl.groups
                    targets = []
                    for gid in groups:
                        group = cl.getGroup(gid)
                        targets.append(group.id)
                    c = int(x[1])
                    c = c-1
                    gid = targets[c]
                    group = cl.getGroup(gid)
                    if group.preventedJoinByTicket == False:
                        cl.updateGroup(group)
                        ticket = cl.reissueGroupTicket(gid)
                        cl.relatedMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                    if group.preventedJoinByTicket == True:
                        group.preventedJoinByTicket = False
                        cl.updateGroup(group)
                        ticket = cl.reissueGroupTicket(gid)
                        cl.relatedMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                elif "開網址 " in msg.text: 
                    gid = msg.text.replace("開網址 ","")
                    group = cl.getGroup(gid)
                    if group.preventedJoinByTicket == False:
                        cl.updateGroup(group)
                        ticket = cl.reissueGroupTicket(gid)
                        cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                    if group.preventedJoinByTicket == True:
                        group.preventedJoinByTicket = False
                        cl.updateGroup(group)
                        ticket = cl.reissueGroupTicket(gid)
                        cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower().startswith("公告:"):
                        separate = text.split(":")
                        a = text.replace(separate[0] + ":","")
                        c = ChatRoomAnnouncementContents()
                        c.displayFields = 5
                        c.text = a
                        c.link = "line://nv/chatMsg?chatId={}&messageId={}".format(to,msg.id)
                        try:            
                            cl.createChatRoomAnnouncement(to, 0, c)
                            sendMention(to, "成功新增公告 by. @!", [sender])
                        except Exception as e:
                            cl.sendMessage(to, str(e))
                elif text.lower().startswith("mc:"):
                    separate = text.split(":")
                    mmid = text.replace(separate[0] + ":","")
                    cl.sendContact(to, mmid)
                elif msg.text.lower().startswith("cn:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.sendReplyMessage(msg.id,to, A)
                elif msg.text.lower().startswith("jp:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("en:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
				#Token
                elif text.lower() == 'tad':
                    t= threading.Thread(target=gettoken, args=(to,))
                    t.start()
                    sleep(2) 
                    f = open('linepy/url.txt','r')
                    url = f.read()
                    f.close()
                    cl.sendMessage(to,"兩分鐘內登入獲取Token")
                    cl.sendMessage(to,url)
                    t.join()
                elif "Yd" in msg.text:
                    try:
                        text = msg.text.replace("Yd","")
                        cl.renameContact(to, text)
                        cl.sendMessage(msg.to, "更改定名:"+cl.getContact(to).displayNameOverridden)
                    except Exception as error:
                        if error.reason == "Invalid mid":
                            cl.sendMessage(to,"不可用於群組")
				#mid或其餘方式功能
                elif text.lower().startswith("mc:"):
                        separate = text.split(":")
                        mmid = text.replace(separate[0] + ":","")
                        cl.sendContact(to, mmid)
                        cl.sendMessage(to,"幫您丟出友資\n友資MID\n"+mmid+"\n幫您生成完畢")
                elif text.lower().startswith("inv:"):
                        separate = text.split(":")
                        midd = text.replace(separate[0] + ":","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(msg.to,[midd])
                        cl.sendMessage(to,"已經幫您邀請\n"+midd+"\n邀請完畢\n或可能此人已經在群組")
                elif text.lower().startswith("ce:"):
                        separate = text.split(":")
                        txt = text.replace(separate[0] + ":","")
                        cl.createPost(txt)
                        cl.sendMessage(to,"正在幫您生成貼文\n貼文創建內容:\n" + txt + "\n貼文創建完畢")
                elif text.lower().startswith("pn:"):
                        separate = text.split(":")
                        string = text.replace(separate[0] + ":","")
                        if len(string) <= 1000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(to,"名稱已更改為\n=>" + string + "")
                        if len(string) >= 1001:
                            cl.sendMessage(to,"[警告]\n名稱不能突破1000字喔!!\n超過1000字強制更改\n將會凍帳一小時\n以下是您想突破的文字名稱\n" + string + "")
                if msg.text in ["sr","Setread","設定"]:
                    cl.sendMessage(msg.to, "設置已讀點 ✔")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["cr","Delread","刪除"]:
                    cl.sendMessage(to, "刪除已讀點 ✘")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["lr","Lookread","偵測"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀的人/順序]:%s\n\n查詢時間:[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")				#後台指令
                elif text.lower() == 'us':
                    try:
                        cl.unsendMessage(msg.sendMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "秒" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.sendMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✘" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.sendMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✔" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.sendMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif text.lower() == 'clopp':
                    settings["admin"] = []
                    cl.relatedMessage(to,"清空權限完成",op.message.id)
                #查詢gid功能
                elif "tg:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.members
                    d = ""
                    d += "群組成員\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            d += "成員:"+mn+"\n"
                        except:
                            pass
                    d += "成員清單生成完畢"
                    cl.sendMessage(to,d)
                elif "tgm:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.members
                    d = ""
                    d += "群組成員\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            mi = cl.getContact(i.mid).mid
                            d += "成員:"+mn+"\n成員Mid:"+mi+"\n"
                        except:
                            pass
                    d += "成員清單生成完畢"
                    cl.sendMessage(to,d)
                elif "te:" in msg.text[0:12]:
                    ff = msg.text.split(":")
                    a = cl.getGroup(ff[1])
                    gmb = a.invitee
                    d = ""
                    d += "群組邀請\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    if gmb != None:
                        for i in gmb:
                            try:
                                mn = cl.getContact(i.mid).displayName
                                d += "=>"+mn+"\n"
                                d += "=>"+i.mid+"\n"
                            except:
                                pass
                    else:
                        d += "無邀請中成員\n"
                        d += "邀請清單生成完畢"
                    cl.sendMessage(to,d)
                elif text.lower() == 'si':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[ 邀請區名單 ]"
                        no = 0 + 1
                        for mem in group.invitee:
                            ret_ += "\n➽{}. 名稱：{}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[ 邀請區成員共 {} 人]".format(str(len(group.invitee)))
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                #群組列表
                elif text.lower() == 'lg':
                    groups = cl.groups
                    ret_ = "[群組列表]"
                    no = 0 + 1
                    for gid in groups:
                        group = cl.getGroup(gid)
                        ret_ += "\n {}. {} | {}\n群組ID:{}".format(str(no), str(group.name), str(len(group.members)),str(group.id))
                        no += 1
                    ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                    cl.sendMessage(to, str(ret_))
                elif text.lower() == 'asp':
                    start = time.time()
                    loop = asyncio.get_event_loop()
                    loop.close
                    elapsed_time = time.time() - start
                    cl.sendReplyMessage(msg.id,to,str(elapsed_time))
                elif msg.text.lower().startswith('un'): #收回指定訊息
                    try:
                        args = text.split(' ')
                        mes = 0
                        try:
                            mes = int(args[1])
                        except:
                            mes = 1
                        M = cl.getRecentMessagesV2(to, 1001)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == clMID:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            cl.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                    except:
                        pass
                elif text.lower() == '踢人名單':
                    mc = "[ 異步名單 ]\n待踢名單:"
                    if ban["tlist"] == {}:
                        mc += "\n無待踢名單"
                    else:
                        for mi_d in ban["tlist"]:
                             mc += "\n➽"+cl.getContact(mi_d).displayName
                    mc += "\n待取消名單:"
                    if ban["klist"] == {}:
                        mc += "\n無待取消名單"
                    else:
                        for mi_d in ban["klist"]:
                             mc += "\n➽"+cl.getContact(mi_d).displayName
                    cl.sendReplyMessage(msg.id, to,mc + "\n[ 已經幫你查詢完畢 ]")
                elif text.lower() == '取消名單':
                    if ban["klist"] == {}:
                        cl.sendReplyMessage(msg.id, to,"➤無預備成員!\n[ 已經幫你查詢完畢 ]")
                    else:
                        mc = "[ 特殊名單 ]\n待取消名單:"
                        for mi_d in ban["klist"]:
                            mc += "\n➽"+cl.getContact(mi_d).displayName
                        cl.sendReplyMessage(msg.id, to,mc + "\n[ 已經幫你查詢完畢 ]")
                elif "ce " in text[0:3].lower():
                     cut = text.lower().split(" ")
                     gg = cl.getGroup(to).invitee
                     cut.remove("ce")
                     textt = ""
                     count = 0
                     for i in cut:
                           count += 1
                           textt += "➽{}.{}\n".format(count,gg[int(i)-1].displayName)
                           ban["klist"][gg[int(i)-1].mid] = True
                     cl.sendMessage(to,textt.rstrip())
                elif "cancel" == text.lower():
                    n = 0
                    for i in ban["klist"]:
                        cl.cancelGroupInvitation(to,[i])
                        threading.Thread(target=kick, args=(n, op.message.to, [i],)).start()
                        n += 1 
                        return
                elif ".cel " in op.message.text:
                    _name = op.message.text.replace(".cel ","")
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a = 0
                    for g in gs.invitee:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in settings["admin"]:
                                pass
                            else:
                                try:
                                    ban["klist"][target] = True
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"加入名單失敗!")
                        cl.sendMessage(op.message.to,"已增加取消名單共" + str(a) + "人")
                        return
                
				#發送文字指令
                elif text.lower().startswith("sy "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.sendMessage(to,x[1])
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.sendMessage(to,x[1])
                        except:
                            cl.sendMessage(to,"無法正確執行此指令")
				#標註指令
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    start = time.time()
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                        elapsed_time = time.time() - start
                    cl.sendMessage(to, "標註完畢 共標註了{}次".format(number))
                    cl.sendMessage(to, "標註完畢\n標註共計: %s秒" % (elapsed_time))
                elif text.lower().startswith('ty'):
                    sendMessageWithMention(to,to)
                elif text.lower().startswith('tg '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessagegat(to, inkey)
                    cl.sendMessage(to, "標註完畢 共標註了{}次".format(number))
                elif text.lower() == 'rgall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'rgone':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//1
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*1 : (a+1)*1]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Mili \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif "bye " in msg.text:
                    lg = msg.text.replace("bye ","")
                    cl.sendMessage(to,"處理中...")
                    aa = cl.getGroupIdsByName(lg)
                    mes = "\n退出的群組名稱\n"
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                    cl.sendMessage(to,"總共有" + str(len(aa)) + "個群符合要求")
                    cl.sendMessage(to,"退出這些群組中...")
                    for x in aa:
                        cl.leaveGroup(x)
                        time.sleep(1)
                    cl.sendMessage(to,"成功退出了喔\n"+ mes)
                elif msg.text.lower().startswith('退出'):
                    x = text.split(' ')
                    groups = cl.groups
                    targets = []
                    for gid in groups:
                        group = cl.getGroup(gid)
                        targets.append(group.id)
                    c = int(x[1])
                    c = c-1
                    gid = targets[c]
                    group = cl.getGroup(gid)
                    cl.sendMessage(gid,"有緣再見啦")
                    cl.leaveGroup(gid)
                    cl.relatedMessage(to, "已退出群組:{}".format(str(group.name)),op.message.id)
                elif "翻掉 " in msg.text:
                    lg = msg.text.replace("翻掉 ","")
                    cl.sendMessage(to,"處理中...")
                    aa = cl.getGroupIdsByName(lg)
                    mes = "\n翻掉群組名稱\n"
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                    cl.sendMessage(to,"總共有" + str(len(aa)) + "個群符合要求")
                    cl.sendMessage(to,"翻掉這些該死的群組中...")
                    for x in aa:
                        cl.sendMessage(x,"..4")
                        time.sleep(1)
                        cl.sendMessage(x,"ti:u2db707c088044deb4757c666d1eea1a0")
                        time.sleep(0.5)
                        cl.leaveGroup(x)
                    cl.sendMessage(to,"成功翻掉了啦\n"+ mes)
                elif "查詢 " in msg.text:
                    lg = msg.text.replace("查詢 ","")
                    cl.sendMessage(to,"查詢中...")
                    aa = cl.getGroupIdsByName(lg)
                    mes = "搜索後符合的群組名稱\n"
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                        mes += "GID:"+cl.getGroup(x).id+"\n"
                    cl.sendMessage(to,mes + "\n總共有" + str(len(aa)) + "個群符合名稱")
                elif "查看:" in msg.text[0:12]:
                    lg = msg.text.replace("查看:","")
                    a = cl.getGroup(lg[1])
                    gmb = a.members
                    d = ""
                    d += "群組成員\n"
                    d += "群組名稱:{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            d += "成員:"+mn+"\n"
                        except:
                            pass
                    d += "成員清單生成完畢"
                    cl.sendMessage(to,d)
				#更改個簽指令
                elif text.lower().startswith("cb:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendMessage(to,"個簽狀態已更改為 :  \n" + string)
				#登出指令
                elif text.lower() in ["logout"]:
                    cl.sendMessage(msg.to, "直接登出請輸入[登出][Y]\n手動登出請輸入[手動][N]")	
                    wait['logout'][msg.to] = sender
                elif text.lower() in ["y","Y","N","n",]:
                    if msg.to in wait['logout'] and msg._from== wait['logout'][msg.to]:
                        if text.lower() in ["登出","y","Y"]:
                            cl.sendMessage(msg.to, "將自動幫您登出機器")	
                            cl.sendMessage(to,"[提示]\n已經自動登出後台伺服器")	
                            os._exit(0)	
                            del wait['logout'][msg.to]
                        elif text.lower() in ["N","n","手動"]:
                            cl.sendMessage(msg.to, "請點擊以下網址\nline://nv/connectedDevices/\n進行手動登出")	
                            del wait['logout'][msg.to]
                    else:
                        pass
                #掃人
                elif text.lower().startswith("mak:"):
                    txt = text[4:].split(' ')
                    ret_ = "[掃黑完成]"
                    a = 0
                    for mid in txt:
                        gid = cl.getGroupIdsJoined() 
                        cl.sendMessage(to, "MID搜尋中…\n搜尋完成\n被掃人員：" + cl.getContact(mid).displayName + "\n開始執行ฅ^•ﻌ•^ฅ")
                        for i in gid:
                            group = cl.getGroup(i)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in txt:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                pass
                            else:
                                for jj in matched_list:
                                    cl.kickoutFromGroup(i,[jj])
                                    a += 1
                                cl.sendMessage(i, "掃人目標以踢除")
                        ret_ += "\n搜索 {} 個群組".format(str(len(gid)))
                        ret_ += "\n掃到 {} 個群組".format(str(a))
                        cl.sendMessage(to, str(ret_))
                #共同群組
                elif text.lower().startswith("sg:"):
                    txt = text[3:].split(' ')
                    ret_ = "[共同群組]"
                    a = 0
                    for mid in txt:
                        gid = cl.getGroupIdsJoined() 
                        cl.sendMessage(to, "MID搜尋中…\n搜尋完成\n被查人員：" + cl.getContact(mid).displayName + "\n開始執行ฅ^•ﻌ•^ฅ")
                        for i in gid:
                            group = cl.getGroup(i)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in txt:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                pass
                            else:
                                for jj in matched_list:
                                    a += 1
                                    ret_ += "\n {}. {} | {}\nGid➲{}".format(str(a), str(group.name), str(len(group.members)),str(group.id))
                        ret_ += "\n共同 {} 個群組".format(str(a))
                        cl.sendMessage(to, str(ret_))
                elif text.lower().startswith("abg "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    a = 0
                    for target in targets:
                        if target not in cbg:
                            if target not in ban["blacklist"]:
                                cbg[target] = True
                                a += 1
                            else:
                                cl.sendMessage(to,"此人為黑單")
                        else:
                            cl.sendMessage(to,"早就是了")
                    cl.sendMessage(msg.to,"已加入共" + str(a) + "人")
                    backupData()
                elif text.lower() == 'alloff':
                    settings["text"] = False
                    settings["id"] = False
                    settings["mid"] = False
                    settings["sound"] = False
                    settings["file"] = False
                    settings["image"] = False
                    settings["video"] = False
                    cl.sendMessage(to,"已關閉")
                elif text.lower() == 'allon':
                    settings["text"] = True
                    settings["id"] = True
                    settings["mid"] = True
                    settings["sound"] = True
                    settings["file"] = True
                    settings["image"] = True
                    settings["video"] = True
                    cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收狀態':
                    bb = "=====收回狀態=====\n"
                    if settings["text"]: bb += "文字:開啟✔\n"
                    else: bb += "文字:關閉✘\n"
                    if settings["video"]: bb += "影片:開啟✔\n"
                    else: bb += "影片:關閉✘\n"
                    if settings["id"]: bb += "貼圖:開啟✔\n"
                    else: bb += "貼圖:關閉✘\n"
                    if settings["mid"]: bb += "友資:開啟✔\n"
                    else: bb += "友資:關閉✘\n"
                    if settings["sound"]: bb += "語音:開啟✔\n"
                    else: bb += "語音:關閉✘\n"
                    if settings["image"]: bb += "圖片:開啟✔\n"
                    else: bb += "圖片:關閉✘\n"
                    if settings["file"]: bb += "檔案:開啟✔\n"
                    else: bb += "檔案:關閉✘\n"
                    if settings["sendall"]: bb += "公開收回:開啟✔\n"
                    else: bb += "公開收回:關閉✘\n"
                    bb += "=====收回狀態====="
                    cl.sendMessage(to,bb)
                elif text.lower() == '查收公開':
                    if settings["sendall"] == True:
                        settings["sendall"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["sendall"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 文字':
                    if settings["text"] == True:
                        settings["text"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["text"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 影片':
                    if settings["video"] == True:
                        settings["video"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["video"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 貼圖':
                    if settings["id"] == True:
                        settings["id"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["id"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 友資':
                    if settings["mid"] == True:
                        settings["mid"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["mid"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 語音':
                    if settings["sound"] == True:
                        settings["sound"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["sound"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 圖片':
                    if settings["image"] == True:
                        settings["image"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["image"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower() == '查收 檔案':
                    if settings["file"] == True:
                        settings["file"] = False
                        cl.sendMessage(to,"已關閉")
                    else: settings["file"] = True; cl.sendMessage(to,"已開啟")
                elif text.lower().startswith("rbg "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    a = 0
                    for target in targets:
                        if target not in cbg:
                            cl.sendMessage(to,"他不是保鑣阿==")
                        else:
                            try:
                                del cbg[target]
                                a += 1
                            except:
                                cl.sendMessage(msg.to,"刪除" + str(target) + "失敗 !")
                    cl.sendMessage(msg.to,"已刪除保鑣共" + str(a) + "人")
                    backupData()
                elif text.lower() in ['bgs']:
                    if cbg == {}:
                        cl.sendMessage(msg.to,"無保鑣!")
                    else:
                        mc = "[ 保鑣列表 ]"
                        no = 0	
                        try:
                            for mi_d in cbg:
                                try:
                                    no += 1
                                    mc += "\n➲{}.".format(str(no))+cl.getContact(mi_d).displayName+"\n➲"+str(mi_d)
                                except:
                                    print("錯誤:" +str(mi_d))
                            cl.sendMessage(msg.to,mc +"\n≡≡總共"+str(len(cbg))+ "個人為保鑣≡≡")
                        except:
                            cl.sendMessage(to,"保鑣【"+(str(len(cbg)))+"】")
                #專武線程
                elif op.message.text.lower().startswith("專武test"):
                    n = 0
                    for i in AuthToken: threading.Thread(target=i.sendMessage, args=(op.message.to, str(n),)).start(); n += 1
                    return
                elif op.message.text.lower().startswith("k") and "MENTION" in op.message.contentMetadata:
                    if settings["kick"] == True:
                        key = eval(op.message.contentMetadata["MENTION"]); key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            threading.Thread(target=cl.kickoutFromGroup, args=(op.message.to, [x["M"]],)).start()
                        return cl.sendMessage(op.message.to, "以踢除")
                    else:
                        cl.sendMessage(op.message.to, "你的專武已關閉,機器不會踢人")
                elif op.message.text.lower().startswith("ttk") and "MENTION" in op.message.contentMetadata:
                    if settings["kick"] == True:
                        key = eval(op.message.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        n = 0
                        for x in key["MENTIONEES"]:
                            if n == len(AuthToken): n = 0
                            threading.Thread(target=kick, args=(n, op.message.to, [x["M"]],)).start(); n += 1
                            cl.sendMessage(op.message.to, "以踢除")
                        return
                    else:
                        cl.sendMessage(op.message.to, "你的專武已關閉,機器不會踢人")    
                elif "spk" == op.message.text.lower(): 
                    t1 = time.time()
                    threading.Thread(target=cl.sendMessage, args=(op.message.to, "線程測速中",)).start()
                    t2 = time.time() - t1
                    time.sleep(0.2)
                    return cl.sendMessage(op.message.to, "%s 秒" %t2)
                elif op.message.text.lower().startswith("ka") and len(op.message.text) == len("ka"):
                    cl.sendMessage(op.message.to, "【C4引爆裝置】\n開始引爆 請輸入「y」\n拆掉引爆 請輸入「n」\n倒數30後未回覆視同確認")
                    datadir["switch"] = True
                    datadir["gid"] = op.message.to
                    threading.Thread(target=Timer).start()
                    return
                elif op.message.text.lower().startswith("..1") and len(op.message.text) == len("..1"):
                    cl.sendMessage(op.message.to, "你是翻群狗，我要檢舉你")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in settings["admin"]:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith("..2") and len(op.message.text) == len("..2"):
                    cl.sendMessage(op.message.to, "卍陌•生の1番目のリングは再び栄光です\n卍の陌•生\n陌生の滅殺す")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in settings["admin"]:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith("老子瘋狗啦,不服來辯") and len(op.message.text) == len("老子瘋狗啦,不服來辯"):
                    cl.sendMessage(op.message.to, "我中路,開始炸你啦")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in settings["admin"]:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1 
                elif op.message.text.lower().startswith("..4") and len(op.message.text) == len("..4"):
                    if settings["kick"] == True:
                        cl.sendMessage(op.message.to, "瘋狗聯盟降臨")
                        n = 0
                        cl.sendMessage(op.message.to, "自動幫你開啟進群踢")
                        jg["JoinGroup"][op.message.to] = True
                        time.sleep(0.5)
                        for i in [contact for contact in cl.getGroup(op.message.to).members]:
                            if n == len(AuthToken):
                                n = 0
                            if i.mid not in settings["admin"]:
                                threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                                n += 1 
                    else:
                        cl.sendMessage(op.message.to, "你的專武沒開")
                elif "tnk:" in op.message.text:
                    _name = op.message.text.replace("tnk:","")
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        n = 0
                        for i in targets:
                            if n == len(AuthToken):
                                n = 0
                            if i not in settings["admin"]:
                                threading.Thread(target=kick, args=(n, op.message.to, [i],)).start()
                                n += 1
                        return
                elif op.message.text.lower().startswith("特殊拆") and len(op.message.text) == len("特殊拆"):
                    if msg.toType == 2:
                        if settings["kick"] == True:
                            group = cl.getGroup(op.message.to)
                            gMembMids = [contact.mid for contact in group.members]
                            gMembMid = [contact.mid for contact in group.invitee]
                            matched_lists = []
                            matched_list = []
                            for tag in ban["tlist"]:
                                matched_lists+=filter(lambda str: str == tag, gMembMids)
                            for tag in ban["klist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMid)
                            if matched_lists == []:
                                cl.sendMessage(op.message.to, "沒人在名單內")
                            else:
                                n = 0
                                cl.sendMessage(op.message.to, "自動開啟進群踢")
                                jg["JoinGroup"][op.message.to] = True
                                time.sleep(0.5)
                                for i in matched_lists:
                                    if n == len(AuthToken):
                                        n = 0
                                    if i not in settings["admin"]:
                                        threading.Thread(target=kick, args=(n, op.message.to, [i],)).start()
                                        n += 1
                                for i in matched_list:
                                    try:
                                        cl.cancelGroupInvitation(msg.to,[i])
                                    except Exception as e:
                                        cl.sendMessage(to,"主人抱歉，老子規制了")
                                return
                        else:
                            cl.sendMessage(op.message.to, "專武已關閉,無法執行")
                elif op.message.text.lower().startswith("特殊取消") and len(op.message.text) == len("特殊取消"):
                    if msg.toType == 2:
                        if settings["kick"] == True:
                            group = cl.getGroup(op.message.to)
                            gMembMid = [contact.mid for contact in group.invitee]
                            matched_list = []
                            for tag in ban["klist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMid)
                            if matched_list == []:
                                cl.sendMessage(op.message.to, "沒人在名單內")
                            else:
                                for i in matched_list:
                                    try:
                                        cl.cancelGroupInvitation(msg.to,[i])
                                    except Exception as e:
                                        cl.sendMessage(to,"主人抱歉，老子規制了")
                                return
                        else:
                            cl.sendMessage(op.message.to, "專武已關閉,無法執行")
                elif op.message.text.lower().startswith("清空") and len(op.message.text) == len("清空"):
                    for mi_d in ban["tlist"]:
                        ban["tlist"] = {}
                    for mi_d in ban["klist"]:
                        ban["klist"] = {}
                    cl.sendMessage(op.message.to, "已清空名單")
                elif op.message.text.lower().startswith("ktlist") and len(op.message.text) == len("ktlist"):
                    if msg.toType == 2:
                        group = cl.getGroup(op.message.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["tlist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(op.message.to, "沒人在名單內")
                        else:
                            n = 0
                            cl.sendMessage(op.message.to, "自動開啟進群踢模式")
                            jg["JoinGroup"][op.message.to] = True
                            time.sleep(0.5)
                            for i in matched_list:
                                if n == len(AuthToken):
                                    n = 0
                                if i not in settings["admin"]:
                                    threading.Thread(target=kick, args=(n, op.message.to, [i],)).start()
                                    n += 1
                            return
                elif "tta " in op.message.text:
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["tlist"][target] = True
                        except:
                            cl.sendMessage(op.message.to,"增加名單失敗 !")
                            break
                    cl.sendMessage(op.message.to,"成功")
                elif "ttd " in op.message.text:
                    targets = []
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["tlist"][target]
                            cl.sendMessage(op.message.to,"刪除名單成功 !")
                            break
                        except:
                            cl.sendMessage(op.message.to,"刪除名單失敗 !")
                            break
                elif "tma:" in op.message.text:
                    txt = op.message.text.replace("tma:","")
                    try:
                        ban["tlist"][txt] = True
                        cl.sendMessage(op.message.to,"已踢人名單!")
                    except:
                        cl.sendMessage(op.messageto,"添加名單失敗 !" +txt)
                elif "tmd:" in op.message.text:
                    txt = op.message.text.replace("tmd:","")
                    try:
                        del ban["tlist"][txt]
                    except:
                        cl.sendMessage(op.message.to,"刪除" + str(txt) + "失敗 !")
                    cl.sendMessage(op.message.to,"已刪除名單")
                elif "加入 " in op.message.text:
                    _name = op.message.text.replace("加入 ","")
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a = 0
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in settings["admin"]:
                                pass
                            else:
                                try:
                                    ban["tlist"][target] = True
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"加入名單失敗!")
                        cl.sendMessage(op.message.to,"已增加名單共" + str(a) + "人")
                elif "tnd " in op.message.text:
                    _name = text.replace("tnd ","")
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a=0
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in settings["admin"]:
                                pass
                            else:
                                try:
                                    del ban["tlist"][target]
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"刪除名單失敗!")
                        cl.sendMessage(op.message.to,"已刪除名單共" + str(a) + "人")
                elif op.message.text.lower().startswith("名單") and len(op.message.text) == len("名單"):
                    if ban["tlist"] == {}:
                        cl.sendMessage(op.message.to,"沒有人")
                    else:
                        mc = "[ 待踢名單 ]"
                        for mi_d in ban["tlist"]:
                            if ban["tlist"][mi_d] == True:
                                mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                            else:
                            	mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                        cl.sendMessage(op.message.to,mc + "\n[ 以上Ouo]")
                elif op.message.text.lower().startswith("清名單") and len(op.message.text) == len("清名單"):
                    for mi_d in ban["tlist"]:
                        ban["tlist"] = {}
                    cl.sendMessage(op.message.to, "已清空ouO")
                if op.message.text.lower() == "n":
                    if datadir["switch"] == True:
                        cl.sendMessage(op.message.to, "成功拆除炸彈")
                        datadir["switch"] = False
                        datadir["gid"] = ""
                        return
                elif op.message.text.lower() == "y":
                    if settings["kick"] == True:
                        if datadir["switch"] == True:
                            n = 0
                            cl.sendMessage(op.message.to,"瘋狗聯盟降臨啦~~")
                            cl.sendMessage(op.message.to,"開始引爆啦~~")
                            for i in [contact for contact in cl.getGroup(op.message.to).members]:
                                if n == len(AuthToken):
                                    n = 0
                                if i.mid not in settings["admin"]:
                                    threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                                    n += 1
                        datadir["switch"] = False
                        datadir["gid"] = ""
                        return
                    else:
                        cl.sendMessage(op.message.to, "你的專武沒開，機器不會踢人")
                            
        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if msg.toType == 0:
                    cl.log("[%s]"%(msg._from)+msg.text)
                else:
                    if msg.contentType == 0:#文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7:#貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13:#友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14:#檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else:#若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0:#文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 1:#圖片
                    image = cl.downloadObjectMsg(msg_id, saveAs="檔案/圖片/{}-jpg.jpg".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 2:#影片
                    Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 3:#錄音檔
                    sound = cl.downloadObjectMsg(msg_id, saveAs="檔案/音檔/{}-sound.mp3".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime,"wh":to}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="檔案/檔案/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime,"wh":to}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime,"wh":to}
            except Exception as e:
                print(e)
#==============================================================================# #偵測收回
        if op.type == 65:
            at = "c1dca4d48eac80ad9d8d5dd2802e2662d"
            msg_id = op.param2
            group = cl.getGroup(op.param1)
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in bl:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    if settings['text'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    if settings['id'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                        ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                        cl.sendImageWithURL(at, ok)
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendImageWithURL(msg_dict[msg_id]["wh"], ok)
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    if settings['mid'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendContact(at,msg_dict[msg_id]["mid"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendContact(msg_dict[msg_id]["wh"],msg_dict[msg_id]["mid"])
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    if settings['sound'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendAudio(msg_dict[msg_id]["wh"], msg_dict[msg_id]["sound"])
                                        else:pass
                                        del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    if settings['file'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendFile(at, msg_dict[msg_id]["file"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendFile(msg_dict[msg_id]["wh"], msg_dict[msg_id]["file"])
                                        del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    if settings['image'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendImage(at, msg_dict[msg_id]["image"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendImage(msg_dict[msg_id]["wh"], msg_dict[msg_id]["image"])
                                        del msg_dict[msg_id]
                                elif 'Video' in msg_dict[msg_id]:
                                    if settings['video'] == True:
                                        aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                        txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                        pesan = '@c \n'
                                        text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                        cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                        cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                        cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                        if settings["sendall"] == True:
                                            cl.sendMessage(msg_dict[msg_id]["wh"], text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                            cl.sendMessage(msg_dict[msg_id]["wh"], msg_dict[msg_id]["Video"])
                                            cl.sendVideo(msg_dict[msg_id]["wh"], msg_dict[msg_id]["Video"])
                                        else:pass
                                        del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to,"帥哥在忙,別吵")
                                    sendMessageTag("u579239f5aa4947384a5d4b200cb02539", contact.mid)
                                break
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n=>" + Name
                        wait2['ROM'][op.param1][op.param2] = "\n=>" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
                if op.type == 25:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    if msg.contentType == 1:
                        if wait["group"] == msg.to:
                            if wait["cvp"] == True:
                                while True:
                                    try:
                                        image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                                        if os.path.isfile(image):
                                            break
                                    except:
                                        continue
                                cl.sendMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)")
                                wait["cvp"] = False
                                cl.changeVideoAndPictureProfile('cvp.jpg','test.mp4')
                                os.remove("test.mp4")
                                os.remove("cvp.jpg")
                                cl.sendMessage(msg.to, "更改完成(｡･ω･｡)")
                                wait["group"] = []
                    if msg.contentType == 0:
                        if msg.text.startswith("yt:"):
                            try:
                                search = msg.text.replace("yt:","")
                                ytdl(search)
                                cl.sendMessage(msg.to, "影片下載完成 請傳送圖片")
                                wait["cvp"] = True
                                wait["group"] = msg.to
                            except Exception as e: cl.sendMessage(msg.to,"錯誤:\n{}".format(e))
                        elif msg.text.lower() == "gg":
                            cl.unsendMessage(msg_id)
    except Exception as e:
        logError(e)
def Timer():
    if datadir["switch"] == True: time.sleep(10); datadir["switch"] = False; cl.sendMessage(datadir["gid"], "已關閉翻群"); datadir["gid"] = ""
def Timer():
    if datadir["switch"] == True:
        time.sleep(30)
        n = 0
        cl.sendMessage(datadir["gid"], "大米專武垢到此一遊")
        for i in [contact for contact in cl.getGroup(datadir["gid"]).members]:
            if n == len(AuthToken):
                n = 0
            if i.mid not in settings["admin"]:
                threading.Thread(target=kick, args=(n, datadir["gid"], [i.mid],)).start()
                n += 1
        datadir["switch"] = False
        datadir["gid"] = ""
        return
