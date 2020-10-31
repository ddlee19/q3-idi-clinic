import pandas as pd
import numpy as np
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default = 'Mills_Treeloss.csv',
                        help='Path of the input csv file')
    parser.add_argument('--output',
                        default='Mills_risk_score_PALM.csv',
                        help='Path of the output csv file with risk scores')

    args = parser.parse_args()

    # Bring in Mills Tree Cover Loss data.
    df = pd.read_csv(args.input)

    def PALM_analyze(year, df):
        # Set relevant column names
        prev_2_col = 'treeloss_' + str(year - 2)
        prev_1_col = 'treeloss_' + str(year - 1)
        pred_col = 'loss_mean_' + \
                   str(int(str(year)[2:]) - 2) + \
                   str(int(str(year)[2:]) - 1)
        actual_col = 'treeloss_' + str(year)
        pred_z_col = 'z_' + pred_col
        actual_z_col = 'z_' + actual_col
        error_col = 'error_' + str(year)

        # Create a new column that is the mean of the columns from the previous
        # 2 years.  This is the prediction for the current year.
        df[pred_col] = df.loc[:, prev_2_col:prev_1_col].mean(axis=1)

        # Run a correlation between the prediction and the current year tree loss.
        print('Correlation between predicted and actual tree loss for {}: '.format(
                                year),df[actual_col].corr(df[pred_col]))


        # Add a column that is the z-score for the prediction column.
        mu = df[pred_col].mean()
        sd = df[pred_col].std()
        df[pred_z_col] = (df[pred_col] - mu)/sd

        # Add a column that is the z-score for the actual column.
        mu2 = df[actual_col].mean()
        sd2 = df[actual_col].std()
        df[actual_z_col] = (df[actual_col] - mu2)/sd2

        # Compute the residuals and RMSE.
        df[error_col] = df[pred_z_col] - df[actual_z_col]
        print('RMSE on predicted tree loss for {}: '.format(year),
              np.sqrt(np.mean(df[error_col]**2)))

    for year in range(2015, 2020):
        PALM_analyze(year, df)

    # Save data as csv.
    df.to_csv(args.output, index = False)

if __name__ == '__main__': main()
