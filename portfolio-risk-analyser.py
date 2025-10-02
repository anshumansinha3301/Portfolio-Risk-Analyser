#!/usr/bin/env python3
import random
import statistics
from typing import List, Dict

class PortfolioRiskAnalyzer:
    def __init__(self, assets: Dict[str, float]):
        self.assets = assets  # { "AAPL": weight, "MSFT": weight }
        self.returns = {asset: [] for asset in assets}

    def generate_synthetic_returns(self, days: int = 100):
        for asset in self.assets:
            self.returns[asset] = [random.uniform(-0.02, 0.02) for _ in range(days)]

    def expected_return(self) -> float:
        return sum(statistics.mean(self.returns[a]) * w for a, w in self.assets.items())

    def variance(self) -> float:
        port_rets = []
        days = len(next(iter(self.returns.values())))
        for i in range(days):
            daily_ret = sum(self.returns[a][i] * w for a, w in self.assets.items())
            port_rets.append(daily_ret)
        return statistics.variance(port_rets) if len(port_rets) > 1 else 0.0

    def risk_metrics(self) -> Dict[str, float]:
        exp_ret = self.expected_return()
        var = self.variance()
        std_dev = var ** 0.5
        sharpe = exp_ret / std_dev if std_dev != 0 else 0.0
        return {
            "Expected Return": round(exp_ret, 4),
            "Variance": round(var, 6),
            "Standard Deviation": round(std_dev, 4),
            "Sharpe Ratio": round(sharpe, 4)
        }

def demo():
    portfolio = PortfolioRiskAnalyzer({"AAPL": 0.5, "MSFT": 0.3, "GOOG": 0.2})
    portfolio.generate_synthetic_returns(120)
    print("Portfolio Risk Metrics:")
    print(portfolio.risk_metrics())

if __name__ == "__main__":
    demo()
