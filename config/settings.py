# Configuration file for gradient descent experiments

# Experiment parameters
EXPERIMENT_CONFIG = {
    'random_seed': 42,
    'test_size': 0.2,
    'epochs': 30,
    'dataset': 'iris',
    'classes': ['Versicolor', 'Virginia']  # Binary classification
}

# Optimizer configurations
OPTIMIZER_CONFIGS = {
    'SGD': {
        'learning_rate': 0.05,
        'epochs': 30
    },
    'SGD_Momentum': {
        'learning_rate': 0.03,
        'gamma': 0.9,
        'epochs': 30
    },
    'RMSProp': {
        'learning_rate': 0.05,
        'rho': 0.9,
        'epsilon': 1e-8,
        'epochs': 30
    },
    'Adam': {
        'learning_rate': 0.05,
        'beta1': 0.9,
        'beta2': 0.999,
        'epsilon': 1e-8,
        'epochs': 30
    }
}

# Plotting configurations
PLOT_CONFIG = {
    'figsize': (10, 6),
    'colors': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
    'linestyles': ['-', '--', '-.', ':'],
    'markers': ['o', 's', '^', 'D'],
    'font_size': 12,
    'title_size': 16,
    'label_size': 14,
    'dpi': 300
}

# File paths
PATHS = {
    'results_dir': '../results',
    'docs_dir': '../docs',
    'figures_dir': '../results/figures',
    'data_dir': '../data',
    'latex_main': '../docs/main.tex'
}
