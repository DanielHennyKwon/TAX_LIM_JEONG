# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
양도소득세={
    '건물 기준시가 산정방법':{
        '건물기준시가 고시 : 국세청 www.nts.go.kr  >...>고시(매년 연말에 고시함)':{},
        '건물기준시가 산정방법 해설:국세청>국세정보>국세청발간책자>..>건물기준시가산정방법 해설서': {},
        '건물기준시가계산프로그램 홈택스>조회>기타조회>기준시가조회>건물기준시가': {},
    },
    "개별공시지가 고시일":{},
    "개별주택가격 고시일": {},
    '토지': {
        '기준시가 산정': {},
        '기준시가 고시전에 취득 또는 양도하는 경우의 적용기준일': {},
        '토지의 기준시가 적용사례': {},
        '1990.8.30 이전에 취득한 경우': {},
        '토지등급가액의 적용방법': {},
        '토지,건물의 기준시가 산정 및 기준시가 조정이 동일한 경우': {},
        '토지의 수용,경매대금 등이 양도 당시 공시지가보다 낮은 경우': {},
    },
    '건물': {
        '기준시가 산정': {},
        '취득당시 기준시가가 없는 경우': {},
        '건물의 기준시가 산정 및 기준시가 조정기간이 동일한 경우': {},
        '건물 등의 정의': {},
        '건물의 수용,경매대금 등이 양도 당시 기준시가보다 낮은 경우': {},
    },
    '오피스텔및상업용건물': {
        '기준시가 산정': {},
        '취득당시 기준시가가 없는 경우': {},
        '토지,건물의 기준시가 산정 및 기준시가 조정기간이 동일한 경우': {},
        '오피스텔 및 사업용건물의 수용,경매대금 등이 양도 당시 기준시가보다 낮은 경우': {},
        '기준시가 고시전 의견 청취 등': {},
        '기준시가의 재산정,고시 신청': {},
    },
    '주택': {
        '기준시가 산정': {},
        '취득당시 기준시가가 없는 경우': {},
        '토지,건물의 기준시가 산정 및 기준시가 조정기간이 동일한 경우': {},
        '주택의 수용,경매대금 등이 양도 당시 기준시가보다 낮은 경우': {},
        '개별주택가격이 공시된 주택부수토지의 범위를 초과하는 토지 안분':{},
    },
    '부동산에 관한 권리': {
        '부동산을 취득할 수 있는 권리(아파트당첨권 등)':{},
        '지상권,전세권 및 등기된 부동산 임차권': {},
    },
    '주식 및 출자지분': {
        '주권상장법인의 주식 등': {},
        '주권비상장법인의주식 등': {},
        '신주인수권': {},
        '주식 등의 기준시가 동일한 경우': {},
    },
    '기타자산': {
        '특정주식 및 부동산과다보유법인주식 등': {},
        '영업권': {},
        '시설물이용권(골프호원권 등)': {},
    },
    '파생상품': {},
    '기준시가 산정요약': {},
}
#___________________________________________________
제목='기준시가'
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