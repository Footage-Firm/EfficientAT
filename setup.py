import os
from setuptools import setup, find_packages

# read version and requirements from special files explicitly set up for this
version = {}
_here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_here, "efficientat", "__version__.py")) as f:
    exec(f.read(), version)

setup(name='efficientat',
      description='EfficientAT',
      version=version['__version__'],
      packages=find_packages(),
      install_requires=["av==10.0.0",
                        "h5py==3.7.0",
                        "librosa==0.9.2",
                        "numpy==1.23.3",
                        "pandas==1.5.2",
                        "scikit_learn==1.1.3",
                        "torch==1.13.1",
                        "torchaudio==0.13.1",
                        "torchvision==0.14.1",
                        "tqdm==4.64.1",
                        "wandb==0.13.5", ],
      include_package_data=True,
      python_requires='>=3.7')
