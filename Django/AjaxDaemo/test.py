import json

st = '''{
    "报警主机": "服务",
    "报警IP": "192.168.179.132",
    "报警时间": "2019.08.02-19:28:07",
    "报警等级": "High",
    "事件ID": "13301",
    "报警信息": "Zabbix value cache. % used 未获取到书记"}'''

json_dir = json.loads(st)
print(json_dir["报警主机"])
print(json_dir["报警IP"])

# dir_st = "{%s}" %
# dir_st = {st.strip()}
# print(type(dir_st))
# print(dir_st)
# print(dir_st["报警主机"])
# json_st = json.dumps(dir_st)
# print(json_st)
