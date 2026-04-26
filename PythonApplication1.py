from http import HTTPStatus
import dashscope
dashscope.api_key = "your_api_key_here"

def pot_test():
    prompt = """
问题：小明有5个苹果，给了小红2个，又买了3个，最后有几个？
步骤：1. 5-2=3  2. 3+3=6  答案：6

问题：一盒蛋糕12块，吃了4块，妈妈又买了2盒，现在有多少块？
步骤：1. 12-4=8  2. 2×12=24  3. 8+24=32  答案：32

问题：图书馆有30本书，借出去10本，还回来5本，又新买了8本，现在有多少本？
步骤：
"""
    resp = dashscope.Generation.call(model='qwen-turbo', prompt=prompt)
    print("✅ 少样本CoT输出：\n", resp.output.text)

few_pot_test()




