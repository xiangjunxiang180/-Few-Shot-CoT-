from http import HTTPStatus
import dashscope
dashscope.api_key = "your_api_key_here"

def pot_test():
    prompt = """
用Python代码计算：一个人走3公里每小时，走了2.5小时，一共走多远？
请只写代码，不要多余解释。
"""
    resp = dashscope.Generation.call(model='qwen-turbo', prompt=prompt)
    print("✅ PoT 生成的代码：\n", resp.output.text)

pot_test()

