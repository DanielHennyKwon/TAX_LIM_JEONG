# -*- coding: utf-8 -*-
# 2018-12-26 권달현
import 국세기본법,법인세법,세무조정,수정신고,경정청구
신고납세제도={
    "신고납세제도란 납부하여야 할 세액을 납세자가 신고하여 확정하고,신고가 없거나 사실과 다르게 신고한 경우에 한하여 정부가 결정/경정에 의하여 세액을 확정하는 제도를 말한다.":{},
    "국세기본법 제21조(납세의무의 성립시기)":국세기본법.제21조,
    "국세기본법 제22조(납세의무의 확정)":국세기본법.제22조,
    "신고납세제도와 부과납세제도의 비교":{
        "부과과세제도하에서는 설령 납세자가 과다하게 신고한 경우라도 정부가 조사 결정에 의하여 이를 시정하여야 한다.":{
            "만일 이를 시정하지 아니한 경우에는 납세자가 불복절차를 통하여 구제받을 수 있다.":{},
        },
        "신고납세제도하에서는 과다신고가 있다 하더라도 경정청구기한이 경과된 후에는 원칙적으로 정부가 이;르 감액하여야 할 믜누는 없다.":{
            "납세자가 이에 대하여 불복을 신청할 수 없다.":{},
        },
        "의의":{
            "신고납세제도 : 납부할 세액을 납세자의 신고에 의하여 확정하는 제도":{},
            "부과과세제도 : 납부할 세액을 행정관청의 처분에 의하여 확정하는 제도":{},
        },
        "조세채권확정의 주체":{
            "신고납세제도 납세의무자: ":{},
            "부과과세제도 : 정부(세무서장)":{},
        },
        "조세채권확정의 시기":{
            "신고납세제도 : 납세의무의 신고시":{},
            "부과과세제도 : 정부의 조사결정시":{},
        },
        "조세채권확정의 절차":{
            "신고납세제도 : 신고서의 제출":{},
            "부과과세제도 : 결정,납세고지":{},
        },
        "탈루세액에 대한 조치":{
            "신고납세제도 : 세액추징,처벌 가능":{},
            "부과과세제도 : 세액추징":{},
        },
        "조사권의 성질":{
            "신고납세제도 : 과세관청의 권한,납세의무자도 청구 가능":{},
            "부과과세제도 : 과세관청의 권한인 동시에 의무":{},
        },
        "범칙행위의 기수시기":{
            "신고납세제도 : 신고,납부기한이 경과한 때":{},
            "부과과세제도 : 경정,결정후 납부기한이 경과한 때":{},
        },
    },
}
법인세={
    "신고납세제도의 개요":신고납세제도,
    "법인세법 제60조(과세표준 등의 신고)":법인세법.제60조,
    "법인세법 제66조(결정 및 경정)":법인세법.제66조,
    "신고납세제도의 운용을 위한 제도":{
        "외부세무조정계산서 첨부":세무조정.외부,
        "수정신고":수정신고._,
        "경정청구":경정청구._,
        "세무조정계산서의 법정서식화":세무조정.계산서,
    },
}
#___________________________________________________
제목='신고납세제도'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"양도소득세":양도소득세,
    #"농어촌특별세":{},
}
tax=_
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=제목)
        self.SetSize(420,320*2)
        self.mainPanel=wx.Panel(self)
        self.expandButton=wx.Button(self.mainPanel,label='펼침')
        self.tree=wx.TreeCtrl(self.mainPanel)
        root=self.tree.AddRoot(제목)
        for i in tax:
            ii=self.tree.AppendItem(root,i)
            for j in tax[i]:
                jj=self.tree.AppendItem(ii,j)
                for k in tax[i][j]:
                    kk=self.tree.AppendItem(jj,k)
                    for m in tax[i][j][k]:
                        mm=self.tree.AppendItem(kk,m)
                        for n in tax[i][j][k][m]:
                            nn=self.tree.AppendItem(mm,n)
                            for p in tax[i][j][k][m][n]:
                                pp=self.tree.AppendItem(nn,p)
                                for q in tax[i][j][k][m][n][p]:
                                    qq=self.tree.AppendItem(pp,q)
                                    for r in tax[i][j][k][m][n][p][q]:
                                        rr=self.tree.AppendItem(qq,r)

        self.staticText =wx.TextCtrl(self.mainPanel,style=wx.TE_MULTILINE)


        self.vtBoxSizer=wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton,0,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.tree        ,5,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.staticText  ,0,wx.EXPAND|wx.ALL,5)


        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON          ,self.OnExpandButton,self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnNodeSelected,self.tree)
    def OnExpandButton(self,e):
        self.tree.ExpandAll()
    def OnNodeSelected(self,e):
        selected=self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________