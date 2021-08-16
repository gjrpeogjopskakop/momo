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
####################################################
botStart = time.time() 
####################################################
ts = time.time()
#################################################### 
cl = LINE("bruce930611@gmail.com","leofghj4458")
####################################################
cl.log(cl.authToken)
AuthToken = []
for i in range(1,81): AuthToken.append(LINE(cl.authToken))
AuthToken1 = []
for i in range(1,21): AuthToken1.append(LINE(cl.authToken))

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
admin=[clMID,'u2db707c088044deb4757c666d1eea1a0','u50cecb839be2e71b76c7fcdf97a0c87d']
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
            if i not in admin:
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
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@MiliSun "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mid")
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
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 
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
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd","通知好友更改名稱:\n" + contact.displayName)
                if op.param2 == "8":
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd","通知好友更改動態頭貼:\n" + contact.displayName)
                if op.param2 == "16":
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd","通知好友更改個簽:\n" + contact.displayName)
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
        if op.type == 5:#自動防封鎖
            print ("[ 5 ] INV PRO")
            if settings["invBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "•防邀機功能運行中•\n•[已啟動自動封鎖]•\nÇręätør:大米 我的作者網址:line.me/ti/p/~0970737883".format(str(cl.getContact(op.param1).displayName))) 
        if op.type == 5:#自動防封鎖
            print ("[ 5 ] kick PRO")
            if settings["Block"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1, "已啟動封鎖".format(str(cl.getContact(op.param1).displayName)))       
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
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if op.param3 in clMID:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('【自動入群】\n')
                        arr = []
                        mention = "@Mili "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "一言不合讓你全家爆炸🥰"
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendContact(op.param1, "u80ac59fd2b11d905b320de833417f98c")
                        cl.sendMessage('u77c34b6198166ffe142d671369fed4bd',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
                    except Exception as error:
                        print(error)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if op.param3 in clMID:
                if settings["asyncJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('【自動入群】\n')
                        arr = []
                        mention = "@Grk "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "異步功能運作中"
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendContact(op.param1, "u77c34b6198166ffe142d671369fed4bd")
                        cl.sendMessage('u77c34b6198166ffe142d671369fed4bd',"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
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
                if op.param2 not in admin:
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
            cl.sendMessage("u77c34b6198166ffe142d671369fed4bd","有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param3 in admin:
                try:
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                    pass
            if settings["protect"] == True:
                if op.param2 in admin:
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
            if sender in admin or sender not in admin:
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
                                cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "網址成功進入《%s》群組" % str(group.name))
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
            if sender in admin:
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
            if sender in admin:
				#指令表txt版本
                if text.lower() == 'help':
                        cl.relatedMessage(to, help(),op.message.id)
                elif text.lower() == 'help1':
                        cl.relatedMessage(to, help1(),op.message.id)
                elif text.lower() == 'help2':
                        cl.relatedMessage(to, help2(),op.message.id)
                elif text.lower() == 'help3':
                        cl.relatedMessage(to, help3(),op.message.id)
                elif text.lower() == 'help4':
                        cl.relatedMessage(to, help4(),op.message.id)
                elif text.lower() == 'help5':
                        cl.relatedMessage(to, help5(),op.message.id)
                elif text.lower() == 'help6':
                        cl.relatedMessage(to, help6(),op.message.id)
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
                    cl.relatedMessage(to, str(ret_),op.message.id)
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
                    cl.relatedMessage(to,slot,op.message.id)
                    if a == e == i == j == o:
                        cl.relatedMessage(to,"[自動回覆]\n恭喜拉霸機中獎~~",op.message.id)
                        return
                    cl.relatedMessage(to,"[自動回覆]\n可惜啦ww再試一次吧w",op.message.id)	
                elif msg.text in ["本日運勢","rls"]:
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.relatedMessage(to,slot,op.message.id)
                    cl.relatedMessage(to,"[自動回覆]\n在測試一次吧！ヽ(✿ﾟ▽ﾟ)ノ",op.message.id)
                elif msg.text.lower().startswith('id'):
                    try:
                        list_ = msg.text.split(":")
                        msgs = list_[1]		
                        conn = cl.findContactsByUserid(msgs)
                        cl.sendMessage(to, "http://line.me/ti/p/~" + msgs)
                        cl.sendMessage(to, None, contentMetadata={'mid': conn.mid}, contentType=13)	
                    except:
                        cl.sendMessage(to, '執行命令錯誤')
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
                elif msg.text.lower().startswith("name "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendMessage(msg.to,"[Name]\n" + cl.getContact(inkey).displayName)
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
                elif msg.text.lower().startswith("addop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendMessage(op.message.to, "已獲得權限！")
                elif msg.text.lower().startswith("delop "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendMessage(op.message.to, "已取消權限！")
                elif msg.text.lower().startswith("主人"):
                    cl.sendMessage(op.message.to, "👇👇我的主人!!👇👇")
                    cl.sendContact(op.message.to, "u4f749287486340aff896823734edbea2")
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(op.message.to,"無擁有權限者!")
                    else:
                        mc = "[ 權限者  ]"
                        for mi_d in admin:
                            mc += "\n➽➤"+cl.getContact(mi_d).displayName
                        cl.sendMessage(op.message.to,mc + "\n[ 結束  ]")
                elif msg.text.lower().startswith("system "):
                    BanText = ["cd ..", "root", "passwd"]
                    txt = text[7:]
                    if sender != King:
                        for i in BanText:
                            if i in cmd:
                                return cl.sendMessage(to, "You are not a privilege")
                    cl.relatedMessage(to, str(subprocess.Popen([txt], shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]),op.message.id  )
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
                    cl.relatedMessage(to,"成功加入好友",op.message.id)
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
                #少數重要功能
                elif text.lower() == 'reb':
                    cl.relatedMessage(to, "重新啟動中....",op.message.id)	
                    cl.relatedMessage(to, "重啟完成",op.message.id)
                    restartBot()
                elif text.lower() == '.setk':
                    cl.relatedMessage(to, " ☵☲核彈設定☱☴\n核彈已開啟✔\n進群踢已關閉\n線呈數{}\n取消線呈{}\n版本:半垢核彈".format(len(AuthToken),len(AuthToken1)),op.message.id)	
                elif text.lower() == '增線':
                    AuthToken.append(LINE(cl.authToken))
                    cl.relatedMessage(to, "已增加線呈數",op.message.id)	
                elif text.lower() == '增加線呈':
                    for i in range(1,51):
                        try:
                            AuthToken.append(LINE(cl.authToken))
                        except:
                            pass
                    cl.relatedMessage(to, "已增加線呈數50",op.message.id)
                elif text.lower() == '增加線呈數':
                    for i in range(1,11):
                        try:
                            AuthToken1.append(LINE(cl.authToken))
                        except:
                            pass
                    cl.relatedMessage(to, "已增加線呈數21",op.message.id)	
                elif text.lower() == 'ren':
                    eltime = time.time() - mulai
                    bot = "運行時間長達\n" +Runtime(eltime)
                    cl.relatedMessage(msg.to,bot,op.message.id)	
                elif text.lower() == 'res':
                    backupData()
                    cl.relatedMessage(to,"儲存設定成功!",op.message.id)
                elif text.lower() == 'rbye':
                    if msg.toType == 2:
                        cl.sendMessage(op.message.to,"各位再見,有心邀回")
                        ginfo = cl.getGroup(to)
                        try:
                            cl.leaveGroup(to)
                        except:
                            cl.leaveRoom(to) 
				#進群退群退副本
                elif text.lower() == 'raj on':
                    settings["autoJoin"] = True
                    cl.relatedMessage(to, "自動加入群組已開啟 ✔",op.message.id)	
                elif text.lower() == 'raj off':
                    settings["autoJoin"] = False
                    cl.relatedMessage(to, "自動加入群組已關閉 ✘",op.message.id)	
                elif text.lower() == 'ra on':
                    settings["asyncJoin"] = True
                    cl.relatedMessage(to, "自動加入群組已開啟 ✔",op.message.id)	
                elif text.lower() == 'ra off':
                    settings["asyncJoin"] = False
                    cl.relatedMessage(to, "自動加入群組已關閉 ✘",op.message.id)	
                elif text.lower() == 'ral on':
                    settings["autoLeave"] = True
                    cl.relatedMessage(to, "自動離開副本已開啟 ✔",op.message.id)	
                elif text.lower() == 'ral off':
                    settings["autoLeave"] = False
                    cl.relatedMessage(to, "自動離開副本已關閉 ✘",op.message.id)	
                elif text.lower() == 'rqj on':
                    settings["autoJoinTicket"] = True
                    cl.relatedMessage(to, "網址自動入群已開啟 ✔",op.message.id)	
                elif text.lower() == 'rqj off':
                    settings["autoJoinTicket"] = False
                    cl.relatedMessage(to, "網址自動入群已關閉 ✘",op.message.id)	
                elif text.lower() == 'ct on':
                    settings["checkSticker"] = True
                    cl.relatedMessage(to, "貼圖查詢已開啟 ✔",op.message.id)	
                elif text.lower() == 'ct off':
                    settings["checkSticker"] = False
                    cl.relatedMessage(to, "貼圖查詢已關閉 ✘",op.message.id)	
				#其餘加好友收回自動已讀
                elif text.lower() == 'rdd on':
                    settings["autoAdd"] = True
                    cl.relatedMessage(to, "自動加入好友已開啟 ✔",op.message.id)	
                elif text.lower() == 'rdd off':
                    settings["autoAdd"] = False
                    cl.relatedMessage(to, "自動加入好友已關閉 ✘",op.message.id)	
                elif text.lower() == 'red on':
                    settings["reread"] = True
                    cl.relatedMessage(to, "查詢收回開啟 ✔",op.message.id)	
                elif text.lower() == 'red off':
                    settings["reread"] = False
                    cl.relatedMessage(to, "查詢收回關閉 ✘",op.message.id)	
                elif text.lower() == 'rd on':
                    settings["autoRead"] = True
                    cl.relatedMessage(to, "自動已讀已開啟 ✔",op.message.id)	
                elif text.lower() == 'rd off':
                    settings["autoRead"] = False
                    cl.relatedMessage(to, "自動已讀已關閉 ✘",op.message.id)	
				#更改顯示
                elif text.lower() == 'rt on':
                    wait["resset"] = True
                    cl.relatedMessage(to, "偵測更新帳號\n名子✘/圖片✘/個簽✘\n更新為開啟偵測狀態✔\n名子✔/圖片✔/個簽✔",op.message.id)	
                elif text.lower() == 'rt off':
                    wait["resset"] = False
                    cl.relatedMessage(to, "偵測更新帳號\n名子✔/圖片✔/個簽✔\n更新為關閉偵測狀態✘\n名子✘/圖片✘/個簽✘",op.message.id)	
				#踢人顯示
                elif text.lower() == 'rc on':
                    settings["kickContact"] = True
                    cl.relatedMessage(to, "踢人標註已開啟 ✔═",op.message.id)	
                elif text.lower() == 'rc off':
                    settings["kickContact"] = False
                    cl.relatedMessage(to, "踢人標註已關閉 ✘═",op.message.id)	
				#進群退群
                elif text.lower() == 'rj on':
                    settings["seeJoin"] = True
                    cl.relatedMessage(to, "入群通知已開啟 ✔═",op.message.id)	
                elif text.lower() == 'rj off':
                    settings["seeJoin"] = False
                    cl.relatedMessage(to, "入群通知已關閉 ✘═",op.message.id)	
                elif text.lower() == 'rl on':
                    settings["seeLeave"] = True
                    cl.relatedMessage(to, "退群通知已開啟 ✔═",op.message.id)	
                elif text.lower() == 'rl off':
                    settings["seeLeave"] = False
                    cl.relatedMessage(to, "退群通知已關閉 ✘═",op.message.id)	
                elif text.lower() == 'rm on':
                    settings["detectMention"] = False
                    cl.relatedMessage(to, "標註回覆已開啟 ✔",op.message.id)	
                elif text.lower() == 'rm off':
                    settings["detectMention"] = True
                    cl.relatedMessage(to, "標註回覆已關閉 ✘",op.message.id)	
                elif text.lower() == 'ru on':
                    wait["um"] = True
                    cl.relatedMessage(to, "收回已開啟 ✔",op.message.id)	
                elif text.lower() == 'ru off':
                    wait["um"] = False
                    cl.relatedMessage(to, "收回已關閉 ✘",op.message.id)	
                elif text.lower() == 'cn on':
                    wait["contact"] = True
                    cl.relatedMessage(to, "已開啟 ✔",op.message.id)	
                elif text.lower() == 'cn off':
                    wait["contact"] = False
                    cl.relatedMessage(to, "已關閉 ✘",op.message.id)	
				#保護項目
                elif text.lower() == 'rop on':
                    settings["protect"] = True
                    cl.relatedMessage(to, "群組保護已開啟 ✔",op.message.id)
                elif text.lower() == 'rop off':
                    settings["protect"] = False
                    cl.relatedMessage(to, "群組保護已關閉 ✘",op.message.id)
                elif text.lower() == 'rip on':
                    settings["inviteprotect"] = True
                    cl.relatedMessage(to, "群組邀請保護已開啟 ✔",op.message.id)
                elif text.lower() == 'rip off':
                    settings["inviteprotect"] = False
                    cl.relatedMessage(to, "群組邀請保護已關閉 ✘",op.message.id)
                elif text.lower() == 'rqp on':
                    settings["qrprotect"] = True
                    cl.relatedMessage(to, "群組網址保護已開啟 ✔",op.message.id)
                elif text.lower() == 'rqp off':
                    settings["qrprotect"] = False
                    cl.relatedMessage(to, "群組網址保護已關閉 ✘",op.message.id)
                elif text.lower() in ['開啟']:
                    if msg.toType ==2:
                        jg["JoinGroup"][to] = True
                        cl.relatedMessage(to, "開啟 ✔",op.message.id)
                elif text.lower() in ['關閉']:
                    if msg.toType ==2 :
                        try:
                            del jg["JoinGroup"][to]
                            cl.relatedMessage(to, "關閉 ✘",op.message.id)
                        except:
                            cl.relatedMessage(to, "關閉狀態中 ✘",op.message.id)
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
                    cl.relatedMessage(to,"已開啟戰爭模式",op.message.id)
                    settings["warmode"][to] = True
                elif text.lower() == 'war:off':
                    cl.relatedMessage(to,"已關閉戰爭模式",op.message.id)
                    del settings["warmode"][to]
                elif text.lower() == 'war':
                    if to in settings["warmode"]:
                        cl.relatedMessage(to,"戰爭狀態:開啟",op.message.id)
                    else:
                        cl.relatedMessage(to,"戰爭狀態:關閉",op.message.id)
                elif text.lower() == '模式 邀請':
                    settings["bgi"] = False
                    cl.relatedMessage(to, "模式:1(邀請)✘維修中",op.message.id)
                    cl.relatedMessage(to, "已幫您轉為網址入群",op.message.id)
                elif text.lower() == '模式 網址':
                    settings["bgi"] = False
                    cl.relatedMessage(to, "模式:2(網址)",op.message.id)
                elif text.lower() == '模式':
                    bgin = None
                    if settings["bgi"] == False:
                        bgin = "網址"
                    elif settings["bgi"] == True:
                        bgin = "邀請"
                    cl.relatedMessage(to,"模式:{}".format(len(bgin)),op.message.id)
                elif text.lower() == 'joing on':
                    settings["bodyguard"] = True
                    cl.relatedMessage(to, "進群已開啟 ✔",op.message.id)	
                elif text.lower() == 'joing off':
                    settings["bodyguard"] = False
                    cl.relatedMessage(to, "進群保鑣已關閉 ✘",op.message.id)	
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
                        cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "About檢查中......")
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
                        cl.relatedMessage(to, str(ret_),op.message.id)
                    except Exception as e:
                        cl.relatedMessage(msg.to, str(e),op.message.id)
                #網址開關
                elif text.lower() == 'ru':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.relatedMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                        else:
                            cl.relatedMessage(to, "群組沒有開啟網址",op.message.id)
                elif text.lower() == 'ro':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.relatedMessage(to, "群組網址已開",op.message.id)
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "開啟成功",op.message.id)
                elif text.lower() == 'rc':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.relatedMessage(to, "群組網址已關",op.message.id)
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "關閉成功",op.message.id)
                #廣播
                elif text.lower().startswith("rt:"):
                    id = text[3:].split(':')
                    for x in range(int(id[1])):
                        cl.sendPostToTalk(to,id[0])
                    cl.relatedMessage(to, "文章分享完畢",op.message.id)
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
                        cl.relatedMessage(to,'請發送你要廣播的東西~',op.message.id)
				#測速功能
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "檢查中......")
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,format(str(elapsed_time)) + "秒",op.message.id)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.relatedMessage(to, "[群組mid : ]\n" + gid.id,op.message.id)
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.relatedMessage(to,'處理速度\n' + str1 + '秒',op.message.id)
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒',op.message.id)
                elif msg.text in ["/sp","/speed"]:
                    t1 = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "第1次速度")
                    t2 = time.time() - t1
                    time.sleep(0.01)
                    t3 = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "第2次速度")
                    t4 = time.time() - t3
                    time.sleep(0.01)
                    t5 = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "第3次速度")
                    t6 = time.time() - t5
                    time.sleep(0.01)
                    t7 = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "第4次速度")
                    t8 = time.time() - t7
                    time.sleep(0.01)
                    t9 = time.time()
                    cl.sendMessage("u77c34b6198166ffe142d671369fed4bd", "第5次速度")
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
                    cl.relatedMessage(to, str(ret_),op.message.id)
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
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif msg.text.lower().startswith("fk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromRoom(msg.to,[target])
                        except:
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
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
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif text.lower() == 'join':
                    if to in settings['jm']:
                        cl.sendMessage(to, settings['jm'][to])
                    else:
                        cl.sendMessage(to, "未設置")
                elif msg.text.startswith("join:"):
                    _name = msg.text.replace("join:","")
                    if _name == '':
                        cl.relatedMessage(to,"已關閉",op.message.id)
                        settings["jm"][to] = ""
                    else:
                        settings["jm"][to] = _name
                        cl.relatedMessage(to,"已更改至{}".format(str(_name)),op.message.id)
                elif msg.text.startswith("joinleave:"):
                    _name = msg.text.replace("joinleave:","")
                    if _name == '':
                        cl.relatedMessage(to,"已關閉",op.message.id)
                        settings["seeLeave"][to] = ""
                    else:
                        settings["seeLeave"][to] = _name
                        cl.relatedMessage(to,"已更改至{}".format(str(_name)),op.message.id)
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
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
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
                            cl.relatedMessage(to,"目前處於 帳號規制狀態中",op.message.id)
                elif text.lower() == 'mine':
                     try:
                         cl.kickoutFromGroup(msg.to, ["fuck you"])
                         cl.sendMessage(msg.to, "正常")
                     except Exception as e:
                         if e.reason == "request blocked":
                            me = cl.getContact(sender)
                            cl.relatedMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: request blocked\n邀請狀態: request blocked\n取消狀態: 可以執行\n[完]",op.message.id)
                         else:
                            me = cl.getContact(sender)
                            cl.relatedMessage(msg.to,"[查詢資料]\n"+"使用者名稱: "+me.displayName+"\n使用者Mid: "+sender+"\n踢人狀態: 可以執行\n邀請狀態: 可以執行\n取消狀態: 可以執行\n[完]",op.message.id)
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
                elif "開網址 " in msg.text: 
                    gid = msg.text.replace("開網址 ","")
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
                        cl.relatedMessage(msg.to, str(ret_),op.message.id)
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
                    cl.relatedMessage(msg.to, A,op.message.id)
                elif msg.text.lower().startswith("jp:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.relatedMessage(msg.to, A,op.message.id)
                elif msg.text.lower().startswith("en:"):
                    separate = text.split(":")
                    isi = text.replace(separate[0] + ":","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.relatedMessage(msg.to, A,op.message.id)
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
                        cl.relatedMessage(msg.to, "更改定名:"+cl.getContact(to).displayNameOverridden,op.message.id)
                    except Exception as error:
                        if error.reason == "Invalid mid":
                            cl.relatedMessage(to,"不可用於群組",op.message.id)
				#mid或其餘方式功能
                elif text.lower().startswith("mc:"):
                        separate = text.split(":")
                        mmid = text.replace(separate[0] + ":","")
                        cl.sendContact(to, mmid)
                        cl.relatedMessage(to,"幫您丟出友資\n友資MID\n"+mmid+"\n幫您生成完畢",op.message.id)
                elif text.lower().startswith("inv:"):
                        separate = text.split(":")
                        midd = text.replace(separate[0] + ":","")
                        cl.findAndAddContactsByMid(midd)
                        cl.inviteIntoGroup(msg.to,[midd])
                        cl.relatedMessage(to,"已經幫您邀請\n"+midd+"\n邀請完畢\n或可能此人已經在群組",op.message.id)
                elif text.lower().startswith("ce:"):
                        separate = text.split(":")
                        txt = text.replace(separate[0] + ":","")
                        cl.createPost(txt)
                        cl.relatedMessage(to,"正在幫您生成貼文\n貼文創建內容:\n" + txt + "\n貼文創建完畢",op.message.id)
                elif text.lower().startswith("pn:"):
                        separate = text.split(":")
                        string = text.replace(separate[0] + ":","")
                        if len(string) <= 1000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.relatedMessage(to,"名稱已更改為\n=>" + string + "",op.message.id)
                        if len(string) >= 1001:
                            cl.relatedMessage(to,"[警告]\n名稱不能突破1000字喔!!\n超過1000字強制更改\n將會凍帳一小時\n以下是您想突破的文字名稱\n" + string + "",op.message.id)
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
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "秒" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✘" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                elif "✔" in msg.text.lower():
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
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
                    cl.relatedMessage(to,d,op.message.id)
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
                    cl.relatedMessage(to,d,op.message.id)
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
                    cl.relatedMessage(to,d,op.message.id)
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
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif msg.text.lower().startswith('un'): #收回指定數量訊息
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
                elif text.lower() == '特殊名單':
                    mc = "[ 專武特殊名單 ]\n待踢名單:"
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
                            if target in admin:
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
                        cl.relatedMessage(to,x[1],op.message.id)
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.relatedMessage(to,x[1],op.message.id)
                        except:
                            cl.relatedMessage(to,"無法正確執行此指令",op.message.id)
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
                    cl.relatedMessage(to, "標註完畢 共標註了{}次".format(number),op.message.id)
                    cl.relatedMessage(to, "標註完畢\n標註共計: %s秒" % (elapsed_time),op.message.id)
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
                    cl.relatedMessage(to, "標註完畢 共標註了{}次".format(number),op.message.id)
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
                elif "inv " in msg.text:
                    lg = msg.text.replace("inv ","")
                    cl.sendMessage(to,"處理中...")
                    aa = cl.getGroupIdsByName(lg)
                    mes = "\n邀請的群組名稱\n"
                    for x in aa:
                        mes += cl.getGroup(x).name+"\n"
                    cl.sendMessage(to,"總共有" + str(len(aa)) + "個群符合要求")
                    cl.sendMessage(to,"邀請至群組中...")
                    for x in aa:
                        cl.findAndAddContactsByMid(x)
                        time.sleep(1)
                    cl.sendMessage(to,"成功邀請了喔\n"+ mes)
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
                    cl.relatedMessage(to,d,op.message.id)
				#更改個簽指令
                elif text.lower().startswith("cb:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.relatedMessage(to,"個簽狀態已更改為 :  \n" + string,op.message.id)
				#登出指令
                elif text.lower() in ["logout"]:
                    cl.relatedMessage(msg.to, "直接登出請輸入[登出][Y]\n手動登出請輸入[手動][N]",op.message.id)	
                    wait['logout'][msg.to] = sender
                elif text.lower() in ["y","Y","N","n",]:
                    if msg.to in wait['logout'] and msg._from== wait['logout'][msg.to]:
                        if text.lower() in ["登出","y","Y"]:
                            cl.relatedMessage(msg.to, "將自動幫您登出機器",op.message.id)	
                            cl.relatedMessage(to,"[提示]\n已經自動登出後台伺服器",op.message.id)	
                            os._exit(0)	
                            del wait['logout'][msg.to]
                        elif text.lower() in ["N","n","手動"]:
                            cl.relatedMessage(msg.to, "請點擊以下網址\nline://nv/connectedDevices/\n進行手動登出",op.message.id)	
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
                        cl.relatedMessage(to, "MID搜尋中…\n搜尋完成\n被掃人員：" + cl.getContact(mid).displayName + "\n開始執行ฅ^•ﻌ•^ฅ",op.message.id)
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
                        cl.relatedMessage(to, str(ret_),op.message.id)
                #共同群組
                elif text.lower().startswith("sg:"):
                    txt = text[3:].split(' ')
                    ret_ = "[共同群組]"
                    a = 0
                    for mid in txt:
                        gid = cl.getGroupIdsJoined() 
                        cl.relatedMessage(to, "MID搜尋中…\n搜尋完成\n被查人員：" + cl.getContact(mid).displayName + "\n開始執行ฅ^•ﻌ•^ฅ",op.message.id)
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
                        cl.relatedMessage(to, str(ret_),op.message.id)
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
                                cl.relatedMessage(to,"此人為黑單",op.message.id)
                        else:
                            cl.relatedMessage(to,"早就是了",op.message.id)
                    cl.relatedMessage(msg.to,"已加入共" + str(a) + "人",op.message.id)
                    backupData()
                elif text.lower().startswith("rbg "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    a = 0
                    for target in targets:
                        if target not in cbg:
                            cl.relatedMessage(to,"他不是保鑣阿==",op.message.id)
                        else:
                            try:
                                del cbg[target]
                                a += 1
                            except:
                                cl.relatedMessage(msg.to,"刪除" + str(target) + "失敗 !",op.message.id)
                    cl.relatedMessage(msg.to,"已刪除保鑣共" + str(a) + "人",op.message.id)
                    backupData()
                elif text.lower() in ['bgs']:
                    if cbg == {}:
                        cl.relatedMessage(msg.to,"無保鑣!")
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
                            cl.relatedMessage(msg.to,mc +"\n≡≡總共"+str(len(cbg))+ "個人為保鑣≡≡",op.message.id)
                        except:
                            cl.relatedMessage(to,"保鑣【"+(str(len(cbg)))+"】",op.message.id)
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
                        if i.mid not in admin:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith("..2") and len(op.message.text) == len("..2"):
                    cl.sendMessage(op.message.to, "卍陌•生の1番目のリングは再び栄光です\n卍の陌•生\n陌生の滅殺す")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in admin:
                            threading.Thread(target=kick, args=(n, op.message.to, [i.mid],)).start()
                            n += 1
                elif op.message.text.lower().startswith("..3") and len(op.message.text) == len("..3"):
                    cl.sendMessage(op.message.to, "消滅の仏光山協会が来ます")
                    n = 0
                    for i in [contact for contact in cl.getGroup(op.message.to).members]:
                        if n == len(AuthToken):
                            n = 0
                        if i.mid not in admin:
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
                            if i.mid not in admin:
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
                            if i not in admin:
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
                                    if i not in admin:
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
                                if i not in admin:
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
                            if target in admin:
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
                            if target in admin:
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
                                if i.mid not in admin:
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
                msg_id = msg.id
                sender = msg._from
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
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                elif msg.contentType == 1:#圖片
                    image = cl.downloadObjectMsg(msg_id, saveAs="file/image/{}-jpg.jpg".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime}
                #elif msg.contentType == 2:#影片
                    #Video = cl.downloadObjectMsg(msg_id, saveAs="檔案/影片/{}-Video.mp4".format(msg.createdTime))
                    #msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":msg.createdTime}
                elif msg.contentType == 3:#錄音檔
                    sound = cl.downloadObjectMsg(msg_id, saveAs="file/sound/{}-sound.mp3".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime}
                elif msg.contentType == 7:#貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime}
                elif msg.contentType == 13:#友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime}
                elif msg.contentType == 14:#檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="file/file/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime}
                else:#若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime}
            except Exception as e:
                print(e)
#==============================================================================# #偵測收回
        if op.type == 65:
            at = "u77c34b6198166ffe142d671369fed4bd"
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
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    pesan = '@c \n'
                                    text_ =  pesan + "群組名稱："+ str(group.name) + "\n" + txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                #elif 'Video' in msg_dict[msg_id]:
                                    #aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    #txr = '[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    #pesan = '@c \n'
                                    #text_ =  pesan + txr
                                    #cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    #cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    #cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    #del msg_dict[msg_id]
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
                                cl.relatedMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)",op.message.id)
                                wait["cvp"] = False
                                cl.changeVideoAndPictureProfile('cvp.jpg','test.mp4')
                                os.remove("test.mp4")
                                os.remove("cvp.jpg")
                                cl.relatedMessage(msg.to, "更改完成(｡･ω･｡)",op.message.id)
                                wait["group"] = []
                    if msg.contentType == 0:
                        if msg.text.startswith("yt:"):
                            try:
                                search = msg.text.replace("yt:","")
                                ytdl(search)
                                cl.relatedMessage(msg.to, "影片下載完成 請傳送圖片",op.message.id)
                                wait["cvp"] = True
                                wait["group"] = msg.to
                            except Exception as e: cl.relatedMessage(msg.to,"錯誤:\n{}".format(e),op.message.id)
                        elif msg.text.lower() == "gg":
                            cl.unsendMessage(msg_id)
    except Exception as e:
        logError(e)
def Timer():
    if datadir["switch"] == True: time.sleep(10); datadir["switch"] = False; client.sendMessage(datadir["gid"], "已關閉翻群"); datadir["gid"] = ""
def Timer():
    if datadir["switch"] == True:
        time.sleep(30)
        n = 0
        cl.sendMessage(datadir["gid"], "大米專武垢到此一遊")
        for i in [contact for contact in cl.getGroup(datadir["gid"]).members]:
            if n == len(AuthToken):
                n = 0
            if i.mid not in admin:
                threading.Thread(target=kick, args=(n, datadir["gid"], [i.mid],)).start()
                n += 1
        datadir["switch"] = False
        datadir["gid"] = ""
        return
