# Sizing-hybrid-power-plants-under-round-the-clock-tender-compliance-in-India

This repository is a compilation of my work for my Master's Thesis at the Technical University of Denmark, DTU. 

India aims to quadruple its renewable electricity capacity by 2030, using auction-based renewable power tenders as a mechanism to achieve that goal.
An optimization problem to optimise a power producer’s plant sizing for this tariff-based bidding process is formulated. The outcome is an investment optimisation model for a hybrid power system that complies with the specific Round-the-Clock tender criteria.

The Thesis can be found here: https://findit.dtu.dk/en/catalog/6141d49bd9001d0162189967?single_revert=%2Fen%2Fcatalog%3Fq%3Dsizing%2Bhybrid%2Bpower%2Bplants%2Bunder%2Bround-the-clock%2Btender%2Bcompliance%2Bin%2BIndia%26show_single%3Doff%26utf8%3D%25E2%259C%2593

- Data files: coal_prices.xlsx, merchant_prices.xlsx and ts_output_clean.csv
- Data is processed in the files: clean_data_NEW.py, parameters_NEW.py and parameters_Scenarios.py

Due to data sharing regulations, no real data is given. The data files are in correct format for direct use with the code, but includes zeros as entry. For test runs, please fill in random values. 
Parameters are example values.

- Economic dispatch model: OperationalV5.py
- Relaxed investment model: InvestmentV4.py
- Full firm compliance investment model: DeterministicV4.py
- Stochastic investment model with 2 scenarios: StochasticV5.py
- Stochastic investment model with 3 scenarios: StochasticV5_scenarios3.py
- Stochastic investment model with 10 scenarios: Stochastic_S10.py
- Sensitivity analyses: Sensitivity_XX.py
- Visualisation: plots_XX.py

DOI: 10.5281/zenodo.6457041
