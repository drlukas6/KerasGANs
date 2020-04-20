from PIL import Image
import glob
import sys

folder_name = sys.argv[1]

print(f'Folder name: {folder_name}')

imgs = glob.glob(f'./{folder_name}/*.png')
frames = []
for img in imgs:
    frames.append(Image.open(img))

frames[0].save(f'{folder_name}.gif',
                format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300,
                loop=0)
