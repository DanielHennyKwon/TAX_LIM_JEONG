# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
법인세= { #To: 결정세액
    "세율":{
        "일반 법인세율":{
            "과세표준":{
                "200억원 초과:22%":{},
                "2억원~200억원 이하:20%":{},
                "2억원 이하:10%":{},
            },
        },
        "조합 법인세율":{},
        "중과세율(법인세에 양도소득의 10% 추가과세)":{},
    },
    "사업연도가 1년 미만인 경우 세율 적용":{},
    "영리법인의 법인세율 변천":{},
}
농어촌특별세={
	'...':{},
	}
양도소득세={
    "국내자산의 세율":{},
    "국외자산의 세율": {},
    '양도소득세 산출세액 계산의 특례':{},
    '지정지역(투기지역)안의 비사업용토지 등 중과세율': {},
    '조정대상지역 내의 다주택자 중과세율': {},
    '양도소득세의 특례(한시적) 세율': {},
    '양도소득세의 세율적용시 보유기간의 계산': {},
    '미등기양도자산의 범위': {},
    '양도소득세의 세율 등 적용시 보유기간의 기산일': {},
    '과세표준과 산출세액':{
        '양도소득세의 세율적용':{}
    },
    '자진납부세액의 계산':{
        '자진납부할 세액 계산구조':{},
        '양도소득 감면세액의 계산':{},
        '외국납부세액의 공제':{}
    },
}
#___________________________________________________
제목='세율'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    "양도소득세":양도소득세,
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