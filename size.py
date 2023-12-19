from PIL import Image

# 打开图片文件
image_path = "/Users/zhongzhichen/Desktop/pygame/R-C.png"  # 替换成你的图片路径
img = Image.open(image_path)

# 获取图片尺寸
width, height = img.size

# 打印尺寸信息
print(f"图片宽度: {width} 像素")
print(f"图片高度: {height} 像素")
