_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]
load_from = '/home/UNT/sd0570/mmdetection/work_dirs/faster_rcnn_final/latest.pth'
work_dir = './work_dirs/mask_rcnn_final'
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

