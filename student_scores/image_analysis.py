import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

folder_path = r"C:\Users\siddu\PycharmProjects\NP_PD_PLT\student_scores\grayscale images"
data = []
valid_ext = (".png", ".jpg", ".jpeg")

target_size = (256 , 256)

for file in os.listdir(folder_path):
    if file.lower().endswith(valid_ext):
        file_path = os.path.join(folder_path, file)
        img = Image.open(os.path.join(folder_path, file)).convert('L')
        img = img.resize(target_size)
        info = {
            'filename': file,
            'file_size': os.path.getsize(file_path),
            'height': img.height,
            'width': img.width,
            'format': img.format,
            'mode': img.mode,
            'image': np.array(img, dtype=np.float32).reshape(-1) / 255.0
        }
        data.append(info)

metadata_df = pd.DataFrame(data)
metadata_df['mean_pixel_density'] = metadata_df['image'].apply(lambda x: x.mean())

image_series = metadata_df['image']
number_of_images = len(image_series)
img_size = (256, 256)
columns = 2
rows = 2

fig, axes = plt.subplots(rows, columns, figsize=(12, 3*rows))
axes = axes.flatten()

for i in range(number_of_images):
    img_2d = image_series.iloc[i].reshape(img_size)
    axes[i].imshow(img_2d, cmap='gray')
    axes[i].set_title(metadata_df.loc[i, 'filename'], fontsize=8)
    axes[i].axis('off')

for j in range(number_of_images, len(axes)):
    axes[j].axis('off')

plt.tight_layout()
plt.show()

filenames = metadata_df['filename'].unique()
plt.figure(figsize=(10, 6))

for file in filenames:
    subset = metadata_df[metadata_df['filename'] == file]
    plt.hist(subset['mean_pixel_density'], bins=20, alpha=0.5, label=file)

plt.xlabel('Mean pixel density')
plt.ylabel('Number of images')
plt.title('Histogram of mean pixel density')
plt.legend()
plt.show()

X = np.stack(metadata_df['image'].values)
X_flat = X.reshape(len(X), -1)
X_mean = X_flat.mean(axis=0)
X_centered = X_flat - X_mean

U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
X_pca = X_centered @ Vt.T[:, :2]

for file in filenames:
    subset = metadata_df['filename'].values == file
    plt.scatter(X_pca[subset, 0], X_pca[subset, 1], label=file, alpha=0.5)

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend()
plt.show()