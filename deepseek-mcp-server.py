import os
from fastmcp import FastMCP
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('OPENAI_BASE_URL')
)


mcp = FastMCP("DeepSeek V3 Service")

@mcp.tool()
def generate_text(prompt: str, max_tokens: int = 100) -> str:
    """使用 DeepSeek V3 模型生成文本。"""
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content + "這是DeepSeek V3的回答XDD"


if __name__ == "__main__":
    mcp.run(transport="stdio")
