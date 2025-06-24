"""
SGD with Momentum optimizer implementation.
"""

import numpy as np
from typing import Tuple, List
from .base_optimizer import BaseOptimizer


class SGDMomentum(BaseOptimizer):
    """
    SGD with Momentum optimizer.
    
    Accumulates a velocity vector in directions of persistent reduction
    in the objective across iterations.
    """
    
    def __init__(self, learning_rate: float = 0.03, momentum: float = 0.9):
        """
        Initialize SGD with Momentum optimizer.
        
        Args:
            learning_rate (float): Learning rate for weight updates
            momentum (float): Momentum factor (typically 0.9)
        """
        super().__init__(learning_rate)
        self.momentum = momentum
        self.name = "SGD + Momentum"
    
    def optimize(self, X: np.ndarray, y: np.ndarray, epochs: int = 30) -> Tuple[np.ndarray, List[float]]:
        """
        Optimize weights using SGD with momentum.
        
        Args:
            X (np.ndarray): Training features (m x n)
            y (np.ndarray): Training labels (m,)
            epochs (int): Number of training epochs
            
        Returns:
            Tuple[np.ndarray, List[float]]: Final weights and cost history
        """
        m, n = X.shape
        w = np.random.normal(0, 0.01, n)  # Small random initialization
        v = np.zeros(n)  # Initialize velocity
        costs = []
        
        for epoch in range(epochs):
            # Shuffle indices for each epoch
            indices = np.random.permutation(m)
            
            # Update for each individual example
            for i in indices:
                # Compute prediction for current example
                z = X[i].dot(w)
                h = self.sigmoid(z)
                
                # Compute gradient for current example
                grad = (h - y[i]) * X[i]
                
                # Momentum update
                v = self.momentum * v + self.learning_rate * grad
                w = w - v
            
            # Compute cost at end of epoch
            cost = self.compute_cost(w, X, y)
            costs.append(cost)
        
        self.costs_history = costs
        return w, costs
