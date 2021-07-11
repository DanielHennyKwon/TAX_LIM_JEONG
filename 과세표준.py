# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 각사업연도소득의계산,비과세,소득공제,이월결손금
법인세_과세표준의계산={
    '각 사업연도의 소득금액':각사업연도소득의계산.법인세,
    '(-)이월결손금':이월결손금.법인세,
    '(-)비과세소득':비과세.법인세,
    '(-)소득공제':소득공제.법인세,
}
법인세_해운기업={
    "개요":{
        "해운기업":{},
        "해운소득":{},
    },
    "과세표준계산 특례":{
        "해운소득":{
            '선박의 경우':{},
            '선박표준이익 - 개별선박순톤수 × 톤당 1운항일 이익 * × 운항일수 × 사용률':{},
            '1천톤이하 14원, 1천톤초과 1만톤이하 11원, 1만톤초과 2만5천톤 이하 7원, 2만5천톤 초과4원':{},
        },
        "비해운소득(고정자산처분손익,배당소득,터미널 운용소득 등)":{},
    },
}
법인세_기능통화해외사업장={
    '기능통화 도입기업 과세표준 계산특례':{
        "과세표준 계산방법의 선택과 신고":{
            "선택가능한 방법":{},
            "과세표준계산방법신고와 변경":{},
        },
        "기능통화 변경시 소득금액의 계산:일시상각충당금 또는 압축기장충당금의 계상":{},
        "기능통화 도입 기업의 과세표준 계산 관련 세부 규정":{},
    },
    '해외사업장의 과세표준 계산특례':{
        "과세표준 계산방법의 선택과 신고":{},
        "해외사업장 도입 기업의 과세표준계산방법 관련 세부 규정":{},
    },
}
법인세={ # To : a1_제7부법인세계산
    '일반의 경우':법인세_과세표준의계산,
    '해운기업에 대한 과세표준 계산특례':법인세_해운기업,
    '기능통화 도입기업 및 해외사업장의 과세표준 계산특례':법인세_기능통화해외사업장,
}
농어촌특별세={
	'...':{},
}
증여세={
    '과세표준 계산':{},
    '증여재산공제':{},
    '재해손실공제':{},
    '감정평가수수료':{}
}
#___________________________________________________
제목='과세표준'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    #"상속세":상속세,
    #"양도소득세":양도소득세,
    "농어촌특별세":{},
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