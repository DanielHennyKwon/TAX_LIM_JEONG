# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 납부
import  납세지 , 납세의무 , 납세지 , 납부기한,신고기한 , 신고서류 , 전자신고 ,  세무조정 ,  과세표준신고
import 수정신고 , 경정청구 , 불성실신고_불이익 , 가산세 , 중소기업 , 계산서교부및계산서합계표제출 , 지출증명서류의수취및보관
import 농어촌특별세, 농어촌특별세 , 납세의무,물납,분납,신고납세제도,신고기한
import 신고

지방소득세_법인세분={}

법인세={

    '지출증명서류의 수취 및 보관':지출증명서류의수취및보관.법인세,
    '접대비 지출액에 대한 정규영수증 수취의무':{},
    '계산서 교부 및 계산서 합계표 제출':계산서교부및계산서합계표제출.법인세,
    '중소기업의 신고에 관한 주요내용':중소기업._,

}
연결={
    # 연결납세제도
    '연결과세표준과 법인세의 신고':{},
    '연결모법인의 연결법인세액의 납부':{},
    "연결자법인의 개별귀속세액의 지급":{},
    '연결법인의 개별귀속세액의 익금(손금)불산입':{},
    "물납 등":{},
}
양도소득세={
    '양도소득세 신고 납부(농특세 및 지방소득세)':{ },
    '양도소득세 신고 납부': {
        '예정신고 납부': {
            '예정신고': {},
            '예정신고납부': {},
            '예정신고 산출세액의 계산': {},
            '예정신고납부세액공제': {},
            '신고기간 경과후 다른 자산과 함께 예정신고한 경우': {},
        },
        '확정신고 납부': {
            '확정신고': {},
            '확정신고납부': {},
            '확정신고세액의 납부절차': {},
        },
        '양도소득세의 분할납부': {},
        '양도소득세의 물납': {},
        '수정신고와 경정 등의 청구': {}
    },
    '양도소득세 과세표준과 세액의 결정': {
        '결정사유(무신고)': {},
        '경정사유(탈루,오류)': {},
        '재경정사유': {},
        '결정방법': {},
        '통지': {},
        '주식거래 내역 드의 금융조회': {},
        '수시부과결정': {},
        '양도소득세의 징수': {},
        '가산세': {},
        '부동산 양도소득세 예정신고분에 대한 경정청구 기산점': {},
        '명의대여자 자신의 재산으로 납부한 종합소득세를 명의대여자에게 환급이 가능한지 여부': {},
    },
    '수정신고':{},
    '경정 등의 청구':{},
    '농어촌특별세 등의 신고 납부': {
        '농어촌특별세의 신고 납부': 농어촌특별세.양도소득세,
        '지방소득세(소득세분)의 신고납부': {}
    },
}
증여세={
    '증여세 신고 납부':{
        '증여세 과세가액과 과세표준 신고':{},
        '증여세 경정청구의 특례':{},
        '증여세의 납부':{}
    },
    '연부연납과 물납':{
        '연부연납제도':{},
        '물납제도':{},
    },
}
#___________________________________________________
제목='신고납부절차'
_={
    "연결신고납부":연결,

    #"기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
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