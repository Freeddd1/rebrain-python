def parsing_log(parsed_logs_f, *args):
    for log in args:
        time = log[:15]
        pc_name = log.split()[3]
        service_name = log.split()[4].replace(":", "")
        message = ' '.join(log.split()[5:])

        dict_log = \
            {
            'time': time,
            'pc_name': pc_name,
            'service_name': service_name,
            'message': message
            }

        parsed_logs_f.append(dict_log)

    print("2.4 вывод полученного списка на экран", end="\n")
    for log in parsed_logs_f:
        print(log, end="\n")



def analyze_info(info_f):
    mem_crit = []
    mem_not_enough = []
    mem_ok = []

    for log in info_f:
        memory = log['total'] - log['used']
        GB = 1073741824
        percent5 = (log['total'] * 5) / 100
        percent10 = (log['total'] * 10) / 100

        if memory < percent5 or memory < 10 * GB:
            mem_crit.append(log['id'])
        elif memory < percent10 or memory < 30 * GB:
            mem_not_enough.append(log['id'])
        else:
            mem_ok.append(log['id'])

    mem_dict = \
        {
        'memory_crit': mem_crit,
        'memory_not_enough': mem_not_enough,
        'memory_ok': mem_ok
        }
    return mem_dict


parsed_logs = []

log1 = "May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated"
log2 = "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations."
log3 = "May 20 11:01:12 PC-00102 PackageKit: daemon start"

parsing_log(parsed_logs, log1, log2, log3)

info = [
{'id': 382, 'total': 999641890816, 'used': 228013805568},
{'id': 385, 'total': 61686008768, 'used': 52522710872},
{'id': 398, 'total': 149023482194, 'used': 83612310700},
{'id': 400, 'total': 498830397039, 'used': 459995976927},
{'id': 401, 'total': 93386008768, 'used': 65371350065},
{'id': 402, 'total': 988242468378, 'used': 892424683789},
{'id': 430, 'total': 49705846287, 'used': 9522710872},
]

print()
print(analyze_info(info))
