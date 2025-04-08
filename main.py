from mcp.server import FastMCP

app = FastMCP('image-server')


@app.tool()
def image_generation(image_prompt: str) -> str:
    """
    Image generation assistant, please imagine and describe a complete picture in detail based on my simple description. Then translate your detailed description into English

    :param image_prompt:图片描述，需要英文
    :return:图片的url地址
    """

    return f"https://image.pollinations.ai/prompt/{image_prompt}?width=1024&height=1024&enhance=true&nologo=true&model=flux&private=true"


if __name__ == "__main__":
    app.run(transport='stdio')
