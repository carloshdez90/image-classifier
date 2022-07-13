# This project is based on [this repo](https://github.com/Alibaba-MIIL/ImageNet21K)

## ImageNet-21K Pretraining for the Masses

[Paper](https://arxiv.org/pdf/2104.10972v4.pdf) |
[Pretrained models](MODEL_ZOO.md)

Official PyTorch Implementation

> Tal Ridnik, Emanuel Ben-Baruch, Asaf Noy, Lihi Zelnik-Manor<br/> DAMO Academy, Alibaba
> Group

**Abstract**

ImageNet-1K serves as the primary dataset for pretraining deep learning models for computer vision tasks. ImageNet-21K dataset, which contains more pictures and classes, is used less frequently for pretraining, mainly due to its complexity, and underestimation of its added value compared to standard ImageNet-1K pretraining.
This paper aims to close this gap, and make high-quality efficient pretraining on ImageNet-21K available for everyone.
Via a dedicated preprocessing stage, utilizing WordNet hierarchies, and a novel training scheme called semantic softmax, we show that different models, including small mobile-oriented models, significantly benefit from ImageNet-21K pretraining on numerous datasets and tasks.
We also show that we outperform previous ImageNet-21K pretraining schemes for prominent new models like ViT.
Our proposed pretraining pipeline is efficient, accessible, and leads to SoTA reproducible results, from a publicly available dataset.

## Citation

```
@misc{ridnik2021imagenet21k,
      title={ImageNet-21K Pretraining for the Masses},
      author={Tal Ridnik and Emanuel Ben-Baruch and Asaf Noy and Lihi Zelnik-Manor},
      year={2021},
      eprint={2104.10972},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

# Instructions

1. Install pytorch with GPU support `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113`
2. Install dependencies `pip install -r requirements.txt`
3. Rename `.env.example` to `.env` and fill the vars
4. Test project with `uvicorn main:app --reload`
