# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    lianJiaBianHao = scrapy.Field()

    guanZhuRenShu = scrapy.Field()
    kanGuoRenShu = scrapy.Field()
    faBuShiJian = scrapy.Field()

    zongJiaGe = scrapy.Field()
    danWeiFangJia = scrapy.Field()
    shuiFeiMiaoShu = scrapy.Filed()

    fangWuChaoXiang = scrapy.Filed()
    fangWuMianJi = scrapy.Filed()
    jianFangShiJian = scrapy.Filed()

    xiaoQuMingCheng = scrapy.Field()
    suoZaiQuYu = scrapy.Field()
    
    desc = scrapy.Field()

    fangWuHuXing = scrapy.Field()
    suoZaiLouCeng = scrapy.Field()
    zongLouCeng = scrapy.Field()
    jianZhuMianJi = scrapy.Field()
    jianZhuLeiXing = scrapy.Field()
    fangWuChaoXiang = scrapy.Field()
    jianZhuJieGou = scrapy.Field()
    zhuangXiuQingKuang = scrapy.Field()
    tiHuBiLi = scrapy.Field()
    gongNuanFangShi = scrapy.Field()
    peiBeiDianTi = scrapy.Field()

    guaPaiShiJian = scrapy.Field()
    jiaoYiQuanSu = scrapy.Field()
    shangCiJiaoYi = scrapy.Field()
    fangWuYongTu = scrapy.Field()
    fangBenNianXian = scrapy.Field()
    chanQuanSuoShu = scrapy.Field()
    diYaXinXi = scrapy.Field()
    fangBenBeiJian = scrapy.Field()

    fangYuanBiaoQian = scrapy.Field()
    heXinMaiDian = scrapy.Field()
    huXingJieShao = scrapy.Field()
    shuiFeiJieXi = scrapy.Field()
    jiaoTongChuXing = scrapy.Field()
    xiaoQuJieShao = scrapy.Field()

    huXingFenJian = scrapy.Filed()
    fangYuanZhaoPian = scrapy.Filed()
    kanFangJiLu = scrapy.Filed()

    pass
