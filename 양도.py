# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
간주={#과세원인
    "양도의 개념": {},
    "매매": {},
    "교환": {},
    "대물변제": {},
    "이혼위자료": {},
    "현물출자": {
        "현물출자란?":{},
        "법인에 현물출자": {},
        "공동사업을 영위하기 위하여 부동산을 현물출자한 경우": {},
    },
    "경락된 경우": {},
    "환매조건부인 경우": {},
    "신탁재산을 유상이전한 경우": {},
    "환지처분": {},
    "상속세 등이 부과된 토지 등을 물납한 경우": {},
    "피상속인이 부동산매매계약을 체결하고 잔금을 청산하기 전에 사망한 경우": {},
}
불간주={
    "명의신탁해지":{},
    "매매원인 무효":{},
    "이전등기후 합의해제로 환원한 경우":{},
    "공유물분할": {},
    "토지거래허가를 받지 아니한 상태에서 매매대금을 지급한 경우 과세 여부": {},
    "본인이 경락받은 경우": {},
    "등기착오로 다르게 등기되어 정정하는 경우": {},
    "사해행위 취소판결에 따라 소유권이 이전된 경우": {},
    "재산분할청구권에 따른 유상양도":{
        "유상양도 해당 여부": {},
        "취득시기 등의 판정": {},
        "혼인 전 취득한 재산의 적용 여부": {},
    },
    "환지처분": {
        "도시재개발법 등에 의한 환지처분 등": {},
    },
    "양도담보": {
        "양도로 보지 아니한 경우": {},
        "양도로 보는 경우": {},
    },
    "양도소득이 아닌 기타소득 등인 경우": {
        "기타소득인 경우": {},
        "기타소득 아닌 경우": {},
        "양도소득 아닌 경우": {},
        "사업소득인 경우": {},
        "사해행위 등": {},
    },
}

_={
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"양도소득세":양도소득세,
    "간주":간주,
    "불간주":불간주,
}
tax=_;제목='양도'
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
