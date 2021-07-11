# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:55:08 2018

@author: SAMSUNG 11
"""
import 준비금

법인세={
        '비영리법인의 범위':{},
        '수익사업의 범위':{},
        '수익사업 소득에 대한 과세':{
            '비영리법인의 고유목적사업준비금 손금산입':{
                '준비금 설정 대상법인':{},
                '준비금 설정한도':{},
                '준비금의 사용':{},
                '준비금의 익금산입':{},
                },
            '비영리법인의 이자소득에 대한 법인세 신고특례':{
                '비영리법인의 이자소득에 대한 과세 및 신고특례':{
                    "과세 특례":{},
                    "신고 특례":{},
                },
                '이자소득만 있는 비영리법인의 법인세 신고특례':{},
                },
            "재무제표 등 미첨부시 미신고간주 배제":{},
            "기장의무의 면제":{},
            "무기장가산세 적용 배제":{},
            "고유목적사업준비금의 손금산입":준비금.고유목적사업준비금,
            "비영리내국법인의 자산양도소득에 대한 과세특례":{},
            '조합법인 등에 대한 당기순이익 과세특례':{},
            '정비사업조합에 대한 과세특례':{
                "개요":{},
                "수익사업에서 제외되는 사업의 범위":{},
                "잔여재산의 분배를 받는 자에 대한 제2차납세의무":{},
                "기타":{},
            },
        },
        '기타 사항 ':{
            '법인으로 보는 단체의 최초 사업연도 개시일':{},
            '수익사업 개시 신고':{},
            "결손금 공제":{},
            "비영리법인의 잉여금 처분":{},
            '기부금영수증 발급명세의 작성,보관,제출의무':{},
            },
        }

#__________________________________________________________________
제목='비영리법인에 대한 과세특례'
_={
    "법인세":법인세,

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
#__________________________________________________________________