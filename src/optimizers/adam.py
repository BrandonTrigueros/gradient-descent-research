"""
Adam optimizer implementation.
"""

import numpy as np
from typing import Tuple, List
from .base_optimizer import BaseOptimizer


class Adam(BaseOptimizer):
    """
    Adam (Adaptive Moment Estimation) optimizer.
    
    Combines ideas from RMSProp and momentum by keeping track of both
    first and second moments of the gradients.
    """
    
    def __init__(self, learning_rate: float = 0.05, beta1: float = 0.9, 
                 beta2: float = 0.999, epsilon: float = 1e-8):
        """
        Initialize Adam optimizer.
        
        Args:
            learning_rate (float): Learning rate for weight updates
            beta1 (float): Exponential decay rate for first moment estimates (typically 0.9)
            beta2 (float): Exponential decay rate for second moment estimates (typically 0.999)
            epsilon (float): Small constant to prevent division by zero
        """
        super().__init__(learning_rate)
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.name = "Adam"
    
    def optimize(self, X: np.ndarray, y: np.ndarray, epochs: int = 30) -> Tuple[np.ndarray, List[float]]:
        """
        Optimize weights using Adam.
        
        Args:
            X (np.ndarray): Training features (m x n)
            y (np.ndarray): Training labels (m,)
            epochs (int): Number of training epochs
            
        Returns:
            Tuple[np.ndarray, List[float]]: Final weights and cost history
        """
        m, n = X.shape
        w = np.random.normal(0, 0.01, n)  # Small random initialization
        m_moment = np.zeros(n)  # First moment estimate
        v_moment = np.zeros(n)  # Second moment estimate
        costs = []
        t = 0  # Time step counter
        
        for epoch in range(epochs):
            # Shuffle indices for each epoch
            indices = np.random.permutation(m)
            
            # Update for each individual example
            for i in indices:
                t += 1  # Increment time step
                
                # Compute prediction for current example
                z = X[i].dot(w)
                h = self.sigmoid(z)
                
                # Compute gradient for current example
                grad = (h - y[i]) * X[i]
                
                # Update biased first moment estimate
                m_moment = self.beta1 * m_moment + (1 - self.beta1) * grad
                
                # Update biased second moment estimate
                v_moment = self.beta2 * v_moment + (1 - self.beta2) * (grad ** 2)
                
                # Compute bias-corrected first moment estimate
                m_hat = m_moment / (1 - self.beta1 ** t)
                
                # Compute bias-corrected second moment estimate
                v_hat = v_moment / (1 - self.beta2 ** t)
                
                # Adam update
                w = w - (self.learning_rate / (np.sqrt(v_hat) + self.epsilon)) * m_hat
            
            # Compute cost at end of epoch
            cost = self.compute_cost(w, X, y)
            costs.append(cost)
        
        self.costs_history = costs
        return w, costs
