_base_ = [
    '../_base_/models/fast_rcnn_r50_fpn.py',
    '../_base_/datasets/voc0712_fast_rcnn.py',
    '../_base_/default_runtime.py'
]
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
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
# yapf:enable
# runtime settings
total_epochs = 4  # actual epoch = 4 * 3 = 12
dist_params = dict(backend='nccl')
log_level = 'INFO'
#work_dir = '../work_dirs/faster_rcnn_r50_fpn_1x_voc0712_2c'
load_from = None
resume_from = None
workflow = [('train', 1)]
work_dir = './work_dirs/fast_rcnn_finalwithproposals'
