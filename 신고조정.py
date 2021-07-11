# -*- coding: utf-8 -*-
# 2018-12-26 권달현
import 법인세법,법인세법시행령
법인세={
    "의의":{
        "세무조정에는 결산조정과 신고조정이 있다.":{},
        "신고조정이란 기업이 스스로 장부에 계상함이 없이 결산서상의 당기순이익을 기초로 하여 과세표준시고서에만 계상해도 되는 사항을 통하여 세무조정을 하는 절차를 이른다.":{},
        },
    "결산반영 없이 신고서 계상 가능":{},
    "신고조정은 결산조정과 달리 결산확정에 의한 손금산입/이금산입을 강요하지 않고,과세표준 조정계산서에서 재무제표상의 당기순손익에 익금과 손금을 가감조정하여 과세표준을 계산할 수 있는 항목으로서 다음과 같다.":{},
    "대표자 등의 가지급금 인정이자의 익금산입 :법인세법시행령 제88조(부당행위계산의 유형 등)제1항 6호 ":법인세법시행령.제88조,
    "퇴직보험료 등의 손금산입 : 법인세법시행령 제44조의2(퇴직보험료 등의 손금불산입) ":법인세법시행령.제44_02조,
    "자산계상기부금의 손금산입 ":{
        "법인세법 제24조(기부금의 손금불산입) ":법인세법.제24조,
        "법인세법시행령 제37조(기부금의 가액 등) 제2항": 법인세법시행령.제37조,
    },
    "부당행위계산 부인에 관계되는 익금산입 및 손금불산입":{
        "법인세법 제52조(부당행위계산의 부인) ": 법인세법.제52조,
    },
    '회계감사받는 비영리내국법인의 고유목적사업준비금':{
        "법인세법 제29조(고유목적사업준비금의 손금산입) 제1항": 법인세법.제29조,
        "...고유목적사업준비금을 손금으로 계상한 경우에는 ... 이를 손금에 산입한다.": {},
        "단,외부감사를 받는 비영리내국법인은 신고조정 가능:법인세법제61조(준비금의 손금 계상 특례)": 법인세법.제61조,
    },
    '손익귀속시기 차이':{
        "법인세법 제40조(손익의 귀속사업연도) ": 법인세법.제40조,
    },
}
#___________________________________________________
제목='신고조정'
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