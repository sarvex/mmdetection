# Copyright (c) OpenMMLab. All rights reserved.
def trigger_visualization_hook(cfg, args):
    default_hooks = cfg.default_hooks
    if 'visualization' not in default_hooks:
        raise RuntimeError(
            'VisualizationHook must be included in default_hooks.'
            'refer to usage '
            '"visualization=dict(type=\'VisualizationHook\')"')

    visualization_hook = default_hooks['visualization']
    # Turn on visualization
    visualization_hook['draw'] = True
    if args.show:
        visualization_hook['show'] = True
        visualization_hook['wait_time'] = args.wait_time
    if args.show_dir:
        visualization_hook['test_out_dir'] = args.show_dir
    return cfg
