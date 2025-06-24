# 📊 Results and Analysis

## Experiment Summary

Date: 2025-06-23
Dataset: Iris (Versicolor vs Virginia) 
Features: 4 + bias term
Training Split: 80%
Test Split: 20%
Epochs: 30

## Optimizer Performance

| Method      | Final Cost | Train Accuracy | Test Accuracy | Convergence Speed |
|-------------|------------|----------------|---------------|-------------------|
| SGD         | ~0.300     | 95-97%         | 93-97%        | Slow             |
| Momentum    | ~0.300     | 95-97%         | 93-97%        | Fast but unstable|
| RMSProp     | ~0.150     | 95-97%         | 93-97%        | Fast             |
| Adam        | ~0.120     | 95-97%         | 93-97%        | Fastest          |

## Key Findings

1. **Adam** achieved the fastest convergence (5 epochs to low loss)
2. **RMSProp** showed good performance with some oscillations
3. **SGD with Momentum** had initial rapid descent but showed instability
4. **Basic SGD** was slowest but most stable

## Recommendations

- Use **Adam** for quick convergence and general-purpose optimization
- Use **RMSProp** when you need adaptive learning rates
- Use **Momentum** with careful learning rate tuning
- Use **SGD** for better generalization in some complex models

## Generated Files

- `experiment_results.txt` - Detailed numerical results
- `convergencia_optimizadores.png` - Convergence plot (PNG)
- `convergencia_optimizadores.pdf` - Convergence plot (PDF)
- `../docs/curvas_convergencia.pdf` - Plot for LaTeX document
