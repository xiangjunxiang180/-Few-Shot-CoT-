from http import HTTPStatus
import dashscope
dashscope.api_key = "sk-f063550363944f1682e3dc38a9d72728"

def pot_test():
    prompt = """
用Python代码计算：一个人走3公里每小时，走了2.5小时，一共走多远？
请只写代码，不要多余解释。
"""
    resp = dashscope.Generation.call(model='qwen-turbo', prompt=prompt)
    print("✅ PoT 生成的代码：\n", resp.output.text)

pot_test()




