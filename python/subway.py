#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time

line1 = [
    '苹果园', '古城路', '八角游乐园', '八宝山', '玉泉路', '五棵松',
    '万寿路', '公主坟', '军事博物馆', '木樨地', '南礼士路', '复兴门',
    '西单', '天安门西', '天安门东', '王府井', '东单', '建国门', '永安里',
    '国贸', '大望路', '四惠', '四惠东'
]

line2 = [
    '西直门', '车公庄', '阜成门', '复兴门', '长椿街', '宣武门', '和平门',
    '前门', '崇文门', '北京站', '建国门', '朝阳门', '东四十条', '东直门',
    '雍和宫', '安定门', '鼓楼大街', '积水潭'
]

line4 = [
    '天宫院', '生物医药基地', '义和庄', '黄村火车站', '黄村西大街',
    '清源路', '枣园', '高米店南', '高米店北', '西红门', '新宫',
    '公益西桥', '角门西', '马家堡', '北京南站', '陶然亭', '菜市口',
    '宣武门', '西单', '灵境胡同', '西四', '平安里', '新街口', '西直门',
    '动物园', '国家图书馆', '魏公村', '人民大学', '海淀黄庄', '中关村',
    '北京大学东门', '圆明园', '西苑', '北宫门', '安河桥北'
]

line5 = [
    '宋家庄', '刘家窑', '蒲黄榆', '天坛东门', '磁器口', '崇文门', '东单',
    '灯市口', '东四', '张自忠路', '北新桥', '雍和宫', '和平里北街', '和平西桥',
    '惠新西街南口', '惠新西街北口', '大屯桥东', '北苑路北', '立水桥南', '立水桥',
    '天通苑南', '天通苑', '天通苑北'
]

line6 = [
    '海淀五路居', '慈寿寺', '白石桥南', '车公庄西', '车公庄', '平安里',
    '北海北', '南锣鼓巷', '东四', '朝阳门', '东大桥', '呼家楼', '金台路',
    '十里堡', '青年路', '褡裢坡', '黄渠', '常营', '草房', '物资学院路',
    '通州北关', '通运门', '北运河西', '北运河东', '郝家府', '东夏园', '潞城'
]

line8 = [
    '朱辛庄', '育知路', '平西府', '回龙观东大街', '霍营', '育新', '西小口',
    '永泰庄', '林萃桥', '森林公园南门', '奥林匹克公园', '奥体中心', '北土城',
    '安华桥', '鼓楼大街', '什刹海', '南锣鼓巷'
]

line9 = [
    '国家图书馆', '白石桥南', '白堆子', '军事博物馆', '北京西站', '六里桥东',
    '六里桥', '七里庄', '丰台东大街', '丰台南路', '科怡路', '丰台科技园', '郭公庄'
]

line10 = [
    '劲松', '双井', '国贸', '金台夕照', '呼家楼', '团结湖', '农业展览馆',
    '亮马桥', '三元桥', '太阳宫', '芍药居', '惠新西街南口', '安贞门', '北土城',
    '健德门', '牡丹园', '西土城', '知春路', '知春里', '海淀黄庄', '苏州街',
    '巴沟', '火器营', '长春桥', '车道沟', '慈寿寺', '西钓鱼台', '公主坟', '莲花桥',
    '六里桥', '西局', '泥洼', '丰台站', '首经贸', '纪家庙', '草桥', '角门西',
    '角门东', '大红门', '石榴庄', '宋家庄', '成寿寺', '分钟寺', '十里河', '潘家园'
]

line13 = [
    '西直门', '大钟寺', '知春路', '五道口', '上地', '西二旗', '龙泽', '回龙观',
    '霍营', '立水桥', '北苑', '望京西', '芍药居', '光熙门', '柳芳', '东直门'
]

line14 = ['张郭庄', '园博园', '大瓦窑', '郭庄子', '打井', '七里庄', '西局']

line15 = [
    '俸伯', '顺义', '石门', '南法信', '后沙峪', '花梨坎', '国展',
    '孙河', '马泉营', '崔各庄', '望京', '望京西'
]


class Station(object):
    def __init__(self, name):
        self.name = name


class Edge(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def has(self, station):
        return station == self.start or station == self.end

    def to_tuple(self):
        return (self.start, self.end)

    def __unicode__(self):
        return self.start + ' --> ' + self.end


class Line(object):
    def __init__(self, name):
        self.name = name


def get_edges(line, circle=False):
    edges = []
    z = [iter(line[i:]) for i in range(2)]
    for ab in zip(*z):
        edges.append(Edge(*ab))
    if circle:
        edges.append(Edge(line[-1], line[0]))
    return edges


def make_graph(**lines):
    _all_edges = set()
    for line, circle in lines.values():
        _all_edges.update(set(get_edges(line, circle=circle)))
        _all_edges.update(set(get_edges(line[::-1], circle=circle)))
    return _all_edges


def get_paths(edges, src, dst):
    if src == dst:
        return unicode(Edge(src, dst))

    def get_edges_by_station(station):
        return [e for e in edges if e.start == station]

    start_edges = [e for e in edges if e.start == src]  # 以src为起始点的edge

    paths = [[e] for e in start_edges]
    while True:
        explored = set()

        # print '*************************************************'
        # for ps in paths:
        #     print '-----------------------------------------------'
        #     for p in ps:
        #         print unicode(p)
        #     print '-----------------------------------------------'

        temp_path_list = []
        for path in paths:
            if path[-1] and path[-1].end != dst:
                temp_paths = []
                for e in edges:
                    if e not in explored:
                        if path[-1].end == e.start and path[-1].start != e.end:
                            temp_paths.append(e)
                            explored.add(e)

                if not temp_paths:
                    temp_path_list.append(path + [''])
                    continue

                for t in temp_paths:
                    temp_path_list.append(path + [t])

            else:
                temp_path_list.append(path)

        paths = temp_path_list

        flags = []
        for p in paths:
            if p[-1]:
                flags.append(p[-1].end == dst)
            else:
                flags.append(True)

        # time.sleep(0.1)

        if all(flags):
            return paths


if __name__ == "__main__":
    graph = make_graph(line1=(line1, False),
                       line2=(line2, True),
                       line4=(line4, False),
                       line10=(line10, True),
                       line13=(line13, False))

    for ps in get_paths(graph, '八宝山', '公主坟'):
        print '**************************************'
        for p in ps:
            print unicode(p)
