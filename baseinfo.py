
# -*- coding: utf-8 -*-

def baseinfo(ID):
	
	import urllib2
	import json
	import platform
	
	# 判断运行系统
	sys = platform.system()
	
	# 获取玩家基本信息
	url = 'http://300report.jumpw.com/api/getrole?name=' + ID
	response = urllib2.urlopen(url)
	rolejson = response.read()
	roledata = json.loads(rolejson)
	
	if roledata['Result'] != 'OK':
		if sys == 'Windows':
			print '查无此人'.decode('utf-8').encode('gbk')
		else:
			print '查无此人'
	else:
		if sys == 'Windows':
			print '查询成功'.decode('utf-8').encode('gbk')
		else:
			print '查询成功'
		
		# 玩家基本信息
		Role 		= roledata['Role']
		RoleName 	= Role['RoleName']
		RoleLevel 	= Role['RoleLevel']		
		JumpValue 	= Role['JumpValue']
		WinCount 	= Role['WinCount']
		MatchCount 	= Role['MatchCount']
		UpdateTime 	= Role['UpdateTime']
		
		# 团队实力评分
		Rank 		= roledata['Rank']
		Ranklen		= len(Rank)
		rRankValue	= 0
		rRankIndex	= 0
		for i in range(Ranklen):
			rRank		= Rank[i]
			rRankName	= rRank['RankName']
			print rRankName
			if rRankName == u'\u56e2\u961f\u5b9e\u529b\u6392\u884c':
				rRankValue	= rRank['Value']
				rRankIndex	= rRank['Rank']		
		
		with open('baseinfo.txt','w') as info:
			info.writelines(['角色名    ',	RoleName.encode('utf-8'),	'\n'])
			info.writelines(['角色等级  ',	str(RoleLevel),				'\n'])
			info.writelines(['节操值    ',	str(JumpValue),				'\n'])
			info.writelines(['胜场数    ',	str(WinCount),				'\n'])
			info.writelines(['总场数    ',	str(MatchCount),			'\n'])
			info.writelines(['更新日期  ',	UpdateTime.encode('utf-8'),	'\n'])
			info.writelines(['团队实力  ',	str(rRankValue),			'\n'])
			info.writelines(['团分排行  ',	str(rRankIndex),			'\n'])
			info.close()
			