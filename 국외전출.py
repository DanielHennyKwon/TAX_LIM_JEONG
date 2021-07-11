# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
양도소득세={
    '국외전출세 입법취지': {},
    '거주자의 출국시 납세의무': {
        '국외전출세의 납세의무자': {
            '국외전출자의 범위':{},
        },
        '주식 등의 평가이익': {},
        '양도소득': {},
    },
    '과세표준의 계산':{
        '양도가액': {},
        '필요경비': {},
        '양도소득금액': {},
        '양도소득과세표준': {},
        '종합소득과 구분': {},
        '시가의 산정 등': {},
    },
    '세액계산구조': {},
    '세율 및 산출세액': {},
    '조정공제 등': {
        '출국한 후 실제 양도한 경우': {},
        '세액공제신청': {},
    },
    '외국납부세액공제': {
        '외국납부세애공제되는 경우': {},
        '왹구납부세액공제 안되는 경우': {},
    },
    '비가주자의 국ㄴ내원천소득 세액공제 등': {},
    '신고납부절차': {
        '납세관리인의 주식 보유현황 신고': {},
        '양도소득세과세표준신고기한': {},
        '감면세액 등': {},
        '재취득가액': {},
    },
    '납부유예': {
        '납부유예신청': {},
        '출국일로부터 5년 이내에 양도하지 아니한 경우': {},
        '실제 양도한 경우': {},
        '이자상당액': {},
    },
    '재전입 등에 따른 환급 등': {
        '환급신청 등': {},
        '신청을 받은 경우': {},
        '국세환급가산금': {},
    },
    '준용규정등': {},
    '서식': {},
}
#___________________________________________________
제목='국외전출'
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