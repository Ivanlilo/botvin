# -*- coding: utf-8 -*-
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json, requests, urllib

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient() 
client._tokenLogin("EmDpgTBgfvbift5NBTK5.7Ypk1xpgjyOCa5VaoNwI1q.V8BTEl2LFqgCWYabha4xuiEOIq2G/9xQVE+ft+4deEg=")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait2 = {    
    'copy':False,
    'target':{},
    'midsTarget':{},
    }

setTime = {}
setTime = wait["setTime"]

contact = client.getProfile() 
backup = client.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

wait2 = {    
    'message':"Thanks for add me,My Creator Http://line.me/ti/p/~muhmursalind" 
    }

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for mm in nama:
      akh = akh + 3
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 4
      akh = akh + 1
      bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       client.sendMessage(msg)
    except Exception as error:
        print error
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)
    
def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + "My Creator : \n\nHttp://line.me/ti/p/~muhmursalind\nID LINE : muhmursalind")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + ", Selamat Datang")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
				client.kickoutFromGroup(op.param1,[op.param2])
				client.inviteIntoGroup(op.param1,[op.param3])
				sendMessage(op.param1, client.getContact(op.param2).displayName + ", Kicker kampret")				
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_UPDATE_GROUP(op):
    try:
                sendMessage(op.param1, client.getContact(op.param2).displayName + ", Jangan Dimainin QR-nya :3\nSaya Kick ya")
                client.kickoutFromGroup(op.param1,[op.param2])
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_UPDATE_GROUP\n\n")
        return

tracer.addOpInterrupt(11,NOTIFIED_UPDATE_GROUP)

def NOTIFIED_CANCEL_INVITATION_GROUP(op):
    try:
                sendMessage(op.param1, client.getContact(op.param2).displayName + ", Kenapa dibatalin?\nitu temen saya")
                client.kickoutFromGroup(op.param1,[op.param2])
                client.inviteIntoGroup(op.param1,[op.param3])
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_CANCEL_INVITATION_GROUP\n\n")
        return

tracer.addOpInterrupt(32,NOTIFIED_CANCEL_INVITATION_GROUP)

def CANCEL_INVITATION_GROUP(op):
    try:
        client.cancelGroupInvitation(op.param1,[op.param3])
    except Exception as e:
        print e
        print ("\n\nCANCEL_INVITATION_GROUP\n\n")
        return

tracer.addOpInterrupt(31,CANCEL_INVITATION_GROUP)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 0:
            if msg.contentType == 0:
                if msg.text == "Mid":
                    sendMessage(msg.to, msg.to)
                if msg.text == "Me":
                    sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
                elif wait["contact"] == True:
                    msg.contentType = 0
                    sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = client.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        sendMessage(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = client.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        sendMessage(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                if msg.text == "Gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                else:
                    pass
            else:
                pass
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text in ["Key","Help","help"]:
                    sendMessage(msg.to,"✞ COMMAND GRUP✞\n\n✞ Me\n✞ Mid @\n✞ Mysp\n✞ Mygrup\n✞ Mygid\n✞ Myginfo\n✞ My gurl\n✞ My url\n✞ Link on\n✞ Link off\n✞ Summon\n✞ Cctv 「Set Point Read」\n✞ Ciduk 「Melihat Sider」")
                    sendMessage(msg.to,"✞ COMMAND SPAM/Broadcast ✞\n\n✞ 「Bc:ct/grup Teks」\n✞ 「Spam on/off Jumlah Teks」\n✞ 「Spam @」")
                    sendMessage(msg.to,"✞ COMMAND Profile ✞\n\n✞ 「Mybio/name 「Teks」\n✞ 「Mysteal @」\n✞ 「Mycopy @」\n✞ Mybackup\n✞ Block @\n✞ Blocklist")
                    sendMessage(msg.to,"✞ COMMAND Kicker ✞\n\n✞ 「Ratakan」\n✞ 「Kick @」\n✞ 「Uni」")
                if msg.text in ["Mysp","Speed","speed"]:
                    start = time.time()
                    sendMessage(msg.to, text="Mohon Bersabar Ini Gratisan...", contentMetadata=None, contentType=None)
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
                elif msg.text in ["Mygrup"]:
                    gid = client.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[★] %s\n" % (client.getGroup(i).name +"→["+str(len(client.getGroup(i).members))+"]")
                    sendMessage(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")
                if msg.text in["Summon"]:
                     group = client.getGroup(msg.to)
                     nama = [contact.mid for contact in group.members]
                     nm1, nm2, nm3, nm4, nm5, nm6, jml = [], [], [], [], [], [], len(nama)
                     if jml <= 100:
                        mention(msg.to, nama)
                     if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        mention(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        mention(msg.to, nm2)
                     if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        mention(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        mention(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        mention(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        mention(msg.to, nm4)
                        for m in range(400, 499):
                            nm5 += [nama[m]]
                        mention(msg.to, nm5)
                        for n in range(500, len(nama)-1):
                            nm6 += [nama[n]]
                        mention(msg.to, nm6)
                     if jml > 500:
                         print "Terlalu Banyak Men 500+"
                     cnt = Message()
                     cnt.text = "Done:"+str(jml)
                     cont.to = msg.to
                     client.sendMessage(cnt)
                     
                elif "Mycopy @" in msg.text:
                    print "[Copy] OK"
                    _name = msg.text.replace("Mycopy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = client.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMassage(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                                client.CloneContactProfile(target)
                                sendMessage(msg.to, "Success Copy profile ~")
                            except Exception as e:
                                print e
    
                elif msg.text in ["Mybackup","backup"]:
                    try:
                        client.updateDisplayPicture(backup.pictureStatus)
                        client.updateProfile(backup)
                        sendMessage(msg.to, "Backup done")
                    except Exception as e:
                        sendMessage(msg.to, str(e))
                elif msg.text.lower() == 'blocklist':
                    blockedlist = client.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = client.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                elif "Spam @" in msg.text:
                    _name = msg.text.replace("Spam @","")
                    _nametarget = _name.rstrip(' ')
                    gs = client.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Spam Goblog !")
                           sendMessage(g.mid,"Hai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
                           sendMessage(g.mid,"Maaf kan Saya ^_^ Aku Khilaf Sayang :v")
                           print " Spammed !"
                elif msg.text == "Link bokep":
                    sendMessage(msg.to,"nekopoi.host")
                    sendMessage(msg.to,"sexvideobokep.com")
                    sendMessage(msg.to,"memek.com")
                    sendMessage(msg.to,"pornktube.com")
                    sendMessage(msg.to,"faketaxi.com")
                    sendMessage(msg.to,"videojorok.com")
                    sendMessage(msg.to,"watchmygf.mobi")
                    sendMessage(msg.to,"xnxx.com")
                    sendMessage(msg.to,"pornhd.com")
                    sendMessage(msg.to,"xvideos.com")
                    sendMessage(msg.to,"vidz7.com")
                    sendMessage(msg.to,"m.xhamster.com")
                    sendMessage(msg.to,"xxmovies.pro")
                    sendMessage(msg.to,"youporn.com")
                    sendMessage(msg.to,"pornhub.com")
                    sendMessage(msg.to,"anyporn.com")
                    sendMessage(msg.to,"hdsexdino.com")
                    sendMessage(msg.to,"rubyourdick.com")
                    sendMessage(msg.to,"anybunny.mobi")
                    sendMessage(msg.to,"cliphunter.com")
                    sendMessage(msg.to,"sexloving.net")
                    sendMessage(msg.to,"free.goshow.tv")
                    sendMessage(msg.to,"eporner.com")
                    sendMessage(msg.to,"Pornhd.josex.net")
                    sendMessage(msg.to,"m.hqporner.com")
                    sendMessage(msg.to,"m.spankbang.com")
                    sendMessage(msg.to,"m.4tube.com")
                    sendMessage(msg.to,"brazzers.com")
                
                elif msg.text == "Myspam":
                    sendMessage(msg.to,"3")
                    sendMessage(msg.to,"2")
                    sendMessage(msg.to,"1")
                    sendMessage(msg.to,"Fuck Off")
                    sendMessage(msg.to,"Ku mengejar bus yang mulai berjalan")
                    sendMessage(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    sendMessage(msg.to,"Kabut dalam hatiku telah menghilang")
                    sendMessage(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    sendMessage(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    sendMessage(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    sendMessage(msg.to,"Untukku menjadi diri sendiri")
                    sendMessage(msg.to,"Ku harus jujur, pada perasaanku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untukku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Saat ku sadari sesuatu menghilang")
                    sendMessage(msg.to,"Hati ini pun resah tidak tertahankan")
                    sendMessage(msg.to,"Sekarang juga yang bisa ku lakukan")
                    sendMessage(msg.to,"Merubah perasaan ke dalam kata kata")
                    sendMessage(msg.to,"Mengapa sedari tadi")
                    sendMessage(msg.to,"Aku hanya menatap langit")
                    sendMessage(msg.to,"Mataku berkaca kaca")
                    sendMessage(msg.to,"Berlinang tak bisa berhenti")
                    sendMessage(msg.to,"Di tempat kita tinggal, didunia ini")
                    sendMessage(msg.to,"Dipenuhi cinta, kepada seseorang")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Janji tak lepas dirimu lagi")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Akhirnya kita bisa bertemu")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Ku akan bahagiakan dirimu")
                    sendMessage(msg.to,"Ku ingin kau mendengarkan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Jika jika kamu ragu")
                    sendMessage(msg.to,"Takkan bisa memulai apapun")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga")
                    sendMessage(msg.to,"Jika kau bersuar")
                    sendMessage(msg.to,"Cahaya kan bersinar")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Sampaikan rasa sayangku ini")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriakkan ditengah angin")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untuk ku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Katakan dengan berani")
                    sendMessage(msg.to,"Jika kau diam kan tetap sama")
                    sendMessage(msg.to,"Janganlah kau merasa malu")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga..")
                    sendMessage(msg.to,"Anugerah terindah adalah ketika kita masih diberikan waktu untuk berkumpul bersama orang-orang yang kita sayangi.")
                    sendMessage(msg.to,"Cuma dirimu seorang yang bisa meluluhkan hati ini. Kamulah yang terindah dalam hidupku.")
                    sendMessage(msg.to,"Aku ingin meraih kembali cintamu menjadi kenyataan. Saat diriku dalam siksaan cinta, dirimu melenggang pergi tanpa pernah memikirkan aku.")
                    sendMessage(msg.to,"Tak ada yang salah dengan CINTA. Karena ia hanyalah sebuah kata dan kita sendirilah yang memaknainya.")
                    sendMessage(msg.to,"Mencintaimu adalah inginku. memilikimu adalah dambaku. meski jarak jadi pemisah, hati tak akan bisa terpisah.")
                    sendMessage(msg.to,"Dalam cinta ada bahagia, canda, tawa, sedih, kecewa, terluka, semua itu tidak akan terlupakan dalam hal cinta, itu yang artinya cinta.")
                    sendMessage(msg.to,"Seseorang yang berarti, tak akan dengan mudah kamu miliki. Jika kamu sungguh mencintai, jangan pernah berhenti berusaha untuk hati.")
                    sendMessage(msg.to,"Jika esok pagi menjelang, akan aku tantang matahari yang terbangun dari tidur lelap nya.")
                    sendMessage(msg.to,"Ketulusan cinta hanya dapat dirasakan mereka yang benar-benar mempunyai hati tulus dalam cinta.")
                    sendMessage(msg.to,"Kamu tak perlu menjadikan dirimu cantik/ganteng untuk bisa memilikiku, kamu hanya perlu menunjukkan bahwa aku membutuhkanmu.")
                    sendMessage(msg.to,"Ada seribu hal yang bisa membuatku berpikir ununtuk meninggalkanmu, namun ada satu kata yang membuatku tetap disini. Aku Cinta Kamu.")
                    sendMessage(msg.to,"Aku pernah jatuhkan setetes air mata di selat Sunda. Di hari aku bisa menemukannya lagi, itulah waktunya aku berhenti mencintaimu.")
                    sendMessage(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    sendMessage(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang ku bahagia kadang ku bersedih.")
                    sendMessage(msg.to,"Cinta adalah caraku bercerita tentang dirimu, caraku menatap kepergian mu dan caraku tersenyum, saat menatap indah wajahmu.")
                    sendMessage(msg.to,"Saat jarak memisahkan, satu yang harus kamu ketahui. Akan aku jaga cinta ini ununtukmu.")
                    sendMessage(msg.to,"Bersandarlah di pundaku sampai kau merasakan kenyamanan, karena sudah keharusan bagiku ununtuk memberikanmu rasa nyaman.")
                    sendMessage(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu menjelaskan apa yang membuatmu terluka.")
                    sendMessage(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    sendMessage(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun untuk melupakanmu butuh waktu seumur hidupku.")
                    sendMessage(msg.to,"Hidup tidak bisa lebih baik tanpa ada cinta, tapi cinta dengan cara yang salah akan membuat hidupmu lebih buruk.")
                    sendMessage(msg.to,"Mencintaimu hanya butuh waktu beberapa detik, namun ununtuk melupakanmu butuh waktu seumur hidupku.")
                    sendMessage(msg.to,"Cinta merupakan keteguhan hati yang ditambatkan pada kemanusiaan yang menghubungkan masa lalu, masa kini dan masa depan.")
                    sendMessage(msg.to,"Ketika mencintai seseorang, cintailah apa adanya. Jangan berharap dia yang sempurna, karena kesempurnaan adalah ketika mencinta tanpa syarat.")
                    sendMessage(msg.to,"Cinta bukanlah tentang berapa lama kamu mengenal seseorang, tapi tentang seseorang yang membuatmu tersenyum sejak kamu mengenalnya.")
                    sendMessage(msg.to,"Ketika mereka bertanya tentang kelemahanku, aku ingin mengatidakan bahwa kelemahanku itul adalah kamu. Aku merindukanmu di mana-mana dan aku sanagat mencintaimu.")
                    sendMessage(msg.to,"Kehadiranmu dalam hidupku, aku tahu bahwa aku bisa menghadapi setiap tantangan yang ada di hadapanku, terima kasih telah menjadi kekuatanku.")
                    sendMessage(msg.to,"Meneriakkan namamu di deras hujan, memandangmu dari kejauhan, dan berdo’a di hening malam. Cinta dalam diam ini lah yang mampu kupertahankan.")
                    sendMessage(msg.to,"Perempuan selalu menjaga hati orang yang dia sayangsehingga hati dia sendiri tersiksa. inilah pengorbanan perempuan ununtuk lelaki yang tidak pernah sadar.")
                    sendMessage(msg.to,"Ketika kau belum bisa mengambil keputusan ununtuk tetap bertahan dengan perasaan itu, sabarlah, cinta yang akan menguatkanmu.")
                    sendMessage(msg.to,"Aku tidak akan pernah menjajikan ununtuk sebuah perasaan, tapi aku bisa menjanjikan ununtuk sebuah kesetiaan.")
                    sendMessage(msg.to,"Cinta yang sebenarnya tidak buta, cinta yaitu adalah hal yang murni, luhur serta diharapkan. Yang buta itu jika cinta itu menguasai dirimu tanpa adanya suatu pertimbangan.")
                    sendMessage(msg.to,"Aku tercipta dalam waktu, ununtuk mengisi waktu, selalu memperbaiki diri di setiap waktu, dan semua waktu ku adalah ununtuk mencintai kamu.")
                    sendMessage(msg.to,"Cinta akan indah jika berpondasikan dengan kasih sang pencipta. Karena sesungguhnya Cinta berasal dari-Nya Dan cinta yang paling utama adalah cinta kepada Yang Kuasa.")
                    sendMessage(msg.to,"Bagi aku, dalam hidup ini, hidup hanya sekali, cinta sekali dan matipun juga sekali. Maka tidak ada yang namanya mendua.")
                    sendMessage(msg.to,"Tuhan..jagalah ia yang jauh disana, lindungi tiap detik hidup yang ia lewati,sayangi dia melebihi engkau menyayangiku.")
                    sendMessage(msg.to,"Kapan kau akan berhenti menyakitiku, lelah ku hadapi semua ini tapi aku tidak bisa memungkiri aku sangat mencintaimu.")
                    sendMessage(msg.to,"Ketidakutan terbesar dalam hidupku bukan kehilanganmu, tapi melihat dirimu kehilangan kebahagiaanmu.")
                    sendMessage(msg.to,"Cinta yang sesungguhnya akan mengatidakan aku butuh kamu karna aku siap ununtuk mencintaimu dan menjalani suka duka bersamamu")
                    sendMessage(msg.to,"Seseorang pacar yang baik adalah dia yang JUJUR dan tidak pernah membuat kamu selalu bertanya-tanya atau selalu mencurigai dia")
                    sendMessage(msg.to,"Cinta bukanlah sebuah kata cinta, yang sebenarnya adalah cinta yang menyentuh hati dan perasaan")
                    sendMessage(msg.to,"Kau datang di saat ke egoisan akan cinta tengah mendera. Membawa cahaya dan kedamaian, membuatku tidak mudah menyerah ununtuk merengkuh kisah cinta bersamamu")
                    sendMessage(msg.to,"Aku sangat menyukai kebersamaan karena kebersamaan mengajarkan kita tentang suka dan duka di lalui bersama")
                    sendMessage(msg.to,"Mungkin Tuhan sengaja memberi kita berjumpa dengan orang yang salah sebelum menemui insan yang betul supaya apabila kita akhirnya menemui insan yang betul, kita akan tahu bagaimana ununtuk bersyukur dengan pemberian dan hikmah di balik pemberian tersebut.")
                    sendMessage(msg.to,"Getaran di hatiku yang lama haus akan belaianmu seperti saat dulu dan kau bisikan kata ‘aku cinta padamu’ aku merindukannya")
                    sendMessage(msg.to,"Terkadang air mata adalah tanda kebahagiaan yang tidak terucapkan. Dan senyuman adalah tanda sakit yang mencoba ununtuk kuat")
                    sendMessage(msg.to,"Dicintai dan disayangi kamu adalah anugerah terindah yang tuhan berikan padaku.")
                    sendMessage(msg.to,"Mencintai kamu butuh waktu beberapa detik, Namun melupakanmu butuh waktu ku seumur hidup.")
                    sendMessage(msg.to,"Datang dan pergi seperti angin tidak beraturan dan arah merasakan cinta dalam kehidupan kadang aku bahagia dan juga kadang aku bersedih.")
                    sendMessage(msg.to,"Air mata merupakan satu-satunya cara bagimana mata berbicara ketika bibir tidak mampu lagi menjelaskan apa yang membuatmu terluka.")
                    sendMessage(msg.to,"Jauh sebelum bertemu denganmu, aku telah mengenalmu dalam doaku.")
                    sendMessage(msg.to,"Mungkin dia tidak sadar bahwa aku itu cemburu dan mungkin juga dia tidak merasa bahwa aku sangat terluka, tidak mendengar bahwa hatiku sedang menangis.")
                    sendMessage(msg.to,"Kehadirmu membawa cinta, memberi bahagia, dan juga rasa rindu yang tiada pernah ada akhirnya.")
                    sendMessage(msg.to,"Aku nngak mau jadi wakil rakyat, aku maunya jadi wali murid yang ngambil raport anak kita besok.")
                    sendMessage(msg.to,"Seperti hujan yang turun di tanah yang tandus, seperti itulah arti hadirmu dengan cinta dan kasih sayang untukku.")
                    sendMessage(msg.to,"Tanda-tanda cinta adalah ketika anda merasa bahwa kebahagiaan orang tersebut lebih penting daripada kebahagiaanmu sendiri.")
                    sendMessage(msg.to,"Cinta tidak hanya apa yang anda rasakan, tetapi apa yang harus anda lakukan.")
                    sendMessage(msg.to,"Cinta adalah sebuah kekuatan untuk melihat kesamaan dan tidak kesamaan.")
                    sendMessage(msg.to,"Cinta adalah pengalaman penuh emosi yang dirasakan banyak orang tetapi hanya beberapa orang saja yang bisa menikmatinya.")
                    sendMessage(msg.to,"Cinta adalah berbagi. Karena walau ada di dua raga yang berbeda, setiap pasangan hanya memiliki satu hati.")
                    sendMessage(msg.to,"Saat kita berjauhan, sebenarnya hanya raga kitalah yang jauh. Namun hati kita selalu dekat, karena hatiku ada di hatimu.")
                    sendMessage(msg.to,"Cinta datang dengan pengorbanan yang akan memberikan petunjuk siapa diri kita yang sebenarnya.")
                    sendMessage(msg.to,"Cinta begitu lembut dan merdu, namun jangan kau gunankan untuk merayu. Karena rayuan hanyalah akan mengosongkan makna kecintaan yang sesungguhnya.")
                    sendMessage(msg.to,"Cinta bukanlah penuntutan, penguasaan, pemaksaan, dan pengintimidasian. Tak lain itu hanyalah cara manusia mendefinisikannya. Karena cinta adalah perjuangan, pengorbanan, tanggungjawab, kejujuran, dan keikhlasan.")
                    sendMessage(msg.to,"Derajat cinta hanya bisa diukur dengan seberapa besar “Pemberian” yang kita korbankan.")
                    
                elif "Send " in msg.text:
                    cond = msg.text.split(" ")
                    target = cond[1]
                    text = msg.text.replace("Send " + str(target) + " Chat ","")
                    try:
                        client.findAndAddContactsByMid(target)
                        sendMessage(target,"From Alin : \"" + text + "\"")
                        sendMessage(msg.to,"Berhasil mengirim pesan")
                    except:
                        sendMessage(msg.to,"Gagal mengirim pesan, mungkin midnya salah")
                if msg.text == "Myginfo":
                    group = client.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    sendMessage(msg.to,md)
                if msg.text == "Uni":
		            sendMessage(msg.to,"Hai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
                elif "Block @" in msg.text:
                    if msg.toType == 2:
                        print "[block] OK"
                        _name = msg.text.replace("Block @","")
                        _nametarget = _name.rstrip('  ')
                        gs = client.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   client.blockContact(target)
                                   sendMessage(msg.to, "Success block contact~")
                                except Exception as e:
                                   print e
                elif msg.text.lower() == 'blocklist':
                    blockedlist = client.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = client.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                    sendMessage(msg.to, msgs)
                elif msg.text.lower() == 'Mygid':
                    gid = client.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "✞ %s\nID : %s\n" % (client.getGroup(i).name,i)
                    sendMessage(msg.to,h)
                elif msg.text.lower() == 'bubar':
                    gid = client.getGroupIdsJoined()
                    for i in gid:
                        client.leaveGroup(i)
                    if wait["lang"] == "JP":
                        sendMessage(msg.to,"Sudah Keluar Di semua grup")
                    else:
                        sendMessage(msg.to,"He declined all invitations")
                elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 60000000000:
                        profile = client.getProfile()
                        profile.statusMessage = string
                        client.updateProfile(profile)
                        sendMessage(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
                elif "Myname " in msg.text:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 60000000:
                        profile = client.getProfile()
                        profile.displayName = string
                        client.updateProfile(profile)
                        sendMessage(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
                elif "Mysteal @" in msg.text:          
                   _name = msg.text.replace("Mysteal @","")
                   _nametarget = _name.rstrip('  ')
                   gs = client.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       sendMessage(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = client.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               client.sendImageWithURL(msg.to, path)
                           except:
                               pass
                elif "Ratakan" in msg.text:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = client.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           sendMassage(msg.to,"Tidak Ada Member")
                           pass
                       else:
                           for target in targets:
                              try:
                                  client.kickoutFromGroup(msg.to,[target])
                                  print (msg.to,[g.mid])
                              except:
                                  sendMessage(msg.to,"Rata? Protect Anjeng")
                                  sendMessage(msg.to,"masih mauko sundala")
                elif msg.text in ["My gurl"]:
                    if msg.toType == 2:
                        x = client.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            client.updateGroup(x)
                        gurl = client.reissueGroupTicket(msg.to)
                        sendMessage(msg.to,"line://ti/g/" + gurl)
                    else:
                        if wait["lang"] == "JP":
                            sendMessage(msg.to,"Can't be used outside the group")
                        else:
                            sendMessage(msg.to,"Not for use less than group")
                elif "Mid @" in msg.text:
                    _name = msg.text.replace("Mid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = client.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            sendMessage(msg.to, g.mid)
                        else:
                            pass
                elif "Kick " in msg.text:
                    nk0 = msg.text.replace("Kick ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = client.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"User Tidak Di Temukan")
                        pass
                    else:
                        for target in targets:
                            try:
                                client.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                print(msg.to,"Sundala")
                                print(msg.to,"Masih Mauko Bangsat!!!")
                elif "Invite " in msg.text:
                    midd = msg.text.replace("Invite ","")
                    client.findAndAddContactsByMid(midd)
                    client.inviteIntoGroup(msg.to,[midd])
                elif "Kick " in msg.text:
                    midd = msg.text.replace("Kick ","")
                    client.kickoutFromGroup(msg.to,[midd])
                elif ("Kick " in msg.text):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                       try:
                          client.kickoutFromGroup(msg.to,[target])
                       except:
                          pass
                elif "Ratakan" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = client.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Grup Tidak Ada")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[client]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    sendMessage(msg.to,"Kasian Di Kick....")
                                    sendMessage(msg.to,"Hehehe")
                elif "Bc:ct " in msg.text:
                    bctxt = msg.text.replace("Bc:ct ", "")
                    a = client.getAllContactIds()
                    for manusia in a:
                        sendMessage(manusia, (bctxt))
                elif "Bc:grup " in msg.text:
                    bctxt = msg.text.replace("Bc:grup ", "")
                    n = client.getGroupIdsJoined()
                    for manusia in n:
                        sendMessage(manusia, (bctxt))
                elif "Spam " in msg.text:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 100000:
                             for x in range(jmlh):
                                    sendMessage(msg.to, teks)
                        else:
                               sendMessage(msg.to, "Melebihi Batas!!! ")
                   elif txt[1] == "off":
                         if jmlh <= 100000:
                               sendMessage(msg.to, tulisan)
                         else:
                               sendMessage(msg.to, "Melebihi Batas!!! ")
                if msg.text == "Mid":
                    sendMessage(msg.to, msg.from_)
                if msg.text == "Gid":
                    sendMessage(msg.to, msg.to)
                if "Mygn" in msg.text:
                    key = msg.text[22:]
                    group = client.getGroup(msg.to)
                    group.name = key
                    client.updateGroup(group)
                    sendMessage(msg.to,"Group Name"+key+"Canged to")
                if msg.text == "My url":
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
                if "Join" in msg.text:
                    G = client.getGroup(msg.to)
                    ginfo = client.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    client.updateGroup(G)
                    invsend = 0
                    Ticket = client.reissueGroupTicket(msg.to)
                    client.acceptGroupInvitationByTicket(msg.to,Ticket)
                if msg.text == "Link on":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "already open")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL Open")
                if msg.text == "Link off":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "already close")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL close")
                if msg.text == "Cancel":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "No one is inviting.")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + " Done")
                if msg.text == "Me":
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': msg.from_}
                    client.sendMessage(M)
                if "Show " in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = client.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")
                if msg.text == "Gift":
                    sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
                if msg.text == "Cctv":
                    sendMessage(msg.to, "Cek CCTV")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
                if msg.text == "Ciduk":
                    if msg.to in wait['readPoint']:
                        if wait["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        sendMessage(msg.to, "T E R C Y D U K %s\n􀜁􀅔Har Har􏿿\n\nT E R S A N G K A\n%s􀜁􀅔Har Har􏿿\n\nTanggal Dan Waktu Kejadian:\n[%s]"  % (wait['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        sendMessage(msg.to, "Ketik「Cctv」􀜁􀅔Har Har􏿿")
                else:
                    pass
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()
