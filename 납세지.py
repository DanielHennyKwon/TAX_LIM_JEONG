﻿# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현

법인세={
	'...':{},
	}
지방소득세_법인세분={
	'...':{},
	}

양도소득세={
	"거주자의 납세지": {},
	"비거주자의 납세지": {},
	"납세지가 불분명한 경우": {},
	"비거주자로부터 부동산 등 양수한 자의 원천징수 소득세의 납세지": {},
	"상속 등 특별한 경우의 납세지": {},
}
납세지={
	"법인세_납세지":법인세,
	"양도소득세_납세지": 지방소득세_법인세분,
	"지방소득세_법인세분_납세지": 양도소득세,
	"": {},
	"": {},
}