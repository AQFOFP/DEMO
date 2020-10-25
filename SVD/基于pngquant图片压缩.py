import pngquant

pngquant.config(r'D:\pngquant\pngquant.exe')
image = pngquant.quant_image('chiji.png', dst='666_2.png', ndeep=2)



'''
--force --speed=1 --quality=50-90
--force 强制覆盖现有的输出文件(短选项：-f)
--skip-if-larger 在压缩时仅保存小于原始的文件
--output file    输出文件目标文件路径，而不是--ext (短命令: -o)
--ext 设置输出文件名的自定义后缀/扩展名
--quality 设置图片颜色范围，值为0-100
--speed   设置速度和图片质量，速度越快质量越差。参数：1=slow, 3=default, 11=fast & rough
--nofs    禁止Floyd-Steinberg抖动
'''

