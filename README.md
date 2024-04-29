```markdown
# Health Insurance Cost Prediction

## Description
This project implements a machine learning model to predict medical insurance costs for individuals based on various factors such as age, BMI, smoking status, and region. The model is trained on a dataset containing historical insurance data. It provides an interactive web interface for users to input their information and receive the predicted insurance cost.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Model Training](#model-training)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/HarshJain69/health-insurance-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd health-insurance-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure that the dataset file (`insurance.csv`) is present in the project directory.
2. Run the Flask web application:
   ```bash
   python app.py
   ```
3. Open a web browser and navigate to `http://localhost:5000` to access the application.
4. Fill in the required details in the form (age, BMI, number of children, smoker status), and submit to get the predicted insurance cost.

## Features
- Predict medical insurance costs based on individual characteristics.
- Provide an interactive web interface for users to input their information.
- Display the predicted insurance cost to the user.

## Model Training
- Utilizes linear regression for cost prediction.
- Feature engineering includes mapping categorical variables like smoking status and region to numerical values.

## Technologies Used
- Python
- Flask
- HTML/CSS
- JavaScript
- scikit-learn

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References
1. Xiong, L., & Ma, X. (2007). Forecasting China's Medical Insurance Policy for Urban Employees Using a Microsimulation Model. Journal of Artificial Societies and Social Simulation, 10(1), 8.
2. Anwar ul Hassan, C., Iqbal, J., Hussain, S., Alsalm, H., Mosleh, M. A. A., & Ullah, S. S. (2021). A Computational Intelligence Approach for Predicting Medical Insurance Cost. Mathematical Problems in Engineering, 2021, Article ID 1162553, 13 pages.
3. Orji, U., & Ukwandu, E. (2024). Machine Learning for an Explainable Cost Prediction of Medical Insurance. Machine Learning with Applications, 15, 100516.
4. Umemoto, K., Goda, K., Mitsutake, N., & Kitsuregawa, M. (2019). A Prescription Trend Analysis using Medical Insurance Claim Big Data. In 2019 IEEE 35th International Conference on Data Engineering (ICDE) (pp. 1928-1939). Macao, China.
5. Shakhovska, N., Melnykova, N., Chopiyak, V., & Gregus ml, M. (2022). An Ensemble Methods for Medical Insurance Costs Prediction Task. Computers, Materials & Continua, 70(2), 3969.
6. Goundar, S., Prakash, S., Sadal, P., & Bhardwaj, A. (2020). Health Insurance Claim Prediction Using Artificial Neural Networks. International Journal of System Dynamics Applications (IJSDA), 9(3), 40-57.
7. Goundar, S., Bhardwaj, A., Prakash, S. S., & Sadal, P. (2022). Use of Artificial Neural Network for Forecasting Health Insurance Entitlements. Journal of Information Technology Research (JITR), 15(1), 1-18.
8. Fang, K., Jiang, Y., & Song, M. (2016). Customer Profitability Forecasting using Big Data Analytics: A Case Study of the Insurance Industry. Computers & Industrial Engineering, 101, 554-564.
9. Xie, Y., Yu, H., Lei, X., & Lin, A. J. (2020). The Impact of Fertility Policy on the Actuarial Balance of China’s Urban Employee Basic Medical Insurance Fund–The Selective Two-child Policy vs. The Universal Two-child Policy. The North American Journal of Economics and Finance, 53, 101212.
10. Kalra, G., Rajoria, Y. K., Boadh, R., Rajendra, P., Pandey, P., & Khatak, N., et al. (2022). Study of Fuzzy Expert Systems towards Prediction and Detection of Fraud Case in Health Care Insurance. Materials Today: Proceedings, 56(Part 1), 477-480.
11. Harrington, S. E., Danzon, P. M., & Epstein, A. J. (2008). "Crises" in Medical Malpractice Insurance: Evidence of Excessive Price-cutting in the Preceding Soft Market. Journal of Banking & Finance, 32(1), 157-169.
12. Zhang, X.-j., & Zhou, L.-l. (2011). GM (1, 1) Model-Based Analysis and Forecasting of Medical Insurance Funds in China. In 2011 5th International Conference on Bioinformatics and Biomedical Engineering (pp. 1-4). Wuhan, China.
13. Jang, K. P., Kam, S., & Park, J. Y. (1991). Trend and Forecast of the Medical Care Utilization Rate, the Medical Expense per Case, and the Treatment Days per Case in Medical Insurance Program for Employees by ARIMA Model. Journal of Preventive Medicine and Public Health, 24(3), 441-458.
14. Zhai, X., & Zhang, S.-Q. (2023). Analysis of Influencing Factors and Demand Forecast of Single Disease Demand in Chinese Public Hospitals. American Journal of Health Behavior, 47(2), 386-396.
15. Wang, O., Qin, Z., Hsu, J., & Zhou, B. (2024). A Fusion of Machine Learning Algorithms and Traditional Statistical Forecasting Models for Analyzing American Healthcare Expenditure. Healthcare Analytics, 5, 100312.
16. Sun, J., & Lyu, S. (2020). The Effect of Medical Insurance on Catastrophic Health Expenditure: Evidence from China. Cost Eff Resour Alloc, 18(10).
17. Lu, Y., & Xu, Z. (2013). Study on Basic Medical Insurance Fund Revenue and Expenditure Risk Early Warning System. In W. Du (Ed.), Informatics and Management Science I (pp. 204). Springer, London.
18. Chowdhury, S., Mayilvahanan, P., & Govindaraj, R. (2022). Opt

imal Feature Extraction and Classification-Oriented Medical Insurance Prediction Model: Machine Learning Integrated with the Internet of Things. International Journal of Computers and Applications, 44(3), 278–290.
19. Inoue, S., Xu, H., Maswana, J.-C., & Kobayashi, M. (2022). Forecasting of Future Medical Care Expenditure in Japan Using a System Dynamics Model.
20. Sanjai, K. S., & Rekha. (2024). Insurance Prediction of Medical Resource Using Cross Gradient Regression Model. In 2024 IEEE International Conference on Computing, Power and Communication Technologies (IC2PCT) (Vol. 5, pp. 934-937).2011, pp. 1-4, doi: 10.1109/icbbe.2011.5781519.
```
