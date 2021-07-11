# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 기업회계의_결산서상_당기순손익,손익의귀속사업연도,익금산입,익금불산입,손금불산입,손금산입,손금불산입,기부금,합병분할
차가감소득금액={
	'...':{},
	}
연결={
        # 연결납세제도
        '계산구조':{},
        '각 단계별 계산방법':{},
        "각 연결사업연도 소득의 계산":{
                "연결법인별 각 사업연도의 소득 또는 결손금의 계산":{},
                "연결법인별 연결조정항목의 제거":{},
                "연결법인간 거래손익의 조정": {},
                "연결조정항목의 연결법인별 배분": {},
                "각 연결사업연도 소드금액(결손금)의 계산": {},
        },
}
법인세={
    "국세청": {
        "각 사업연도 소득금액은 그 사업연도에 속하는 익금의 총액에서 손금의 총액을 공제한 금액으로 하고, 손금의 총액이 익금의 총액을 초과하는 경우 그 초과하는 금액은 각사업연도의 결손금으로 합니다.": {},
        "- 익금：자본 또는 출자의 납입 및 법인세법에서 규정하는 것을 제외하고 그 법인의 순자산을 증가시키는 거래로 인하여 발생하는 수익의 금액(법법§15①)": {},
        "- 손금：자본 또는 출자의 환급, 잉여금의 처분 및 법인세법에서 규정하는 것을 제외하고 그 법인의 순자산을 감소시키는 거래로 인하여 발생하는 손비의 금액(법법§19①) ": {},
    },
    '기업회계의 결산서상 당기순손익':기업회계의_결산서상_당기순손익.기업회계의_결산서상_당기순손익,
    '손익의 귀속사업연도':손익의귀속사업연도.법인세,
    '(+)익금산입'  :익금산입.법인세,
    '(+)손금불산입':손금불산입.법인세,
    '(-)손금산입'  :손금산입.법인세,
    '(-)익금불산입':익금불산입.법인세,
    '차가감소득금액':차가감소득금액,
    '(+)기부금한도초과액 및 (-)기부금손금추인액':기부금.법인세,
    '합병 및 분할 등에 관한 특례':합병분할.법인세,
    '(=)각사업연도소득':{},
    "연결 각사업연도소득":연결,
}

#___________________________________________________
제목='각사업연도소득의 계산'
_={
    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"상속세":상속세,
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
        #self.
        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________