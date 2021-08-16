from linepy import *
from akad.ttypes import *
from time import sleep
from datetime import datetime
import time, os



cl = LINE("yuqnefrp@yomail.info","a0970737883") 
cl.sendMessage("u2db707c088044deb4757c666d1eea1a0","取消機登入成功")
oepoll = OEPoll(cl)

lineSettings = cl.getSettings()
clMID = cl.profile.mid
clProfile = cl.getProfile()
clSetting = cl.getSettings()

X =['u2db707c088044deb4757c666d1eea1a0']
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        cl.acceptGroupInvitation(op.param1)
        cl.sendMessage(op.param1, cl.getContact(op.param2).displayName + "我的作者網址:http://line.me/ti/p/~0970737883")
        group = cl.getGroup(op.param1)
        if group.invitee is None:
            cl.sendMessage(op.param1, cl.getContact(op.param2).displayName + "\n系統偵測邀請區中....")
            time.sleep(0.5)
            cl.sendMessage(op.param1, "【偵測完畢】\n【偵測結果】\n【邀請區沒人】")
            cl.leaveGroup(op.param1)
        else:
            gInviMids = (contact.mid for contact in group.invitee)
            ginfo = cl.getGroup(op.param1)
            sinvitee = str(len(ginfo.invitee))
            cl.sendMessage(op.param1, "【偵測完畢】\n【偵測結果】\n【邀請區有 " + sinvitee + " 人】")
            time.sleep(0.5)
            cl.sendMessage(op.param1, "開始取消邀請")
            start = time.time()
            for cancelmod in gInviMids:
                cl.cancelGroupInvitation(op.param1, [cancelmod])
                time.sleep(1)
                elapsed_time = time.time() - start
            cl.sendMessage(op.param1, "已取消完成\n取消時間: %s秒" % (elapsed_time))
            cl.sendMessage(op.param1, "取消人數:" + sinvitee)
            cl.sendMessage("u2db707c088044deb4757c666d1eea1a0","群組名稱:" + str(ginfo.name)+"\n取消人數:" + sinvitee + "\n取消時間: %s秒" % (elapsed_time))
            cl.leaveGroup(op.param1)
    except Exception as e:
        print (e)
        print ("發生錯誤 正在自動重新登入")
        return 
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
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
    except Exception as error:
        logError(error)


oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})

while True:
    oepoll.trace()
