# -*- coding: utf-8 -*-
# MCDR-Get 插件安装
# 请根据提示修改

def info() -> tuple:
    name = 'ItemStack' # 插件名字
    pip_lib = '' # pip支持库 多个请用 ',' 分割（自带的无需填写）
    lib = '' # mcdr仓库api 多个请用 ',' 分割
    auther = 'dogdie233' # 作者
    api = True # 是否为Api
    remarks_cn = '一个仿造Bukkit物品API的API' # 介绍 中文
    remarks = 'An Item api like Bukkit.' # 介绍 英文
    raw = 'https://raw.githubusercontent.com/dogdie233/ItemStack/master/ItemStack.py' # 下载地址
    raw_cn = 'https://dogdieself.coding.net/p/itemstack/d/itemstack/git/raw/master/ItemStack.py' # 国内下载地址
    return name, pip_lib, lib, auther, api, remarks ,remarks_cn, raw, raw_cn

def install(server):
    download_successful = server.download("https://raw.githubusercontent.com/dogdie233/ItemStack/master/ItemStack.py")
	if download_successful == False:
		server.say("\u00A7c[ItemStack] 从github下载失败, 尝试使用备用链接")
		download_successful = server.download("https://dogdieself.coding.net/p/itemstack/d/itemstack/git/raw/master/ItemStack.py")
		if download_successful == False:
			server.say("\u00A7c[ItemStack] 使用备用链接下载失败, 请重试")
