# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
양도소득세={#양도소득세
    '필요경비의 의의':{},
    '취득가액 등 필요경비의 계산':{
        '필요경비의 범위': {},
        '필요경비의 계산': {},
        '감가상가자산의 필요경비 계산': {},
        '취득에 든 실지거래가액의 범위': {},
        '취득세(등록세)의 세율 등 요약': {},
        '토지와 정착물을 일괄 양도한 경우': {},
        '부동산과 비품 등을 함께 양도한 경우': {},
        '부가가치세의 필요경비 산입 여부': {},
        '양수인 부담의 양도소득세': {},
        '전세보증금': {},
        '명도비용 등을 지급한 경우': {},
        '이주택지 분양권': {},
        '이축권의 취득비용': {},
        '위약금 등 지급한 경우': {},
        '합의금 등을 지급한 경우': {},
        '경락받은 자산': {},
        '기부금': {},
        '필요경비 해당되는 경우': {},
        '필요경비 해당 안되는 경우': {},
    },
    '자본적지출액의 계산':{
        '자본적 지출의 범위': {},
        '철거된 건물의 필요경비 해당여부': {},
        '장애철거비용': {},
        '묘지 이장 비용': {},
        '법무사비용 및 컨설팅비용': {},
        '택지초과소유부담금': {},
        '개발부담금': {},
        '개발제한구역의 보전부담금': {},
        '토지초과이득세': {
            '필요경비로 인정되는 토지초과이득세': {},
        },
        '학교용지 확보부담금': {},
        '하수도 원인자부담금': {},
        '기반시설부담금': {},
        '농지전용에 소요된 경비': {},
        '주택의 샤시,방 확장 등 내부시설공사비': {},
        '신축과 관련된 설계비': {},
        '지적측량수수료': {},
        '공사비': {},
        '법인세법에 따라 상여 등의 처분을 받은 경우': {},
    },
    '양도비용 계산':{},
    '필요경비 해당되는 경우': {},
    '필요경비 해당 안되는 경우': {},
    '기타의 경우 취득가액 및 필요경비 계산':{},
}
제목='필요경비'
_={
    #"기업회계":기업회계,
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    "양도소득세":양도소득세,
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