from PIL import Image
import time
import torch
import torchvision
from torch.utils.data import Dataset
from torchvision import transforms
import albumentations
import albumentations.pytorch
from matplotlib import pyplot as plt
import cv2
import numpy as np


class TorchvisionDataset(Dataset):
    def __init__(self, file_paths, labels, transform=None):
        self.file_paths = file_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        label = self.labels[idx]
        file_path = self.file_paths[idx]

        # Read an image with PIL
        image = Image.open(file_path)

        start_t = time.time()
        if self.transform:
            image = self.transform(image)
        total_time = (time.time() - start_t)

        return image, label, total_time

torchvision_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.RandomCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])

torchvision_dataset = TorchvisionDataset(
    file_paths=["D:/Different_backgrounds/Black/screw_random_dataset_6_2.png"],
    labels=[1],
    transform=torchvision_transform,
)

total_time = 0
for i in range(100):
  sample, _, transform_time = torchvision_dataset[0]
  total_time += transform_time

print("torchvision time/sample: {} ms".format(total_time*10))

plt.figure(figsize=(10, 10))
plt.imshow(transforms.ToPILImage()(sample))
plt.show()


class AlbumentationsDataset(Dataset):
    """__init__ and __len__ functions are the same as in TorchvisionDataset"""

    def __init__(self, file_paths, labels, transform=None):
        self.file_paths = file_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        label = self.labels[idx]
        file_path = self.file_paths[idx]

        # Read an image with OpenCV
        image = cv2.imread(file_path)

        # By default OpenCV uses BGR color space for color images,
        # so we need to convert the image to RGB color space.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        start_t = time.time()
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']
            total_time = (time.time() - start_t)
        return image, label, total_time

"""
torchvision_transform = transforms.Compose([
    transforms.Resize((256, 256)), 
    transforms.RandomCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])
"""

# Same transform with torchvision_transform
albumentations_transform = albumentations.Compose([
    albumentations.Resize(256, 256),
    albumentations.RandomCrop(150, 150), #default: 224
    albumentations.HorizontalFlip(), # Same with transforms.RandomHorizontalFlip()
    albumentations.pytorch.transforms.ToTensorV2()
])

# Same dataset with torchvision_dataset
albumentations_dataset = AlbumentationsDataset(
    file_paths=["D:/Different_backgrounds/Black/screw_random_dataset_6_2.png"],
    labels=[1],
    transform=albumentations_transform,
)
total_time = 0
for i in range(100):
  sample, _, transform_time = albumentations_dataset[0]
  total_time += transform_time

albumentations_transform_oneof = albumentations.Compose([
    albumentations.Resize(256, 256),
    albumentations.RandomCrop(100, 100), #default: 224
    albumentations.OneOf([
                          albumentations.HorizontalFlip(p=1),
                          albumentations.RandomRotate90(p=1),
                          albumentations.VerticalFlip(p=1)
    ], p=1),
    albumentations.OneOf([
                          albumentations.MotionBlur(p=1),
                          albumentations.OpticalDistortion(p=1),
                          albumentations.GaussNoise(p=1)
    ], p=1),
    albumentations.pytorch.ToTensorV2()
])

albumentations_dataset = AlbumentationsDataset(
    file_paths=["D:/Different_backgrounds/Black/screw_random_dataset_6_2.png"],
    labels=[1],
    transform=albumentations_transform_oneof,
)

num_samples = 5
fig, ax = plt.subplots(1, num_samples, figsize=(25, 5))
for i in range(num_samples):
  ax[i].imshow(transforms.ToPILImage()(albumentations_dataset[0][0]))
  img = transforms.ToPILImage()(albumentations_dataset[0][0])
  imname = str(i) +'.png'
  img.save(imname)

  #image_name = 'image_' + str(i)
  #ax[i].imsave(image_name, transforms.ToPILImage()(albumentations_dataset[0][0]))

  ax[i].axis('off')

print("albumentations time/sample: {} ms".format(total_time*10))

#plt.figure(figsize=(10, 10))
#plt.imshow(transforms.ToPILImage()(sample))
plt.show()
