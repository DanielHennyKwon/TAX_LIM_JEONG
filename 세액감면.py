﻿# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import  농지,부동산,주택
무신고등_공제감면적용배제={# To:결정세액
    "추계결정,경정시 공제,감면 등의 적용 배제":{},
    "무신고,과소신고,기한후신고,수정신고 등의 경우 공제,감면 배제":{},
}
공제감면세액_순위_중복적용배제={# To:결정세액
    "면제,감면과 세액공제가 동시에 적용되는 경우":{},
    "최저한세 적용대상과 적용배제되는 공제,감면이 동시에 해당되는 경우":{},
    "공제감면세액의 중복적용 배제":{
        "조세특례제한법상 투자세액공제의 중복적용 배제": {},
        "외국인 투자지분이 있는 경우의 조세특례제한법상 세액의 공제,감면": {},
        "조세특례제한법상 기한부 면제,감면 등과 세액공제의 중복적용 배제": {},
        "감면규정의 중복적용 배제": {},
    },
}

법인세={ # To:결정세액
    "면제,감면세액의 계산방법":{},
    "법엔세의 면제":{},
    "법인세의 감면":{
        "감면대상 소득의 범위":{},
        "수정신고 또는 경정청구에 의한 세액감면의 적용":{},
        "당초 적용한 세액감면의 다른 유형으로의 변경":{},
        "감면세액의 승계":{},
        "종류 및 내용":{
            '창업중소기업에 대한 법인세 감면':{},
        },
    },
    "공제감면세액의 적용순위와 중복적용 배제": 공제감면세액_순위_중복적용배제,
    "무신고,과소신고 및 수정신고 등의 경우 공제,감면 배제": 무신고등_공제감면적용배제,
}
농어촌특별세={
	'...':{},
	}
증여세={
    "조세특례제한법상":농지.증여세_감면,
    '증여세 감면의 종합한도': 농지.증여세_감면한도,
}
양도소득세={
    '농지_양도소득세_감면':농지.양도소득세_감면,
    '주택_양도소득세_감면':주택.양도소득세_감면,
    '부동산_양도소득세_감면':부동산.양도소득세_감면,
}

_={
    "무신고등_공제감면적용배제": 무신고등_공제감면적용배제,
    "공제감면세액_순위_중복적용배제": 공제감면세액_순위_중복적용배제,

    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    "양도소득세":양도소득세,
    "농어촌특별세":{},
}
tax=_;제목='세액감면'
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
