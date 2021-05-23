from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


def get_html2(times, kk):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return f'ppppp=========> {times}, {kk}'


executor = ThreadPoolExecutor(max_workers=5)
urls = [3, 2, 4]  # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]

task_new = executor.submit(get_html2, 5, 9)
all_task.append(task_new)

for future in as_completed(all_task):
    data = future.result()
    print("in main: get page {}s success".format(data))

