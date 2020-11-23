# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------   
# Author:  chenhao
# Date:  2020-09-29
# Description:
#-------------------------------------------------------------------------------
import pandas as pd
import sys, collections, json
from collections import namedtuple
import re

data = namedtuple('user','tab_name,dashboard_id,query_engine,query_status,tab_id,return_rows,dashboard_name,misid,query_sql,action,dt,hour,ctime')


def parse_input(line):
    datas = line.strip("\n").split("\t")
    if len(datas) == 13:
        return data(tab_name=datas[0], dashboard_id=datas[1], query_engine=datas[2], query_status=datas[3], tab_id=datas[4],return_rows=datas[5], dashboard_name=datas[6], misid=datas[7], query_sql=datas[8],action=datas[9], dt=datas[10], hour=datas[11], ctime=datas[12])


if __name__ == '__main__':
    input = open('./query3.txt','r',encoding='utf-8')
    output = []
    for line in input.readlines():
        row = parse_input(line)
        dic = row._asdict()
        if ';' in dic['query_sql']: #如果dic['query_sql']中有;代表有多个SQL
            sqls = dic['query_sql'].split(';')
            for sql in sqls:
                print(sql)
                cur_dic = dic.copy()
                cur_dic['query_sql'] = sql
                output.append(cur_dic)
        else:#如果没有;直接跳过
            cur_dic = dic.copy()
            output.append(cur_dic)

    for i in output:
        print(i)