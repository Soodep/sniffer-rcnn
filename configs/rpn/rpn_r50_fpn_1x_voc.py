_base_ = [
    '../_base_/models/rpn_r50_fpn.py', '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_label=False),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes']),
]
data = dict(train=dict(pipeline=train_pipeline))
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
total_epochs = 4  # actual epoch = 4 * 3 = 12
dist_params = dict(backend='nccl')
log_level = 'INFO'
optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(policy='step', step=[3])  # actual epoch = 3 * 3 = 9
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
evaluation = dict(interval=1, metric='proposal_fast')
work_dir = './work_dirs/fast_rcnn_final'
#load_from='/home/UNT/sd0570/mmdetection/work_dirs/fast_rcnn_final/latest.pth'