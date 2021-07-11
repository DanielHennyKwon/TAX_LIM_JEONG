# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
과세특례={
    "개요":{},
    "적격현물출자요건":{},
    "압축기장충당금":{
        "출자법인의 손금산입":{},
        "익금산입":{},
    },
}
법인세={
    "과세특례":과세특례,
    "현물출자로 인한 자산양도차익 상당액의 손금산입 (법법§47의2) ": {

            "현물출자란 회사의 설립 또는 신주의 발행 시에 금전 이외의 재산을 출자하는 것을 말하며, 현물출자는 재산승계의 대가로서 피출자법인의 주식을 취득한다는 점에서 물적분할과 유사하나, 특정재산을 선택적으로 승계 시킨다는 점에서 분할사업부문의 권리ㆍ의무를 당연 포괄승계함을 전제로 하는 물적분할과 차이점이 있습니다. ": {},
            "☞ 토지 및 건물, 사업용 유형자산 등의 현물출자로 인한 자산양도차익에 대하여는  조세특례제한법  제38조에서 과세이연 규정을 두고 있었으나, ’08.12.30. 관련 규정을  법인세법  제47조의2 조항으로 이관하고, 과세이연 대상의 범위를 물적분할에서 지원하는 범위와 일치시켰음 ": {},
            "가. 손금산입 요건 ": {

                "  현물출자법인이 아래의 요건을 갖춘 현물출자(이하 “적격현물출자”라 함)를 하는 경우": {},
                "- 피출자법인의 주식 등의 가액 중 현물출자로 발생한 자산의 양도차익에 상당하는 금액은 피출자법인의 주식 등의 압축기장충당금으로 계상하는 방법에 의하여 현물출자일이 속하는 사업연도의 손금에 산입할 수 있습니다(단, 법령§84의2⑪에서 정하는 부득이한 사유가 있는 경우에는 ② 또는 ④의 요건을 갖추지 못한 경우에도 자산의 양도차익에 상당하는 금액을 손금에 산입할 수 있음(법법§47의2) ": {},

                "① 출자법인이 현물출자일 현재 5년 이상 사업을 계속한 법인일 것": {},
                "② 피출자법인이 그 현물출자일이 속하는 사업연도의 종료일까지 출자법인 으로부터 승계받은 사업을 계속할 것": {},
                "③ 다른 내국인 또는 외국인과 공동으로 출자하는 경우 공동으로 출자한 자가 출자법인의 특수관계인이 아닐 것": {},
                "④ 출자법인 및 위 ③에 따라 출자법인과 공동으로 출자한 자가 현물출자일 다음 날 현재 피출자법인의 발행주식총수 또는 출자총액의 80% 이상의 주식등을 보유하고, 현물출자일이 속하는 사업연도의 종료일까지 그 주식등을 보유할 것": {},
                "⑤ 출자법인이 분리하여 사업이 가능한 독립된 사업부문을 현물출자를 통하여 피출자법인에 승계할 것(독립된 사업부분 판단시 법령§84의2⑭⑮ 참조) ": {},
            },
            "나. 손금산입 금액의 익금산입 ": {

                "  출자법인이 피출자법인으로부터 받은 주식 등을 처분하거나 피출자법인이 출자법인 (공동출자한 자 포함)으로부터 승계받은  법인세법시행령  제84조의2 제4항에 의한 자산을 처분하는 경우에는 같은 조 제3항의 규정에 해당하는 금액을 그 사유가 발생한 사업연도의 익금에 산입해야 합니다(법법§47의2②)": {},
                "  또한, 피출자법인이 출자법인으로부터 승계받은 사업을 현물출자일이 속하는 사업연도의 다음 사업연도 개시일부터 2년내에 폐지하거나 출자법인(공동 출자한 자포함)이 피출자법인의 발행주식 총수 또는 출자총액의 50%미만으로 주식 등을 보유하게 되는 경우에는 위에 따라 익금에 산입하고 남은 금액을 그 사유가 발생한 날이 속하는 사업연도의 소득금액을 계산할 때 익금에 산입해야 합니다(법법§47의2③) ": {},

            },
        },
}

#___________________________________________________
제목='현물출자'
_={
    #"지방소득세_법인세분 가산세": 지방소득세_법인세분,
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