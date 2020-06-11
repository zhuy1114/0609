# 定义断言函数
import json


def assert_common(self, http_code, status, msg, response):
    # 添加断言
    # 响应码
    self.assertEqual(http_code, response.status_code)
    # 状态
    self.assertEqual(status, response.json().get("status"))
    # 信息
    self.assertIn(msg, response.json().get("msg"))


# 定义读取json数据的函数
def load_data(filepath):
    with open(filepath, mode="r", encoding="utf-8")as f:
        # 读取数据
        jsondata = json.load(f)
        # 定义空列表，遍历数据追加到列表中
        data_list = []
        for item in jsondata:  # type:dict
            data_list.append(item.values())
    return data_list


if __name__ == '__main__':
    file_path = "./data/reg_and_log_data.json"
    json = load_data(file_path)
    print(json)
