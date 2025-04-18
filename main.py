from mcp.server import FastMCP

app = FastMCP('image-server')


@app.tool()
def image_generation(image_prompt: str, width: int = 1024, height: int = 1024) -> str:
    """
    Image generation assistant, please imagine and describe a complete picture in detail based on my simple description. Then translate your detailed description into English

    :param width: 图片宽度，默认1024
    :param height: 图片高度，默认1024
    :param image_prompt:图片描述，需要英文
    :return:图片的url地址
    """

    return f"![image](https://image.pollinations.ai/prompt/{image_prompt}?width={width}&height={height}&enhance=true&nologo=true&model=flux)"


if __name__ == "__main__":
    app.run(transport='stdio')
